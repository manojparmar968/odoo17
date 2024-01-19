n= 5
k = (n*2) - 2

middle_row = (n+2)//2

for i in range(middle_row):
  print(" " * (middle_row-i),"*" * (i*2+1))
for i in range(middle_row-2,-1,-1):
  print(" " * (middle_row -i), "*" * (i*2+1))