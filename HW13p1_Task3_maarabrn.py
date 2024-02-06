# Activity Python 13: Task 3
# File: ACT_Python_HeaderTemplate_Team355_maarabrn.py 
# Date:    26 11 2023
# By:      Rania Maaraba
# Section: 21
# Team:    355
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# The program uses a given flow chart to calculate
# prime and perfect numbers.

import math
#user input K
K = int(input('Input K, a whole number: '))
C1 = 0
C2 = 0

# calculate and increment
for w in range(2, (K), 1): 
    S = 0
    n = w
    m = math.ceil(n/2) + 1
    
    for p in range (2, (m), 1):
        R = n % p
        if R == 0 :
            S = S + p
        else:
            pass
    if S == 0:
        print('{} is a prime number '.format(n))
        C1=C1+1
    elif S == n-1:
        print('{} is a perfect number'.format(n))
        C2=C2+1
    else:
        pass
        
print('The total number of prime numbers found is C1= ' , C1)
print('The total number of perfect numbers found is C2=' , C2)


    

