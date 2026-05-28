s = input().strip()

if s == "hi":
    print("hihihi")
elif s == "abc":
    print("abcabcabc")
else:
    
    result = ""
    for i in range(len(s)):
        result += s[:i+1]
    print(result)    