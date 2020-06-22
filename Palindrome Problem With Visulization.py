import numpy as np
import matplotlib.pyplot as plt #for visulization

'''
The function below is trying to solve a math problem that asks: For any number if you add its inverse a certian amount 
of times, it will eventually become a palindrome, True or False? For example, 23 + its inverse, 32 = 55. 
Numbers that are already palindromes like 3, or 77 don't go through this process.


There are 2 inputs that you need to provide:
1. The amount of numbers you want to examine.
2. The maximum number of times that each number goes through the adding its inverse process.
'''
def palindrome_conjecture(): 
    y = int(input("what would you like your range of numbers to be?:"))
    x = int(input("what would you like your counter range to be?:"))
    step_counter = 0 #counts the amount of steps each number takes before becoming a palindrome
    non_palindrome_counter = 0 #counts the amount of numbers that take more than your input steps to become a palindrome
    counter_array = np.zeros(x,dtype = int) #sets up a list with your input 0's so it can become a counter later
    plt_array = np.zeros(y,dtype = int)
    number_of_steps = np.zeros(y,dtype = int)
    y_dividedby_10 = y/10
    for num in range(y): #for numbers in the input that is given
        str_num = str(num)         
        while not int(str_num) == int(str_num[::-1]) and not step_counter > x: # while its not a palindrome and the
            #step counter is less than your input
            
            str_num = str(int(str_num)+int(str_num[::-1])) #number is added to its inverse
            step_counter = step_counter + 1 #another step is added to the amount of steps
        
        if step_counter > x: #if the amount of steps is bigger than your input
            print(num, "takes more than",x,"steps to become a palindrome")# print out the number and that it takes more steps
            non_palindrome_counter +=1 #another number does not become a palindrome in less than your input
            step_counter = 0 #step counter restets
            
            
        
        else: #if the number becomes a palindrome in less than your input
            print(num,"becomes a palindrome in",step_counter,"steps") #print the number and how many steps it takes
            counter_array[step_counter] +=1 # the amount of numbers that take that amount of steps, goes up by 1
            plt_array[num] = step_counter
        step_counter = 0 #step counter restets
    print('\n')
    print('\n')
    for i in range(len(counter_array)): # for number in the length of the counter list
             if not counter_array[i] == 0:
                print("There are",counter_array[i],"numbers that take",i,"steps") #print out the amount of numbers there are that take each amount of steps
                number_of_steps[i] = i
    print("There are",non_palindrome_counter,"numbers, less than",y, "that take more than",x,"steps to become a palindrome") #print out the aount of numbers that don't become a palindrome
    
    # The visulization
    plt.hist(plt_array,color='blue',density=True)
    plt.margins(.000001)
    plt.title('Palindrome Visulization')
    plt.ylim(.1)
    plt.xlabel('number of steps')
    plt.ylabel('amount of numbers')
    plt.xticks(np.arange(number_of_steps.max()+2,step=2))
    plt.yticks(np.arange(1,step=.1))
    plt.show()

    
palindrome_conjecture()