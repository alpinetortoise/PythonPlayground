##########
#
#   Author: AB Luke Miller
#   Creation date: 18/02/2025
#   Name:Simple Conversion Program
#   Version:3.0
#
##########

import os
##
#   Setup the main menu
##
menu = {}
menu['1']="Convert Centimeters and Inches"
menu['2']="Convert Meters and Feet"
menu['3']="Convert Kilometers and Miles"
menu['4']="Convert Grams and Ounces"
menu['5']="Convert Kilograms and Pounds"
menu['6']="Convert Mililitres and Fluid Ounces"
menu['7']="Convert Litres and Quarts"
menu['8']="Exit"
##
#   Setup the sub menu for centimeter and inches
##
menu1={}
menu1['1']="Centimeters to Inches"
menu1['2']="Inches to Centimeters"
##
#   Setup the sub menu for meters and feet
##
menu2={}
menu2['1']="Convert Meters to Feet"
menu2['2']="Convert Feet to Meters"
##
#   Setup the sub menu for kilometers and miles
##
menu3={}
menu3['1']="Convert Kilometers to Miles"
menu3['2']="Convert Miles to Kilometers"
##
#   Setup the sub menu for grams and ounces
##
menu4={}
menu4['1']="Conver Grams to Ounces"
menu4['2']="Convert Ounces to Grams"
##
#   Setup the sub menu for kilograms and pounds
##
menu5={}
menu5['1']="Convert Kilograms to Pounds"
menu5['2']="Convert Pounds to Kilograms"
##
#   Setup the sub menu for mililiters to fluid ounces 
##
menu6={}
menu6['1']="Convert Mililiters to Fluid ounces"
menu6['2']="Convert Fluid Ounces to Mililiters"
##
#   Setup the sub menu for liters to quarts
##
menu7={}
menu7['1']="Convert Liters to Quarts"
menu7['2']="Convert Quarts to Liters"
##
#   Start the main block
##
while True:
    os.system('cls||clear')
    for entry in menu:
        print (entry, menu[entry])
##
#   Ask the user what conversion type they want to run.
##
    selection=input("Please select:")
##
#   Centimeter and Inches block start
##
    if selection =='1':
        os.system('cls||clear')
        while True:
            for entry in menu1:
                print (entry, menu1[entry])
            try:
                option=int(input("Please Select:"))
            except ValueError:
                os.system('cls||clear')
                print("Please enter a valid integer")
                input("Press any key to continue...")
                os.system('cls||clear')
                continue
            break
        if option ==1:
            os.system('cls||clear')
            while True:
                try:
                    value1 = float(input("Please enter Centimeters to be converted to Inches:"))
                except ValueError:
                    os.system('cls||clear')
                    print('Please enter a valid integer')
                    input("Press any key to continue...")
                    os.system('cls||clear')
                    continue
                break
            os.system('cls||clear')
            value2=float(value1)*0.393
            print(str(value1) + " CM is " + str(value2) + " in Inches" )
            input("Press any key to continue...")
            os.system('cls||clear')
        elif option ==2:
            os.system('cls||clear')
            while True:
                try:
                    value1 = float(input("Please enter Inches to be converted to Centimeters:"))
                except ValueError:
                    os.system('cls||clear')
                    print('Please enter a valid integer')
                    input("Press any key to continue...")
                    os.system('cls||clear')
                    continue
                break
            os.system('cls||clear')
            value2=float(value1)*2.54
            print(str(value1) + " Inches is " + str(value2) + " in Centimeters" )
            input("Press any key to continue...")
            os.system('cls||clear')
##
#   Centimeter and inches end
##

##
#   Meters and Feet Start
##
    elif selection =='2':
        os.system('cls||clear')
        while True:
            for entry in menu2:
                print (entry, menu2[entry])
            try:
                option=int(input("Please Select:"))
            except ValueError:
                os.system('cls||clear')
                print("Please enter a valid integer")
                input("Press any key to continue...")
                os.system('cls||clear')
                continue
            break
        if option ==1:
            os.system('cls||clear')
            while True:
                try:
                    value1 = float(input("Please enter Meters to be converted to Feet:"))
                except ValueError:
                    os.system('cls||clear')
                    print('Please enter a valid integer')
                    input("Press any key to continue...")
                    os.system('cls||clear')
                    continue
                break
            os.system('cls||clear')
            value2=float(value1)*3.281
            print(str(value1) + " Meters is " + str(value2) + " in Feet" )
            input("Press any key to continue...")
            os.system('cls||clear')
        elif option ==2:
            os.system('cls||clear')
            while True:
                try:
                    value1 = float(input("Please enter Feet to be converted to Meters:"))
                except ValueError:
                    os.system('cls||clear')
                    print('Please enter a valid integer')
                    input("Press any key to continue...")
                    os.system('cls||clear')
                    continue
                break
            os.system('cls||clear')
            value2=float(value1)*0.305
            print(str(value1) + " Feet is " + str(value2) + " in Meters" )
            input("Press any key to continue...")
            os.system('cls||clear')
##
#   Meters and Feet end
##

##
#   Kilometer and Miles Start
##
    elif selection =='3':
        os.system('cls||clear')
        while True:
            for entry in menu3:
                print (entry, menu3[entry])
            try:
                option=int(input("Please Select:"))
            except ValueError:
                os.system('cls||clear')
                print("Please enter a valid integer")
                input("Press any key to continue...")
                os.system('cls||clear')
                continue
            break
        if option ==1:
            os.system('cls||clear')
            while True:
                try:
                    value1 = float(input("Please enter Kilometers to be converted to Miles:"))
                except ValueError:
                    os.system('cls||clear')
                    print('Please enter a valid integer')
                    input("Press any key to continue...")
                    os.system('cls||clear')
                    continue
                break
            os.system('cls||clear')
            value2=float(value1)*0.621
            print(str(value1) + " Kilometers is " + str(value2) + " in Miles" )
            input("Press any key to continue...")
            os.system('cls||clear')
        elif option ==2:
            os.system('cls||clear')
            while True:
                try:
                    value1 = float(input("Please enter Miles to be converted to Kilometers:"))
                except ValueError:
                    os.system('cls||clear')
                    print('Please enter a valid integer')
                    input("Press any key to continue...")
                    os.system('cls||clear')
                    continue
                break
            os.system('cls||clear')
            value2=float(value1)*1.609
            print(str(value1) + " Kilometers is " + str(value2) + " in Miles" )
            input("Press any key to continue...")
            os.system('cls||clear')
##
#   Kilometers and Miles end
##

##
#   Grams and Ounces start
##
    elif selection =='4':
        os.system('cls||clear')
        while True:
            for entry in menu4:
                print (entry, menu4[entry])
            try:
                option=int(input("Please Select:"))
            except ValueError:
                os.system('cls||clear')
                print("Please enter a valid integer")
                input("Press any key to continue...")
                os.system('cls||clear')
                continue
            break
        if option ==1:
            os.system('cls||clear')
            while True:
                try:
                    value1 = float(input("Please enter Grams to be converted to Ounces:"))
                except ValueError:
                    os.system('cls||clear')
                    print('Please enter a valid integer')
                    input("Press any key to continue...")
                    os.system('cls||clear')
                    continue
                break
            os.system('cls||clear')
            value2=float(value1)*0.035
            print(str(value1) + " Grams is " + str(value2) + " in Ounces" )
            input("Press any key to continue...")
            os.system('cls||clear')
        elif option ==2:
            os.system('cls||clear')
            while True:
                try:
                    value1 = float(input("Please enter Ounces to be converted to Grams:"))
                except ValueError:
                    os.system('cls||clear')
                    print('Please enter a valid integer')
                    input("Press any key to continue...")
                    os.system('cls||clear')
                    continue
                break
            os.system('cls||clear')
            value2=float(value1)*28.35
            print(str(value1) + " Grams is " + str(value2) + " in Ounces" )
            input("Press any key to continue...")
            os.system('cls||clear')
##
#   Grams and Ounces end
##

##
#   Kilograms and Pounds start
##
    elif selection =='5':
        os.system('cls||clear')
        while True:
            for entry in menu5:
                print (entry, menu5[entry])
            try:
                option=int(input("Please Select:"))
            except ValueError:
                os.system('cls||clear')
                print("Please enter a valid integer")
                input("Press any key to continue...")
                os.system('cls||clear')
                continue
            break
        if option ==1:
            os.system('cls||clear')
            while True:
                try:
                    value1 = float(input("Please enter Kilograms to be converted to Pounds:"))
                except ValueError:
                    os.system('cls||clear')
                    print('Please enter a valid integer')
                    input("Press any key to continue...")
                    os.system('cls||clear')
                    continue
                break
            os.system('cls||clear')
            value2=float(value1)*2.204
            print(str(value1) + " Kilograms is " + str(value2) + " in Pounds" )
            input("Press any key to continue...")
            os.system('cls||clear')
        elif option ==2:
            os.system('cls||clear')
            while True:
                try:
                    value1 = float(input("Please enter Pounds to be converted to Kilograms:"))
                except ValueError:
                    os.system('cls||clear')
                    print('Please enter a valid integer')
                    input("Press any key to continue...")
                    os.system('cls||clear')
                    continue
                break
            os.system('cls||clear')
            value2=float(value1)*0.454
            print(str(value1) + "Pounds is " + str(value2) + "in Kilograms" )
            input("Press any key to continue...")
            os.system('cls||clear')
##
#   Kilograms and Pounds end
##

##
#   Mililiters and Fliud Ounces
##
    elif selection =='6':
        os.system('cls||clear')
        while True:
            for entry in menu6:
                print (entry, menu6[entry])
            try:
                option=int(input("Please Select:"))
            except ValueError:
                os.system('cls||clear')
                print("Please enter a valid integer")
                input("Press any key to continue...")
                os.system('cls||clear')
                continue
            break
        if option ==1:
            os.system('cls||clear')
            while True:
                try:
                    value1 = float(input("Please enter Mililiters to be converted to Fluid Ounces:"))
                except ValueError:
                    os.system('cls||clear')
                    print('Please enter a valid integer')
                    input("Press any key to continue...")
                    os.system('cls||clear')
                    continue
                break
            os.system('cls||clear')
            value2=value1
            value1=float(value1)*0.035
            print(str(value2) + " Mililiters is " + str(value1) + " in Fluid Ounces" )
            input("Press any key to continue...")
            os.system('cls||clear')
        elif option ==2:
            os.system('cls||clear')
            while True:
                try:
                    value1 = float(input("Please enter Fluid Ounces to be converted to Mililiters:"))
                except ValueError:
                    os.system('cls||clear')
                    print('Please enter a valid integer')
                    input("Press any key to continue...")
                    os.system('cls||clear')
                    continue
                break
            os.system('cls||clear')
            value2=float(value1)*28.413
            print(str(value1) + " Mililiters is " + str(value2) + " in Fluid Ounces" )
            input("Press any key to continue...")
            os.system('cls||clear')
##
#   Mililiters and Fluid Ounces end
##

##
#   Liters and Quarts Start
##
    elif selection =='7':
        os.system('cls||clear')
        while True:
            for entry in menu7:
                print (entry, menu7[entry])
            try:
                option=int(input("Please Select:"))
            except ValueError:
                os.system('cls||clear')
                print("Please enter a valid integer")
                input("Press any key to continue...")
                os.system('cls||clear')
                continue
            break
        if option ==1:
            os.system('cls||clear')
            while True:
                try:
                    value1 = float(input("Please enter Liters to be converted to Quarts:"))
                except ValueError:
                    os.system('cls||clear')
                    print('Please enter a valid integer')
                    input("Press any key to continue...")
                    os.system('cls||clear')
                    continue
                break
            os.system('cls||clear')
            value2=float(value1)*0.878
            print(str(value1) + " Liters is " + str(value2) + " in Quarts" )
            input("Press any key to continue...")
            os.system('cls||clear')
        elif option ==2:
            os.system('cls||clear')
            while True:
                try:
                    value1 = float(input("Please enter Quarts to be converted to Liters:"))
                except ValueError:
                    os.system('cls||clear')
                    print('Please enter a valid integer')
                    input("Press any key to continue...")
                    os.system('cls||clear')
                    continue
                break
            os.system('cls||clear')
            value2=float(value1)*1.137
            print(str(value1) + " Quarts is " + str(value2) + " in Liters" )
            input("Press any key to continue...")
            os.system('cls||clear')
##
#   Liters and Quarts end
##

# Exit option
    elif selection =='8':
        break
# Catch any mis inputs
    else:
        os.system('cls||clear')
        print ("Unknown Option Selected")
        input('Press any key to continue...')
        os.system('cls||clear')