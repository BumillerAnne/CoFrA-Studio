import pandas as pd
import datetime
import numpy as np



timeDiff=[]
timeDiffSec=[]
timeDiffVar=[]


def robotSus(userPath):
    for i in range(0,len(userPath)-1):

        timeDiff.append(userPath["Login Timestamp"][i+1]-userPath["Login Timestamp"][i])
        timeDiffSec.append(timeDiff[i].seconds)
        timeDiffVar.append(np.var(timeDiffSec))

    robotSuspected=[]   
    for i in timeDiffVar:
        if i <= 10:
            robotSuspected.append("True")
        else:
            robotSuspected.append("False")
    return robotSuspected

def robotRisk(userPath):
    
    Risk=[]
    for i in robotSus(userPath):
        if i=='True':
            Risk.append("Robot")
        else:
            Risk.append("")
    return Risk

def allocateAuth(userPath):
    auths=[]
    for i in robotRisk(userPath):
        if i=='Robot':
            auths.append("Captcha")
        else:
            auths.append("")
            
    return pd.DataFrame(auths)

def IAlerting_robotSuspected(userPath):
    robotSus(userPath)
    robotRisk(userPath)
    allocateAuth(userPath)
    Authentication_Path_rb=pd.concat([userPath, allocateAuth(userPath)], axis=1)
    cols=[]
    for i in userPath.columns:
        cols.append(i)
    cols.append("authenticationMechanism")
    Authentication_Path_rb.columns=cols

    return Authentication_Path_rb