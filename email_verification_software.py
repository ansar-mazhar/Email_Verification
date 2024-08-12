# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 10:23:39 2024

@author: STAR LAPTOP
"""

email = input(" Enter your email: ")
k = 0
j = 0
d = 0
if len(email) >= 6:
    if email[0].isalpha():
        if '@' in email and email.count("@")==1:
            if email[-3] == '.' or email[-4] == '.':
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == '.' or i == '@' or i == '_':
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1:
                    print(" Wrong Email!")
            else:
                print(" Wrong Email! Issue with dot .")
        else:
            print(" Wrong Email! Issue with the @")
    else:
        print(" Wrong Email! Issue with starting letter ")
else:
    print(" Wrong Email! Issue with length ")
    
    
    
