'''
Created on:

Author: Yi Zheng, Department of Electrical Engineering, DTU

'''
import numpy_financial as npf
import matplotlib.pyplot as plt
import numpy as np

def npv_ele(h2_price = 3, interest_rate = 0.05):
    h2_price = h2_price
    Ele_price = 40
    stack_power = 90*4.33
    CAPEX_stack = stack_power * 1200
    annual_hydrogen = 8.1*24*365
    annual_ele_consumption = 389.7*24*365/1000 # MW
    cash_flow = [-CAPEX_stack]
    for y in range(1, 11):
        cash_flow.append(annual_hydrogen * h2_price - annual_ele_consumption * Ele_price - 0.02 * CAPEX_stack)

    print(cash_flow)
    npv = npf.npv(interest_rate, cash_flow)
    print(npf.irr(cash_flow))
    return npv

npv_list_5 = []
npv_list_8 = []
h2_price_range = np.linspace(1.0, 5.0, 50)
for h2_price in np.linspace(1.0, 5.0, 50):
    npv_list_5.append(npv_ele(h2_price = h2_price))
    npv_list_8.append(npv_ele(h2_price = h2_price, interest_rate= 0.08))

plt.plot(h2_price_range, npv_list_5, label = 'Discount rate = 0.05')
plt.plot(h2_price_range, npv_list_8, label = 'Discount rate = 0.08')
plt.legend()
plt.title('Net present value (€)')
plt.ylabel('NPV (€)')
plt.xlabel('Hydrogen price (€/kg)')
plt.show()

LCOH = (467640 + sum((136550 + 9352)/(1 + 0.08)**i for i in range(1, 11)))/(sum(70956/(1+0.08)**i for i in range(1,11)))
print(LCOH)

