'''
Created on Apr 4, 2017

@author: Luqmaan
'''

school = raw_input ("Type in a word: ")
print school+"\n"
'''
print school[1]
'''
num = len(school)
'''
print num
'''


a = 1
f = 0

while a == 1:
    
    print school[f]
    f+=1
    
    if f < num:
        a = 1
        
    elif f == num:
        a = 2
    
