


~~~~~~~~~~~~~~~
Recipe Roulette
~~~~~~~~~~~~~~~

A python script searches for a recipe "semi-randomly" using recipepuppy.com's API (http://www.recipepuppy.com/about/api/).
The user has the option of inputting an ingredient they would like the recipe to use, if they do not input
an ingredient one will be chosen at random to guide the search.

~~~~~~~~~~~~~~~
How it works
~~~~~~~~~~~~~~~

Recipepuppy.com’s API has to following base structure:

http://www.recipepuppy.com/api/?

Some optional parameters for this URL are:
i : ingredients
p : page

For example: http://www.recipepuppy.com/api/?i=onions&p=3 will return page 3 of a search for recipes that include onions as an ingredient. See http://www.recipepuppy.com/about/api/ for more details. 

This script asks a user to input a preferred ingredient to guide a recipe search. If the user does not have any ingredient preference, the script will choose an ingredient at random from a list to guide the search. Once an ingredient is chosen (either by user input or at random), the ingredient is appended to the API URL in addition to a random integer to designate the search page number. 

Using this newly generated URL a request is made to recipepuppy.com which returns the results page of a search. These results are in JSON format by default. Finally, the script chooses one of these recipes at random (there are usually multiple recipes on a page) and returns a link to that recipe.

See: http://www.recipepuppy.com/ for more details.

