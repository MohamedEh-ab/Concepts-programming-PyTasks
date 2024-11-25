# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:24:23 2024

@author: Moham
"""

# 1
while(1):
    step_input = input("Enter Number of steps for 30 days seperate each number by space:\n\t>>> ")
    print("----------------------------------------")
    steps = list(map(int, step_input.split()))
    if len(steps) > 30:
        print("Steps count exceeded month, please enter only count for 30 days!")
        continue
    else:
        break
# 2
# one answer(using sorted())
sorted_steps = sorted(steps)
print(sorted_steps)
lowest_step, highest_step = sorted_steps[0], sorted_steps[-1]
#another answer(using max() and min())
highest_step2, lowest_step2 = max(steps), min(steps)
#------------
print(f"Your Highest Step count is {highest_step2}\nYour lowest Step count is {lowest_step2}")
# 3
avg_steps = round(sum(steps) / 30, 3) 
# ------------
print(f"Your average daily steps is {avg_steps}")
# 4
# one answer(using sorted(x, reverse=True))
sorted_desc_steps = sorted(steps, reverse=True)
print(sorted_desc_steps)
# another answer(looping)
desc_steps = steps
for i in range(len(desc_steps)):
    for j in range(i+1, len(desc_steps)):
        if desc_steps[j] > desc_steps[i]:
            desc_steps[i], desc_steps[j] = desc_steps[j], desc_steps[i]
        
print(desc_steps)