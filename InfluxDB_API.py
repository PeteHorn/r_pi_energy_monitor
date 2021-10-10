from influxdb import InfluxDBClient

import PersonalData

IP = PersonalData.getValues()['InfluxDB_IP']
user = PersonalData.getValues()['InfluxDB_user']
pw = PersonalData.getValues()['InfluxDB_pw']
port = 8086

def WriteData(dbname, json_body):
    client = InfluxDBClient(host=IP, port=port, username=user, password=pw, database=dbname)
    client.write_points(json_body)
    result = client.query('select value from cpu_load_short;')
    print("Result: {0}".format(result))
    client.close()

