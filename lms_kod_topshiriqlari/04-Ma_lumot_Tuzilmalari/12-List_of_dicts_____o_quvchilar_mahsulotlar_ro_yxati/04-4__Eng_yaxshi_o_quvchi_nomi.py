n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
best = students[0]
for s in students:
    if s['score'] > best['score']:
        best = s
print(best['name'])