a = list(map(int, input().split()))

stats = {
    'count': len(a),
    'sum': sum(a),
    'min': min(a),
    'max': max(a)
}

print(stats)