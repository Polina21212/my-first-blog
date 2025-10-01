'''def say_hello():
    print("Hello")


say_hello()
say_hello()
say_hello()
say_hello()
'''

'''def say_hello():
    print("Hello")


def say_goodbye():
    print("Good Bye")


say_hello()
say_goodbye()'''


'''def print_messages():

    def say_hello(): print("Hello")

    def say_goodbye(): print("Good Bye")


    say_hello()
    say_goodbye()
    
print_messages()'''


'''def main():
    say_hello()
    say_goodbye()


def say_hello():
    print("Hello")


def say_goodbye():
    print("Good Bye")

main()
'''


'''def say_hello(name):
    print(f"Hello, {name}")

say_hello("Tom")
say_hello("Bob")
say_hello("Alice")'''

'''def say_hello(name= "Tom"):
    print(f"Hello, {name}")

say_hello()
say_hello("Bob")
'''

def print_person(name, age=18):
    print(f"Name: {name}  Age: {age}")


print_person("Bob")
print_person("Tom", 37)

