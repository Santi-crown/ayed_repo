from sys import stdin

def summation(i,j,numbers = []):
    if i > j or i >= len(numbers):
        return 0
    return numbers[i] + summation(i+1,j,numbers) # invariante

#print(summation(8,9, [1,2,3,4,5,6,7,8,9,10]))

line1 = int(stdin.readline().strip())
line2 = int(stdin.readline().strip())
line3 = stdin.readline().strip().split()

print(line3)
# We map each string as int
line3_int = list(map(int,line3))
print(line3_int)

print(summation(line1,line2,line3_int))

# while len(line1) > 0 and len(line2) > 0 and len(line3) > 0:
#     numbers = [int(num) for num in line3]
#     i, j, sequence = int(line1), int(line2), line3
#     print(summation(i, j, sequence))
#     line1 = stdin.readline().strip()
#     line2 = stdin.readline().strip()
#     line3 = stdin.readline().strip().split()