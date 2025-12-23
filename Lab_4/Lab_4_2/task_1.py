import numpy as np 

def analyze_transport_expenses(exps_arr):
    winter_idx = [11, 0, 1]
    summer_idx = [5, 6, 7]

    sum_winter = np.sum(exps_arr[winter_idx])
    sum_summer = np.sum(exps_arr[summer_idx])

    if sum_winter > sum_summer:
        print("Расходы в зимний период больше, чем в летний")
    elif sum_winter < sum_summer:
        print("Расходы в летний период больше, чем в зимний")
    else:
        print("Расходы за зимний и летний период равны")

    print("Топ 3 месяца по расходам:")
    top_indices = np.argsort(exps_arr)[::-1][:3]

    for i in range(3):
        idx = top_indices[i]
        print(f"{i+1} место: {idx + 1} месяц с расходом {exps_arr[idx]}")

exps_trans = np.array([2500, 2400, 2300, 2200, 2100, 2000, 1900, 1800, 1700, 1600, 1500, 3000])
analyze_transport_expenses(exps_trans)