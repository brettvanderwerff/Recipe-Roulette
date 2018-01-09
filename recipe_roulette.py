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
import webbrowser # this is a module included in the standard library that allows Python to open the user's browser 

def get_user_ingredient():
    """Gets a preferred ingredient from the user, which will be used to guide the 'random' recipe search.
    """
    while True:
        user_chosen_ingredient = input('Please enter your ingredient of choice and press \'enter\' when finished!')
        if not (user_chosen_ingredient.strip()).isalpha(): # replaced .replace(' ', '') with .strip(), which is a string method
            print('I\'m sorry we only take alphabet input here.')      # that accomplishes the same thing, with the added benefit 
            continue                                                   # of being able to remove multiple spaces or tab characters
        else:
            return user_chosen_ingredient

def get_random_ingredient():
    """Generates a random ingredient to guide the recipe search.
    """
    # removed needless variable here  
    return random.choice(default_ingredient_list) # and moved the logic of the function to the return statement

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
            user_ingredient = get_random_ingredient() # this is a bit unneccesarry, can very easily inline this function's logic 
            print('That\'s okay, we\'ll pick something out for you! \n'
                  'Why don\'t we try something including {} as an ingredient?' # replaced period with question mark
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
        sanitized_ingredient_for_url = ingredient.replace(' ', '+') # using verbs to name variables is bad practice 
        url = 'http://www.recipepuppy.com/api/?i={}&p={}'.format(sanitized_ingredient_for_url, random.randint(1,100))
        request_recipe = requests.get(url) # url doesn't need to be a var if this is the only place it's going to be evoked
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
            print('Sorry there was an error.') # there was a small typo here
            break


def main():
        while True:
            random_recipe = get_random_recipe()
            if random_recipe:
                print('opening {} in your browser'.format(random_recipe)) #
                webbrowser.open_new_tab(random_recipe) # this opens a new tab in the user's browser if their browser is open, will 
                break                                  # launch the user's browser before opening a new tab otherwise
            else:
                continue

if __name__ == '__main__': # this tells the Python interpreter whether the program is being evoked directly and should run main()
        main()             # or being imported into another program so that it's other functions may be used 


