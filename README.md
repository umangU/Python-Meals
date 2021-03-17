# Python-Meals

Meals
Meals is a Python program designed to get the patient's dietary needs and provide an appropriate diet based on the lowest error criteria while appending the result in a file to be sent to the kitchen.

Run
The file should be made executable first and then the program should be run using python3 interpreter.

chmod +x meals.py
python3 meals.py

Additional Libraries
Re - The python library provides regular expression matching operations.
CSV - The python library provides classes to read and write tabular data in CSV format.

import re
import csv

re.compile('[a-zA-Z]+$') # compiles regular expressions in '' into pattern objects
re.match(re_pattern, input_string) # matching the regular expression pattern to input string
csv.writer(csvfile) # returns a writer object responsible for converting the entered data into delimited strings.
csvwriter.writerow(row) # writes the row parameter to the writer’s file object, formatted as per the current dialect.

License
GNU AGPLv3
