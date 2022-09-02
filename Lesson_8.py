'''
Created on Apr 19, 2017

@author: Luqmaan
'''
num1 = input ("Please enter one number: ")
num2 = input ("Please enter another number: ")
num3 = input ("Please enter your final number: ")
'''
if num1 > num2:
    print str(num1)+" is greater than "+str(num2)+", therefore\nthe first number is greater than the second"

elif num1 == num2:
    print str(num1)+" is equal to "+str(num2)+", therefore, \nboth numbers are equal."    

else:
    print str(num2)+" is greater than "+str(num1)+", therefore,\nthe second number is greater than the first"
'''
if num1 >= num2 and num1 >= num3:
    print +str(num1)+" is the greatest."
    
elif num2 >= num1 and num2 >= num3:
    print str(num2)+" is the greatest."

else:
    print str(num3)+" is the greatest."
