from sys import argv

def greeting(name):
    print("Hello {}!".format(str(name)))

if len(argv) > 1:
    greeting(argv[1])
else:
    greeting("John Doe")