"""
Recipe Roulette
~~~~~~~~~~~~~~~

Script searches for a random recipe using recipepuppy.com's API (http://www.recipepuppy.com/about/api/).
The user has the option of inputting an ingredient they would like the recipe to use, if they do not input
an ingredient one will be chosen at random to guide the search.

See: http://www.recipepuppy.com/ for more details.
"""
from default_ingedient_list import default_ingredient_list
import random
import requests
import time

def get_user_ingredient():
    """Gets a preferred ingredient from the user, which will be used to guide the 'random' recipe search.
    """
    while True:
        user_chosen_ingredient = input('Please enter your ingredient of choice and press \'enter\' when finished!')
        if not user_chosen_ingredient.isalpha():
            print('I\'m sorry we only take alphabet input here.')
            continue
        else:
            return user_chosen_ingredient
            break

def get_random_ingredient():
    """Generates a random ingredient to guide the recipe search.
    """
    random_ingredient = random.choice(default_ingredient_list)
    return random_ingredient

def get_user_input():
    """Asks the user if they have a preference for an ingredient, which is used to guide the recipe search.
    If they don't have a preference a function is called to generate an ingredient randomly to guide the recipe search.
    """
    while True:
        user_input = input('Do you have a type of ingredient you would like to work with? (enter \'y\' or \'n\')')
        if user_input.lower() == 'y':
            user_ingredient = get_user_ingredient()
            print('Great! We\'ll try to find something including {} as an ingredient.'
                  .format(user_ingredient.lower()))
            break
        elif user_input.lower() == 'n':
            user_ingredient = get_random_ingredient()
            print('That\'s okay, we\'ll pick something out for you! \n'
                  'Why don\'t we try something including {} as an ingredient.'
                  .format(user_ingredient.lower()))
            break
        else:
            print('I did not understand could you try that again?')
            continue
    return user_ingredient

def get_random_recipe():
    """Retrieves a random recipe link using recipepuppy.com API (http://www.recipepuppy.com/about/api/).
    The API usese the following format and return JSON:

    Example:
    http://www.recipepuppy.com/api/?i=onions&p=3

    Parameters:
    i : ingredients
    p : page

    If JSON is returned empty after two attempts to get recipe link, there may be no recipe that
    uses that ingredient and process will exit to prevent spamming recipepuppy.com.
    """
    ingredient = get_user_input()
    try_counter = 0
    while True:
        sanitize_ingredient_for_url = ingredient.replace(' ', '+')
        url = 'http://www.recipepuppy.com/api/?i={}&p={}'.format(sanitize_ingredient_for_url, random.randint(1,100))
        request_recipe = requests.get(url)
        if request_recipe.status_code == 200:
            try:
                request_recipe_json = request_recipe.json()
                random_result = random.choice(request_recipe_json['results'])
                random_result_link = (random_result['href'])
            except IndexError:
                print('Hold please...')
                try_counter += 1
                time.sleep(10)
                if try_counter == 2:
                    print('Hmm not much is coming back on this request, maybe we should try again.')
                    break
            else:
                return random_result_link
                break
        else:
            print(request_recipe.status_code)
            print('Sorry there was en error.')
            break

while True:
    random_recipe = get_random_recipe()
    if random_recipe:
        print(random_recipe)
        break
    else:
        continue




