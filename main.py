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
sodium = [0, 512, 10, 210, 24]
vitC = [5.7, 32, 0, 9.5, 8.4]
vitA = [20.25, 0, 0, 20.27, 843.9]
protein = [0.3, 17.6, 5, 2.2, 1]

model += 1.50 * choice1 + 2.75*choice2 + .5*choice3 + 1*choice4 + 2*choice5
model += pulp.lpSum([calories[i]*choices[i] for i in range(len(choices))]) == 2000
model += pulp.lpSum([fat[i]*choices[i] for i in range(len(choices))]) <= 10
model += pulp.lpSum([sodium[i]*choices[i] for i in range(len(choices))]) <= 2200
model += pulp.lpSum([vitC[i]*choices[i] for i in range(len(choices))]) >= 100
model += pulp.lpSum([vitA[i]*choices[i] for i in range(len(choices))]) >= 700
model += pulp.lpSum([protein[i]*choices[i] for i in range(len(choices))]) >= 50

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
    totalCals, totalFat, totalSod, totalVitC, totalVitA, totalProt = (0, 0, 0, 0, 0, 0)
    for i in range(len(totalServings)):
        totalCals += totalServings[i]*calories[i]
        totalFat += totalServings[i]*fat[i]
        totalSod += totalServings[i]*sodium[i]
        totalVitC += totalServings[i]*vitC[i]
        totalVitA += totalServings[i]*vitA[i]
        totalProt += totalServings[i]*protein[i]

    print("\nTotal Calories: {}/2000".format(round(totalCals)))
    print("Total Fat: {}/10".format(round(totalFat)))
    print("Total Sodium: {}/2200".format(round(totalSod)))
    print("Total Vitamin C: {}/100".format(round(totalVitC)))
    print("Total Vitamin A: {}/700".format(round(totalVitA)))
    print("Total Protein: {}/50".format(round(totalProt)))

totalNutrients(choice1.varValue, choice2.varValue, choice3.varValue, choice4.varValue, choice5.varValue)
