# s = [int(s) for s in input().split(',')]
# s.reverse()
# print(s)

# s = [int(s) for s in input().split(',')]
# li_reverse=s[::-1]
# print(li_reverse)

def reverseArray(arr):
 neww = arr[::-1]
 return neww

print(reverseArray([int(s) for s in input().split(',')]))