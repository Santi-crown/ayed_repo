cases_list = []
cases = 0
cases_breaker = int(input())
blink_cases = 0
#index
for cases in range(cases_breaker + 1):
    line = input()
    # Un caso
    while line != "":
        cases_list.append(line.split())
        line = input()
print(cases_list)