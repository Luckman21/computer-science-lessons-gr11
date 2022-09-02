'''
Created on May 4, 2017

@author: Luqmaan
'''
'''
while True:
    num = input ("Enter a number: ")
    
    if num%2 > 0:
        print "Odd"
    
    else:
        print "Even"

total = 0
while True:
    num = input ("Enter a number: ")
    
    if num != 0:
        total+=num
        
    else:
        num = input ("Enter a number: ")
        total+=num
        break
    
print total
'''
'''
money = 100

while money >= 1:
    
    spend = raw_input ("What would you like to buy?\n\n1 - Nintendo RPG ($59.99)\n2 - Cookies ($2.50)\n3 - Soccer Ball ($26.00)\n4 - Protection ;) ($99.00)\n5 - Lolipop ($1.00)\n\nPRESS A TO QUIT\n\n\n: ")
    
    if spend.upper() == "A":
        break
    else:
        if spend == "1":
            money -= 59.99
            if money > 0:
                print "You bought a \"Nintendo RPG\" video game!"
                
            else:
                print "Sorry, you don't have enough money!"
            
        elif spend == "2":
            money -= 2.5
            if money > 0:
                print "You bought a Cookie!"
               
            else:
                print "Sorry, you don't have enough money!"
           
        elif spend == "3":
            money -= 26
            if money > 0:
                print "You bought a Soccer Ball!" 
               
            else:
                print "Sorry, you don't have enough money!"
           
        elif spend == "4":
            money -= 99
            if money > 0:
                print "You bought some \"Protection\"! ;)"
               
            else:
                print "Sorry, you don't have enough money!"
            
        elif spend == "5":
            money -= 1
            if money > 0:
                print "You bought a Lolipop!" 
               
            else:
                print "Sorry, you don't have enough money!"
                
        print "\n"+str(money)+"\n"

if money <= 0:
    print "Your broke.  Go kill yourself."

else:
    print "Come back again!"
           
'''
            
        