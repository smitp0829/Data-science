% read from file 
file = fopen('simpson5.txt','r');

% number of points 
func = fgetl(file);
a = str2num(fgetl(file));
b = str2num(fgetl(file));
n = str2num(fgetl(file));

f = inline(func, 'x')
disp(sprintf('%f', compsimp(a, b, n, f)))

% The function for the composite Simpson's rule
function [x] = compsimp(a,b,n,f)

h = (b-a)/n;
x = zeros(1,n+1);
x(1) = a;
x(n+1) = b;
odd  = 0;
even = 0;

%calculate value of x 
for i = 2:n
    x(i) = a + (i-1)*h;
end

% calculate even and odd terms 
for j = 1:n-1
    if mod(j,2)==0
        even = even + (f(x(j+1)));
    else
        odd = odd + (f(x(j+1)));
    end
end

% Calculate approximation of integration
x = (h/3)*(f(a) + f(b) + 2*even + 4*odd);
end