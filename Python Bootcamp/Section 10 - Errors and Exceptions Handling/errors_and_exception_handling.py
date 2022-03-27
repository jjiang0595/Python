# def add(n1, n2):
#     print(n1 + n2)
#
#
# number1 = 10
# number2 = input("Please provide a number: ")
#
# try:
#     result = 10 + 10
# except:
#     print("Hey it looks like you aren't adding correctly!")
# else:
#     print("Add went well")
#     print(result)


# try:
#     f = open('testfile', 'r')
#     f.write("Write a test line")
# except TypeError:
#     print("There was a type error!")
# except OSError:
#     print('Hey you have an OS Error')
# finally:
#     print("I always run")


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end!")

ask_for_int()
