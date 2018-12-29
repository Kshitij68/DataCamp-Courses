def square():  # THis is called a function header
    """ Returns the square of a value"""  # Docstrings are very important


a = (2, 3, 4)  # Cretes a tuple. Their values cannot be changed
print(a[1])  # Returns 3


# Scope in Functions
# Name that is in the local scope means it is defined in the fucntion only
# name that is in the global scope means it is defined in the global environment
# built in scope Functions that are predefined

def outer():
    n = 1

    def inner():
        nonlocal n  # non local to ensure its partially global
        n = 2
        print(n)

    inner()
    print(n)


# Scopes Searched:
# L: Local Scope
# E: Enclosing functions
# G: Global
# B: Built-in

def echo(n):
    # Define inner_echo
    def inner_echo(word1):
        echo_word = word1 * n
        return echo_word

    return inner_echo  # NO need of having paranthesis


def echo(word1, echo=1):  # echo = 1 ensures that echo is defined irrespective of whether the value is given or not
    echo("yolo", 2)  # this overwrites the value of echo and makes it 2


def gibberish(*args):  # *args defines a flexible quantity variable. It creates a tuple of all the input
    result2 = gibberish("lang", "source")  # This is how you run the function


def report_status(**kwargs):  # **kwards defines a flexible dictionary. It creates a dictionary of all the input
    report_status(name="luke", affiliation="jedi", status="missing")  # Method to call a dictionary


nums = [4, 6, 9, 10, 13]
square = map(lambda num: num ** 2, nums)  # Using lambda we can define a function faster
print(square)  # Shows that it is a map type object
print(list(square))  # Prints as a list

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
result = filter(lambda member: len(member) > 6, fellowship)
print(list(result))

raise ValueError('echo must be greater than 0')  # To raise a value error