import pandas as pd
import datetime

def fastLocationChange(userPath):
    fastLocChange=[False] #For the first connection, we do not know whether the session is expired or not
    for i in range(0,len(userPath)-1):
        if userPath["Login Timestamp"][i+1]-userPath["Login Timestamp"][i]<=datetime.timedelta(days=1) and userPath["Country"][i+1]!=userPath["Country"][i]:

            fastLocChange.append("True")
        else:
            fastLocChange.append("False")
    return fastLocChange

def fastLocChangeRisk(userPath):
    
    Risk=[]
    for i in fastLocationChange(userPath):
        if i=='True':
            Risk.append("MemorialCredentialTheft")
        else:
            Risk.append("")
    return Risk

def allocateAuth(userPath):
    auths=[]
    for i in fastLocChangeRisk(userPath):
        if i=='MemorialCredentialTheft':
            auths.append("sms_OTP")
        else:
            auths.append("")
            
    return pd.DataFrame(auths)

def IAlerting_flc(userPath):
    fastLocationChange(userPath)
    fastLocChangeRisk(userPath)
    allocateAuth(userPath)
    Authentication_Path_flc=pd.concat([userPath, allocateAuth(userPath)], axis=1)
    cols=[]
    for i in userPath.columns:
        cols.append(i)
    cols.append("authenticationMechanism")
    Authentication_Path_flc.columns=cols

    return Authentication_Path_flc