'''
Created on: 20220517

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
from wind_turbine import wind_turbine
import pandas as pd

# Read historical wind speed data
meteorological_data = pd.read_csv('./Historical_data.csv', index_col = 'time')
wind_speed_all = meteorological_data['WS10m']
wind_speed = wind_speed_all['20130101:0011':'20130101:2311']

# Instantiate a wind turbine object
wt = wind_turbine(height=50, V_ci=3, V_co=22.5, r=75, capital_cost=1311, V_r=14.32, C_p=0.15)
print(wt.rated_power())

# Calculate the daily hydrogen production. Before doing that, you need to use the wind turbine model to convert wind speed to power.

# Recalculate the hydrogen production using an electrolyser model with varing efficiency.

# Change the capacity of the electrolyser (2, 5, 10, 15, 20) and compare the hydrogen production.
