# FILE NAME - grade_converter.py

# NAME: Joaquin Darby
# DATE: 9/30/2025
# BRIEF DESCRIPTION: Converting a numerical grade into a letter grade.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print('===== Grade Converter =====')

numerical_grade = int(input('Enter a numerical grade (1-100): '))

if numerical_grade in range(0, 65) or numerical_grade < 0:
    print('F')
elif numerical_grade in range(65, 70):
    print('D')
elif numerical_grade in range(70, 80):
    print('C')
elif numerical_grade in range(80, 90):
    print('B')
elif numerical_grade in range(90, 101):
    print('A')
elif numerical_grade >= 100:
    print('A+')

'''
print('===== Grade Converter =====')

percent = int(input('Enter a numerical grade (1-100): '))

if percent > 100:
    print('A+')
elif percent >= 90:
    print('A')
elif percent >= 80:
    print('B')
elif percent >= 70:
    print('C')
elif percent >= 65:
    print('D')
else:
    print('F')
'''
########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?







'''
