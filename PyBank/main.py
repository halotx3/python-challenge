import os
import csv

budgetCSV = os.path.join("Resources", "budget_data.csv")

with open(budgetCSV, newline="") as budgetFile:
    csvreader = csv.reader(budgetFile, delimiter=",")

    # Getting the number of dates in the CSV
    dateNum = 0
    for row in csvreader:
        dateNum = dateNum + 1
    #Accounts for the header when counting
    dateNum = dateNum -1

    
    print (dateNum)