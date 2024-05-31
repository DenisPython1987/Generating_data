import plotly.express as px

from die import Die

#Create a D6
die = Die()

#Make some rolls, and store the results in a list.
results = []

for roll_num in range(1_000):
    result = die.roll()
    results.append(result)

#Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results.
title = "Results of rolling one D6 1,000 times."
labels = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.bar(x = poss_results, y = frequencies, title=title, labels=labels)
fig.show()

