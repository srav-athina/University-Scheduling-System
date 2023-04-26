import sys
sys.path.append("C:\\Users\\jnaat\\OneDrive\\Documents\\School\\Thesis\\Honors Thesis\\scheduler\\LocalThesis")
from algorithm.genetic_alg import GeneticAlg
import json
import time
#import cProfile

# Load data from JSON file
with open('output5.json') as json_file:
    data = json.load(json_file)

course_inputs = data["courses"]
dependencies = data["dependencies"]
profs_inputs = data["prof_names"]
hard_prefs_inputs = data["hard_times"]
soft_prefs_inputs = data["soft_times"]
course_prefs_inputs = data["course_prefs"]
rooms_inputs = data["rooms"]

g = GeneticAlg()
#import cProfile, pstats
#profiler = cProfile.Profile()
#profiler.enable()
case_times = []

for i in range(100):
    start_time = time.time()

    g.run(course_inputs, dependencies, profs_inputs, hard_prefs_inputs, soft_prefs_inputs, course_prefs_inputs, rooms_inputs)
    #profiler.disable()
    #stats = pstats.Stats(profiler).sort_stats('cumtime')
    #stats.print_stats()

    t = (time.time() - start_time)
    print(i)
    case_times.append(t)
sum_times = 0
for t in case_times:
    sum_times += t
avg_time = sum_times/len(case_times)

with open('graph_data.txt', 'a') as f:
# append some data to the file
    f.write(str(avg_time))
    f.write("\n")
