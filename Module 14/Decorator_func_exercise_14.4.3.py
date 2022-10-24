def calculated_values_cache(func):
    """ This decorator creates sort of cache - a dictionary where the calculated values of 1-argument function are put
      as {n: f(n)}. Each time the function is recalled the decorator searches if the value for the perticular argument already exists
      in cache and returns it to function. """
    values_dict = {}
    def wrapper(arg):
        nonlocal values_dict
        if arg not in values_dict.keys():
            values_dict[arg] = func(arg)
            print(f"New function value was added to cache {arg}: {values_dict[arg]}")
        else:
            print(f"The function value for an argument {arg} has been calculated earlier: {values_dict[arg]}")
        print(values_dict)
        return values_dict[arg]
    return wrapper


@calculated_values_cache
def f(n):
    return n * 123456789

for i in 2, 4, 6, 2:
    f(i)
