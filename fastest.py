import time as t

    
visited = set()

def step(n):
    summ = 0
    while n // 10 >0:
        digit = n %10
        
        summ += digit*digit
        n = n//10
    summ += (n%10)**2
    return summ

cache_ = {}
def check_happy(n):
    if n in cache_: return cache_[n]
    if n == 1:
        return True
    if n in visited:
        return False
    visited.add(n)
    a = step(n)
    result = check_happy(a)
    cache_[n] = result
    return result






#num = int(input('Enter a number: '))

#print(f'Is happy: {check_happy(num)}')

# Benchmarking (You can remove all this)
ammount = 100000
start = t.time()*1000
for i in range(ammount):
    check_happy(i)
end = t.time()*1000


print(f'Duration: {end-start} ms for {ammount} iterations.')