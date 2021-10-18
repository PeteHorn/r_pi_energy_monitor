import paho.mqtt.client as mqtt
import PersonalData
import json

def DailyUpdate(data):
    MQTT_client = mqtt.Client()
    MQTT_client.connect(PersonalData.getValues()['MQTT_IP'], 1883, 60)
    j = json.loads(data)
    for element in j:
        MQTT_client.publish(element['topic'], payload=element['data'], qos=0, retain=False)
    MQTT_client.disconnect()