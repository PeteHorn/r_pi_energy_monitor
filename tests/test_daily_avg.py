from tariff_functions import GetDailyAvg

result = GetDailyAvg.calcAvg("blah")

if (result == 3.5):
    assert True
else:
    assert False