# def my_func(*args):
#     pass

# my_func()

def my_func(**kwargs):
    print("Hello " + kwargs["name"] + " " + kwargs["lname"])

my_func(name="Phina", lname="Chikezie")