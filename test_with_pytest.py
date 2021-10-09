# test_with_pytest.py
import GetDailyStats
import GetPeriodValues

def test_always_passes():
    assert True

def test_always_fails():
    assert False

def test_calcAvg():
    numericArrayTestValue = [3.591, 3.465, 3.78, 4.452]
    result = GetDailyStats.calcAvg(numericArrayTestValue)
    if result == 3.822:
        assert True
    else:
        assert False

def test_calcMaxMin():
    numericArrayTestValue = [3.591, 3.465, 3.78, 4.452]
    MaxResult, MinResult = GetDailyStats.calcMaxMin(numericArrayTestValue)
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