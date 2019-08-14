# BEGIN FallingDistance
#     Define constant g = 9.8
#     Create Function falling_distance
#     def falling_distance(time)
#        return 0.5* g * time^2
#     Create for loop to loop function through 1..10
#     for x in range(11)
#         falling_distance(x)
# END

g = 9.8

def falling_distance(time):
    print(0.5 * g * time**2)

for x in range (11):
    falling_distance(x)