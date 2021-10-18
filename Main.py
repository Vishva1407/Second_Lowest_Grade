marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])
second_low_mark = sorted(list(set([marks for name,marks in marksheet])))[1]
print(*[name for name,mark in sorted(marksheet) if mark == second_low_mark],end = "\n")
