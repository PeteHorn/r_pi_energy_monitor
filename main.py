import MQTT as mqtt_custom
import paho.mqtt.client as mqtt_standard
import datetime
import time
import OctopusEnergy
import GetPeriodValues

def process():
    today = datetime.datetime.date(datetime.datetime.today())
    periodJSON = OctopusEnergy.ReturnEnergyDataStr(today, 'tariff')
    print(periodJSON)
    confirm, periodTariffs = GetPeriodValues.GetArray(periodJSON)
    print(periodTariffs)