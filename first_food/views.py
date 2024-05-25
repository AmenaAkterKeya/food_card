

from django.shortcuts import render

# Create your views here.
def index(request):
    meals = [
       {
        "strMeal": "BeaverTails",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
        "idMeal": "52928",
        "strInstructions": "Mix flour, sugar, yeast, and warm water to form dough. Let it rise. Roll out the dough into flat oval shapes and fry in hot oil until golden brown. Sprinkle with cinnamon sugar or your favorite toppings."
    },
    {
        "strMeal": "Breakfast Potatoes",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
        "idMeal": "52965",
        "strInstructions": "Dice potatoes and parboil them. Season with salt, pepper, and your favorite herbs. Spread on a baking sheet and bake at 425°F until crispy, turning occasionally for even browning."
    },
    {
        "strMeal": "Canadian Butter Tarts",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
        "idMeal": "52923",
        "strInstructions": "Prepare a pastry dough and line tart shells. Fill with a mixture of butter, brown sugar, and corn syrup. Bake at 350°F until the filling is bubbly and the crust is golden."
    },
    {
        "strMeal": "Montreal Smoked Meat",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
        "idMeal": "52927",
        "strInstructions": "Rub brisket with a spice mix and cure for several days. Smoke the meat until tender. Steam the smoked meat before slicing thinly against the grain. Serve on rye bread with mustard."
    },
    {
        "strMeal": "Nanaimo Bars",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
        "idMeal": "52924",
        "strInstructions": "Create a base layer of graham cracker crumbs, cocoa, and coconut. Top with a custard-flavored butter icing. Finish with a layer of melted chocolate. Refrigerate until set before cutting into bars."
    },
    {
        "strMeal": "Pate Chinois",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
        "idMeal": "52930",
        "strInstructions": "Layer seasoned ground beef, canned corn, and mashed potatoes in a baking dish. Bake at 375°F until the top is golden brown and the dish is heated through."
    },
    {
        "strMeal": "Pouding chomeur",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
        "idMeal": "52932",
        "strInstructions": "Prepare a simple cake batter. Pour a hot syrup made from brown sugar and water over the batter. Bake at 350°F until the cake is set and the syrup forms a rich sauce."
    },
    {
        "strMeal": "Poutine",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
        "idMeal": "52804",
        "strInstructions": "Fry potatoes until crispy. Place hot fries on a plate, top with fresh cheese curds, and smother with hot gravy. Serve immediately while the cheese is melting."
    },
    {
        "strMeal": "Rappie Pie",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
        "idMeal": "52933",
        "strInstructions": "Grate potatoes and squeeze out excess water. Mix with seasoned broth and cooked meat (such as chicken). Bake at 350°F until the top is golden and crispy."
    },
    {
        "strMeal": "Split Pea Soup",
        "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
        "idMeal": "52925",
        "strInstructions": "Simmer split peas with a ham hock, onions, carrots, and celery until the peas are tender. Remove the ham hock, chop the meat, and return it to the pot. Season to taste and serve hot."
    }
    ]
    return render(request,'index.html',{'meals' :meals})