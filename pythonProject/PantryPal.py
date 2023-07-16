
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



# Base url for calling API endpoint.
url = f'https://api.spoonacular.com/recipes/complexSearch'

# Define spoonacular username
username = 'pantrypals'

# Define parameters
params = {
    'apiKey': 'a9f8933985dd4c2285428df3faf937a4',
    'ingredients': Pantry_items,
    'includeIngredients': Pantry_items,
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

# process recipe name data
    if recipes:
        for i, recipe in enumerate(recipes,1):
            recipe_name = recipe['title']
            print(f"{i}. {recipe_name}")
    else:
        print("nada")

    try:
        choice = int(input("Choose Recipe Number Bitch:"))

        # validate response
        if choice < 1 or choice > len(recipes):
            print("can you type a number?")
        else:
            selection = recipes[choice - 1]
            print("You have chosen:", selection)
            if 'id' and 'title' in selection:
                selection_id = selection['id']
                selection_name = selection['title']
                #URL encoding
                selection_name_encoded = urllib.parse.quote_plus(selection_name)
                selection_url = f"https://spoonacular.com/recipes/{selection_name_encoded}-{selection_id}"
                print(selection_url)
                # Open in browser
                webbrowser.open(selection_url)
            else:
                print('id or title not found')

    except ValueError:
            print("idiot. Enter a number")

else:
    print("No recipes found.")