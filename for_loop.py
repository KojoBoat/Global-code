# for i in range (1,11):
#     print (i)

# for j in [1,2,3]:
#     print (j)
# print (type(j))

# for j in range (1,4):
#     print (j)
# print (type(j))

# program to print even numbers from 0 to 18
# for i in range (0,19):
#     if(i % 2 == 0):
#         print (i)


#function to produce
#****
#****
#****
#****

# def asterisk():
#     for i in range (1,5):
#         print ("****")

# asterisk()

# another way of printing
#****
#****
#****
#****

# def asterisk():
#     for i in range (1,5):
#         for j in range (1,2):
#             print ("****")

# asterisk()

#function to print
# *
# **
# ***
# ****
# ***
# **
# *

# def ast():
#     asti = ""
#     for i in range (1,6):
#             asti += "*"
#             if i > 4:
#                 x = range(3,0,-1)
#                 for i in x:
#                     print ("*" * i)
#             else:
#                 print (asti)

# ast()

#function to get a string and determine a specific character..

def find_char(sentence):
    for i in range(0,len(sentence),1):
        if sentence[i] == 'm' or sentence[i] == 's':
            print ('true')
            break
        if(i == len(sentence)-1):
            print ('false')

sentence = input("enter the sentence... \n")
# letter = input("which letter do you want to search for \n")
# find_char(sentence)

def different_letters():
    find_char(sentence)
different_letters()


