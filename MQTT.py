import paho.mqtt.client as mqtt
import PersonalData


client = mqtt.Client()

client.connect(PersonalData.getValues['MQTT_IP'], 1883, 60)
client.publish('test_topic', payload='blah', qos=0, retain=False)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()