% read from the file
file = fopen('horner5.txt','r');
file_input = fscanf(file, '%f');

% degree of polynomial
num_inputs = file_input(1);

% coefficients 
arr = ones(num_inputs + 1, 1);
for i = 1 : length(arr)
    arr(i)= file_input(i+1);
end

%to get x0 
x0 = file_input(i+2);

%horner method to get value P(x0)(alpha) and P'(x0)(beta)
alpha = arr(length(arr));
beta = arr(length(arr));

for index = (length(arr)-1) :-1: 1
    alpha = arr(index)+(alpha*x0);
    if index > 1
        beta = alpha+(beta*x0);
    end
end

disp(sprintf('alpha %f, beta %f', alpha, beta ));

