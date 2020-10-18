from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    for code , name in COUNTRIES.items():
        if name  == country_name:
            return code
    return None

# The COUNTRIES is a set of Thousands of international country code names
# If the country has a code then it would be returned with get_country_code
