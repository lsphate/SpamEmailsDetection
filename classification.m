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
        temp_H = exp(-w*trainH');
        temp_S = exp(-w*trainS');

        for i = 1:T_H
            factor_H(i) = alpha*(factor_H(i) - 1/(1+temp_H(i)));
        end

        for i = 1:T_S
            factor_S(i) = alpha*(factor_S(i) - 1/(1+temp_S(i)));
        end

        w = w + factor_H'*trainH;
        w = w + factor_S'*trainS;
    end

    d = size(X);
    Y = [];
    test_TA = exp(-w*X');

    for i =1:d(1)
        if(1/(1+test_TA(i)) <= 0.5)
            Y = [Y 1];
        else
            Y = [Y 0];
        end
    end
end

