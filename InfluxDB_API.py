from InfluxDB import InfluxDBClient

import PersonalData

IP = PersonalData.getValues()['InfluxDB_IP']
user = PersonalData.getValues()['InfluxDB_user']
pw = PersonalData.getValues()['InfluxDB_pw']
port = 8086

def WriteData(dbname, json_body):
    client = InfluxDBClient(host=IP, port=port, username=user, password=pw, database=dbname)
    client.write_points(json_body)
    client.close()