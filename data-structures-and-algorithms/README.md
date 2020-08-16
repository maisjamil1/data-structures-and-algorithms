# Reverse an Array
manipulate an array and rearrange it in reversed order
## Challenge
<!-- Description of the challenge -->
we will Write a function called reverseArray which takes an array as an argument.and return an array with elements in reversed order.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Solution
<!-- Embedded whiteboard image -->
def reverseArray(arr):
 neww = arr[::-1]
 return neww

print(reverseArray([int(s) for s in input().split(',')]))