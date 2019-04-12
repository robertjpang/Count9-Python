import math
from tkinter.constants import LEFT
from pickle import FALSE

#global
gIterations = 0
recursiveCount = 0

def NaiveCount(Max, Digit):
    TotalCount = 0; 
    iterationCalc = 0
    for x in range(0, int(n)+1,1):
        num = x; 
        while (num > 0): 
            iterationCalc = iterationCalc + 1
            #s = str(x) + ":" + str(num) 
            #print (s)
            if (num != 0) and (num % 10) == int(Digit): 
                TotalCount = TotalCount + 1
                #s = "Match: " + str(TotalCount)
                #print(s)
            num = int(num / 10); 
    calc = int(n) * math.log(int(n), 10)
    s = "Brute Force - Total Count: " + str(TotalCount) + " IterationCount:" + str(iterationCalc) + " Theoretical Calc: " + str(calc)
    print(s)
    return;




# add my comments

def CountDigitN(num, dd, depth, sum):
    global recursiveCount
    global gIterations
    recursiveCount += 1
    count = 0
    weight = 10**depth
    digit = num % 10
    prevsum = sum
    sum += digit*weight
    cweight = 1
    #print(dd)
    gIterations +=1
    
    if (depth > 1): 
        cweight = (10 ** (depth-1)) * depth    
    
    #s = "CountDigit-" + str(num) + " Digit-" + str(digit) + " Depth-" + str(depth) + " Cweight-" + str(cweight) + " Weight-" + str(weight) + " Sum-" + str(sum)+ " Recursive-" + str(recursiveCount)
    #print(s)

    # Special case - lowest digit is either 1 or 0
    if (depth == 0): 
        if digit >= dd: 
            count = 1
        else: 
            count = 0
    else: 
        count = digit*cweight
        
        # if this digit == the match, then count lower significant digits including itself  
        if (digit == dd):
            count += prevsum + 1
        #if this digit > match, then include the sum 
        elif digit > dd: 
            count += weight

    #Non base case. 
    if num >= 10: 
        count += CountDigitN(int(num/10), dd, depth+1, sum)
    #print(count)
    recursiveCount -= 1 
    return count

n = input("Enter N - 0 to N\n")
b = input("Enter Digit\n")

#n = '973'
#b = '2'

NaiveCount(n, b)

gIterations = 0
count = CountDigitN(int(n), int(b), 0, 0)
s = "Optimized - Count: " + str(count) + " Iterations: " + str(gIterations)
print(s)






