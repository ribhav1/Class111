import csv
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

with open('studentMarks.csv') as f:
    file_data = pd.read_csv(f)

data = file_data['Math_score'].tolist()

data_mean = statistics.mean(data)
print(data_mean)

data_stddev = statistics.stdev(data)
print(data_stddev)

marks_graph = ff.create_distplot([data], ['Math_score'], show_hist=False)
marks_graph.show()

