def func():
    return 1


print(func())


def hello():
    return "Hello!"


hello()
greet = hello
print(greet())
del hello
print(greet())


def hello(name='Jerry'):
    print("The hello() function has been executed!")

    def greet():
        return '\t This is the greet() func inside hello'

    def welcome():
        return '\t This is welcome() inside hello'

    print("I am going to return a function!!")

    if name == 'Jerry':
        return greet
    else:
        return welcome


my_new_func = hello('Jerry')
print(my_new_func())


def cool():

    def super_cool():
        return 'I am very cool!'

    return super_cool


some_func = cool()
print(some_func())


def hello():
    return 'Hi Jerry!'


def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())


other(hello)


def new_decorator(original_func):

    def wrap_func():

        print('Some extra code, before the original function')

        original_func()

        print('Some extra code, after the original function')

    return wrap_func


def func_needs_decorator():
    print("I want to be decorated!!")


decorated_func = new_decorator(func_needs_decorator)
decorated_func()


@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")


func_needs_decorator()
