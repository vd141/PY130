def later(func, argument):
    def inner():
        return func(argument)
    return inner

def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()  # The system is shutting down!

def later2(func, argument):
    def inner(new_arg):
        return func(argument, new_arg)
    return inner

def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!