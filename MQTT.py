import paho.mqtt.client as mqtt
import PersonalData

def DailyUpdate(topic, data):
    client = mqtt.Client()
    client.connect(PersonalData.getValues()['MQTT_IP'], 1883, 60)
    client.publish(topic, payload=data, qos=0, retain=False)
    client.disconnect()