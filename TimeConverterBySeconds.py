x=int(input('Please Enter The Number Of Remaining Seconds: '))
a=x//43200
print(a,"day(s)",end=' ')
b=x%43200
c=b//3600
print(c,'hour(s)',end=' ')
d=b%3600
e=d//60
print(e,'minute(s)',end=' ')
f=d%60
print(f,'second(s)',end=' ')
