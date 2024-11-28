for i in range(1,  11):
    n = int(input())
    sub_char = str(input())
    char = str(input())
    if sub_char in char:
        print('#'+str(n), char.count(sub_char))
    else:
        print('#'+str(n), 0)