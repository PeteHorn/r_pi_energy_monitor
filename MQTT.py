import paho.mqtt.client as mqtt
import PersonalData
import json

def DailyUpdate(data):
    client = mqtt.Client()
    client.connect(PersonalData.getValues()['MQTT_IP'], 1883, 60)
    for element in data:
        j = json.loads(element)
        client.publish(j['topic'], payload=j['data'], qos=0, retain=False)
    client.disconnect()