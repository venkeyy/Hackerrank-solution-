# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

marks={}
n=int(input())
for i in range(n):
    name, *line = input().split()
    score=list(map(float,line))
    marks[name]= score
specific = input()
m = list(marks[specific])
average =sum(m) / len(m)
print("{:.2f}".format(average))
