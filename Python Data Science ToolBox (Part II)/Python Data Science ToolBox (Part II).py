word = "Da"
it = iter(word)
next(it)  # prints 'D'
next(it)  # Prints 'A'
next(it)  # Throws a Stopiteration error
word = "Da"
it = iter(word)
print(*it)

file = open('file.text')
it = iter(file)
print(next(it))  # Prints the first line

values = range(10, 21)  # Creates a function that has the range(10,21) (Not including 21)
print(type(values))  # Returns range function
print(values)  # range(10,21)
enu

va = enumerate(['yolo', 'toto', 'popo'])
print(type(va))  # prints enumertes type
print(list(va))  # Prints as a list

z = zip(values, va)  # Iterator of zip objects to make a tuple
print(type(z))  # Returns zip file
print(list(z))  # Returns a tuple in a list

for chunk in pd.read_csv('yolo.csv', chunksize=1000):  # Loads 1000 datarows at a time
    total += chunk['s']  # The chunk is loaded as a generator

squares = [i ** 2 for i in range(10)]
matrix = [[col for col in range(5)] for row in range(5)]  # Creates 5 rows each from 0 to 4
[num ** 2 for num in range(10) if num % 2 == 0]
[num ** 2 if num % 2 == 0 else 0 for num in range(10)]
pos_neg = {num: -num for num in range(10)}  # Here key is neg and value is -num

# Generator does not contain the numbers in the memory
result = (num for num in range(10))
print(next(result))  # Yes! It work like a list
print(list(result))


def num_seq(n):
    i = 0
    while i < n:
        yield i
        i += 1


data = file_object.readline()  # Reads a line of text file. Printing it again and again prints line by line
