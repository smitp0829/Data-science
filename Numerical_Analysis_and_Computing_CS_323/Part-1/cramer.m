% read file
file = fopen('cramer5.txt','r');
file_input = fscanf(file, '%f');

%A matrix size
num_inputs = file_input(1);

%A matrix with size nxn
count = 2; 
A = ones(num_inputs , num_inputs); 
for i = 1 : num_inputs
    for j = 1 : num_inputs
        A(i, j) = file_input(count);
        count = count + 1; 
    end
end

%b matrix
b = ones(num_inputs,1);
for k = 1: num_inputs
    b(k)= file_input(count);
    count = count + 1;
end

%-------------------------determinant of A--------------------------
% copy original A
matrix_A = A;
%just to pass something as b we don't really need to compute b side
%therefore I am passing zero matrix 
b_matrix = zeros(num_inputs,1);
[sign_change, U_wth_b] = gaussElimination(matrix_A,b_matrix);
U = U_wth_b(:,(1:num_inputs));
deter_A = product_diagonal(U)* sign_change;
disp(sprintf('determinant A = %f' ,deter_A));
%----------------------------------------------------------------

%--------------------determinant of A1, A2, A3, ...-----------------
for q = 1:num_inputs
    %copy matrix A 
    matrix = A; 
    %place the column b at ith position 
    matrix(:,q) = b(:);
    %disp(matrix)
    [sign_change,U_wth_b] = gaussElimination(matrix,b_matrix);
    U = U_wth_b(:,(1:num_inputs));
    deter_U = product_diagonal(U)*sign_change;
    disp(sprintf('determinant A%d = %f, \tx%d = %f' ,q,deter_U,q,(deter_U/deter_A)));
end
%--------------------------------------------------------------------

% -------------------Guauss Elimination method---------------------- 
function [sign, arg] = gaussElimination(A,b) 
sign = 1; 
arg = [A b];
% disp(arg)
for m=1: length(arg)-1 
    max = abs(arg(m,m));
    n = m;
    for r = m+1: length(arg)-1
        if abs(arg(r,m)) > max
            n = r;
            max = abs(arg(r,m));
            sign = sign*(-1);
        end
    end
    temp = arg(n,:);
    arg(n,:) = arg(m,:);
    arg(m,:) = temp;
    %disp(arg)
    if arg(m,m) == 0 || abs(arg(m,m)) < 0.001
        exception = MException('MyComponent:zero', 'No Solution');
        throw(exception)
     else
         for p = m+1: length(arg)-1
            arg(p,:) = arg(p,:)-((arg(p,m)/arg(m,m))* arg(m,:));
         end
    end
end
end
%-------------------------------------------------------------

%---------------------------Product of diagonal----------------- 
function [product]= product_diagonal(mat)
product = 1;
for s=1: length(mat)
    product = product*mat(s,s);
end
end
%----------------------------------------------------------------



