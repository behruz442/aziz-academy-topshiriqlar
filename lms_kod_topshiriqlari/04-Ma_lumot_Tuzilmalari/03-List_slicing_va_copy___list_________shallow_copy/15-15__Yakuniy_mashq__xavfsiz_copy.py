n = int(input())
orginal_list = list(map(int, input().split()))
copied_list = orginal_list[:]
copied_list.reverse()
print(orginal_list)
print(copied_list)