import MQTT as mqtt_custom
import paho.mqtt.client as mqtt_standard
import datetime
import time
import OctopusEnergy
import GetPeriodValues
import json

def process():
    today = str(datetime.datetime.date(datetime.datetime.today()))
    periodJSON = OctopusEnergy.ReturnEnergyDataStr(today, 'tariff')
    print(json.dumps(periodJSON))
    confirm, periodTariffs = GetPeriodValues.GetArray(periodJSON)
    print(confirm)

process()