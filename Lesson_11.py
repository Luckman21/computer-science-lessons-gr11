'''
Created on May 3, 2017

@author: Luqmaan
'''
import time

total = 0
num1 = 0

print "Welcome to the \"Mark Calculator\"!\n"
time.sleep(1)
num = input ("How many marks will you enter?\n: ")
print

while num1 < num:
    
    while True:

        time.sleep(1)
        num1+=1
        mark = input ("Enter your mark: ")
        
        if mark >= 0 and mark <= 100:
            total+=mark
            break
        
        else:
            print "\nInvalid input.  Please enter number between 0 and 100.\n"

time.sleep(1)  
print "\nYou entered "+str(num)+" marks."
time.sleep(1)
total = "%.1f" %(total/num)
print "Your average is "+total