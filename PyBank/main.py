# Import packages
import os
import csv

# Import CSV
budget_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)

    # Establish necessary variables
    Count = 0
    Total = 0
    PriorRow = []
    CurrentRow = []
    Month = []

    # Iterate through the rows in the CSV
    for row in csv_reader:
        Count = Count + 1
        Total = int(row[1]) + Total
        PriorRow.append(row[1])
        CurrentRow.append(row[1])
        Month.append(row[0])

    # Start the building blocks for the average change.
    PriorRow_Index = range(0, len(PriorRow)-1)
    PriorRow_List = list(PriorRow_Index)
    PriorRow_Value = []

    for index in PriorRow_List:
        PriorRow_Value.append(PriorRow[index])

    CurrentRow_Index = range(1, len(CurrentRow))
    CurrentRow_List = list(CurrentRow_Index)
    CurrentRow_Value = []

    for index in CurrentRow_List:
        CurrentRow_Value.append(CurrentRow[index])

    #Calculate the average change and iterate to find the corresponding dates.
    TotalChange = 0
    GreatestCalc = []

    for Value in range(0, len(CurrentRow_Value)):
        Change = int(CurrentRow_Value[Value]) - int(PriorRow_Value[Value])
        TotalChange = TotalChange + Change
        AverageChange = TotalChange / (Count - 1)
        GreatestCalc.append(Change)    
        GreatestIncrease = max(GreatestCalc)
        GreatestDecrease = min(GreatestCalc)
        
    for Value in range(0, len(GreatestCalc)):    
        if GreatestIncrease == GreatestCalc[Value]:
            GreatestIncreaseMonth = Month[Value + 1] 
        elif GreatestDecrease == GreatestCalc[Value]:
            GreatestDecreaseMonth = Month[Value + 1]
        
# Format numbers
AverageChange = '{:.2f}'.format(AverageChange)

# Output to the terminal.
print("Financial Analysis")
print("-------------------------------")
print("Total Months: ", Count)
print("Total: $", Total)
print("Average Change: $", AverageChange)
print("Greatest Increase in Profits: ", GreatestIncreaseMonth,"($", GreatestIncrease, ")")
print("Greatest Decrease in Profits: ", GreatestDecreaseMonth, "($", GreatestDecrease, ")")

# Output to text file.
one = "Financial Analysis"
two = "-------------------------------"
three = "Total Months: ", Count
four = "Total: $", Total
five = "Average Change: $", AverageChange
six = "Greatest Increase in Profits: ", GreatestIncreaseMonth,"($", GreatestIncrease, ")"
seven = "Greatest Decrease in Profits: ", GreatestDecreaseMonth, "($", GreatestDecrease, ")"

lines = [one, two, three, four, five, six, seven] 
with open("Output.txt", "w") as f:
    for line in range(0, len(lines)):
        f.write(str(lines[line]))
        f.write("\n")