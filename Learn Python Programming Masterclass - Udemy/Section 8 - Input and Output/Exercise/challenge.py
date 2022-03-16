with open("sample.txt", 'a') as jabber:
    for i in range(2, 13):
        for index in range(1, 13):
            print(f"{index:>2} times {i} is {i * index}", file=jabber)
        print("------------------", file=jabber)
