n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
count = 0
for students in students:
    if students['score'] > 80:
        count += 1
print(count)