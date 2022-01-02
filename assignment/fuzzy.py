import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import getpass

height = ctrl.Antecedent(np.arange(130,201,1), 'height')
bmi = ctrl.Antecedent(np.arange(10,41,1), 'bmi')
activity = ctrl.Antecedent(np.arange(0,11,1), 'activity')
calories = ctrl.Consequent(np.arange(1800,3400,1), 'calorie')

height['very short'] 	= fuzz.trimf(height.universe, [130, 130, 150])
height['short']		= fuzz.trimf(height.universe, [140, 150, 160])
height['medium']	= fuzz.trimf(height.universe, [150, 165, 180])
height['high']		= fuzz.trimf(height.universe, [165, 180, 190])
height['very high'] = fuzz.trimf(height.universe, [185, 200, 200])


bmi['underweight']		= fuzz.trimf(bmi.universe, [10, 10, 19])
bmi['normal weight']	= fuzz.trimf(bmi.universe, [17, 21, 25])
bmi['overweight']		= fuzz.trimf(bmi.universe, [24, 27, 30])
bmi['obese']			= fuzz.trimf(bmi.universe, [29, 32, 35])
bmi['very obese']		= fuzz.trimf(bmi.universe, [34, 40, 40])

activity.automf(3) # poor, average, good
calories.automf(7) # dismal, poor, mediocre, average, decent, good, excellent

#uncomment to view the fuzzy modules
# height.view()
# bmi.view()
# activity.view()
# calorie.view()

rule1 = ctrl.Rule(bmi['underweight'] & (height['very short'] | height['short']) & activity['poor'], calories['mediocre'])
rule2 = ctrl.Rule(bmi['underweight'] & (height['very short'] | height['short']) & activity['average'], calories['average'])
rule3 = ctrl.Rule(bmi['underweight'] & (height['very short'] | height['short']) & activity['good'], calories['decent'])

rule4 = ctrl.Rule(bmi['underweight'] & height['medium'] & activity['poor'], calories['average'])
rule5 = ctrl.Rule(bmi['underweight'] & height['medium'] & activity['average'], calories['decent'])
rule6 = ctrl.Rule(bmi['underweight'] & height['medium'] & activity['good'], calories['good'])

rule7  = ctrl.Rule(bmi['underweight'] & height['high'] & activity['poor'], calories['decent'])
rule8 = ctrl.Rule(bmi['underweight'] & height['high'] & activity['average'], calories['good'])
rule9 = ctrl.Rule(bmi['underweight'] & height['high'] & activity['good'], calories['excellent'])

rule10 = ctrl.Rule(bmi['underweight'] & height['very high'] & activity['poor'], calories['good'])
rule11 = ctrl.Rule(bmi['underweight'] & height['very high'] & activity['average'], calories['excellent'])
rule12 = ctrl.Rule(bmi['underweight'] & height['very high'] & activity['good'], calories['excellent'])


rule13 = ctrl.Rule(bmi['normal weight'] & (height['very short'] | height['short']) & activity['poor'], calories['poor'])
rule14 = ctrl.Rule(bmi['normal weight'] & (height['very short'] | height['short']) & activity['average'], calories['mediocre'])
rule15 = ctrl.Rule(bmi['normal weight'] & (height['very short'] | height['short']) & activity['good'], calories['average'])

rule16 = ctrl.Rule(bmi['normal weight'] & height['medium'] & activity['poor'], calories['mediocre'])
rule17 = ctrl.Rule(bmi['normal weight'] & height['medium'] & activity['average'], calories['average'])
rule18 = ctrl.Rule(bmi['normal weight'] & height['medium'] & activity['good'], calories['decent'])

rule19  = ctrl.Rule(bmi['normal weight'] & height['high'] & activity['poor'], calories['average'])
rule20 = ctrl.Rule(bmi['normal weight'] & height['high'] & activity['average'], calories['decent'])
rule21 = ctrl.Rule(bmi['normal weight'] & height['high'] & activity['good'], calories['good'])

rule22 = ctrl.Rule(bmi['normal weight'] & height['very high'] & activity['poor'], calories['decent'])
rule23 = ctrl.Rule(bmi['normal weight'] & height['very high'] & activity['average'], calories['good'])
rule24 = ctrl.Rule(bmi['normal weight'] & height['very high'] & activity['good'], calories['excellent'])


rule25 = ctrl.Rule(bmi['overweight'] & (height['very short'] | height['short']) & activity['poor'], calories['dismal'])
rule26 = ctrl.Rule(bmi['overweight'] & (height['very short'] | height['short']) & activity['average'], calories['poor'])
rule27 = ctrl.Rule(bmi['overweight'] & (height['very short'] | height['short']) & activity['good'], calories['mediocre'])

rule28 = ctrl.Rule(bmi['overweight'] & height['medium'] & activity['poor'], calories['poor'])
rule29 = ctrl.Rule(bmi['overweight'] & height['medium'] & activity['average'], calories['mediocre'])
rule30 = ctrl.Rule(bmi['overweight'] & height['medium'] & activity['good'], calories['average'])

rule31  = ctrl.Rule(bmi['overweight'] & height['high'] & activity['poor'], calories['mediocre'])
rule32 = ctrl.Rule(bmi['overweight'] & height['high'] & activity['average'], calories['average'])
rule33 = ctrl.Rule(bmi['overweight'] & height['high'] & activity['good'], calories['decent'])

rule34 = ctrl.Rule(bmi['overweight'] & height['very high'] & activity['poor'], calories['average'])
rule35 = ctrl.Rule(bmi['overweight'] & height['very high'] & activity['average'], calories['decent'])
rule36 = ctrl.Rule(bmi['overweight'] & height['very high'] & activity['good'], calories['good'])


rule37 = ctrl.Rule(bmi['obese'] & (height['very short'] | height['short']) & activity['poor'], calories['dismal'])
rule38 = ctrl.Rule(bmi['obese'] & (height['very short'] | height['short']) & activity['average'], calories['dismal'])
rule39 = ctrl.Rule(bmi['obese'] & (height['very short'] | height['short']) & activity['good'], calories['poor'])

rule40 = ctrl.Rule(bmi['obese'] & height['medium'] & activity['poor'], calories['dismal'])
rule41 = ctrl.Rule(bmi['obese'] & height['medium'] & activity['average'], calories['poor'])
rule42 = ctrl.Rule(bmi['obese'] & height['medium'] & activity['good'], calories['mediocre'])

rule43  = ctrl.Rule(bmi['obese'] & height['high'] & activity['poor'], calories['poor'])
rule44 = ctrl.Rule(bmi['obese'] & height['high'] & activity['average'], calories['mediocre'])
rule45 = ctrl.Rule(bmi['obese'] & height['high'] & activity['good'], calories['average'])

rule46 = ctrl.Rule(bmi['obese'] & height['very high'] & activity['poor'], calories['mediocre'])
rule47 = ctrl.Rule(bmi['obese'] & height['very high'] & activity['average'], calories['average'])
rule48 = ctrl.Rule(bmi['obese'] & height['very high'] & activity['good'], calories['decent'])


rule49 = ctrl.Rule(bmi['very obese'] & (height['very short'] | height['short']) & activity['poor'], calories['dismal'])
rule50 = ctrl.Rule(bmi['very obese'] & (height['very short'] | height['short']) & activity['average'], calories['dismal'])
rule51 = ctrl.Rule(bmi['very obese'] & (height['very short'] | height['short']) & activity['good'], calories['dismal'])

rule52 = ctrl.Rule(bmi['very obese'] & height['medium'] & activity['poor'], calories['dismal'])
rule53 = ctrl.Rule(bmi['very obese'] & height['medium'] & activity['average'], calories['dismal'])
rule54 = ctrl.Rule(bmi['very obese'] & height['medium'] & activity['good'], calories['poor'])

rule55  = ctrl.Rule(bmi['very obese'] & height['high'] & activity['poor'], calories['dismal'])
rule56 = ctrl.Rule(bmi['very obese'] & height['high'] & activity['average'], calories['poor'])
rule57 = ctrl.Rule(bmi['very obese'] & height['high'] & activity['good'], calories['mediocre'])

rule58 = ctrl.Rule(bmi['very obese'] & height['very high'] & activity['poor'], calories['poor'])
rule59 = ctrl.Rule(bmi['very obese'] & height['very high'] & activity['average'], calories['mediocre'])
rule60 = ctrl.Rule(bmi['very obese'] & height['very high'] & activity['good'], calories['average'])

ruleLs = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
	rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
	rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30,
	rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40,
	rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50,
	rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60]

calorie_ctrl = ctrl.ControlSystem(ruleLs)

calcCalorie = ctrl.ControlSystemSimulation(calorie_ctrl)

print("Fuzzy logic based Calorie intake suggestion system")

print("Enter '-1' to stop the system or click any key to continue")
end = input()
while (end !="-1"):
	try:
		print("Enter your height (cm) : ")
		heightInp = float(input())
		calcCalorie.input['height'] = heightInp

		print("Enter your weight (kg) : ")
		weightInp = float(input())
		BMIval = weightInp/((heightInp/100)**2)
		calcCalorie.input['bmi'] = BMIval

		print("On a scale from 0 to 10, how physically active are you every day? : ")
		inpActivity = float(input())
		calcCalorie.input['activity'] = inpActivity

	except(IOError, OSError, ValueError) as err :
		print("Error : " + err)

	calcCalorie.compute()

	print("BMI = %.3f \nYour suggested daily intake is %.3f calories." %(BMIval,calcCalorie.output['calorie']))
	calories.view(sim=calcCalorie)
	print("##################\nEnter '-1' to stop the system or click any key to continue")
	end = input()

