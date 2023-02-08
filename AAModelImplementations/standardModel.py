# Standard model":  "time" --> "timeExpired",--> "sessionExpired",--> "sessionRisk" --> MemorialCredentialTheft" --> "password"
import pandas as pd
import datetime

def sessionExpired(userPath):
    expiredS=[False] #For the first connection, we do not know whether the session is expired or not
    for i in range(0,len(userPath)-1):
        if userPath["Login Timestamp"][i+1]-userPath["Login Timestamp"][i]>=datetime.timedelta(days=1):
            expiredS.append("True")
        else:
            expiredS.append("False")
    return expiredS

def sessionRisk(userPath):
    
    Risk=[]
    for i in sessionExpired(userPath):
        if i=='True':
            Risk.append("accountTakeover")
        else:
            Risk.append("")
    return Risk

def allocateAuth(userPath):
    auths=["password"]
    for i in range(1,len(sessionRisk(userPath))):
        if sessionRisk(userPath)[i]=='accountTakeover':
            auths.append("password")
        else:
            auths.append("")
            
    return pd.DataFrame(auths)



def standardModel(userPath):
    sessionExpired(userPath)
    sessionRisk(userPath)
    allocateAuth(userPath)
    Authentication_Path1=pd.concat([userPath, allocateAuth(userPath)], axis=1)
    cols=[]
    for i in userPath.columns:
        cols.append(i)
    cols.append("authenticationMechanism")
    Authentication_Path1.columns=cols

    return Authentication_Path1

