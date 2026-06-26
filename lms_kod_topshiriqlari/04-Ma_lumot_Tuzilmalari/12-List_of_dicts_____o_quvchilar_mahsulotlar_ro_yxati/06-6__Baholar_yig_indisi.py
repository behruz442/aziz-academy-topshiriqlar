n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
    total = 0
    for student in students:
        total += student['score']
print(total)