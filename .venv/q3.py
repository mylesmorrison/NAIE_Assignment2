import random
import string
import matplotlib.pyplot as plt
# 3 - Hashtables

"""
You may use content from Week 5 tutorial (cite when you use) in order to answer this question.
Imagine you are collecting the data for a university. Not to complicate the example, you are collecting
student ID numbers, and corresponding names.
The ID numbers are of the format CCCCCC X, where an X stands for a digit from [0-9] (inclusive), and C
stands for an uppercase letter [A-Z] (inclusive).
e.g., ANERNC 2
Assume that you have a large collection of data, and that you need to look up the names of students
with a given ID number.

"""

"""
3.1
"""

"""
1. Create 3 hash functions suitable for the given problem. (Separate the hash function into a
hashcode, and a compression function).
"""

# From Lectures (Week 6) - Hash Tables and Maps

# I will test the code using Student_Records.txt

# The length of the Hash Table
# Should be a
HASH_TABLE_SIZE = 1003

def get_student_id_to_test(filename, number):
    file = open(filename)
    student_record = ""
    for i in range(number):
        student_record = file.readline()

    student_record.replace(" ", "")
    student_id_list = []

    for i in range(8):
        if student_record[i] == " ":
            continue
        student_id_list.append(student_record[i])

    return student_id_list


student_id_list = get_student_id_to_test("Student_Records.txt", 1)

# 1st Hash Function
# Positional Multiplied with Index Sum - Hash Code
# Division - Compression Function

def position_mult_index_hash_code(student_id_list):
    value = 0
    for i in range(len(student_id_list)):
        value += ord(student_id_list[i]) * i
    return value, len(student_id_list)


value, length = position_mult_index_hash_code(student_id_list)
#print(f"Hash Code: {value}, m: {HASH_TABLE_SIZE}")
# super simple compression function
def division_hash_compress(value, m):
    return value % m

hash1 = division_hash_compress(value, HASH_TABLE_SIZE)
#print(f"Compression Value: {hash1}")



# 2nd Hash Function
# Polynomial Accumulation - Hash Code
# Multiply, Adding and Divide - Compression Function

#No Horners Rule yet
def polynomial_rolling_hash_code_no_horners(student_id_list, z=31):
    hash_value = 0
    hash_power = 0
    for char in student_id_list:
        hash_value += ord(char) * z ** hash_power
        hash_power+=1
    return hash_value

# set z to 31 as I looked it up and that's the value it said was most common
# got to reference and understand why this is!!!!
def polynomial_rolling_hash_code_horners(student_id_list, z=31):
    hash_value = 0
    for i in range(len(student_id_list)-1, 0, -1):
        if i == len(student_id_list)-1:
            hash_value += ord(student_id_list[i]) * z + ord(student_id_list[i-1])
            continue
        hash_value = (hash_value*z) + ord(student_id_list[i-1])
    return hash_value, len(student_id_list)

#print(polynomial_rolling_hash_code_no_horners(student_id_list))
#print(polynomial_rolling_hash_code_horners(student_id_list))

value, length = polynomial_rolling_hash_code_horners(student_id_list)
#print(f"value: {value}, m: {HASH_TABLE_SIZE}")

# set values for a and b that are constants the rule is that a and b are not divisible by
# length so then I should use prime number
def MAD_hash_compress(value, m, a=31, b=17):
    return (a*value + b) % m

hash2 = MAD_hash_compress(value, HASH_TABLE_SIZE)
#print(f"Compression Value: {hash2}")

# 3rd Hash Function
# Folding Hash Code - Hash Code
# Universal Hash - Compression Function

#reference the folding hash
#reference the Universal Hash

def folding_hash_code(key):
    chunks = [key[i:i + 2] for i in range(0, len(key), 2)]
    total = 0
    for chunk in chunks:
        chunk_value = 0
        for char in chunk:
            chunk_value = (chunk_value << 8) + ord(char)
        total += chunk_value
    return total, len(key)

value, length = folding_hash_code(student_id_list)
#print(f"value: {value}, m: {HASH_TABLE_SIZE}")

def universal_hash_compression(value, a=31, b=17, p=10007, m=1003):
    return ((a * value + b) % p) % m

hash3 = universal_hash_compression(value, a=31, b=17, p=10007, m=HASH_TABLE_SIZE)
#print(f"Compression Value: {hash3}")


# one thing to note is that I have made 3 different hash codes and 3 different compression function
# this means that I have actually made 6 different hash function because you can combine any hash code with
# any compression function

"""
2. Compare and contrast the three hash functions.
"""

# The first hash function that I made was a character multiplied by position index hash code and then the hash
# compression I used was a division compression

# One note about all the hash functions I decided to use the same modulus and hash table size. I decided to use 1003 as
# this is a prime number which is good for modulus and also keeps it large so that there is a lesser chances of
# collision.

# I first just wanted to test numerically how the different hash functions would perform against each other by putting
# the dataset against it and testing it over a range of entries. What I found from this test was that the SUM ASCII and
# division hash compression was the worst performing with most collisions. The folding hash and the universal hash
# compression was a little bit better but only by a small margin. While the polynomial rolling hash with the multiply
# add and divide hash compression was outperforming the other hash functions by a larger margin.

# When comparing the 3 hash functions I will base it upon time and space complexities, ease of implementation, security
# and collision resistance.

# For the first hash function which is the ASCII SUM and division. The ASCII SUM has to loop through each letter and
# then multiply it so this is of O(n) time complexity where n is the number of letters this is 7 letters or characters
# so it is really quite small. The modulus division function is of O(1) time. The space complexity is storing the
# letters in an array so also of O(n) which is the number of letters, again also 7. Probably the easiest to implement
# but in comparison is very similar to the others. The security is not the best either. The security is determined by
# its collision resistance as well as predictability and how one small change can affect the final value of the hash.
# A simple modulus operation does not improve unpredictability and a small change in its value will not affect it as
# much either.

# The second hash function was the polynomial rolling hash which has a space and time complexity of O(n) time. Due to
# Horners rule the rolling hash can be made less computationally expensive by using factorisation. It also has better
# collision resistance for its hash function and the compression function as both use random integers that are less
# predictable.

# The third hash function uses a folding hash which is interesting as it splits the string into chunks and then uses
# bitwise operation to get into a single value. It is quite similar to the ASCII SUM hash and has similar level of
# collision resistance. The universal hash compression function is better though as it uses random constant values for a
# and b that make it less predictable for how a value will be stored.

# I think what is interesting as I said before would be to test all the hash functions with compression functions to get
# a better idea how they work with each other. Another parameter to test would be data sets and the actual size of the
# hash table that will be used.
'''
def testing_collisions_from_hash_functions(filename, number):
    file = open(filename)
    student_record = ""
    hash1codes = []
    hash2codes = []
    hash3codes = []
    hash4codes = []
    for i in range(number):
        student_record = file.readline()
        student_record.replace(" ", "")
        student_id_list = []
        for i in range(8):
            if student_record[i] == " ":
                continue
            student_id_list.append(student_record[i])
        hash1 = division_hash_compress(position_mult_index_hash_code(student_id_list)[0], HASH_TABLE_SIZE)
        hash2 = MAD_hash_compress(polynomial_rolling_hash_code_horners(student_id_list)[0], HASH_TABLE_SIZE)
        hash3 = universal_hash_compression(folding_hash_code(student_id_list)[0], HASH_TABLE_SIZE)
        hash4 = universal_hash_compression(polynomial_rolling_hash_code_horners(student_id_list)[0], HASH_TABLE_SIZE)
        hash1codes.append(hash1)
        hash2codes.append(hash2)
        hash3codes.append(hash3)
        hash4codes.append(hash4)

    return (count_collisions(hash1codes)[1], count_collisions(hash2codes)[1], count_collisions(hash3codes)[1],
            count_collisions(hash4codes)[1])

def count_collisions(list):
    freq = {}
    total_collisions = 0
    for num in list:
        if num in freq:
            freq[num] += 1
            total_collisions += 1  # This is a collision beyond the first time
        else:
            freq[num] = 1
    return freq, total_collisions
results1 = []
results2 = []
results3 = []
results4 = []
entries = list(range(100, 10000, 500))
for i in range(len(entries)):
    results1.append(testing_collisions_from_hash_functions("Student_Records.txt", entries[i])[0])
    results2.append(testing_collisions_from_hash_functions("Student_Records.txt", entries[i])[1])
    results3.append(testing_collisions_from_hash_functions("Student_Records.txt", entries[i])[2])
    results4.append(testing_collisions_from_hash_functions("Student_Records.txt", entries[i])[3])

plt.figure(figsize=(10, 6))
plt.plot(entries, results1, label="Hashcode 1 (Sum ASCII)")
plt.plot(entries, results2, label="Hashcode 2 (Polynomial)")
plt.plot(entries, results3, label="Hashcode 3 (Folding)")
plt.plot(entries, results4, label="Hashcode 4 (Polynomial+Uni)")

plt.xlabel("Number of Data Entries")
plt.ylabel("Number of Collisions")
plt.title("Collision Comparison of Hash Functions")
plt.legend()
plt.grid(True)
plt.show()

print(entries)
print(results1)
print(results2)
print(results3)
'''

"""
3.2
"""

"""
1. Implement a hashtable with double hashing collision handling using two suitable hash functions you
implemented in Question 3.1. Your hashtable should be able to do insertions and searches (no
requirement to do deletions).
"""

class DoubleHashTable:
    def __init__(self, m=57641):
        self.size = m
        self.table = [None] * m
        self.z = 31 # for polynomial rolling hash
        # for universal hash compression (prime numbers)
        self.p = 10007
        self.a1, self.b1 = 31, 29
        self.a2, self.b2 = 13, 17
        # for secondary hash compression
        self.q = 43
        # for counting collisions
        self.collisions = 0

    def hashcode(self, key):
        return polynomial_rolling_hash_code_horners(key, self.z)[0]

    def hash_compress_1(self, key):
        return universal_hash_compression(key, self.a1, self.b1, self.p, self.size)

    def hash_compress_2(self, key):
        return 43 - key % 43 # from lectures and need to ensure that 2nd hash compression cannot equal 0.

    def insert(self, key, value):
        hashcode = self.hashcode(key)
        index = self.hash_compress_1(hashcode)
        step = self.hash_compress_2(hashcode) # step can never be 0
        if step == 0:
            step = 1

        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + step) % self.size
            self.collisions += 1

        self.table[index] = (key, value)

    def search(self, key):
        hashcode = self.hashcode(key)
        index = self.hash_compress_1(hashcode)
        step = self.hash_compress_2(hashcode)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            i += 1
            index = (index + step) % self.size

        return None  # not found

    def get_student_id_to_test(self, filename, number):
        file = open(filename)
        student_record = ""
        for i in range(number):
            student_record = file.readline()

        student_record.replace(" ", "")
        student_id_list = []

        for i in range(8):
            if student_record[i] == " ":
                continue
            student_id_list.append(student_record[i])

        return student_id_list

    def get_student_name(self, filename, number):
        file = open(filename)
        student_record = ""
        for i in range(number):
            student_record = file.readline()

        student_record.replace(" ", "")
        student_name = []

        for i in range(9, len(student_record)-1):
            #print(student_record[i])
            student_name.append(student_record[i])
        student_name = "".join(student_name)
        return student_name



"""
2. Test your hashtable with “Student_Records.txt” file given in the Assignment 2 page. Report the
average collisions for the 3 hash functions from the section 3.1 above, for
a. 100 names,
b. 200 names,
c. 500 names,
d. the entire dataset.
(Choose the size of the hashtable so that the entire dataset can fit on the hashtable). You may
calculate the average collisions as: (number of collisions/ total number of entries added to the
hashtable) * 100.
"""

hashTable = DoubleHashTable()
def report_average_collisions(hashTable, number_of_names):
    for j in range(1, number_of_names):
        student_id_list = hashTable.get_student_id_to_test("Student_Records.txt", j)
        student_name = hashTable.get_student_name("Student_Records.txt", j)
        hashTable.insert(student_id_list, student_name)
    return hashTable.collisions / number_of_names

def report_number_of_collisions(hashTable, number_of_names):
    for j in range(1, number_of_names):
        student_id_list = hashTable.get_student_id_to_test("Student_Records.txt", j)
        student_name = hashTable.get_student_name("Student_Records.txt", j)
        hashTable.insert(student_id_list, student_name)
    return hashTable.collisions

# (a) 100 names
collisions = report_average_collisions(hashTable, 100)
print(f"100 names -> Number of Collisions: {collisions}")
# (b) 200 names
collisions = report_average_collisions(hashTable, 200)
print(f"200 names -> Number of Collisions: {collisions}")
# (c) 500 names
collisions = report_average_collisions(hashTable, 500)
print(f"500 names -> Number of Collisions: {collisions}")
# (d) entire dataset
collisions = report_average_collisions(hashTable, 18239)
print(f"18239 names -> Number of Colllisions {collisions}")

'''
# plotting
entries = list(range(100, 10000, 1000))
collisions = []
for item in entries:
    collisions.append(report_average_collisions(hashTable, item))

plt.figure(figsize=(10, 6))
plt.plot(entries, collisions, label="collisions")


plt.xlabel("Number of Data Entries")
plt.ylabel("Number of Collisions")
plt.title("Collisions of Hash Table")
plt.legend()
plt.grid(True)
plt.show()
'''
"""
3. Explain your results from (2) above.
"""

# one of the issues with the question above is that the student records has a range of 100 to 18239 records this means
# that for such a large range I need to create a hash table size that is greater than 18239 and this means that there
# will be significantly more collisions for 18239 names than 100 names. So I think that I needed to test it with a more
# similar range. As I increase the number of entries into the hash table it seems the number of collisions increases
# exponentially. This makes sense for a double hashing function as there are more numbers already occupying spaces so
# there will be more double hashing required continually until the hash index is found.

# from 100 entries it is an average of 0 collisions
# from 200 entries it is an average of 0 collisions
# from 500 entries it is an average of 0.018 collisions
# from 18239 it is an average of 411.584 collisions

# These are the results and when there are many names the hash function seems to be making a lot of collisions and means
# that another hash function is probably required to make an effective hash function


