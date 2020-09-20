def insertion_Sort(Arr):
    """
    Selection Sort is a sorting algorithm that traverses
    the array multiple times as it slowly builds out the
        sorting sequence. 
    """
    try:
        for i in range(1,len(Arr)):
            temp = Arr[i]
            j = i - 1
            while (j >= 0 and temp < Arr[j]):
                Arr[j + 1] = Arr[j]
                j = j - 1

                Arr[j + 1] = temp

        return Arr
    except Exception as err:
        return err
  


    # print(i)



if __name__ == "__main__":
    print(insertionSort([1,200,23,-1,0]))