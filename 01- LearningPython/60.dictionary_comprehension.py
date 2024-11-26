# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
# -------------------------------------------------------------------------
# MATH EXPRESSION
cities_in_F = {'New York': 32, 'Boston': 75, "São Paulo": 77, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value - 32) * 5 / 9) for (key, value) in cities_in_F.items()}
print(cities_in_C)
# -------------------------------------------------------------------------
# EQUAL ==
weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)
# -------------------------------------------------------------------------
# IF , ELIF , ELSE
cities = cities_in_F
desc_cities = {key: "WARM" if value >= 75 else "COLD" for (key, value) in cities.items()}
print(desc_cities)


# -------------------------------------------------------------------------

# FUNCTION, MULTIPLE CRITERIA:
def check_temp(value):
    if value < 18:
        return "COLD"
    elif 19 <= value <= 25:
        return "PLEASANT"
    elif value >= 26:
        return "HOT"


cities = cities_in_C
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities)
# -------------------------------------------------------------------------
