import paho.mqtt.client as mqtt
import PersonalData

def DailyUpdate(topic, data):
    client.publish(topic, payload=data, qos=0, retain=False)

client = mqtt.Client()
client.connect(PersonalData.getValues()['MQTT_IP'], 1883, 60)
DailyUpdate('test_topic', 'blah blah blah')
client.disconnect()