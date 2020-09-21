import math
def merge_Sort(Arr):
  """ Merge Sort is a Divide and Conquer algorithm. 
  It divides input array in two halves, calls itself
   for the two halves and then merges the two sorted halves."""
  try:
    n=len(Arr)
    if n>1:
      mid = math.floor(n / 2)
      left=Arr[0:mid]
      right=Arr[mid:n]

      merge_Sort(left)
      merge_Sort(right)
      merge(left, right, Arr)

    return Arr
  except Exception as err:
    return err


def merge(left, right,Arr):
  i,j,k=0,0,0
  # return i
  while (i < len(left) and j < len(right)):
    if left[i] <= right[j]:
      Arr[k] = left[i]
      i = i + 1
    else:
      Arr[k] = right[j]
      j = j + 1

    k = k + 1
  if i == len(left):
    Arr[k] = right[j]
  else:
    Arr[k] = left[i]



if __name__ == "__main__":

    print(merge_Sort([8, 4, 23, 42, 16, 15]))