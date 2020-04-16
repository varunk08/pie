from pygal.maps.world import COUNTRIES

def getCountryCode(countryName):
    for code, name in COUNTRIES.items():
        if name == countryName:
            return code

    return None