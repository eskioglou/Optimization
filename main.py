import pulp

model = pulp.LpProblem('Minimizing cost of food problem', pulp.LpMinimize)

x1 = pulp.LpVariable('x1', lowBound=1)
x2 = pulp.LpVariable('x2', lowBound=1)
x3 = pulp.LpVariable('x3', lowBound=1)
x4 = pulp.LpVariable('x4', lowBound=1)
x5 = pulp.LpVariable('x5', lowBound=1)

vars = [x1, x2, x3, x4, x5]
calories = [65, 328, 216, 137, 6.9]
fat = [0, 4, 0, 2, 0]
sodium = [0, 512, 10, 210, 24]
vitC = [5.7, 32, 0, 9.5, 8.4]
vitA = [20.25, 0, 0, 20.27, 843.9]
protein = [0.3, 17.6, 5, 2.2, 1]

model += .50 * x1 + .75*x2 + .5*x3 + 1*x4 + 1*x5
model += pulp.lpSum([calories[i]*vars[i] for i in range(len(vars))]) == 2000
model += pulp.lpSum([fat[i]*vars[i] for i in range(len(vars))]) <= 20
model += pulp.lpSum([sodium[i]*vars[i] for i in range(len(vars))]) <= 2400
model += pulp.lpSum([vitC[i]*vars[i] for i in range(len(vars))]) >= 90
model += pulp.lpSum([vitA[i]*vars[i] for i in range(len(vars))]) >= 700
model += pulp.lpSum([protein[i]*vars[i] for i in range(len(vars))]) >= 56

model.solve()
print(pulp.LpStatus[model.status])

print("Servings of apples = {}".format(x1.varValue))
print("Servings of chicken = {}".format(x2.varValue))
print("Servings of brown rice = {}".format(x3.varValue))
print("Servings of chips = {}".format(x4.varValue))
print("Servings of spinach = {}".format(x5.varValue))

total_cost = pulp.value(model.objective)
print("\nThe total cost is ${} for us to get the required daily nutrients".format(round(total_cost, 5)))

def totalNutrients(x1, x2, x3, x4, x5):
    totalServings=[x1, x2, x3, x4, x5]
    totalCals, totalFat, totalSod, totalVitC, totalVitA, totalProt = (0, 0, 0, 0, 0, 0)
    for i in range(len(totalServings)):
        totalCals += totalServings[i]*calories[i]
        totalFat += totalServings[i]*fat[i]
        totalSod += totalServings[i]*sodium[i]
        totalVitC += totalServings[i]*vitC[i]
        totalVitA += totalServings[i]*vitA[i]
        totalProt += totalServings[i]*protein[i]

    print("\nTotal Calories: {}/2000".format(round(totalCals)))
    print("Total Fat: {}/20".format(round(totalFat)))
    print("Total Sodium: {}/2400".format(round(totalSod)))
    print("Total Vitamin C: {}/90".format(round(totalVitC)))
    print("Total Vitamin A: {}/700".format(round(totalVitA)))
    print("Total Protein: {}/56".format(round(totalProt)))

totalNutrients(x1.varValue, x2.varValue, x3.varValue, x4.varValue, x5.varValue)
