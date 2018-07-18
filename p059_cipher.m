clear
close all

alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

M = csvread("p059_cipher.txt");
M = [M, 0, 0];
list = [];

i= 1;

while i<length(M)-2
    list = [list; [M(i) M(i+1) M(i+2)]];
    i = i +2;
end



%encrypted = categorical(char(list(:,1)))

for i=97:122
    xorlist =  bitxor(list(:,1),i);
    figure
    histogram(xorlist,94)
    title(char(i))
end

a=97:122;

glist = histc(xorlist(97:122),a)

stem(glist)
xticklabels(alphabet)
