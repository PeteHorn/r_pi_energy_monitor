#utility imports
import json
import datetime
import paho.mqtt.client as mqtt_standard
import time


# function py file imports
import GetStats
import GetPeriodValues
import OctopusEnergy
import MQTT as mqtt_custom
import PersonalData

def test_always_passes():
    assert True

def test_always_fails():
    assert False

def test_calcAvg():
    numericArrayTestValue = [3.591, 3.465, 3.78, 4.452]
    result = GetStats.calcAvg(numericArrayTestValue)
    if result == 3.822:
        assert True
    else:
        assert False

def test_calcMaxMin():
    numericArrayTestValue = [3.591, 3.465, 3.78, 4.452]
    MaxResult, MinResult = GetStats.calcMaxMin(numericArrayTestValue)
    if MaxResult == 4.452:
        assert True
    else:
        assert False
    if MinResult == 3.465:
        assert True
    else:
        assert False

def test_getPeriodValues_validInput():
    jsonPeriodTestString = '[{"value_exc_vat":3.42,"value_inc_vat":3.591,"valid_from":"2020-03-29T23:30:00Z","valid_to":"2020-03-30T00:00:00Z"},{"value_exc_vat":3.3,"value_inc_vat":3.465,"valid_from":"2020-03-29T23:00:00Z","valid_to":"2020-03-29T23:30:00Z"},{"value_exc_vat":3.6,"value_inc_vat":3.78,"valid_from":"2020-03-29T22:30:00Z","valid_to":"2020-03-29T23:00:00Z"},{"value_exc_vat":4.24,"value_inc_vat":4.452,"valid_from":"2020-03-29T22:00:00Z","valid_to":"2020-03-29T22:30:00Z"}]'
    confirm, TestResult = GetPeriodValues.GetArray(jsonPeriodTestString)
    if TestResult == [3.591, 3.465, 3.78, 4.452]:
        assert True
    else:
        assert False
    if confirm == "valid":
        assert True
    else:
        assert False

def test_getPeriodValues_invalidInput():
    jsonPeriodTestString = 'this is an invalid input string'
    confirm, TestResult = GetPeriodValues.GetArray(jsonPeriodTestString)
    if TestResult == []:
        assert True
    else:
        assert False
    if confirm == "invalid":
        assert True
    else:
        assert False

def test_OctopusEnergy_createAPI():
    url = OctopusEnergy.createURL('2021-10-08', 'test')
    assert url == 'https://api.octopus.energy/v1/testURL/?period_from=2021-10-08T00:00:00Z&period_to=2021-10-08T23:59:00Z'

def test_OctopusEnergy_getDailyTariffInfo():
    expectedJSON = json.loads('[{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T23:30:00Z","valid_to":"2021-10-09T00:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T23:00:00Z","valid_to":"2021-10-08T23:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T22:30:00Z","valid_to":"2021-10-08T23:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T22:00:00Z","valid_to":"2021-10-08T22:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T21:30:00Z","valid_to":"2021-10-08T22:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T21:00:00Z","valid_to":"2021-10-08T21:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T20:30:00Z","valid_to":"2021-10-08T21:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T20:00:00Z","valid_to":"2021-10-08T20:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T19:30:00Z","valid_to":"2021-10-08T20:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T19:00:00Z","valid_to":"2021-10-08T19:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T18:30:00Z","valid_to":"2021-10-08T19:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T18:00:00Z","valid_to":"2021-10-08T18:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T17:30:00Z","valid_to":"2021-10-08T18:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T17:00:00Z","valid_to":"2021-10-08T17:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T16:30:00Z","valid_to":"2021-10-08T17:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T16:00:00Z","valid_to":"2021-10-08T16:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T15:30:00Z","valid_to":"2021-10-08T16:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T15:00:00Z","valid_to":"2021-10-08T15:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T14:30:00Z","valid_to":"2021-10-08T15:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T14:00:00Z","valid_to":"2021-10-08T14:30:00Z"},{"value_exc_vat":32.49,"value_inc_vat":34.1145,"valid_from":"2021-10-08T13:30:00Z","valid_to":"2021-10-08T14:00:00Z"},{"value_exc_vat":32.55,"value_inc_vat":34.1775,"valid_from":"2021-10-08T13:00:00Z","valid_to":"2021-10-08T13:30:00Z"},{"value_exc_vat":26.88,"value_inc_vat":28.224,"valid_from":"2021-10-08T12:30:00Z","valid_to":"2021-10-08T13:00:00Z"},{"value_exc_vat":32.89,"value_inc_vat":34.5345,"valid_from":"2021-10-08T12:00:00Z","valid_to":"2021-10-08T12:30:00Z"},{"value_exc_vat":28.56,"value_inc_vat":29.988,"valid_from":"2021-10-08T11:30:00Z","valid_to":"2021-10-08T12:00:00Z"},{"value_exc_vat":32.76,"value_inc_vat":34.398,"valid_from":"2021-10-08T11:00:00Z","valid_to":"2021-10-08T11:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T10:30:00Z","valid_to":"2021-10-08T11:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T10:00:00Z","valid_to":"2021-10-08T10:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T09:30:00Z","valid_to":"2021-10-08T10:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T09:00:00Z","valid_to":"2021-10-08T09:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T08:30:00Z","valid_to":"2021-10-08T09:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T08:00:00Z","valid_to":"2021-10-08T08:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T07:30:00Z","valid_to":"2021-10-08T08:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T07:00:00Z","valid_to":"2021-10-08T07:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T06:30:00Z","valid_to":"2021-10-08T07:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T06:00:00Z","valid_to":"2021-10-08T06:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T05:30:00Z","valid_to":"2021-10-08T06:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T05:00:00Z","valid_to":"2021-10-08T05:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T04:30:00Z","valid_to":"2021-10-08T05:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T04:00:00Z","valid_to":"2021-10-08T04:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T03:30:00Z","valid_to":"2021-10-08T04:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T03:00:00Z","valid_to":"2021-10-08T03:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T02:30:00Z","valid_to":"2021-10-08T03:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T02:00:00Z","valid_to":"2021-10-08T02:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T01:30:00Z","valid_to":"2021-10-08T02:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T01:00:00Z","valid_to":"2021-10-08T01:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T00:30:00Z","valid_to":"2021-10-08T01:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T00:00:00Z","valid_to":"2021-10-08T00:30:00Z"}]')
    results = OctopusEnergy.ReturnEnergyDataStr('2021-10-08', 'tariff')
    assert results == expectedJSON

testTopic = 'test_topic'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(testTopic)

response = str('')
def on_message(client, userdata, msg):
    print('hello')
    response = msg.payload
    print(response)

def test_MQTT_publishing():
    mqtt_client = mqtt_standard.Client()
    print('create')
    mqtt_client.on_connect = on_connect
    print('connect callback')
    mqtt_client.on_message = on_message
    print('message callback')
    mqtt_client.connect(PersonalData.getValues()['MQTT_IP'], 1883, 60)
    print('connected')
    testPacket = datetime.datetime.now().strftime("%H:%M:%S")
    testdata = []
    testdata.append({
        'topic': testTopic,
        'data': testPacket
    })
    testJSON = json.dumps(testdata)
    time.sleep(5)
    mqtt_custom.DailyUpdate(testJSON)
    time.sleep(5)
    print('published')
    assert response == testPacket