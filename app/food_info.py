"""
Food information database mapping food items to origin, ingredients, and recipe.
"""

food_database = {
    "spaghetti bolognese": {
        "origin": "Italy (Bologna)",
        "ingredients": ["Spaghetti", "Ground Beef / Pork", "Tomatoes", "Onion", "Garlic", "Olive Oil", "Oregano", "Parmesan"],
        "recipe": "Brown minced meat with onions and garlic. Add tomato puree and simmer for 25-30 minutes. Boil spaghetti in salted water until al dente. Combine and top with fresh grated Parmesan cheese."
    },
    "spaghetti carbonara": {
        "origin": "Italy (Rome)",
        "ingredients": ["Spaghetti", "Guanciale / Pancetta", "Egg Yolks", "Pecorino Romano", "Black Pepper"],
        "recipe": "Crisp guanciale in a pan. Whisk egg yolks with grated pecorino and plenty of black pepper. Toss hot drained pasta with pork, remove from heat, and quickly stir in egg mixture to form a creamy sauce."
    },
    "pasta": {
        "origin": "Italy",
        "ingredients": ["Pasta", "Tomato Sauce", "Garlic", "Olive Oil", "Basil"],
        "recipe": "Boil pasta in salted water until al dente. Heat olive oil with garlic, add tomato sauce, toss with pasta, and garnish with basil."
    },
    "pizza": {
        "origin": "Italy (Naples)",
        "ingredients": ["Pizza Dough", "Tomato Sauce", "Mozzarella Cheese", "Fresh Basil", "Olive Oil"],
        "recipe": "Stretch pizza dough into a round base. Spread tomato sauce, add fresh mozzarella and basil leaves. Bake in a preheated oven at maximum temperature (or pizza oven) until golden and bubbly."
    },
    "sushi": {
        "origin": "Japan",
        "ingredients": ["Sushi Rice", "Fresh Raw Fish (Salmon/Tuna)", "Nori (Seaweed)", "Rice Vinegar", "Soy Sauce", "Wasabi"],
        "recipe": "Season steamed short-grain rice with rice vinegar. Lay nori on a bamboo mat, spread rice evenly, place fish and vegetable strips, and roll firmly. Slice into bite-sized pieces and serve with wasabi and soy sauce."
    },
    "ramen": {
        "origin": "Japan",
        "ingredients": ["Ramen Noodles", "Pork/Chicken Broth", "Chashu Pork", "Soft-boiled Egg", "Scallions", "Nori", "Soy Sauce / Miso"],
        "recipe": "Simmer seasoned rich broth. Cook fresh ramen noodles until chewy. Pour hot broth into a serving bowl, add noodles, and arrange sliced chashu, ajitsuke tamago (marinated egg), scallions, and nori on top."
    },
    "hamburger": {
        "origin": "United States / Germany",
        "ingredients": ["Beef Patty", "Burger Buns", "Cheddar Cheese", "Lettuce", "Tomato", "Pickles", "Onion", "Burger Sauce"],
        "recipe": "Season ground beef and sear patties in a hot skillet for 3-4 minutes per side. Melt cheese on top. Toast buns, spread sauce, add lettuce, tomato, patty, pickles, and serve immediately."
    },
    "french fries": {
        "origin": "Belgium / France",
        "ingredients": ["Russet Potatoes", "Vegetable Oil", "Fine Sea Salt"],
        "recipe": "Cut potatoes into batons and soak in cold water. Par-fry at 150°C (300°F) until tender. Drain, rest, and second-fry at 190°C (375°F) until golden brown and crispy. Toss with salt immediately."
    },
    "tacos": {
        "origin": "Mexico",
        "ingredients": ["Corn Tortillas", "Seasoned Beef / Pork / Chicken", "Cilantro", "Diced Onions", "Lime", "Salsa"],
        "recipe": "Warm soft corn tortillas on a dry griddle. Fill with grilled seasoned meat, top with fresh chopped onions, cilantro, a squeeze of fresh lime juice, and spicy salsa."
    },
    "pad thai": {
        "origin": "Thailand",
        "ingredients": ["Rice Noodles", "Shrimp / Chicken / Tofu", "Eggs", "Tamarind Paste", "Fish Sauce", "Bean Sprouts", "Crushed Peanuts", "Lime"],
        "recipe": "Stir-fry shrimp or tofu in hot oil. Add beaten eggs and scramble lightly. Add soaked rice noodles and tamarind-based sauce. Stir in bean sprouts and garlic chives, then serve topped with crushed peanuts and lime wedges."
    },
    "apple pie": {
        "origin": "England / United States",
        "ingredients": ["Flaky Pie Crust", "Sliced Tart Apples (Granny Smith)", "Sugar", "Cinnamon", "Nutmeg", "Butter"],
        "recipe": "Toss sliced apples with cinnamon, nutmeg, sugar, and flour. Place into rolled pie crust, dot with butter, and cover with top crust. Vent steam and bake at 190°C (375°F) for 50 minutes until golden."
    },
    "lasagna": {
        "origin": "Italy (Naples/Bologna)",
        "ingredients": ["Lasagna Noodles", "Bolognese Meat Sauce", "Béchamel / Ricotta", "Mozzarella", "Parmesan"],
        "recipe": "Layer pasta sheets with rich bolognese sauce, creamy béchamel, and grated cheese. Repeat layers and top with extra mozzarella. Bake at 180°C (350°F) for 35 minutes until bubbling and golden."
    },
    "guacamole": {
        "origin": "Mexico",
        "ingredients": ["Ripe Avocados", "Lime Juice", "Red Onion", "Jalapeño", "Cilantro", "Tomato", "Salt"],
        "recipe": "Mash ripe avocados in a bowl with a fork. Gently fold in finely minced onion, jalapeño, cilantro, diced tomatoes, lime juice, and salt to taste. Serve with crispy tortilla chips."
    },
    "caesar salad": {
        "origin": "Mexico (Tijuana)",
        "ingredients": ["Romaine Lettuce", "Croutons", "Parmesan Cheese", "Caesar Dressing (Egg yolk, anchovy, garlic, lemon, olive oil)"],
        "recipe": "Chop crisp romaine lettuce. Toss with prepared creamy Caesar dressing, garlic croutons, and shaved Parmigiano-Reggiano."
    },
    "ice cream": {
        "origin": "Global / Ancient China & Europe",
        "ingredients": ["Heavy Cream", "Whole Milk", "Sugar", "Egg Yolks", "Vanilla Extract"],
        "recipe": "Heat milk and sugar. Whisk hot milk into egg yolks to temper, cook until custard coats back of a spoon. Chill thoroughly, stir in vanilla and cream, churn in ice cream maker, and freeze."
    },
    "dumplings": {
        "origin": "China",
        "ingredients": ["Dumpling Wrappers", "Minced Pork / Chicken", "Chinese Cabbage", "Ginger", "Scallions", "Soy Sauce", "Sesame Oil"],
        "recipe": "Mix filling ingredients thoroughly. Place a spoonful onto each wrapper, moisten edges with water, pleat and seal tightly. Pan-fry until bottom is golden, add water, cover to steam through."
    },
    "steak": {
        "origin": "Global",
        "ingredients": ["Thick-cut Ribeye / Sirloin Steak", "Coarse Salt", "Black Pepper", "Butter", "Garlic", "Rosemary / Thyme"],
        "recipe": "Season room-temperature steak liberally with salt and pepper. Sear in a screaming-hot cast iron skillet with oil for 3 minutes per side. Add butter, crushed garlic, and herbs; baste steak continuously until desired doneness."
    },
    "chocolate cake": {
        "origin": "United States / Europe",
        "ingredients": ["Flour", "Cocoa Powder", "Sugar", "Baking Powder", "Eggs", "Milk", "Butter", "Chocolate Ganache / Frosting"],
        "recipe": "Whisk dry ingredients together. Combine melted butter, eggs, and milk. Mix wet and dry together until smooth. Pour into greased cake pans and bake at 175°C (350°F) for 30 minutes. Cool and frost."
    }
}

def get_food_info(food_name: str) -> dict:
    """
    Returns information regarding origin, ingredients, and recipe for the food dish.
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
        "ingredients": [
            f"Fresh ingredients typically used in preparing {food_name}",
            "Herbs & Spices to taste",
            "Cooking Oil or Butter",
            "Salt & Pepper"
        ],
        "recipe": f"Carefully prepare and season the ingredients for {food_name}. Cook following traditional culinary techniques until properly done, and serve fresh and warm."
    }
