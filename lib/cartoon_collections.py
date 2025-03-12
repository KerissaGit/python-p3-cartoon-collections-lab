dwarves = ["Doc", "Dopey", "Bashful", "Grumpy"]
def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves):
        print(f"{index+1}. {dwarf}")

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + "!" for call in planeteer_calls]

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

snacks = ["crackers", "gouda", "thyme"]
soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
ingredients = ["garlic", "rosemary", "bread"]

def find_the_cheese(cheeses):
    cheese_list = ["cheddar", "gouda", "camembert"]
    for cheese in cheeses:
        if cheese in cheese_list:
            return cheese
    return None

find_the_cheese(snacks)
find_the_cheese(soup)
find_the_cheese(ingredients)
