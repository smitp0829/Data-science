% read file
file = fopen('LeastSquare5.txt','r');
file_input = fscanf(file, '%f');

% to get number of input and desired degree
num_inputs = file_input(1);
degree = file_input(2);

%to store the value of x and y of points given 
x = zeros(num_inputs, 1);  
y = zeros(num_inputs, 1); 

%getting x and y points value from file
index = 2;
for i = 1 : num_inputs
    index = index + 1;
    x(i) = file_input(index);
    
    index = index + 1;
    y(i) = file_input(index);
end

%intialize matrix A
A = zeros(degree+1, degree+1);
b = zeros(degree+1, 1);

% calculate Matrix A
for i = 1: degree+1
    for j = 1: degree+1
        if (i==1) && (j==1)
           A(i,j) = num_inputs;
        else
            A(i,j) = sum(x.^(i+(j-2)));
        end
    end
end

% calculate Matrix B
for k = 1: degree+1
    b(k) = sum(y.*(x.^(k-1)));
end

%solve Ax=b
a=A\b;

%plot the points 
xx = [min(x):0.1:max(x)];
yy = 0;
for s = 1: length(a)
    yy = yy + a(s)*xx.^(s-1);
end
% a(1) + a(2) *xx + a(3)*xx.^2 + a(4)*xx.^3;

plot(xx, yy, x, y, '*');

for m=1: length(a)
   fprintf('%f ', a(m));
end
fprintf('\n');
