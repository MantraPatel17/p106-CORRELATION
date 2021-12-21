import plotly.express as px
import csv
import numpy as np

def graph(path):
    with open(path) as f:
        data = csv.DictReader(f)
        g = px.scatter(data, x="Days Present", y="Marks In Percentage")
        g.show()


def  get_list(path):
    coffee = []
    hours = []
    with open(path) as f:
        data = csv.DictReader(f)
        for row in data:
            coffee.append(float(row["Days Present"]))
            hours.append(float(row["Marks In Percentage"]))
    return {"x": coffee, "y": hours}

def correlation(dataSource):
    c = np.corrcoef(dataSource["x"], dataSource["y"])
    print(c[0,1])

def setup():
    path = "data_studentMarks_vs_daysPresent.csv"
    dataSource = get_list(path)
    correlation(dataSource)
    graph(path)

setup()
    