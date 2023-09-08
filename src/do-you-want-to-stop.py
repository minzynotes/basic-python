
# You should write a loop around this question, and keep asking until
# the answer is "yes" (lower case).
# input('Do you want to stop?')
#n=0
#while n<7:
#    print ("Hello, World!")
#    n += 1

a = int(input('How many times?'))
n = 0

while n <= a:
    user_input = input("Do you want to stop? (yes/break): ")
    if user_input.lower() == 'yes':
        break
    elif user_input.lower() == "break":
         print("Hello, World!")
         n += 1
    else:
        print('warning')
        n +=1
