clc;
clear all;
F=[1 1 2 3 5 8 13 21 34];
n=6;
a=0;
b=3;
L=b-a;
syms x
f=@(x) 0.65-(0.75/(1+x.^2))-(0.65*x)*(atan(1/x));
%f=@(x) x.^2 + (54./x)
for k=2:1:n
    Ls=(F(n-k+2)./F(n+2))*L
    x1=a+Ls
    x2=b-Ls
    fx1=double(subs(f,x1))
    fx2=double(subs(f,x2))
    if fx1>fx2
        fprintf("minimum does not lie in %5.2f and %5.2f \n",a,x1);
        fprintf("New interval is %5.f and %5.2f \n",x1,b);
        a=x1
    elseif fx1==fx2
        fprintf("Minimum does not lie in %5.2f , %5.2f and %5.2f , %5.2f \n",a,x1,x2,b);
        a=x1;
        b=x2;
    else
        fprintf("Minimum does not lie in %5.2f and %5.2f \n",x2,b);
        fprintf("New interval is %5.2f and %5.2f \n",a,x2);
        b=x2
    end
end

