import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

height = ctrl.Antecedent(np.arange(130,201,1), 'height')
bmi = ctrl.Antecedent(np.arange(10,41,1), 'bmi')
activity = ctrl.Antecedent(np.arange(0,11,1), 'activity')

calorie = ctrl.Consequent(np.arange(1800,3400,1), 'calorie')

height['very low'] 	= fuzz.trimf(height.universe, [130, 130, 150])
height['low']		= fuzz.trimf(height.universe, [140, 150, 160])
height['medium']	= fuzz.trimf(height.universe, [150, 165, 180])
height['high']		= fuzz.trimf(height.universe, [165, 180, 190])
height['very high'] 	= fuzz.trimf(height.universe, [185, 200, 200])

#height['high'].view()
#raw_input()

bmi['underweight']		= fuzz.trimf(bmi.universe, [10, 10, 18.5])
bmi['normal weight']		= fuzz.trimf(bmi.universe, [17, 21, 25])
bmi['overweight']		= fuzz.trimf(bmi.universe, [24, 27, 30])
bmi['obese']			= fuzz.trimf(bmi.universe, [29, 32, 35])
bmi['very obese']		= fuzz.trimf(bmi.universe, [34, 40, 40])

#bmi.view()
#raw_input()

activity.automf(3) # poor, average, good
calorie.automf(7) # dismal, poor, mediocre, average, decent, good, excellent

rule1 = ctrl.Rule(bmi['underweight'] & (height['very low'] | height['low']) & activity['poor'], calorie['mediocre'])
rule2 = ctrl.Rule(bmi['underweight'] & (height['very low'] | height['low']) & activity['average'], calorie['average'])
rule3 = ctrl.Rule(bmi['underweight'] & (height['very low'] | height['low']) & activity['good'], calorie['decent'])

rule4 = ctrl.Rule(bmi['underweight'] & height['medium'] & activity['poor'], calorie['average'])
rule5 = ctrl.Rule(bmi['underweight'] & height['medium'] & activity['average'], calorie['decent'])
rule6 = ctrl.Rule(bmi['underweight'] & height['medium'] & activity['good'], calorie['good'])

rule7  = ctrl.Rule(bmi['underweight'] & height['high'] & activity['poor'], calorie['decent'])
rule8 = ctrl.Rule(bmi['underweight'] & height['high'] & activity['average'], calorie['good'])
rule9 = ctrl.Rule(bmi['underweight'] & height['high'] & activity['good'], calorie['excellent'])

rule10 = ctrl.Rule(bmi['underweight'] & height['very high'] & activity['poor'], calorie['good'])
rule11 = ctrl.Rule(bmi['underweight'] & height['very high'] & activity['average'], calorie['excellent'])
rule12 = ctrl.Rule(bmi['underweight'] & height['very high'] & activity['good'], calorie['excellent'])


rule13 = ctrl.Rule(bmi['normal weight'] & (height['very low'] | height['low']) & activity['poor'], calorie['poor'])
rule14 = ctrl.Rule(bmi['normal weight'] & (height['very low'] | height['low']) & activity['average'], calorie['mediocre'])
rule15 = ctrl.Rule(bmi['normal weight'] & (height['very low'] | height['low']) & activity['good'], calorie['average'])

rule16 = ctrl.Rule(bmi['normal weight'] & height['medium'] & activity['poor'], calorie['mediocre'])
rule17 = ctrl.Rule(bmi['normal weight'] & height['medium'] & activity['average'], calorie['average'])
rule18 = ctrl.Rule(bmi['normal weight'] & height['medium'] & activity['good'], calorie['decent'])

rule19  = ctrl.Rule(bmi['normal weight'] & height['high'] & activity['poor'], calorie['average'])
rule20 = ctrl.Rule(bmi['normal weight'] & height['high'] & activity['average'], calorie['decent'])
rule21 = ctrl.Rule(bmi['normal weight'] & height['high'] & activity['good'], calorie['good'])

rule22 = ctrl.Rule(bmi['normal weight'] & height['very high'] & activity['poor'], calorie['decent'])
rule23 = ctrl.Rule(bmi['normal weight'] & height['very high'] & activity['average'], calorie['good'])
rule24 = ctrl.Rule(bmi['normal weight'] & height['very high'] & activity['good'], calorie['excellent'])


rule25 = ctrl.Rule(bmi['overweight'] & (height['very low'] | height['low']) & activity['poor'], calorie['dismal'])
rule26 = ctrl.Rule(bmi['overweight'] & (height['very low'] | height['low']) & activity['average'], calorie['poor'])
rule27 = ctrl.Rule(bmi['overweight'] & (height['very low'] | height['low']) & activity['good'], calorie['mediocre'])

rule28 = ctrl.Rule(bmi['overweight'] & height['medium'] & activity['poor'], calorie['poor'])
rule29 = ctrl.Rule(bmi['overweight'] & height['medium'] & activity['average'], calorie['mediocre'])
rule30 = ctrl.Rule(bmi['overweight'] & height['medium'] & activity['good'], calorie['average'])

rule31  = ctrl.Rule(bmi['overweight'] & height['high'] & activity['poor'], calorie['mediocre'])
rule32 = ctrl.Rule(bmi['overweight'] & height['high'] & activity['average'], calorie['average'])
rule33 = ctrl.Rule(bmi['overweight'] & height['high'] & activity['good'], calorie['decent'])

rule34 = ctrl.Rule(bmi['overweight'] & height['very high'] & activity['poor'], calorie['average'])
rule35 = ctrl.Rule(bmi['overweight'] & height['very high'] & activity['average'], calorie['decent'])
rule36 = ctrl.Rule(bmi['overweight'] & height['very high'] & activity['good'], calorie['good'])


rule37 = ctrl.Rule(bmi['obese'] & (height['very low'] | height['low']) & activity['poor'], calorie['dismal'])
rule38 = ctrl.Rule(bmi['obese'] & (height['very low'] | height['low']) & activity['average'], calorie['dismal'])
rule39 = ctrl.Rule(bmi['obese'] & (height['very low'] | height['low']) & activity['good'], calorie['poor'])

rule40 = ctrl.Rule(bmi['obese'] & height['medium'] & activity['poor'], calorie['dismal'])
rule41 = ctrl.Rule(bmi['obese'] & height['medium'] & activity['average'], calorie['poor'])
rule42 = ctrl.Rule(bmi['obese'] & height['medium'] & activity['good'], calorie['mediocre'])

rule43  = ctrl.Rule(bmi['obese'] & height['high'] & activity['poor'], calorie['poor'])
rule44 = ctrl.Rule(bmi['obese'] & height['high'] & activity['average'], calorie['mediocre'])
rule45 = ctrl.Rule(bmi['obese'] & height['high'] & activity['good'], calorie['average'])

rule46 = ctrl.Rule(bmi['obese'] & height['very high'] & activity['poor'], calorie['mediocre'])
rule47 = ctrl.Rule(bmi['obese'] & height['very high'] & activity['average'], calorie['average'])
rule48 = ctrl.Rule(bmi['obese'] & height['very high'] & activity['good'], calorie['decent'])


rule49 = ctrl.Rule(bmi['very obese'] & (height['very low'] | height['low']) & activity['poor'], calorie['dismal'])
rule50 = ctrl.Rule(bmi['very obese'] & (height['very low'] | height['low']) & activity['average'], calorie['dismal'])
rule51 = ctrl.Rule(bmi['very obese'] & (height['very low'] | height['low']) & activity['good'], calorie['dismal'])

rule52 = ctrl.Rule(bmi['very obese'] & height['medium'] & activity['poor'], calorie['dismal'])
rule53 = ctrl.Rule(bmi['very obese'] & height['medium'] & activity['average'], calorie['dismal'])
rule54 = ctrl.Rule(bmi['very obese'] & height['medium'] & activity['good'], calorie['poor'])

rule55  = ctrl.Rule(bmi['very obese'] & height['high'] & activity['poor'], calorie['dismal'])
rule56 = ctrl.Rule(bmi['very obese'] & height['high'] & activity['average'], calorie['poor'])
rule57 = ctrl.Rule(bmi['very obese'] & height['high'] & activity['good'], calorie['mediocre'])

rule58 = ctrl.Rule(bmi['very obese'] & height['very high'] & activity['poor'], calorie['poor'])
rule59 = ctrl.Rule(bmi['very obese'] & height['very high'] & activity['average'], calorie['mediocre'])
rule60 = ctrl.Rule(bmi['very obese'] & height['very high'] & activity['good'], calorie['average'])

#rule1.view()
#raw_input()

calorie_ctrl = ctrl.ControlSystem(	[rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
									rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
									rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30,
									rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40,
									rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50,
									rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60])

findCalorie = ctrl.ControlSystemSimulation(calorie_ctrl)

print "Fuzzy logic based Calorie intake suggestion system"

try:
	print "Enter your height (cm) : "
	inpHeight = int(raw_input())
	findCalorie.input['height'] = inpHeight

	print "Enter your weight (kg) : "
	inpWeight = int(raw_input())
	inpBMI = inpWeight/((inpHeight/100)**2)
	findCalorie.input['bmi'] = inpBMI

	print "On a scale from 0 to 10, how physically active are you every day? : "
	inpActivity = int(raw_input())
	findCalorie.input['activity'] = inpActivity

except(IOError, OSError, ValueError) as err :
	print "Error : " + err

findCalorie.compute()

print "\nYour suggested daily intake is " + str(findCalorie.output['calorie']) + " kilocalories.\nAverage calorie intake ranges between 2000 to 2500kcal."
calorie.view(sim=findCalorie)
raw_input()
