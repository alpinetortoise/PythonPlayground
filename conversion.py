print ("Usage: converts a value between Metric and Imperial units")

print("""Valid units:
        - Length:
          - Metric: cm, m, km
          - Imperial: inch, ft, mile
        - Weight:
          - Metric: g, kg
          - Imperial: oz, lb
        - Volume:
          - Metric: ml, l
          - Imperial: floz, qt
        - Temperature: F, C
      """)
# grab a string with the units from the user
userString = input("Input a value: ")
sourceUnit = input("Input your source unit: ")
targetUnit = input("Input your target unit: ")

metricUnits = [ "cm", "m", "km", "g", "kg", "ml", "l" ]
imperialUnits = [ "inch", "ft", "mile", "oz", "lb", "floz", "qt" ]
tempUnits = [ "C", "F" ]

metricConversion = {
        ("cm","inch") : 0.393,
        ("m","inch") : 39.37,
        ("km","inch") : 39370,
        ("cm","ft") : 0.032,
        ("m","ft") : 3.28,
        ("km","ft") : 3280.84,
        ("cm","mile") : 0.0000062137,
        ("m","mile") : 0.0006213712,
        ("km","mile") : 0.6213712,
        ("g","oz") : 0.035,
        ("g","lb") : 0.002205,
        ("kg","oz") : 35.273,
        ("kg","lb") : 2.204,
        ("ml","floz") : 0.035,
        ("ml","qt") : 0.0010566,
        ("l","floz") : 35.195,
        ("l","qt") : 0.878
        }

imperialConversion = {
        ("inch","cm") : 2.54,
        ("inch","m") : 0.0254,
        ("inch","km") : 0.0000254,
        ("ft","km") : 0.0003048,
        ("ft","m") : 0.3048,
        ("ft","cm") : 30.48,
        ("mile","cm") : 160934.4,
        ("mile","m") : 1609.344,
        ("mile","km") : 1.609344,
        ("oz","g") : 28.35,
        ("oz","kg") : 0.02834,
        ("lb","g") : 453.5924,
        ("lb","kg") : 0.45359,
        ("floz","ml") : 28.413,
        ("floz","l") : 0.0284,
        ("qt","ml") : 946.353,
        ("qt","l") : 1.137
        }

value = 0

if sourceUnit in tempUnits:
    if sourceUnit == "F":
       value = (float(userString) - 32) / 1.8
    elif sourceUnit == "C":
        value = (float(userString) * 1.8) + 32
elif sourceUnit in metricUnits:
     conv = metricConversion[(sourceUnit,targetUnit)]
     value = float(userString)
     value = conv * value
else:
     conv = imperialConversion[(sourceUnit,targetUnit)]
     value = float(userString)
     value = conv * value

print("The conversion of {}{} into {} is {}{}".format(userString,sourceUnit,targetUnit,value,targetUnit))
