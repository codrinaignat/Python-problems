s = "Test 1234!!!"
for ch in s:
    if ch.isupper():
        print(ch)
        
for ch in s:
    if ch.isalnum():
        print(ch, end=" ")
        
for ch in s:
    if ch.isdigit():
        print(ch)
