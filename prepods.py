# -*- coding:utf -8 -*-
#!/usr/bin/python3
import math
import csv

with open('exams.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        Surname = row['Surname']
        Name = row['Name']
        LastName = row['LastName']
        print("", Surname, Name, LastName)


