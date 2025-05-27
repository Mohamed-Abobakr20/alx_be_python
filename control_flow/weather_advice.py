"""
Create a Python script named weather_advice.py. This script will ask the user about the current weather conditions and provide clothing recommendations based on the input. This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program
"""

weather_state = input("What's the weather like today? (sunny/rainy/cold): ")
wear_recommend = ""

if weather_state == "sunny":
    wear_recommend = "Wear a t-shirt and sunglasses."
elif weather_state == "rainy":
    wear_recommend = "Don't forget your umbrella and a raincoat."
elif weather_state == "cold":
    wear_recommend = "Make sure to wear a warm coat and a scarf."
else:
    wear_recommend = "Sorry, I don't have recommendations for this weather."


print(wear_recommend)