from GetPeriodValues import GetArray

testString = '[{"value_exc_vat":3.42,"value_inc_vat":3.591,"valid_from":"2020-03-29T23:30:00Z","valid_to":"2020-03-30T00:00:00Z"},{"value_exc_vat":3.3,"value_inc_vat":3.465,"valid_from":"2020-03-29T23:00:00Z","valid_to":"2020-03-29T23:30:00Z"},{"value_exc_vat":3.6,"value_inc_vat":3.78,"valid_from":"2020-03-29T22:30:00Z","valid_to":"2020-03-29T23:00:00Z"},{"value_exc_vat":4.24,"value_inc_vat":4.452,"valid_from":"2020-03-29T22:00:00Z","valid_to":"2020-03-29T22:30:00Z"}]'

TestResult = GetArray(testString)

print(TestResult)
if (TestResult == [3.591, 3.465, 3.78, 4.452]):
    assert True
else:
    assert False