# PROGRAM Population_Approximator
# BEGIN
#     organisms_start = user_input
#     average_pop_inc = user_input
#     multiply_days = user_input
# Create validation for organisms_start and multiply_days to be integers. Convert average_pop_inc to percentage.
# Then, print out the number of each day and the increment in organisms_start
#     FOR x until multiply_days
#         PRINT organisms_start
#         organisms_start * (1 + average_pop_inc)
# END

orgs_string = "Please input the starting number of organisms: "
pops_string = "Please input the average daily increase: "
days_string = "Please input the number of days to multiply: "

def check_input(s):
    while s.isdigit() == False:
        s = input("Please input a valid integer: ")
    return int(s)

def check_perc_input(s):
    while s.isdigit() == False:
        s = input("Please input a valid integer: ")
    perc =  int(s)
    while not 0 < perc < 101:
        perc = int(input("Please input a value between 0 - 100: "))
    return perc/100

organisms_number = check_input(input(orgs_string))
average_pop_inc = check_perc_input(input(pops_string))
multiply_days = check_input(input(days_string))

for x in range(1,multiply_days+1):
    organisms_number = organisms_number * (1 + average_pop_inc)
    print("Day {}: {}".format(x,organisms_number))
    