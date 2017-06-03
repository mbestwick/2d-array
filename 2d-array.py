"""
Context 
Given a 6 x 6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in
this pattern in A's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in A, an hourglass sum = sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in A, then print the maximum
hourglass sum.

Input Format
There are 6 lines of input, where each line contains 6 space-separated integers
describing 2D Array A; every value in A will be in the inclusive range of -9 to 9.

Output Format
Print the largest (maximum) hourglass sum found in A.

Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output
19
"""

arr = []
for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    arr.append(arr_temp)

total = []

for i in range(4):
    for j in range(4):
        subtotal = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                    arr[i + 1][j + 1] +
                    arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])
        total.append(subtotal)

print max(total)
