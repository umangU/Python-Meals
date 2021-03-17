#Importing Regular Expression, CSV file - Reading and Writing Libraries
import re
import csv

#Function declaration while accepting user input as arguments
def choose_diet(p,c,f):
    #Dictionary initialized based on user inputs
    requirement = {patientid:{'Protein':p, 'Carbohydrates':c,'Fat':f}}
    #Dictionary created and initialized as per the diet chart
    diet = {
      'Normal':{'Protein':32.50,'Carbohydrates':60.00,'Fat':40.86},
      'Oncology':{'Protein':35.00,'Carbohydrates':52.50,'Fat':37.63},
      'Cardiology':{'Protein':32.50,'Carbohydrates':30.00,'Fat':26.88},
      'Diabetes':{'Protein':20.00,'Carbohydrates':27.50,'Fat':27.95},
      'Kidney':{'Protein':15.00,'Carbohydrates':55.00,'Fat':23.65}
      }

    #Function call for calculating error
    empty = calculate_error(requirement,diet)

    #Looping through all the dictionary items
    for key in empty.items():
        #Calculating the minimum value amongst all the items in dictionary
        key = min(empty, key = lambda k:empty[k])
    print("Selected diet:",key)

    #Appending the output in the meals.csv file
    outfile = open("./meals.csv","a")
    writer = csv.writer(outfile)
    row = patientid+","+key
    writer.writerow([row])

#Function declaration while accepting requirements and diet dictionary as arguments
def calculate_error(r,d):
    #Creating an empty dictionary
    e = dict()
    #Calculating the absolute difference between the user requirements and diet provided
    res1 = (abs(d['Normal']['Protein'] - float(r[patientid]['Protein'])) + abs((d['Normal']['Carbohydrates'] - float(r[patientid]['Carbohydrates']))) + abs((d['Normal']['Fat'] - float(r[patientid]['Fat']))))
    #Appending the resulted value in the dictionary
    e['Normal'] =res1
    res2 = (abs(d['Oncology']['Protein'] - float(r[patientid]['Protein'])) + abs((d['Oncology']['Carbohydrates'] - float(r[patientid]['Carbohydrates']))) + abs((d['Oncology']['Fat'] - float(r[patientid]['Fat']))))
    e['Oncology'] = res2
    res3 = (abs(d['Cardiology']['Protein'] - float(r[patientid]['Protein'])) + abs((d['Cardiology']['Carbohydrates'] - float(r[patientid]['Carbohydrates']))) + abs((d['Cardiology']['Fat'] - float(r[patientid]['Fat']))))
    e['Cardiology'] = res3
    res4 = (abs(d['Diabetes']['Protein'] - float(r[patientid]['Protein'])) + abs((d['Diabetes']['Carbohydrates'] - float(r[patientid]['Carbohydrates']))) + abs((d['Diabetes']['Fat'] - float(r[patientid]['Fat']))))
    e['Diabetes'] = res4
    res5 = (abs(d['Kidney']['Protein'] - float(r[patientid]['Protein'])) + abs((d['Kidney']['Carbohydrates'] - float(r[patientid]['Carbohydrates']))) + abs((d['Kidney']['Fat'] - float(r[patientid]['Fat']))))
    e['Kidney'] = res5
    #Returning the dictionary
    return e

value = "Sample_Text"
while(value != ""):
    patientid = input("Please enter a patient id (or blank to exit): ")
    #For no user input the loop breaks and program exits
    if(patientid == ""):
        break;
    else:
        pattern = re.compile('[a-zA-Z]+$')
        #Input Validation and asking user to re-enter the data
        while (re.match(pattern, patientid) or patientid[:1] == '0' or len(patientid) > 6 or int(patientid) < 0):
            print("Please enter a valid patient id (six-digit positive integer)")
            patientid = input("Please enter a patient id (or blank to exit): ")

        protein = input("Amount of protein (g) required: ")
        #Input Validation and asking user to re-enter the data
        while (re.match(pattern, protein) or len(protein) == 0 or float(protein) < 0.0):
            print("Please enter a nonnegative number")
            protein = input("Amount of protein (g) required: ")

        carbohydrate = input("Amount of carbohydrates (g) required: ")
        while (re.match(pattern, carbohydrate) or len(carbohydrate) == 0 or float(carbohydrate) < 0.0):
            print("Please enter a nonnegative number")
            carbohydrate = input("Amount of carbohydrates (g) required: ")

        fat = input("Amount of fat (g) required: ")
        while (re.match(pattern, fat) or len(fat) == 0 or float(fat) < 0.0):
            print("Please enter a nonnegative number")
            fat = input("Amount of fat (g) required: ")

        #Declaring a global empty dictionary
        empty = dict()
        #Function call while passing user input as arguments
        choose_diet(protein,carbohydrate,fat)
