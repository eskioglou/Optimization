import pulp

model = pulp.LpProblem('Eλαχιστοποίηση κόστους', pulp.LpMinimize)

choice1 = pulp.LpVariable('choice1', lowBound=1)
choice2 = pulp.LpVariable('choice2', lowBound=1)
choice3 = pulp.LpVariable('choice3', lowBound=1)
choice4 = pulp.LpVariable('choice4', lowBound=1)
choice5 = pulp.LpVariable('choice5', lowBound=1)

choices = [choice1, choice2, choice3, choice4, choice5]
calories = [65, 328, 216, 137, 6.9]
fat = [0, 4, 0, 2, 0]


model += 1.50 * choice1 + 2.75*choice2 + .5*choice3 + 1*choice4 + 2*choice5
model += pulp.lpSum([calories[i]*choices[i] for i in range(len(choices))]) == 2000
model += pulp.lpSum([fat[i]*choices[i] for i in range(len(choices))]) <= 10


model.solve()
#print(pulp.LpStatus[model.status])

print("Servings of apples = {}".format(choice1.varValue))
print("Servings of chicken = {}".format(choice2.varValue))
print("Servings of brown rice = {}".format(choice3.varValue))
print("Servings of chips = {}".format(choice4.varValue))
print("Servings of spinach = {}".format(choice5.varValue))

total_cost = pulp.value(model.objective)
print("\nThe total cost is ${} for us to get the required daily nutrients".format(round(total_cost, 5)))

def totalNutrients(choice1, choice2, choice3, choice4, choice5):
    totalServings=[choice1, choice2, choice3, choice4, choice5]
    totalCals, totalFat = (0, 0)
    for i in range(len(totalServings)):
        totalCals += totalServings[i]*calories[i]
        totalFat += totalServings[i]*fat[i]


    print("\nTotal Calories: {}/2000".format(round(totalCals)))
    print("Total Fat: {}/10".format(round(totalFat)))

totalNutrients(choice1.varValue, choice2.varValue, choice3.varValue, choice4.varValue, choice5.varValue)
