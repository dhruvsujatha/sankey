#! !/miniforge/bin/python

import plotly.graph_objects as go

fig = go.Figure(data = [go.Sankey(
    node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = ["Intl TRF", "Part-Time Salary", "Total Income", "Savings", "Tuition and Fees"],
        color = ["blue", "red", "green", "yellow", "orange"]
    ),
    link = dict(
        source = [0, 1, 2, 2],
        target = [2, 2, 3, 4],
        value = [5000, 512, 50, 4495]
    )
)])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()