def demo_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

demo_function(1, 2, 3, name="Alice", age=25)


# *args = positional arguments (any number of values like a list)

# **kwargs = keyword arguments (any number of key-value pairs like a dictionary)