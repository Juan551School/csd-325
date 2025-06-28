# Juan Macias Vasquez
# Date 06/27/2025
# Module 7.2
# city_functions.py

def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result


# Call the function three times with different combinations
print(city_country("santiago", "chile", 5000000, "Spanish" ))
print(city_country("paris", "france"))
print(city_country("tokyo", "japan", 6661949))