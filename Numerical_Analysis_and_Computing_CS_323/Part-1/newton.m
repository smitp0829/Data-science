% read from the file
file = fopen('newton.txt','r');
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

%error tolerance 
 epsilon = file_input(i+3);

% maximum number of iterations 
N = file_input(i+4);
%to count iteration
iterations = 0; 
error = inf;

while error >= epsilon &&  iterations < N
   iterations = iterations+1; 
    
    %horner method to get value P(x0)(alpha) and P'(x0)(beta)
    alpha = arr(length(arr));
    beta = arr(length(arr));

    for index = (length(arr)-1) :-1: 1
        alpha = arr(index)+(alpha*x0);
        if index > 1
            beta = alpha+(beta*x0);
        end
    end
    
    x1 = x0 - (alpha/beta);
    error = abs(x1 - x0);
    x0 = x1;
end

if iterations < N
    disp(sprintf('found the solution %f in %d iterations', x1, iterations));
else
    disp(sprintf('no solution found after %d iterations', iterations));
end
    