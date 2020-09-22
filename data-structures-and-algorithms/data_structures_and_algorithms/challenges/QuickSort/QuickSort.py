def QuickSort(arr, left, right):
  """
    quick sort is a Divide and Conquer algorithm. 
    It picks an element as pivot and partitions the given array around the picked pivot.
  """
  try:
    if left < right:
        position = Partition(arr, left, right)
        QuickSort(arr, left, position - 1)
        QuickSort(arr, position + 1, right)
    return arr
  except Exception as err:
      return err


def Partition(arr, left, right):
  pivot = arr[right]
  low = left - 1
  i = left
  while i < right:
    if (arr[i] <= pivot):
      low+=1
      Swap(arr, i, low)
    i+=1
  Swap(arr, right, low + 1)
  return low + 1


def Swap(arr, i, low):
  temp = arr[i]
  arr[i] = arr[low]
  arr[low] = temp


if __name__ == "__main__":
    
    print(QuickSort([8, 4, 23, 42, 16, 15], 0, 5))

