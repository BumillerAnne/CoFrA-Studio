import pandas as pd
import datetime

def newIP(userPath):
    newIP=[False] #For the first connection, we do not know whether the session is expired or not
    for i in range(0,len(userPath)-1):
        if userPath["IP Address"][i+1]!=userPath["IP Address"][i]:

            newIP.append("True")
        else:
            newIP.append("False")
    return newIP

def IPAnomalyRisk(userPath):
    
    Risk=[]
    for i in newIP(userPath):
        if i=='True':
            Risk.append("MemorialCredentialTheft")
        else:
            Risk.append("")
    return Risk

def allocateAuth(userPath):
    auths=[]
    for i in IPAnomalyRisk(userPath):
        if i=='MemorialCredentialTheft':
            auths.append("sms_OTP")
        else:
            auths.append("")
            
    return pd.DataFrame(auths)

def IAlerting_nIP(userPath):
    newIP(userPath)
    IPAnomalyRisk(userPath)
    allocateAuth(userPath)
    Authentication_Path_nIP=pd.concat([userPath, allocateAuth(userPath)], axis=1)
    cols=[]
    for i in userPath.columns:
        cols.append(i)
    cols.append("authenticationMechanism")
    Authentication_Path_nIP.columns=cols

    return Authentication_Path_nIP