"""
author: Irem ERSIN

"""
import time # calling time function

def square_matrix_multiplication(matrix1,matrix2): # formation of function
    
    # starting time
    start = time.time()

    # program  body starts

    C=[[0 for i in range(len(matrix1))] for i in range(len(matrix2))] # let C be a new n*n zero matrix
    for i in range(len(matrix1)): # from 1 to number of rows of first matrix
        for j in range(len(matrix2[0])): # from 1 to number of columns of second matrix
            C[i][j]=0 # initially zero
            for k in range(len(matrix2)): # from 1 to number of rows of second matrix
                C[i][j] += matrix1[i][k]*matrix2[k][j] # product of the matrices
                
    # sleeping for 1 sec to get 10 sec runtime
    time.sleep(1)

    # program body ends

    # end time
    end = time.time()

    # total time taken
    print(f"Runtime of the program is {end - start}\n") # printing runtime of the program
    print("Result of the multiplication of matrices: ") # printing result
                
    return C

