import pandas as pd
import datetime
import numpy as np


def Threats(userPath):
    Threats = [None]


    for i in range(0,len(userPath)-1):
        if userPath["Login Timestamp"][i+1]-userPath["Login Timestamp"][i]<=datetime.timedelta(days=1) and userPath["Country"][i+1]!=userPath["Country"][i]:
            Threats.append("flc")

        if userPath["IP Address"][i+1]!=userPath["IP Address"][i]:
            Threats.append("nIP")

        if userPath["Country"][i+1] != userPath["Country"][i]:
            Threats.append("newLoc")
        
        else:
            Threats.append("False")

    return Threats
def Risk(userPath):
    
    Risk=[]
    for i in Threats(userPath):
        if i=='flc':
            Risk.append("MemorialCredentialTheft")
        if i == 'nIP':
            Risk.append("MemorialCredentialTheft1")
        if i == 'newLoc':
            Risk.append("PhysicalTheft")
        else:
            Risk.append("")
    return Risk


def allocateAuth(userPath):
    auths=["password"]
    for i in range(1,len(Risk(userPath))):
        if Risk(userPath)[i]=='PhysicalTheft':
            auths.append("sms_OTP")
        if Risk(userPath)[i]=='MemorialCredentialTheft':
            auths.append("app_OTP")
        if Risk(userPath)[i]=='MemorialCredentialTheft1':
            auths.append("mobileConnect")   
        else:
            auths.append("")
            
    return pd.DataFrame(auths)


def SolutionB(userPath):
    Threats(userPath)
    Risk(userPath)
    allocateAuth(userPath)
    Authentication_Path_nLoc=pd.concat([userPath, allocateAuth(userPath)], axis=1)
    cols=[]
    for i in userPath.columns:
        cols.append(i)
    cols.append("authenticationMechanism")
    Authentication_Path_nLoc.columns=cols

    return Authentication_Path_nLoc
 

