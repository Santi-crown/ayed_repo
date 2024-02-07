lines = []
cases = 0
case_breaker = int(input())
while cases != case_breaker:
    line = input()
    if line != "":
        lines.append(line)
        cases += 1

print(lines)
