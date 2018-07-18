# Test of PE215 with the 9x3 wall with 8 solutions

total = 0;
options_a = {'d'}
options_d = {'a'}
options_b = {'e'}
options_c = {'e'}
options_e = {'b','c'}

options = {'a': options_a,
           'b': options_b,
           'c': options_c,
           'd': options_d,
           'e': options_e}

for i in options:
    for j in options[i]:
        for k in options[j]:
            total = total + 1


print(total)
