"""
Question 4. 1 (30/100)
Consider the 6 sorting algorithms you have learnt: Selection Sort, Insertion Sort, Bubble Sort, Merge
Sort, Heap Sort and Quick Sort. Explain which sorting algorithm(s) is suitable for the three different
scenarios of input data given below. The data is:
1. In random order (i.e., you have no information about the order of the elements)
2. In a nearly sorted order (i.e., only a maximum of 1 or 2 elements are disordered)
3. In reversed order than your expected sorting order (e.g., if your expected order is: 2, 4, 7, 9, 15
The given data is in the reversed order as 15, 9, 7, 4, 2)
You should provide an explanation for the three different scenarios 1, 2, 3 separately (you may take up
to 150-300 words per scenario.). Your explanation should include, why your chosen sorting algorithm(s)
is suitable for the given scenario over the other sorting algorithms. You may use this tool to compare the
different sorting algorithms you have learnt
"""

#1. Random Order

# For a random Order List the best I would personally choose a quick sort as this has an average and best case
# time complexity of O(n*log(n)). This is right on par with a heap sort and a merge sort but you are able to do it in
# place and so you do not require extra memory. It does not say keeping it stable is a requirement and is therefore not
# necessary. The only thing is if this random order is lopsided or skewed and the quick sort choose bad pivots then it
# can be of O(n^2) time complexity at its worst case.

#2. Nearly Sorted Order

# For nearly sorted order I would pick insertion sort as this has a best case of O(n) the only other one that is
# comparable is a bubble sort but I think the in place algorithm is more elegant.

#3. Reverse Order

# For reverse order I think that bubble, insertion and selection are the worst picks as they require the most
# comparisons and swaps on reversed orders. Merge sort I believe would be the safest as the quick sort is based on the
# pivot chosen and if a bad pivot is chosen can make it slower than a merge sort.

"""
Question 4. 2 (70/100)
4. a. Implement the Merge sort algorithm in python to sort a list with “K” elements in the descending
order (decreasing order). You may consider that all “K” elements in the list are integers. You should
write a function “merge_sort” that takes a python list as a parameter and returns a list that is sorted
in the descending order. You are free to write other functions to help with your merge sort
implementation.
Example of the function behavior:
Calling the function:
merge_sort([2, 8, 10, 1, 5, 3, 7, 9, 12, 90])
Function output:
[90, 12, 10, 9, 8, 7, 5, 3, 2, 1]
(30 points)
b. Draw the Merge sort tree for the above example
"""

"""
4.2 (a)
"""

def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left_half = merge_sort(list[0:mid])
    right_half = merge_sort(list[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i < len(left):
        result.append(left[i])
        i+=1
    while j < len(right):
        result.append(right[j])
        j+=1
    return result

print(merge_sort([2, 8, 10, 1, 5, 3, 7, 9, 12, 90]))
print(5//2)

"""
4.2 (b)
"""

# The merge sort tree will be included as a pdf to this document

"""
5. Answer the following questions based on the Merge Sort algorithm
a. Merge sort belongs to the category of Divide and Conquer algorithm design. Explain the Merge
Sort algorithm with respect to the Divide and Conquer algorithm design paradigm (100 - 250
words)
(10 points)
b. Compare and contrast the Merge sort algorithm with another Divide and Conquer sorting
algorithm you have learnt (100 – 250 words).
(10 points)

"""

"""
5 (a)
"""

# Merge sort works as a divide and conquer algorithm by dividing a list in half than taking those sublist and dividing
# these again into halves. This is done until no more division is possible. The sublists are in their final state.
# after this the conquer side is by sorting each of the lists and then they are combined which again are combined and
# sorted at the same time. This goes back up the recursive tree until the sublists become a sorted list.


"""
5 (b)
"""

# Quick sort is different in how it works as a divide and Conquer algorithm. It instead uses a pivot and elements less
# than go to the left and elements greater go the right. It keeps on dividing and choosing a pivot recursively this way
# until it reach no more possible division. The bulk of the work is thus done by the partitioning part which sorts the
# array. In this case there is no need to go back up recursive call back to sort it. In random order the quick sort may
# be faster than merge sort with average case being O(n*log(n)) but it can choose pad pivots and worst case being
# O(n^2).