'''
Program objective - determine the award a person has won in a triathlon.  
Requirements are:
1. read the time in minutes for all three parts of the tri - swim, bike, run
2. calculate the total time for all three
3. print the total time for all three and any award message
Considerations for users inputting letters or other characters or decimals. Error message and loop back to request again  

The qualifying time for an award is 100 mins adjusted by:
 <=100 mins gets "Provincial Colours
 >= 101 and <= 105 gets "Provincial Half Colours
  >=106 and <= 110 gets "Provincial Scroll"
   >=111 mins gets no award 
   
'''

while True:
    swim_split = input("Please input the time in minutes (round up or down) for your swim leg, including your transition time to the bike: ")
    if not swim_split.isnumeric():
        print("Input must be a number rounded to the nearest minute")
        continue
    break
act_swim_split = int(swim_split)

bike_split = input("Please input the time in minutes for your bike leg, including your transition time to the run (note - if you did not finish please put 0): ")
while not bike_split.isnumeric():
    print("Please enter your split time in round minutes")
    bike_split = input("Enter your bike split: ")
act_bike_split = int(bike_split)
run_split = input("Please input the time in minutes for your run leg: ")

while not run_split.isnumeric():
    print("Please enter your split time in round minutes.  If you did not finish, please enter 0.")
    run_split = input("Enter your run split: ")
act_run_split = int(run_split)
total_tri_time = act_swim_split + act_bike_split + act_run_split

if total_tri_time <= 100:
    if act_bike_split <= 0:
        print("Unfortunately, because you didn't finish you're not eligible for an award. Better luck next year!")
    elif act_run_split <= 0:
        print("Unfortunately, because you didn't finish you're not eligible for an award. Better luck next year!")
    else:
        print("You've earned a Provincial Colours award!  Excellent job!")
elif 101 <= total_tri_time <= 105:
    print("You've earned Provincial Half Colours!  Well done.")
elif 106 <= total_tri_time <= 110:
    print("You've earned a Provincial Scroll award.  Keep up the good work!")
else:
    print(f"Good work finisher! Your time, {total_tri_time} minutes, did not earned an award, but keep training and we hope to see you next year!")

# print(f"Your total triathlon time was {total_tri_time} minutes.")