
def greet_person(name):
    print("Hi there "+name)
    
greet_person("Jane")
greet_person("Alice")

def create_greeting_for_person(name):
    return "Hello there "+name

greeting_line = create_greeting_for_person("Joe")
print(greeting_line)

greeting_line2 = create_greeting_for_person("Andy")
print(greeting_line2) 