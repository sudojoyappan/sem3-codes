%Golden Section Method
clc;
clear all;
close all;

f = @(x) 3*exp(x) - x.^3 - 10*x;
a = 0; b = 3;
n = 8;

fw = @(w) f(((b - a) * w) + a);
GR = 0.618;

aw = 0;
bw = 1;
Lw = bw - aw;

w1 = aw + (1 - GR)*Lw;
w2 = aw + GR * Lw;
fw1 = fw(w1);
fw2 = fw(w2);

history = [aw bw];

fprintf('Iter\t\taw\t\tbw\t\tw1\t\tw2\t\tf(w1)\t\tf(w2)\n')
fprintf('------------------------------------------------')

for k = 1:n
    fprintf('%d\t%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t%.6f\n',k,aw,bw,w1,w2,fw1,fw2);
    
    if fw1 > fw2
        aw = w1;
        w1 = w2;
        fw1 = fw2;
        Lw = bw - aw;
        w2 = aw + GR * Lw;
        fw2 = fw(w2);

        else
        bw = w2;
        w2 = w1;
        fw2 = fw1;
        Lw = bw - aw;
        w2 = aw + (1-GR) * Lw;
        fw1 = fw(w1);
    end
    history = [history; aw bw];
end

wmin = (aw + bw) / 2;
xmin = a + (b - a)*wmin;
fmin = f(xmin);

fprintf('\nOptimal Point = %.6f\n', xmin);
fprintf('Minimum f(x) = %.6f\n', fmin);

figure;
subplot(2,1,1);
x_val = linspace(a,b,500);
y_val = f(x_val);

y_min = f(x_val);
plot(x_val, y_val, 'b-', 'LineWidth', 1.5);
hold on;
plot(xmin, fmin, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
xlabel('x');
ylabel('f(x)');
title('Golden Section Search Method');
legend('f(x)','Approxiated Minimum');
grid on;

subplot(2,1,2);
hold on;
for k = 1:size(history,1)
    plot([history(k,1),history(k,2)],[k k],'r','LineWidth',2);
end
xlabel('x');
ylabel('Iteration')
title('Golden Section Search: Interval Shrinking');
grid on;
hold off;