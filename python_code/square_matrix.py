"""
author: Irem ERSIN

"""

import numpy as np
import f_matrix as fm

control=0 # initially control is 0
while control==0: # if the user wants to change the input then this loop will take input from the user again and again until the user enters a number except 0
    
    n=input("Please determine the size of nxn (square) matrix: ") # taking input from user
    
    # checking that the input is valid

    if n.isdigit(): # if n is valid, then it is true
        n=int(n) # converting string to integer
            
    else: # if n is not valid
        print("\nERROR!\nPlease press a positive number") # printing an error message on the screen

    print("\nIf you want to change the size press 0 otherwise press any number: ") # asking the user if the user wants to change it
    control=int(input("Choice: ")) # taking input from user

option=0 # initially option is 0
while option==0: # if the user wants to change the input then this loop will take input from the user again and again until the user enters a number except 0
    
    choice=int(input("Which way do you want to create matrices?\n1:Manually\n2:Randomly\nChoice: ")) # taking input from user
    
    if choice==1: # if the user enters 1
        def matrixA(n):
            print("Please enter elements one by one: ") # creating a matrix
            matrix1=[[0 for i in range(n)] for i in range(n)] # creating a matrix with dimentions n * n  with all zeros     
   
            for i in range(n): # taking row value from 1 to row length of the matrix
                for j in range(n): # taking column value from 1 to column length of the matrix
                    user=input("A[%d][%d]: "% (i, j)) # taking input from the user
                    # controlling the input
                    try:
                        user=float(user)
                    except:
                        print("ERROR!\nPlease enter a number!")
                        
                        return matrixA(n)
                    matrix1[i][j]=user # updating matrix value with the user input
        
            print("Matrix A: ",matrix1) # printing matrix
            return matrix1
        matrix1=matrixA(n)
    

        def matrixB(n):
            print("Please enter elements one by one: ") # creating a matrix
            matrix2=[[0 for i in range(n)] for i in range(n)] # creating a matrix with dimentions n * n  with all zeros     
        
            for i in range(n): # taking row value from 1 to row length of the matrix
                for j in range(n): # taking column value from 1 to column length of the matrix
                    user=input("B[%d][%d]: "% (i, j)) # taking input from the user
                    # controlling the input
                    try:
                        user=float(user) 
                    except:
                        print("ERROR\nPlease enter a number")
                        return matrixB(n)
                    matrix2[i][j]=user # updating matrix value with the user input
                
            print("Matrix B: ",matrix2) # printing matrix
            return matrix2
        matrix2=matrixB(n)
            
        
    elif choice==2: # if the user enters 2
        matrix1=np.random.rand(n,n) # creating first matrix randomly
        matrix2=np.random.rand(n,n) # creating second matrix randomly
        print("Matrix A: ",matrix1) # printing matrix
        print("Matrix B: ",matrix2) # printing matrix
        
        print() # leave a blank line
        C=fm.square_matrix_multiplication(matrix1,matrix2) # calling the function
        print(C) # printin result
        
    else: # if the user does not enter or 2
        print("\nERROR!\nPlease enter a number 1 or 2\n") # printing error message
        
    print("\nIf you want to try again press 0 otherwise press any number: ") # asking the user if the user wants to change it
    option=int(input("\nChoice: ")) # taking input from user
    
print() # leave a blank line
C=fm.square_matrix_multiplication(matrix1,matrix2) # calling the function
print(C) # printing result
        

        

        
    
