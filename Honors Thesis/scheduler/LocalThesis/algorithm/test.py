#take everything from json file and convert
from genetic_alg import GeneticAlg
import json
# Load data from JSON file
with open('output.json') as json_file:
    data = json.load(json_file)

course_inputs = data["courses"]
dependencies = data["dependencies"]
profs_inputs = data["prof_names"]
hard_prefs_inputs = data["hard_times"]
soft_prefs_inputs = data["soft_times"]
course_prefs_inputs = data["course_prefs"]
rooms_inputs = data["rooms"]

g = GeneticAlg
g.run(course_inputs, dependencies, profs_inputs, hard_prefs_inputs, soft_prefs_inputs, course_prefs_inputs, rooms_inputs)