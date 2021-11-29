import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

with open('data1.csv') as f:
    file_data = pd.read_csv(f)

data = file_data['Math_score'].tolist()

data_mean = statistics.mean(data)
data_stdev = statistics.stdev(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean_value = statistics.mean(dataset)
    return mean_value

mean_list = []
for i in (range(0, 1000)):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)
        
mean_list_stdev = statistics.stdev(mean_list)

mean_list_mean, mean_list_median, mean_list_mode, mean_list_stdev = statistics.mean(mean_list), statistics.median(mean_list), statistics.mode(mean_list), statistics.stdev(mean_list)

mean_list_1stdev_start, mean_list_1stdev_end = mean_list_mean - mean_list_stdev, mean_list_mean + mean_list_stdev
mean_list_2stdev_start, mean_list_2stdev_end = mean_list_mean - (2 * mean_list_stdev), mean_list_mean + (2 * mean_list_stdev)
mean_list_3stdev_start, mean_list_3stdev_end = mean_list_mean - (3 * mean_list_stdev), mean_list_mean + (3 * mean_list_stdev)

marks_graph = ff.create_distplot([mean_list], ['Math_score'], show_hist=False)
marks_graph.add_trace(go.Scatter(x = [data_mean, data_mean], y = [0, 0.17], mode = 'lines', name = 'mean'))

marks_graph.add_trace(go.Scatter(x = [mean_list_1stdev_start, mean_list_1stdev_start], y = [0, 0.17], mode = 'lines', name = '1stdev_start'))
marks_graph.add_trace(go.Scatter(x = [mean_list_1stdev_end, mean_list_1stdev_end], y = [0, 0.17], mode = 'lines', name = '1stdev_end'))

marks_graph.add_trace(go.Scatter(x = [mean_list_2stdev_start, mean_list_2stdev_start], y = [0, 0.17], mode = 'lines', name = '2stdev_start'))
marks_graph.add_trace(go.Scatter(x = [mean_list_2stdev_end, mean_list_2stdev_end], y = [0, 0.17], mode = 'lines', name = '2stdev_end'))

marks_graph.add_trace(go.Scatter(x = [mean_list_3stdev_start, mean_list_3stdev_start], y = [0, 0.17], mode = 'lines', name = '3stdev_start'))
marks_graph.add_trace(go.Scatter(x = [mean_list_3stdev_end, mean_list_3stdev_end], y = [0, 0.17], mode = 'lines', name = '3stdev_end'))

marks_graph.show()