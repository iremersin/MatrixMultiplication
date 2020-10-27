% author: Irem ERSIN
function matrix=square_matrix_multiplication(matrix1,matrix2) % formation of function
C=zeros(size(matrix1,1)); % let C be a new n*n zero matrix
for i=1:size(matrix1,1) % from 1 to number of rows of first matrix
        for j=1:size(matrix1,1) % from 1 to number of columns of second matrix
            C(i,j)=0; % initially zero
            for k=1:size(matrix1,1) % from 1 to number of rows of second matrix
                C(i,j)=C(i,j)+(matrix1(i,k)*matrix2(k,j)); % product of the matrices
            end
        end
end
Result=C % result
end

