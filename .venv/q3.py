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

#1 Create 3 hash functions suitable for the given problem

# From Lectures (Week 6) - Hash Tables and Maps

# I will test the code using Student_Records.txt


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
print(f"Hash Code: {value}, length: {length}")
# super simple compression function
def division_hash_compress(value, length):
    return value % length

hash = division_hash_compress(value, length)
print(f"Compression Value: {hash}")

# 2nd Hash Function
# Polynomial Rolling - Hash Function
# Multiply, Adding and Divide - Compression Function
def polynomial_rolling_hash_code(student_id_list):
    value = 0

def MAD_hash_compress(value, length):
    return






