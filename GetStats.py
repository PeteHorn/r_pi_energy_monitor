import json

def calcAvg (Values):
    length = len(Values)
    total = sum(Values)
    avg = total/length
    return avg

def calcMaxMin (Values):
    return max(Values), min(Values)