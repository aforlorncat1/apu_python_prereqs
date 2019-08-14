# PROGRAM IngredientAdjuster
# BEGIN
# Assign variables to denote ingredients required to make 1 batch of 48 cookies as per recipe
#     cookies_per_recipe = 48
#     sugar_recipe = 1.5
#     butter_recipe = 1
#     flour_recipe = 2.75
# Calculate amount of each ingredient to make the number of the user's input
#     sugar_batch = sugar_recipe/cookies_per_recipe*user_input
#     butter_batch = butter_recipe/cookies_per_recipe*user_input
#     flour_batch = flour_recipe/cookies_per_recipe*user_input
# Ask user for input: "how many cookies to make?" and assign value to a variable user_cookies
# Add basic validation to check that input is a valid integer. 
#     user_cookies = user_input
# Calculate amount of each ingredient to produce amount of cookies equivalent to user_cookies and print out the results to user. 
#     Print user_cookies * [INGREDIENT]_single for each ingredient
# END

cookies_per_recipe = 48
sugar_recipe = 1.5
butter_recipe = 1
flour_recipe = 2.75

def check_input(s):
    while s.isdigit() == False:
        s = input("How many cookies would you like to make? Please input a positive, whole number")
    return int(s)

user_cookies = check_input(input("How many cookies would you like to make?"))

# Amount of ingredients to make the user's cookie amount
sugar_batch = sugar_recipe/cookies_per_recipe*user_cookies
butter_batch = butter_recipe/cookies_per_recipe*user_cookies
flour_batch = flour_recipe/cookies_per_recipe*user_cookies

# Output
print('To make {} cookies, you will need {} cups of sugar, {} cups of butter and {} cups of flour'.format(user_cookies, sugar_batch, butter_batch, flour_batch))
