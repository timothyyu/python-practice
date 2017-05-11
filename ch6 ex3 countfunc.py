def count(str, let):
    count = 0
    for letter in str:
        if letter == let:
            count = count +1
    print(count)

count("banana",'a')