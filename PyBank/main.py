# import modules
import os 
import csv

# Setting a Path to a Variable to collect data from the Resources folder called 'bank_file'

bank_file = os.path.join( "Resources", "budget_data.csv")

# Set up variables

Total_Months = 0

Total_Profit_Loss = 0

increase = 0

decrease = 0

Change_Profit_Loss = []

Monthly_Change = []

# Open csv and read it 

with open(bank_file, 'r') as csvfile:
    
    # Splitting data with (Comma) delimiter = ','
    
    csvreader = csv.reader(csvfile, delimiter= ",")

    # This skips header to go on to the next row in csv file

    header = next(csvreader)

    # Looping through rows in file after header
    for row in csvreader:

        # += is same as x = x + 1
        #Total_Profit_Loss is set at 0 and will add the value thats in 
        # column 2 (row[1])
        
        Total_Months += 1
        Total_Profit_Loss += int(row[1])

        
        if int(row[1]) > increase:
            best_month = (row[0])
            increase = int(row[1])
        
        #Keep getting error without setting decrease variable to an integer

        elif int(row[1]) < int(decrease):
            worst_month = (row[0])
            decrease = (row[1])
        
        #append to empty list 
        Change_Profit_Loss.append(int(row[1]))

# Monthly Changes
for i in range(len(Change_Profit_Loss)-1):
    monthly = (Change_Profit_Loss[i+1] - Change_Profit_Loss[i])
    Monthly_Change.append(monthly)

average_Change = round(sum(Monthly_Change) / len(Monthly_Change), 2)

# Print to Terminal

print("Financial Analysis")
print("___________________________________")

print("Total Months: " + str(Total_Months))
print("Total: $" + str(Total_Profit_Loss))
print("Average Change is: $" + str(round(average_Change, 2)))
print("Greatest Increase in Profits: " + str(best_month) + "  ($" + str(increase) + ")")
print("Greatest Decrease in Profits: " + str(worst_month) + "  ($" + str(decrease) + ")")



# Write out to analysis folder

output_path = os.path.join("analysis", "final_analysis.txt")

with open(output_path, 'w') as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("------------------------")
    file.write("\n")
    file.write("Total Months: " + str(Total_Months))
    file.write("\n")
    file.write("Total: $" + str(Total_Profit_Loss))
    file.write("\n")
    file.write("Average Change is: $" + str(round(average_Change, 2)))
    file.write("\n")
    file.write("Greatest Increase in Profits: " + str(best_month) + "  ($" + str(increase) + ")")
    file.write("\n")
    file.write("Greatest Decrease in Profits: " + str(worst_month) + "  ($" + str(decrease) + ")")
