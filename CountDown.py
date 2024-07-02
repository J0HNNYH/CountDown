import time
#creates variable named timer
#takes user input as an integer
timer = int(input(">> "))
#countinues to loop unitl the timer hits 0
while timer > 0:
#displays timer
    print(timer)
#creates time gap of 1
    time.sleep(1)
#updates the number on the timer
    timer -=1
#tells user timer is finished
print("Time is up!")
