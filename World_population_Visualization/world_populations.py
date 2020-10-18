import json
from pygal.maps.world import World
from pygal.style import RotateStyle as RS
from pygal.style import LightColorizedStyle as LCS
from cities_visualization import get_country_code

filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

country_population = {}

for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code: # if the country has an international code, then they will appear.
            country_population[code] = population

            
# Grouping the populations

c_code_1 , c_code_2  , c_code_3 = {} , {} , {}
for c_country , pop in country_population.items():
    if pop < 10000000:
        c_code_1[c_country] = pop
    elif pop < 1000000000:
        c_code_2[c_country] = pop
    else:
        c_code_3[c_country] = pop

# Use RotateStyle and LightColorizedStyle to customize your graph map
world_map_style = RS("#00ffff" , base_style=LCS)

world_map = World(style = world_map_style)
world_map.title = ("World Population in 2010 , by Country [Python Crash Course]")
world_map.add("10 Million" , c_code_1)
world_map.add("10 Mil - 1 Bn" , c_code_2)
world_map.add(">1 Billion" , c_code_3)

world_map.render_to_file("Final_Graph.svg")
