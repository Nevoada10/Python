# File Name: celsiustofahrenheit.py
# Author: Uriel Neves Silva
# Github: https://github.com/nevoada10
# Function: Converts Celsius to Fahrenheit

from typing import List

def celsius_to_fahrenheit(celsius : float) -> float:
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


if __name__ == "__main__":
    print(celsius_to_fahrenheit(30))