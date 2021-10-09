import json

def GetArray (jsonString):
    try:
        jsonArray = json.loads(jsonString)
        avgArray = []
        for obj in jsonArray:
            avgArray.append(obj["value_inc_vat"])
        return "valid", avgArray
    except:
        return "invalid", []