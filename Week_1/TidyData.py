import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("whitegrid")

df_seattle  = pd.read_csv("https://raw.githubusercontent.com/tidyverse/nycflights13/refs/heads/main/data-raw/weather.csv")

print(df_seattle.head())


