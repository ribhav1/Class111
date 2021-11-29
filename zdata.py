import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go


with open('interventions_data\School1.csv') as f:
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

data_1stdev_start, data_1stdev_end = data_mean - data_stdev, data_mean + data_stdev
data_2stdev_start, data_2stdev_end = data_mean - (2 * data_stdev), data_mean + (2 * data_stdev)
data_3stdev_start, data_3stdev_end = data_mean - (3 * data_stdev), data_mean + (3 * data_stdev)

school_data_1 = pd.read_csv('interventions_data\School_1_Sample.csv')
data = school_data_1['Math_score'].tolist()
school_1_data_mean = statistics.mean(data)
print('School 1 data mean: ', str(school_1_data_mean))

marks_graph = ff.create_distplot([mean_list], ['Math_score'], show_hist=False)
marks_graph.add_trace(go.Scatter(x = [school_1_data_mean, school_1_data_mean], y = [0, 0.17], mode = 'lines', name = 'mean'))

marks_graph.add_trace(go.Scatter(x = [data_1stdev_start, data_1stdev_start], y = [0, 0.17], mode = 'lines', name = '1stdev_start'))
marks_graph.add_trace(go.Scatter(x = [data_1stdev_end, data_1stdev_end], y = [0, 0.17], mode = 'lines', name = '1stdev_end'))

marks_graph.add_trace(go.Scatter(x = [data_2stdev_start, data_2stdev_start], y = [0, 0.17], mode = 'lines', name = '2stdev_start'))
marks_graph.add_trace(go.Scatter(x = [data_2stdev_end, data_2stdev_end], y = [0, 0.17], mode = 'lines', name = '2stdev_end'))

marks_graph.add_trace(go.Scatter(x = [data_3stdev_start, data_3stdev_start], y = [0, 0.17], mode = 'lines', name = '3stdev_start'))
marks_graph.add_trace(go.Scatter(x = [data_3stdev_end, data_3stdev_end], y = [0, 0.17], mode = 'lines', name = '3stdev_end'))

marks_graph.show()

school_data_2 = pd.read_csv('interventions_data\School_2_Sample.csv')
data = school_data_2['Math_score'].tolist()
school_2_data_mean = statistics.mean(data)
print('School 2 data mean: ', str(school_2_data_mean))

marks_graph = ff.create_distplot([mean_list], ['Math_score'], show_hist=False)
marks_graph.add_trace(go.Scatter(x = [school_2_data_mean, school_2_data_mean], y = [0, 0.17], mode = 'lines', name = 'mean'))

marks_graph.add_trace(go.Scatter(x = [data_1stdev_start, data_1stdev_start], y = [0, 0.17], mode = 'lines', name = '1stdev_start'))
marks_graph.add_trace(go.Scatter(x = [data_1stdev_end, data_1stdev_end], y = [0, 0.17], mode = 'lines', name = '1stdev_end'))

marks_graph.add_trace(go.Scatter(x = [data_2stdev_start, data_2stdev_start], y = [0, 0.17], mode = 'lines', name = '2stdev_start'))
marks_graph.add_trace(go.Scatter(x = [data_2stdev_end, data_2stdev_end], y = [0, 0.17], mode = 'lines', name = '2stdev_end'))

marks_graph.add_trace(go.Scatter(x = [data_3stdev_start, data_3stdev_start], y = [0, 0.17], mode = 'lines', name = '3stdev_start'))
marks_graph.add_trace(go.Scatter(x = [data_3stdev_end, data_3stdev_end], y = [0, 0.17], mode = 'lines', name = '3stdev_end'))

marks_graph.show()

school_data_3 = pd.read_csv('interventions_data\School_3_Sample.csv')
data = school_data_3['Math_score'].tolist()
school_3_data_mean = statistics.mean(data)
print('School 3 data mean: ', str(school_3_data_mean))

marks_graph = ff.create_distplot([mean_list], ['Math_score'], show_hist=False)
marks_graph.add_trace(go.Scatter(x = [school_3_data_mean, school_3_data_mean], y = [0, 0.17], mode = 'lines', name = 'mean'))

marks_graph.add_trace(go.Scatter(x = [data_1stdev_start, data_1stdev_start], y = [0, 0.17], mode = 'lines', name = '1stdev_start'))
marks_graph.add_trace(go.Scatter(x = [data_1stdev_end, data_1stdev_end], y = [0, 0.17], mode = 'lines', name = '1stdev_end'))

marks_graph.add_trace(go.Scatter(x = [data_2stdev_start, data_2stdev_start], y = [0, 0.17], mode = 'lines', name = '2stdev_start'))
marks_graph.add_trace(go.Scatter(x = [data_2stdev_end, data_2stdev_end], y = [0, 0.17], mode = 'lines', name = '2stdev_end'))

marks_graph.add_trace(go.Scatter(x = [data_3stdev_start, data_3stdev_start], y = [0, 0.17], mode = 'lines', name = '3stdev_start'))
marks_graph.add_trace(go.Scatter(x = [data_3stdev_end, data_3stdev_end], y = [0, 0.17], mode = 'lines', name = '3stdev_end'))

marks_graph.show()

z_score_value = (data_mean - school_2_data_mean) / (data_stdev)
print('Z score value: ', str(z_score_value))