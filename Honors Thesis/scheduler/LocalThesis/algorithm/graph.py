import matplotlib.pyplot as plt

# Read data from file
with open('graph_data.txt', 'r') as f:
    data = [float(line.strip()) for line in f]

# Print the data to verify it was read correctly
print(data)

# Create bar graph
plt.bar(range(len(data)), data)

# Set title and axis labels
plt.title('Algorithm Efficiency for Various Scheduling Scenarios', fontweight = "bold")
plt.xlabel('Constraints', fontweight = "bold")
plt.ylabel('Time in seconds', fontweight = "bold")

# Set x-axis labels
plt.xticks(range(len(data)), [r'Scenario A', r'Scenario B', r'Scenario C', r'Scenario D', r'Scenario E'])

# Save the graph as a PNG image file
plt.savefig('my_bar_graph.png')
