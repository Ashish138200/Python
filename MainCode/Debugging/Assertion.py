#Stop lightcode
market_2nd = {'ns': 'green', 'ew': 'red'}
def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    # assertions(sanity checks) are for detecting programmer errors that are not meant to be recovered from.user errors
    # should raise exception
    assert 'red' in market_2nd.values() , 'Neither light is red!' + str(intersection)
print(market_2nd)
switchLights(market_2nd)
print(market_2nd)