def get_country_code(country):
    country_codes = {"United Kingdom": "gb", "United States": "us", "Austria": "at",
                     "Australia": "au", "Belgium": "be", "Brazil": "br", "Canada": "ca",
                     "Switzerland": "ch", "Germany": "de", "Spain": "es", "France": "fr",
                     "India": "in", "Italy": "it", "Mexico": "mx", "Netherlands": "nl", "New Zealand": "nz",
                     "Poland": "pl", "South Africa": "za", "Singapore": "sg"}
    return country_codes[country]
