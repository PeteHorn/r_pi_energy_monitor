URLs = {
    'test': 'testURL',
    'tariff': 'products/AGILE-18-02-21/electricity-tariffs/E-1R-AGILE-18-02-21-H/standard-unit-rates'
}

def createURL (date, type):
    return 'https://api.octopus.energy/v1/' + URLs[type] + '/?period_from=' + date + 'T00:00:00Z&period_to=' + date + 'T23:59:00Z'