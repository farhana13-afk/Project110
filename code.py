import statistics
import pandas as pd
import plotly.figure_factory as ff
import csv
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].to_list()

population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)

print("population mean: ", population_mean)
print("population standardDeviation: ", population_stdev)

fig = ff.create_distplot([data], ["reading_time"], show_hist = False)
fig.show()

def random_set_of_mean(Counter):
    dataset = []
    for i in range(0, Counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
        sample_counter_mean = statistics.mean(dataset)
    return sample_counter_mean

def setup():
    mean_list = []
    for i in range (0,100):
        set_of_sample_mean = random_set_of_mean(30)
        mean_list.append(set_of_sample_mean)
    print("sampling_mean", statistics.mean(mean_list)),
    print("sampling_standard_deviation", statistics.stdev(mean_list))
    fig = ff.create_distplot([mean_list],["sampling reading_time"], show_hist = False)
    fig.show()

setup()

