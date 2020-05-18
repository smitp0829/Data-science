% read file
file = fopen('cubicSplines5.txt','r');
file_input = fscanf(file, '%f');

% number of points 
num_inputs = file_input(1);

%array to store x values 
x = zeros(num_inputs, 1);
%array to store y values 
y = zeros(num_inputs, 1); 

%storing x and y value in array x and y 
index = 1;
for i = 1 : num_inputs
    index = index + 1;
    x(i) = file_input(index);
    
    index = index + 1;
    y(i)= file_input(index);
end

%matrix size 
matrix = zeros(num_inputs , num_inputs);

matrix(1,1) = 1;
matrix(num_inputs,num_inputs) = 1;

% to get the diffence h0,h1,h2,...
h= x (2: end)-x(1: end -1);

%matrix to find coefficients (Ax = b; this is A)
for j = 2: num_inputs -1
    matrix(j,j-1) = h(j-1);
    matrix(j,j) = 2*(h(j-1)+h(j));
    matrix(j,j+1) = h(j);
end

%to find coefficients another side matrix (Ax = b; this is b)
matrix_b = zeros(num_inputs,1);

for k = 2: num_inputs -1
    matrix_b(k) =((3/h(k)) * (y(k+1)-y(k))) - ((3/h(k-1))*(y(k)-y(k-1)));
end

%solve matrix Ax = b 
c = matrix\matrix_b;

%find b using equation 
b = zeros(num_inputs-1,1);

for n = 1: num_inputs-1
    b(n) = ((y(n+1)-y(n))/h(n)) - ((((2*c(n))+c(n+1))*h(n))/3);
end

%find d using equation 
d = zeros(num_inputs-1,1);

for m = 1: num_inputs-1
    d(m) = (1/(3*h(m)))*(c(m+1)-c(m));
end

% y is eqaul to a 
a = y;

for q = 1 : num_inputs-1
    disp(sprintf('%f %f %f %f', a(q), b(q), c(q),d(q)));
end

%to get p1(x), p2(x), p3(x),....
% for s = 1;num_inputs-1
syms X
hold on 
for s=1: num_inputs-1
    p = a(s)+(b(s)*(X-x(s)))+(c(s)*((X-x(s))^2))+(d(s)*((X-x(s))^3));
    fplot(p,[x(s) x(s+1)])
end

grid on 
xlim([(min(x)-1) (max(x)+ 1)]);
ylim([(min(y)-1) (max(y)+ 1)]);
hold off

fclose('all');