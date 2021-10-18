import paho.mqtt.client as mqtt
import PersonalData
import json

def DailyUpdate(data):
    print(data)
    client = mqtt.Client()
    client.connect(PersonalData.getValues()['MQTT_IP'], 1883, 60)
    j = json.loads(data)
    for element in j:
        print(element)
        j = json.loads(element)
        print(j)
        client.publish(j['topic'], payload=j['data'], qos=0, retain=False)
    client.disconnect()