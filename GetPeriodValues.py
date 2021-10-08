import json

def GetArray (jsonString):
    jsonArray = json.loads(jsonString)
    avgArray = []
    for obj in jsonArray:
        avgArray.append(obj["value_inc_vat"])
    return avgArray