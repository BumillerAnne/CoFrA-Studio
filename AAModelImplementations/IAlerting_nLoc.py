import pandas as pd
import datetime

def locationAnomaly(userPath):
    newLoc=[False] #Fno inof for first connection
    for i in range(0,len(userPath)-1):
        if userPath["Country"][i+1] != userPath["Country"][i]:
            newLoc.append("True")
        else:
            newLoc.append("False")
    return newLoc

def locRisk(userPath):
    
    Risk=[]
    for i in locationAnomaly(userPath):
        if i=='True':
            Risk.append("PhysicalTheft")
        else:
            Risk.append("")
    return Risk

def allocateAuth(userPath):
    auths=["fingerprint"]
    for i in range(1,len(locRisk(userPath))):
        if locRisk(userPath)[i]=='PhysicalTheft':
            auths.append("fingerprint")
        else:
            auths.append("")
            
    return pd.DataFrame(auths)



def IAlerting_nLoc(userPath):
    locationAnomaly(userPath)
    locRisk(userPath)
    allocateAuth(userPath)
    Authentication_Path_nLoc=pd.concat([userPath, allocateAuth(userPath)], axis=1)
    cols=[]
    for i in userPath.columns:
        cols.append(i)
    cols.append("authenticationMechanism")
    Authentication_Path_nLoc.columns=cols

    return Authentication_Path_nLoc