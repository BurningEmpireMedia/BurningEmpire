import pandas as pd
import numpy as np
from bokeh import plotting as bk
from numpy.random import default_rng
rng = default_rng(12345)

date_range = pd.date_range("2024-01-01", periods=50)
data = rng.normal(0, 3, size=50).cumsum()
series = pd.Series(data, index=date_range)
bk.output_file("jofrin.html")

fig = bk.figure(title="Time Series Data",
                x_axis_label="Date",
                x_axis_type="datetime",
                y_axis_label="Value")
fig.line(date_range, series)

bk.show(fig)
