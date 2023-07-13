# Normally you'd have your library imports at the top of the script
# these contain functions that aren't included by default in python
# you need to install these using 'conda install xxxx' where xxxx is the package name
# using the command line (not the python console)


import requests
from requests.auth import HTTPBasicAuth

# This is a sample Python script.
# initializing Dictionary
# RecipeBook = {
#    "chilli": ["stock", "Tomatoes", "beef mince", "onion", "tomato puree", "sugar"],
#    "hot dog": ["bun", "sausage"],
#   "Casserole": ["beef", "beer", "cornflour", "stock"]
# }


# initializing search key string
# Pantry_items = input("Enter ingredient 1: ")


# res = [val for key, val in RecipeBook.items() if Pantry_items in val]
# printing result
# print("Ingredients in recipe: " + str(res))

# Using dict() + filer() + lambda
# Substring key match in dictionary - Returns recipe and ingredients
# res = dict(filter(lambda item: Pantry_items in item[1], RecipeBook.items()))

# printing result
# print("Recipes with your ingredients : " + str(res))

# printing just the keys of the search
# Search_results = res.keys()
# print("Recipe names " + str(Search_results))




# First create an api call on https://spoonacular.com/food-api/docs#Search-Recipes-Complex <- (use this API endpoint
# instead of the one in the example below, just replace it and add author as a header)
# this should return a list of recipe IDs for your own recipes if you use the author parameter

# Feed the IDs extracted from the previous API call into this api call to get recipe information
# https://spoonacular.com/food-api/docs#Get-Recipe-Information-Bulk
# This should return stuff like ingredients ect

# Next step would probably be to convert the output of the previous API call into a format
# which you can match your ingredients to

# Enter ingredients in an input or a list that you want to search your recipes for

# This is an example of how you can make an API call. You'll need to copy this but use the
# relevant URL endpoints for the steps above:

import urllib.parse
import requests
import webbrowser

# Define ingredients in list
# test_list = ['beef mince','onion']
Pantry_items = input("Enter ingredient 1: ")
#test_list = [Pantry_items]

# This converts the list of ingredients into a string of comma separated ingredients which
# is the format required by the api
# test_string = ','.join(test_list)


# Base url for calling API endpoint.
url = f'https://api.spoonacular.com/recipes/complexSearch'

# Define spoonacular username
username = 'pantrypals'

# Define parameters
params = {
    'apiKey': 'a9f8933985dd4c2285428df3faf937a4',
    'ingredients': Pantry_items,
    'author': 'pantrypals',
    'number': 100 #adjust if more recipes required
}

# Make API request for recipes by author
response = requests.get(url, params=params)


# Handle the response: After making the API request, you should handle the response appropriately.
# Check the status code of the response and process the data accordingly.
# if status code is 200, you can extract and work with the returned data

if response.status_code == 200:
    data = response.json()
    recipes = data['results']

    # process the filtered recipe data
    if recipes:
        for i, recipe in enumerate(recipes,1):
            recipe_name = recipe['title']
            print(f"{i}. {recipe_name}")

        # Prompt user to choose recipe
    try:
        choice = int(input("Choose Recipe Number Bitch:"))

        # Validate response
        if choice < 1 or choice > len(recipes):
            print("can you type cunt? Try again")
        else:
            selected_recipe = recipes[choice - 1]
            if 'id' in selected_recipe:
                recipe_id = selected_recipe['id']
                recipe_name_encoded = urllib.parse.quote_plus(recipe_name)
                recipe_url = f"https://spoonacular.com/recipes/{recipe_name_encoded}-{recipe_id}"
                # Open web browser
                webbrowser.open(recipe_url)
            else:
                print("id not found")

    except ValueError:
            print("idiot. Enter a number")

    else:
        print("no recipe found")

else:
    print(f"request failed with status code {response.status_code}")





