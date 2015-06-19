
function [Y] = classification(X)
load('vector.mat');

w = zeros(1,32623);
alpha = 0.1;
final = zeros(30,1);
for T = 1:30
T_H = 2930;
T_S = 1198;

factor_H = ones(T_H,1);
factor_S = zeros(T_S,1);
tmp = exp(-w*trainS');
temp = exp(-w*trainH');

for i = 1:T_H
    factor_H(i) = alpha*(factor_H(i) - 1/(1+temp(i)));
end
for i = 1:T_S
    factor_S(i) = alpha*(factor_S(i) - 1/(1+tmp(i)));
end

w = w + factor_H'*trainH;
w = w + factor_S'*trainS;
%{
factor_tH = ones(742,1);
factor_tS = ones(302,1);
test_S = exp(-w*testS');
test_H = exp(-w*testH');

factor_tH = factor_tH + test_H';
factor_tS = factor_tS + test_S';

error = 0;

for i = 1:742
    if(1/factor_tH(i) <= 0.5)
        error = error+1;
    end
end
for i = 1:302
    if(1/factor_tS(i) > 0.5)
        error = error+1;
    end
end

final(T) = error/(302+742);
%}

end

d = size(X);
Y=[];
test_TA = exp(-w*X');

for i =1:d(1)
    if(1/(1+test_TA(i)) <= 0.5)
        Y = [Y 1];
    else
        Y = [Y 0];
    end
end

end

