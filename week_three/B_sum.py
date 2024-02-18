from sys import stdin

def summation(i,j,numbers = []):                                        # costo   pasos
    if i > j or i >= len(numbers):                                      #   1       1
        return 0                                                        #   1       1
    return numbers[i] + summation(i+1,j,numbers) # invariante           #   n        n

#print(summation(8,9, [1,2,3,4,5,6,7,8,9,10]))                          # Total O = (n)

i = int(stdin.readline().strip())
j = int(stdin.readline().strip())
line3 = stdin.readline().strip().split()
# We map each string as int
line3_int = list(map(int,line3))
print(summation(i,j,line3_int))



