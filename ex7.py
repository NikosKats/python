

def square(n):
    return n * n


def double(n):
  return 2*n 


def decrease(n):
  return n-1

dict = {'1':square(5), '2':double(5),'3':decrease(5)}

print dict['1']
print dict['2']
print dict['3']