import json
import GetPeriodValues

def calcAvg (Values):
    length = len(Values)
    total = sum(Values)
    avg = total/length
    return avg