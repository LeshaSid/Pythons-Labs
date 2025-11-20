import numpy as np 

exps_trans = np.array([2500, 2400, 2300, 2200, 2100, 2000, 1900, 1800, 1700, 1600, 1500, 3000])

def analyze_transport_expenses(exp_arr):
    winter_idx = [11, 0, 1]
    summer_idx = [5, 6, 7]

    sum_winter = np.sum(exp_arr[winter_idx])
    sum_summer = np.sum(exp_arr[summer_idx])

    if sum_winter > sum_summer:
        print("Расходы в зимний период больше, чем в летний")
    elif sum_winter < sum_summer:
        print("Расходы в летний период больше, чем в зимний")
    else:
        print("Расходы за зиминий и летний период равны")
