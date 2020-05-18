% read file
file = fopen('neville8.txt','r');
file_input = fscanf(file, '%f');

% num of points
num_inputs = file_input(1);

%to store the value of x0, x1,..
x = zeros(num_inputs + 1, 1); 

%to store thevalue of y0,y1,..
y = zeros(num_inputs + 1, 1); % array

%to store the value 
p = zeros(num_inputs+1, num_inputs+1);

count = 1; 
for i=1: num_inputs+1 
    count = count + 1;
    x(i) = file_input(count); %fill the value of x from file
    
    count = count + 1;
    y(i) = file_input(count); %fill the value of y from file 
    p(i,i) = y(i);
end 

%get the value of x0 intial guess 
count = count + 1;
x0 = file_input(count);



for d=1: num_inputs+1
    for n=1: (num_inputs+1)-d
    j = d+n;
    p(n,j) = ((((x0-x(n)) * p(n+1,j)) - ((x0-x(j)) * p(n,j-1))) / (x(j)-x(n)));
    end
end

% disp(p)
disp(sprintf('P(%f) = %f ', x0, p(1,num_inputs+1)))
    
   