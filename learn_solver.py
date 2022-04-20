from pulp import *

unit_price = [28.5, 12.5, 29.25, 21.5]
unit_cost = [8, 0.5, 0.75]
unit_frame = [[2, 1, 3, 2], [4, 2, 1, 2], [6, 2, 1, 2]]
res_avail = [4000, 6000, 10000]
max_sales = [1000, 2000, 500, 1000]

prod_f1 = LpVariable("Frame_1", 0, max_sales[0], LpInteger)
prod_f2 = LpVariable("Frame_2", 0, max_sales[1], LpInteger)
prod_f3 = LpVariable("Frame_3", 0, max_sales[2], LpInteger)
prod_f4 = LpVariable("Frame_4", 0, max_sales[3], LpInteger)

prodList = [prod_f1, prod_f2, prod_f3, prod_f4]
# prodList = [LpVariable(f"frame_{x}", 0, max_sales[x], LpInteger) for x in range(len(max_sales))]

prob = LpProblem("The_frame_optimization_Problem", LpMaximize)

prob += lpSum([
                prodList[x] * (unit_price[x] - unit_frame[0][x] * unit_cost[0]
                                             - unit_frame[1][x] * unit_cost[1]
                                             - unit_frame[2][x] * unit_cost[2])
                for x in range(len(prodList))
              ])

# constraints
for i in range(len(res_avail)):
    prob += lpSum([prodList[x] * unit_frame[i][x] for x in range(len(prodList))]) <= res_avail[i]

prob.solve()

# output
print("status: ", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)
print(value(prob.objective))
