# PROGRAM RainfallStatistics
# Create a dictionary, iterate through months 1 to 12 and assign values to correspond to each month.
#     MonthlyDict = {}
#     for x in range(1,13)
#         MonthlyDict[x] = user_input
#     validate user input for integers
# Then find the sum of all the values, iterate and find the average of the values, and use the max and min functions
#       PRINT SUM(MonthlyDict.values)
#       PRINT SUM(MonthlyDict.values)/LEN(MonthlyDict)
#       PRINT MAX(MonthlyDict.values) + MAX(MonthlyDict, key = MonthlyDict.get)
#       repeat for MIN
#    END

def check_input(s):
    while s.isdigit() == False:
        s = input("Please input a positive, whole number: ")
    return int(s)

monthly_dict = {}
for x in range(1,13):
    print("Month #{}".format(x))
    monthly_dict[x] = check_input(input("Please input the total rainfall for this month: "))

# Total Annual Rainfall
total_rain = sum(monthly_dict.values())
print("Total Annual Rainfall: {}".format(total_rain))

# Average Monthly Rainfall
average_rain = total_rain/len(monthly_dict)
print("Average Monthly Rainfall: {}".format(average_rain))
 
#  Max and Min Rainfall
max_rain = max(monthly_dict.values())
max_rain_month = max(monthly_dict, key=monthly_dict.get)
min_rain = min(monthly_dict.values())
min_rain_month = min(monthly_dict, key=monthly_dict.get)

print("Highest rainfall: Month #{} -> {}".format(max_rain_month,max_rain))
print("Lowest rainfall: Month #{} -> {}".format(min_rain_month,min_rain))

