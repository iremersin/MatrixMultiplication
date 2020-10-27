% author: Irem ERSIN
clc
clear
close all
control=0;
while control==0 % if the user wants to change the input then this loop will take input from the user again and again until the user enters a number except
    n=input("Please determine the size of nxn (square) matrix: "); % taking input from user
    
    TF=isnumeric(n); % checking that the input is valid
    
    if TF==1 % if n is valid, then it is 1
        fprintf("\n") % leave a blank line
    end
        
    fprintf("\nIf you want to change the size press 0 otherwise press any number: ") % asking the user if the user wants to change it
    control=input("\nChoice: "); % taking input from user
end

option=0; % initially option is 0
while option==0 % if the user wants to change the input then this loop will take input from the user again and again until the user enters a number except 0
    choice=input("Which way do you want to create matrices?\n1:Manually\n2:Randomly\nChoice: "); % taking input from user
    if choice==1
        fprintf("Please enter elements one by one for first matrix: ") % creating a matrix
        matrix1=zeros(n); % creating a matrix with dimentions n * n  with all zeros     
        for i=1:n; % taking row value from 1 to row length of the matrix
            for j=1:n; % taking column value from 1 to column length of the matrix
            matrix1(i,j)=input("\nElement: ");  % taking input from the user    
            end
        end
        matrix1=reshape(matrix1,n,n); % printing matrix to the screen
        fprintf("\n")
        fprintf("Please enter elements one by one for second matrix: ") % creating a matrix
        matrix2=zeros(n); % creating a matrix with dimentions n * n  with all zeros     
        for i=1:n; % taking row value from 1 to row length of the matrix
            for j=1:n; % taking column value from 1 to column length of the matrix
            matrix2(i,j)=input("\nElement: ");  % taking input from the user    
            end
        end
        matrix2=reshape(matrix2,n,n); % printing matrix to the screen
        
        square_matrix_multiplication(matrix1,matrix2) % calling function
    
    elseif choice==2
        matrix1=rand(n) % creating first matrix randomly
        matrix2=rand(n) % creating second matrix randomly
        
        square_matrix_multiplication(matrix1,matrix2) % calling function
        
    else % if the user does not enter or 2
        fprintf("ERROR!\nPlease enter a number 1 or 2\n") % printing error message
    end
        
    fprintf("\nIf you want to try again press 0 otherwise press any number: ") % asking the user if the user wants to change it
    option=input("\nChoice: "); % taking input from user
end










