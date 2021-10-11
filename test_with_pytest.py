#utility imports
import json
import datetime

# function py file imports
import GetStats
import GetPeriodValues
import OctopusEnergy
import InfluxDB_API
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
    if url == 'https://api.octopus.energy/v1/testURL/?period_from=2021-10-08T00:00:00Z&period_to=2021-10-08T23:59:00Z':
        assert True
    else:
        assert False

def test_OctopusEnergy_getDailyTariffInfo():
    expectedJSON = json.loads('[{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T23:30:00Z","valid_to":"2021-10-09T00:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T23:00:00Z","valid_to":"2021-10-08T23:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T22:30:00Z","valid_to":"2021-10-08T23:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T22:00:00Z","valid_to":"2021-10-08T22:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T21:30:00Z","valid_to":"2021-10-08T22:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T21:00:00Z","valid_to":"2021-10-08T21:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T20:30:00Z","valid_to":"2021-10-08T21:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T20:00:00Z","valid_to":"2021-10-08T20:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T19:30:00Z","valid_to":"2021-10-08T20:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T19:00:00Z","valid_to":"2021-10-08T19:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T18:30:00Z","valid_to":"2021-10-08T19:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T18:00:00Z","valid_to":"2021-10-08T18:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T17:30:00Z","valid_to":"2021-10-08T18:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T17:00:00Z","valid_to":"2021-10-08T17:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T16:30:00Z","valid_to":"2021-10-08T17:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T16:00:00Z","valid_to":"2021-10-08T16:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T15:30:00Z","valid_to":"2021-10-08T16:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T15:00:00Z","valid_to":"2021-10-08T15:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T14:30:00Z","valid_to":"2021-10-08T15:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T14:00:00Z","valid_to":"2021-10-08T14:30:00Z"},{"value_exc_vat":32.49,"value_inc_vat":34.1145,"valid_from":"2021-10-08T13:30:00Z","valid_to":"2021-10-08T14:00:00Z"},{"value_exc_vat":32.55,"value_inc_vat":34.1775,"valid_from":"2021-10-08T13:00:00Z","valid_to":"2021-10-08T13:30:00Z"},{"value_exc_vat":26.88,"value_inc_vat":28.224,"valid_from":"2021-10-08T12:30:00Z","valid_to":"2021-10-08T13:00:00Z"},{"value_exc_vat":32.89,"value_inc_vat":34.5345,"valid_from":"2021-10-08T12:00:00Z","valid_to":"2021-10-08T12:30:00Z"},{"value_exc_vat":28.56,"value_inc_vat":29.988,"valid_from":"2021-10-08T11:30:00Z","valid_to":"2021-10-08T12:00:00Z"},{"value_exc_vat":32.76,"value_inc_vat":34.398,"valid_from":"2021-10-08T11:00:00Z","valid_to":"2021-10-08T11:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T10:30:00Z","valid_to":"2021-10-08T11:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T10:00:00Z","valid_to":"2021-10-08T10:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T09:30:00Z","valid_to":"2021-10-08T10:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T09:00:00Z","valid_to":"2021-10-08T09:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T08:30:00Z","valid_to":"2021-10-08T09:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T08:00:00Z","valid_to":"2021-10-08T08:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T07:30:00Z","valid_to":"2021-10-08T08:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T07:00:00Z","valid_to":"2021-10-08T07:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T06:30:00Z","valid_to":"2021-10-08T07:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T06:00:00Z","valid_to":"2021-10-08T06:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T05:30:00Z","valid_to":"2021-10-08T06:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T05:00:00Z","valid_to":"2021-10-08T05:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T04:30:00Z","valid_to":"2021-10-08T05:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T04:00:00Z","valid_to":"2021-10-08T04:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T03:30:00Z","valid_to":"2021-10-08T04:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T03:00:00Z","valid_to":"2021-10-08T03:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T02:30:00Z","valid_to":"2021-10-08T03:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T02:00:00Z","valid_to":"2021-10-08T02:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T01:30:00Z","valid_to":"2021-10-08T02:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T01:00:00Z","valid_to":"2021-10-08T01:30:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T00:30:00Z","valid_to":"2021-10-08T01:00:00Z"},{"value_exc_vat":33.33,"value_inc_vat":34.9965,"valid_from":"2021-10-08T00:00:00Z","valid_to":"2021-10-08T00:30:00Z"}]')
    results = OctopusEnergy.ReturnEnergyDataStr('2021-10-08', 'tariff')
    assert results == expectedJSON

def test_InfluxDB_writePointsNoDateSpecified():
    json_body = [
        {
            "measurement": "energy_tariff",
            "date": "2021-10-10",
            "fields": {
                "Period_1": 0.67,
                "Period_2": 3.234,
                "Period_3": 23.422,
                "Period_4": 1.34
            }
        }
    ]
    InfluxDB_API.WriteData(json_body)
    result = InfluxDB_API.Query('Select Period_1 FROM energy_tariff').raw.items()[0][1][0]['values']
    revResult = result[::-1]
    assert revResult[0][1] == 0.67
    result = InfluxDB_API.Query('Select Period_2 FROM energy_tariff').raw.items()[0][1][0]['values']
    revResult = result[::-1]
    assert revResult[0][1] == 3.234
    result = InfluxDB_API.Query('Select Period_3 FROM energy_tariff').raw.items()[0][1][0]['values']
    revResult = result[::-1]
    assert revResult[0][1] == 23.422
    result = InfluxDB_API.Query('Select Period_4 FROM energy_tariff').raw.items()[0][1][0]['values']
    revResult = result[::-1]
    assert revResult[0][1] == 1.34

def test_InfluxDB_writePointsDateSpecified():
    today = datetime.date.today().__str__()
    json_body = [
        {
            "measurement": "energy_tariff",
            "fields": {
                "date": today,
                "Period_1": 0.767,
                "Period_2": 3.7234,
                "Period_3": 23.7422,
                "Period_4": 1.734
            }
        }
    ]
    print(json_body)
    InfluxDB_API.WriteData(json_body)
    result = list(InfluxDB_API.Query('Select date, Period_1 FROM energy_tariff'))
    print(result)
    print('-----------------------------------')
    revResult = result[0][::-1]
    print(revResult[0])
    j_res = json.loads(revResult[0])
    print('-----------------------------------')
    print(j_res)
    assert j_res('Period_1') == 0.67