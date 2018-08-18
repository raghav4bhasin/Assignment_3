lst = [5, 10, 12, 13, 15, 18, 16, 19]
even=0
odd=0
for x in lst:
    if(x%2==0):
      even=even+1
    else:
      odd=odd+1
print('Count of Even numbers: ',even)
print('Count of Odd numbers: ',odd)
