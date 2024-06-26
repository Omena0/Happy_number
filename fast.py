import time as t


def check_happy(num: int) -> bool:
    def is_happy(num) -> int:
        num = list(str(num))
        a = 0
        for i in num:
            a += int(i) **2
        return a

    temporary = is_happy(num)
    seen = []
    while temporary not in seen:
        if temporary == 1:
            # print("Number is happy!")
            return True
        seen.append(temporary)
        temporary = is_happy(temporary)
    # print("Number is unhappy =(")
    return False



#num = int(input('Enter a number: '))

#print(f'Is happy: {check_happy(num)}')

# Benchmarking (You can remove all this)
ammount = 100000
start = t.time()*1000
for i in range(ammount):
    check_happy(i)
end = t.time()*1000


print(f'Duration: {end-start} ms for {ammount} iterations.')
