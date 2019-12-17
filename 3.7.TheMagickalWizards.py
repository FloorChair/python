'''
When we read code and predict its output,
it is called tracing code.

For this lesson you will come up with your 
own challenging algorithm for other students to trace. 
It must contain at least 5 - if statements and use at 
least one AND or OR boolean condition. 
Run it in the sandbox, 
then copy and paste your code in Piazza for 
other students to try.

For this challenge try reading 3 or 4 other students' 
code - trace the code and predict what it outputs, 
then run it in the sandbox to see if you got it right.
'''
import random
iterations = 100
count = 0
count_mn = 0
count_mx = 0
count_md = 0
rv = 0
sum = 0
done = False
'''
Explain what this algorithm does along with
describing the variable names.
-(Answer): The top portion provides and import for random numbers to be generated down below. Then variables are provided integers so that they can act as a minimum, maximum and median value.
Secondly, the count function is created to keep track of each variable and print such down below. "rv" Acts as a variable for the random function to be imported into maximum and the minimum value.
Thirdly, done = False provides and variable for the while loop for the user to input the maximum and minimum. Now, the second portion acts as a means to import values until the algorithim detects a minimum value
less than maximum. Done = True pushes the program onwards. Fourthly, the next portion explains as to what the median and random variable is. Also, the print lines state the string rv and " " in order to print the 
random integers from minimum unto maximum. The rest counts the amount of times each variable loops and eventually prints the final values below.
'''
while(done==False):
 mn = int(input("Input a minimum integer value: "))
 mx = int(input("Input a maximum integer value: "))
 iterations = int(input("Input an iteration value: "))
 if(mn<mx):
  done=True
md = int((mx - mn)/2)
while(count < iterations):
 rv = random.randint(mn,mx)
 sum = sum + rv
 if (count % 10 == 0 and count != 0):
  print()
 print str(rv)+str(" ")
 count = count+1
 if(rv == mn):
  count_mn = count_mn + 1
 if(rv == mx):
  count_mn = count_mx + 1
 if(rv == md):
  count_mn = count_md + 1
'''
Write code to explain what this output represents.
'''
print("\n\nmn = minimum value output , count_mn = count the minimum value, md = median output, count_md = count median output, mx = maximum value output, count_mx = count the maximum value")
print(mn, count_mn, md, count_md, mx, count_mx)
print("The MEAN is the average of all the numbers.")
print("MEAN = " ,float(sum/iterations))
