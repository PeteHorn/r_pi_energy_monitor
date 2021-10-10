from influxdb import InfluxDBClient

import PersonalData

dbname = PersonalData.getValues()['TestInfluxDBName']
IP = PersonalData.getValues()['InfluxDB_IP']
user = PersonalData.getValues()['InfluxDB_user']
pw = PersonalData.getValues()['InfluxDB_pw']
port = 8086

def getClient():
    client = InfluxDBClient(host=IP, port=port, username=user, password=pw, database=dbname)
    return client

def WriteData(json_body):
    client = getClient()
    client.write_points(json_body)
    client.close()

def Query(queryString):
    client = getClient()
    result = client.query(queryString)
    return result
