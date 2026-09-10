import random

recipes = [
    {
        "name": "Bulgogi",
        "difficulty":"medium",
        "tags": ["Korean", "beef", "stir fry"],
        "ingredients": [
            {"item": "soy sauce", "amount": "1/3 cup"},
            {"item": "green onions", "amount": "2, segragated"},
            {"item": "yellow onion", "amount": "1/4, thinly sliced"},
            {"item": "white sugar", "amount": "3 tablespoons"},
            {"item": "garlic", "amount": "3 cloves minced"},
            {"item": "toasted sesame seeds", "amount": "2 tablespoons"},
            {"item": "sesame oil", "amount": "1 tablespoon"},
            {"item": "Korean red pepper flakes", "amount": "1/4 teaspoon"},
            {"item": "fresh ginger", "amount": "1/4 teaspoon, minced"},
            {"item": "black pepper", "amount": "1/8 teaspoon"},
            {"item": "beef sirloin steak", "amount": "1.5 pounds, cut very thin"},
            {"item": "honey", "amount": "1 teaspoon"}
        ]
    },
    {
        "name": "Fried Rice",
        "tags": ["Asian", "rice"],
        "ingredients": [
            {"item": "rice", "amount": "2 cups"},
            {"item": "egg", "amount": "2"},
            {"item": "soy sauce", "amount": "2 tablespoons"}
        ]
    },
    {
        "name":"Jerk Shrimp tacos",
        "tags": ["shrimp", "seafood", "tacos"],
        "difficulty":"easy",
        "ingredients":[
            {"item": "shrimp", "amount":"idk" },
            {"item": "garlic", "amount":"idk" },
            {"item":"salt", "amount": "idk"},
            {"item":"oil", "amount": "idk"},
            {"item":"hot sauce", "amount":"idk" },
        ]
    },
    {
        "name": "Mongolian Beef",
        "tags": ["Asian", "rice or noodles", "beef"],
        "difficulty":"hard",
        "ingredients":[
            {"item": "idk", "amount": "idk"},
        ]
    },
    {
        "name": "Tuna Casserole",
        "tags": ["casserole", "seafood"],
        "difficulty":"easy",
        "ingredients":[
            {"item": "tuna", "amount":  "idk"},
            {"item": "bow tie noodles", "amount": "idk"},
            {"item": "frozen peas and carrots", "amount": "idk"},
            {"item": "parmesan or cheddar", "amount": "idk"},
        ]
    },
    {
        "name": "Chicken Parm",
        "tags": ["italian", "chicken"],
        "difficulty":"medium",
        "ingredients":[
            {"item":"chicken breast", "amount": "amount of ppl *1.5"},
            {"item": "parmesan", "amount": "1/2 cup, grated"},
            {"item": "basil", "amount": "1/4 cup"},
            {"item": "oregano", "amount": "1 tsp."},
            {"item": "eggs", "amount": "3"},
            {"item": "crumbs, bead or cracker", "amount": "1 cup"},
            {"item": "parsley", "amount": "2 tbsp."},
            {"item": "garlic powder", "amount": "1/2 tsp."},
            {"item": "all pupose flour", "amount": "1 cup"}
        ],
        "steps":[
            "Preheat oven to 400 degrees F (200 degrees C).",
            "Pound breasts, then salt and pepper them.",
            "One bowl:Parmesan cheese, basil, oregano, parsley, and garlic powder. 2nd bowl, beat the eggs. 3rd bowl, place the flour."
            "Breasts go 3rd bowl, then 2nd, then 1st. Place on a baking sheet.",
            "400 degrees F, preheated, 30 minutes or not piink in middle."
        ]
    },
    {
        "name": "Poppy Seed Chicken Casserole",
        "difficulty":"medium",
        "tags": ["casserole", "rice", "chicken"],
        "ingredients":[
            {"item": "chicken breast", "amount": "idk"},
            {"item": "cream of chicken", "amount": "1 can"},
            {"item": "sour cream", "amount": "1 cup"},
            {"item": "crushed Ritz", "amount": "1.5 rolls"},
            {"item": "butter", "amount": "1/2 cup, melted"},
            {"item": "rice", "amount": "2 cups"},
        ]
    },
    {
        "name": "Asian Noodles",
        "difficulty":"medium",
        "tags": ["Asian", "pork", "steak", "noodles"],
        "ingredients": [
            {"item": "ground pork or steak", "amount": "1 package"},
            {"item": "bok choy", "amount": "1 bunch"},
            {"item": "carrots", "amount": "1"},
            {"item": "udon noodles", "amount": "1 packs"},
            {"item": "garlic", "amount": "2 cloves"},
            {"item": "soy sauce", "amount": "2 tablespoons"},
            {"item": "teriyaki sauce (optional)", "amount": "1 tablespoons"},
            {"item": "sesame oil (toasted)", "amount": "1 teaspoon"},
            {"item": "chili flakes or Korean chili flakes", "amount": "to taste"},
            {"item": "brown sugar or honey", "amount": "1 teaspoon"},
            {"item": "oil (for cooking)", "amount": "1 tablespoon"}
        ],
        "steps": [
            "Cook noodles according to package, then set aside",
            "Heat oil in a pan and cook meat until browned",
            "Add garlic and cook briefly",
            "Add vegetables and cook until slightly soft",
            "Add sauces, sesame oil, sugar, and chili flakes",
            "Add noodles and toss everything together",
            "Cook until heated through"
        ]
    },
    {
        "name":"calico beans",
        "tags": ["beans", "casserole"],
        "difficulty":"easy",
        "ingredients":[
            {"item":"kidney beans", "amount":"1 can"},
            {"item":"baked beans", "amount":"1 can"},
            {"item":"lima beans", "amount":"1 can"},
            {"item":"bacon", "amount":"1/2 cup, chopped"},
            {"item":"frozen peppers", "amount":"half a bag"},
            {"item":"brown sugar", "amount":"1 cup"},
            {"item":"ground beef", "amount":"1 pound"},
        ],
        "steps":[
            "cook beef and bacon",
            "put everything into a pot on medium"
        ]
    },
    {
        "name":"white chicken chili",
        "tags": ["chili", "chicken"],
        "difficulty":"medium",
        "ingredients":[
            {"item":"chicken breast", "amount":"1 lb"},
            {"item":"black beans", "amount":"1 can"},
            {"item":"kidney beans", "amount":"1 can"},
            {"item":"tomato sauce", "amount":"1 can"},
            {"item":"chili powder", "amount":"2 tbsp"},
            {"item":"cumin", "amount":"1 tsp"},
            {"item":"garlic powder", "amount":"1 tsp"},
        ]
    },
    {
        "name": "Pork tacos",
        "difficulty":"easy",
        "tags": ["tacos", "pork"],
        "ingredients": [
            {"item": "ground pork", "amount": "1 lb"},
            {"item": "frozen peppers and onions", "amount": "half a bag"},
            {"item": "cheese", "amount": "1/2 cup"},
            {"item": "tortillas", "amount": "6"},
            {"item": "sour cream", "amount": "2 tbsp"},
            {"item": "lime", "amount": "1"},
            {"item":"chili powder", "amount":"1 tsp"},
            {"item":"cumin", "amount":"1/2 tsp"},
            {"item":"garlic powder", "amount":"1/2 tsp"},
            {"item":"salt, pepper", "amount":"to taste"},
            {"item":"paprika", "amount":"1/2 tsp"},
        ],
        "steps": [
            "Mix chili powder, cumin, garlic powder, salt, pepper, and paprika together for seasoning",
            "Mix sour cream, lime juice, and chili powder together for sauce",
            "Assemble tacos with meat, cheese, and sauce",
            "bake at 350 for 10 minutes"
        ]
    },
    {
        "name":"Korean fried chicken",
        "tags": ["Korean", "chicken"],
        "servings": "4-6",
        "glaze ingredients": [
            {"item": "garlic(powder)", "amount": "10 cloves(2.5 tbsps)"},
            {"item": "canola oil", "amount": "1 tbsp"},
            {"item": "soy sauce", "amount": "1/2 cup"},
            {"item": "brown sugar", "amount": "1/2 cup"},
            {"item": "rice vinegar", "amount": "1/4 cup"},
            {"item": "cornstarch", "amount": "1 tbsp"},
            {"item": "water", "amount": "1 tbsp"},
            {"item": "gochujang (Korean chili paste)", "amount": "2 tbsps"},
            {"item": "toasted sesame oil", "amount": "2 tsps"},
        ],
        "chicken ingredients": [
            {"item": "boneless, skinless chicken thighs", "amount": "2-2 1/4 lbs"},
            {"item": "cornstarch", "amount": "2 cups"},
            {"item": "garlic powder", "amount": "2 tsps"},
            {"item": "salt", "amount": "2 1/2 tsps(divided)"},
            {"item": "white pepper", "amount": "1 1/2 tsps(divided)"},
            {"item": "black pepper", "amount": "1 1/2 tsps(divided)"},
            {"item": "garlic", "amount": "3 cloves"},
            {"item": "ginger", "amount": "1 1inch piece"},
            {"item": "cold water", "amount": "3/4 cup"},
            {"item": "soy sauce", "amount": "1 tbsp"},
            {"item": "rice vinegar", "amount": "1 tbsp"},
            {"item": "canola oil", "amount": "5 cups for frying"},
        ],
        "glaze steps": [
            "1. Heat 1 tbsp oil in a pan and cook garlic until fragrant",
            "2. Add soy sauce, brown sugar, rice vinegar. Increase the heat to medium high.",
            "3. Whisk cornstarch and water together, until cornstarch is suspended, then add to the pan. Cook until thickened."
        ],
    }
]

def get_recipes_by_tag(recipes, tag):
    matches = []
    for recipe in recipes:
        if tag in recipe["tags"]:
            matches.append(recipe)
    return matches

def which_recipe():
    print("What are we making tonight?\n")

    # show list
    for i, recipe in enumerate(recipes, start=1):
        print(i, "-", recipe["name"])

    # get input
    choice = int(input("\nEnter a number: "))

    # get recipe
    selected = recipes[choice - 1]

    # output recipe
    print("\nYou chose:", selected["name"])

    print("\nIngredients:")
    for ing in selected["ingredients"]:
        print("-", ing["amount"], ing["item"])

    if "steps" in selected:
        print("\nSteps:")
        for i, step in enumerate(selected["steps"], start=1):
            print(i, ".", step)

get_recipes_by_tag(7, "chicken")