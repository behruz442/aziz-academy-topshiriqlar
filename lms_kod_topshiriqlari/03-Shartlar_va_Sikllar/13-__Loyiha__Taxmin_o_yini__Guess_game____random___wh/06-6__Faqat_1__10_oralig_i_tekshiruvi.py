secret = 6

while True:
    guess = int(input())
    
    if guess == secret:
        print("Correct")
        break
    else:
        print("Invalid")