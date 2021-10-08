from GetDailyAvg import calcAvg

def test_calcAvg():
    result = calcAvg()

    if (result == 3.5):
        assert True