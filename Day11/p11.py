'''
Given an Array A consisting of N positive integers, you have to answer Q queries on it. Queries can be of the two types: * 1 X Y - Update X at location Y in the array. * 2 L R - Print the sum of range [L, R], i.e. Both L and R are inclusive.

Note:- Array indexing is from 0.
Input:

    The first line contains two space separated integers N(Length of Array) and Q(Queries).
    Next Line contains N space separated integers denoting array A.
    Next Q Line contains 3 space separated integers for each line, as described above
Output: Answer to the each query of type 2 in a new line, only when range is valid, otherwise ouput `-1`
SAMPLE INPUT 
5 5
2 3 4 8 9
1 0 3
2 0 1
2 0 4
1 2 5
2 0 3
SAMPLE OUTPUT 
6
27
19
'''

