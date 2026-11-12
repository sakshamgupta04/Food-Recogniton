"""
=============================================================================
Food Recognition & Recipe Finder - Culinary Knowledgebase & Nutrition
Author: Saksham Gupta
GitHub: https://github.com/sakshamgupta04
Repository: https://github.com/sakshamgupta04/Food-Recogniton
Copyright (c) 2026 Saksham Gupta. All rights reserved.
=============================================================================
"""

food_database = {
    "spaghetti bolognese": {
        "origin": "Italy (Bologna)",
        "nutrition": {"calories": "480 kcal", "protein": "24g", "carbs": "62g", "fat": "15g"},
        "ingredients": ["Spaghetti", "Ground Beef / Pork", "Tomatoes", "Onion", "Garlic", "Olive Oil", "Oregano", "Parmesan"],
        "recipe": "Brown minced meat with onions and garlic. Add tomato puree and simmer for 25-30 minutes. Boil spaghetti in salted water until al dente. Combine and top with fresh grated Parmesan cheese."
    },
    "spaghetti carbonara": {
        "origin": "Italy (Rome)",
        "nutrition": {"calories": "560 kcal", "protein": "22g", "carbs": "58g", "fat": "27g"},
        "ingredients": ["Spaghetti", "Guanciale / Pancetta", "Egg Yolks", "Pecorino Romano", "Black Pepper"],
        "recipe": "Crisp guanciale in a pan. Whisk egg yolks with grated pecorino and plenty of black pepper. Toss hot drained pasta with pork, remove from heat, and quickly stir in egg mixture to form a creamy sauce."
    },
    "gnocchi": {
        "origin": "Italy",
        "nutrition": {"calories": "390 kcal", "protein": "11g", "carbs": "65g", "fat": "9g"},
        "ingredients": ["Potato Gnocchi", "Tomato Sauce / Butter Sage", "Garlic", "Parmesan", "Fresh Basil"],
        "recipe": "Boil potato gnocchi in salted water until they float to the surface (2-3 minutes). Toss gently in warm marinara sauce or browned sage butter, and finish with grated Parmesan."
    },
    "pasta": {
        "origin": "Italy",
        "nutrition": {"calories": "420 kcal", "protein": "14g", "carbs": "70g", "fat": "8g"},
        "ingredients": ["Pasta", "Tomato Sauce", "Garlic", "Olive Oil", "Basil"],
        "recipe": "Boil pasta in salted water until al dente. Heat olive oil with garlic, add tomato sauce, toss with pasta, and garnish with basil."
    },
    "pizza": {
        "origin": "Italy (Naples)",
        "nutrition": {"calories": "680 kcal (2 slices)", "protein": "28g", "carbs": "72g", "fat": "30g"},
        "ingredients": ["Pizza Dough", "Tomato Sauce", "Mozzarella Cheese", "Fresh Basil", "Olive Oil"],
        "recipe": "Stretch pizza dough into a round base. Spread tomato sauce, add fresh mozzarella and basil leaves. Bake in a preheated oven at maximum temperature (or pizza oven) until golden and bubbly."
    },
    "sushi": {
        "origin": "Japan",
        "nutrition": {"calories": "320 kcal (6 rolls)", "protein": "18g", "carbs": "52g", "fat": "4g"},
        "ingredients": ["Sushi Rice", "Fresh Raw Fish (Salmon/Tuna)", "Nori (Seaweed)", "Rice Vinegar", "Soy Sauce", "Wasabi"],
        "recipe": "Season steamed short-grain rice with rice vinegar. Lay nori on a bamboo mat, spread rice evenly, place fish and vegetable strips, and roll firmly. Slice into bite-sized pieces and serve with wasabi and soy sauce."
    },
    "ramen": {
        "origin": "Japan",
        "nutrition": {"calories": "540 kcal", "protein": "26g", "carbs": "68g", "fat": "19g"},
        "ingredients": ["Ramen Noodles", "Pork/Chicken Broth", "Chashu Pork", "Soft-boiled Egg", "Scallions", "Nori", "Soy Sauce / Miso"],
        "recipe": "Simmer seasoned rich broth. Cook fresh ramen noodles until chewy. Pour hot broth into a serving bowl, add noodles, and arrange sliced chashu, ajitsuke tamago (marinated egg), scallions, and nori on top."
    },
    "hamburger": {
        "origin": "United States / Germany",
        "nutrition": {"calories": "580 kcal", "protein": "32g", "carbs": "44g", "fat": "29g"},
        "ingredients": ["Beef Patty", "Burger Buns", "Cheddar Cheese", "Lettuce", "Tomato", "Pickles", "Onion", "Burger Sauce"],
        "recipe": "Season ground beef and sear patties in a hot skillet for 3-4 minutes per side. Melt cheese on top. Toast buns, spread sauce, add lettuce, tomato, patty, pickles, and serve immediately."
    },
    "french fries": {
        "origin": "Belgium / France",
        "nutrition": {"calories": "365 kcal (medium)", "protein": "4g", "carbs": "48g", "fat": "17g"},
        "ingredients": ["Russet Potatoes", "Vegetable Oil", "Fine Sea Salt"],
        "recipe": "Cut potatoes into batons and soak in cold water. Par-fry at 150°C (300°F) until tender. Drain, rest, and second-fry at 190°C (375°F) until golden brown and crispy. Toss with salt immediately."
    },
    "tacos": {
        "origin": "Mexico",
        "nutrition": {"calories": "450 kcal (3 tacos)", "protein": "26g", "carbs": "36g", "fat": "22g"},
        "ingredients": ["Corn Tortillas", "Seasoned Beef / Pork / Chicken", "Cilantro", "Diced Onions", "Lime", "Salsa"],
        "recipe": "Warm soft corn tortillas on a dry griddle. Fill with grilled seasoned meat, top with fresh chopped onions, cilantro, a squeeze of fresh lime juice, and spicy salsa."
    },
    "pad thai": {
        "origin": "Thailand",
        "nutrition": {"calories": "520 kcal", "protein": "21g", "carbs": "74g", "fat": "16g"},
        "ingredients": ["Rice Noodles", "Shrimp / Chicken / Tofu", "Eggs", "Tamarind Paste", "Fish Sauce", "Bean Sprouts", "Crushed Peanuts", "Lime"],
        "recipe": "Stir-fry shrimp or tofu in hot oil. Add beaten eggs and scramble lightly. Add soaked rice noodles and tamarind-based sauce. Stir in bean sprouts and garlic chives, then serve topped with crushed peanuts and lime wedges."
    },
    "apple pie": {
        "origin": "England / United States",
        "nutrition": {"calories": "410 kcal (1 slice)", "protein": "3g", "carbs": "58g", "fat": "19g"},
        "ingredients": ["Flaky Pie Crust", "Sliced Tart Apples (Granny Smith)", "Sugar", "Cinnamon", "Nutmeg", "Butter"],
        "recipe": "Toss sliced apples with cinnamon, nutmeg, sugar, and flour. Place into rolled pie crust, dot with butter, and cover with top crust. Vent steam and bake at 190°C (375°F) for 50 minutes until golden."
    },
    "lasagna": {
        "origin": "Italy (Naples/Bologna)",
        "nutrition": {"calories": "580 kcal", "protein": "31g", "carbs": "46g", "fat": "28g"},
        "ingredients": ["Lasagna Noodles", "Bolognese Meat Sauce", "Béchamel / Ricotta", "Mozzarella", "Parmesan"],
        "recipe": "Layer pasta sheets with rich bolognese sauce, creamy béchamel, and grated cheese. Repeat layers and top with extra mozzarella. Bake at 180°C (350°F) for 35 minutes until bubbling and golden."
    },
    "guacamole": {
        "origin": "Mexico",
        "nutrition": {"calories": "160 kcal (1/2 cup)", "protein": "2g", "carbs": "9g", "fat": "14g"},
        "ingredients": ["Ripe Avocados", "Lime Juice", "Red Onion", "Jalapeño", "Cilantro", "Tomato", "Salt"],
        "recipe": "Mash ripe avocados in a bowl with a fork. Gently fold in finely minced onion, jalapeño, cilantro, diced tomatoes, lime juice, and salt to taste. Serve with crispy tortilla chips."
    },
    "caesar salad": {
        "origin": "Mexico (Tijuana)",
        "nutrition": {"calories": "310 kcal", "protein": "9g", "carbs": "14g", "fat": "24g"},
        "ingredients": ["Romaine Lettuce", "Croutons", "Parmesan Cheese", "Caesar Dressing (Egg yolk, anchovy, garlic, lemon, olive oil)"],
        "recipe": "Chop crisp romaine lettuce. Toss with prepared creamy Caesar dressing, garlic croutons, and shaved Parmigiano-Reggiano."
    },
    "ice cream": {
        "origin": "Global / Ancient China & Europe",
        "nutrition": {"calories": "270 kcal (1 cup)", "protein": "5g", "carbs": "32g", "fat": "14g"},
        "ingredients": ["Heavy Cream", "Whole Milk", "Sugar", "Egg Yolks", "Vanilla Extract"],
        "recipe": "Heat milk and sugar. Whisk hot milk into egg yolks to temper, cook until custard coats back of a spoon. Chill thoroughly, stir in vanilla and cream, churn in ice cream maker, and freeze."
    },
    "dumplings": {
        "origin": "China",
        "nutrition": {"calories": "380 kcal (6 pcs)", "protein": "18g", "carbs": "42g", "fat": "14g"},
        "ingredients": ["Dumpling Wrappers", "Minced Pork / Chicken", "Chinese Cabbage", "Ginger", "Scallions", "Soy Sauce", "Sesame Oil"],
        "recipe": "Mix filling ingredients thoroughly. Place a spoonful onto each wrapper, moisten edges with water, pleat and seal tightly. Pan-fry until bottom is golden, add water, cover to steam through."
    },
    "steak": {
        "origin": "Global",
        "nutrition": {"calories": "610 kcal (8 oz)", "protein": "52g", "carbs": "0g", "fat": "43g"},
        "ingredients": ["Thick-cut Ribeye / Sirloin Steak", "Coarse Salt", "Black Pepper", "Butter", "Garlic", "Rosemary / Thyme"],
        "recipe": "Season room-temperature steak liberally with salt and pepper. Sear in a screaming-hot cast iron skillet with oil for 3 minutes per side. Add butter, crushed garlic, and herbs; baste steak continuously until desired doneness."
    },
    "chocolate cake": {
        "origin": "United States / Europe",
        "nutrition": {"calories": "450 kcal (1 slice)", "protein": "5g", "carbs": "60g", "fat": "22g"},
        "ingredients": ["Flour", "Cocoa Powder", "Sugar", "Baking Powder", "Eggs", "Milk", "Butter", "Chocolate Ganache / Frosting"],
        "recipe": "Whisk dry ingredients together. Combine melted butter, eggs, and milk. Mix wet and dry together until smooth. Pour into greased cake pans and bake at 175°C (350°F) for 30 minutes. Cool and frost."
    }
}

def get_food_info(food_name: str) -> dict:
    """
    Returns information regarding origin, ingredients, recipe, and nutrition for the food dish.
    Falls back to partial matching or structured defaults if not in database.
    """
    cleaned = food_name.strip().lower()

    # 1. Exact match
    if cleaned in food_database:
        return food_database[cleaned]

    # 2. Key word / Substring match
    for key, data in food_database.items():
        if key in cleaned or cleaned in key:
            return data

    # 3. Intelligent default for unlisted dishes
    return {
        "origin": "International / Traditional Recipe",
        "nutrition": {"calories": "~400 kcal", "protein": "~15g", "carbs": "~50g", "fat": "~15g"},
        "ingredients": [
            f"Fresh ingredients typically used in preparing {food_name}",
            "Herbs & Spices to taste",
            "Cooking Oil or Butter",
            "Salt & Pepper"
        ],
        "recipe": f"Carefully prepare and season the ingredients for {food_name}. Cook following traditional culinary techniques until properly done, and serve fresh and warm."
    }
