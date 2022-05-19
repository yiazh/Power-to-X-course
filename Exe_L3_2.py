'''
Created on: 20220519

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''

from wind_turbine import wind_turbine
import pandas as pd

# Read the yearly historical wind speed data
meteorological_data = pd.read_csv('./Historical_data.csv', index_col = 'time')
wind_speed_all = meteorological_data['WS10m']
wind_speed = wind_speed_all['20130101:0011':'20131231:2311']

# Instantiate a wind turbine object

wt = wind_turbine(height=50, V_ci=3, V_co=22.5, r=75, capital_cost=1311, V_r=14.32, C_p=0.15)
print(wt.rated_power())


#1. Calculate the yearly hydrogen production using fixed efficiency model

#2. Assume that the project life is 15 years, calculate the cash flow of every year. Express the result in a list with length of 16.
# (Assume the hydrogen price is 2€/kg and the yearly wind power remains the same)

#3. Based on the cash flow you got from (2), calculate the NPV. (discount rate is 0.05)

#4. Calculate the LCOH (discount rate is 0.05), using the two definitions and compare the results.

