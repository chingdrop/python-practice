def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

      # Median parameter is assigned by calling the MedianOfThree module.
       median = MedianOfThree(alist,first,last)

      # Partition uses a new parameter called "median".
       splitpoint = partition(alist,first,last,median)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

# MedianOfThree module is used to find the median pivot point. /
# Thank you for the help with the MedianOfthree logic structure. 
def MedianOfThree(alist,first,last):

   # Median is discovered by adding the first and last index  then dividing by 2. /
   # Must be converted to integer to later be used as a list index. 
   median = (first+last)//2

   # Checks if the value of the first postion is more than the value of the last position. 
   if alist[first] < alist[last]:

      # Returns the last index in the list, or the median index. /
      # This depends on whether the last value in the list is less than the value of the median. 
      return last if alist[last] < alist[median] else median

   else:

      # Returns the first index if the first value is less than the median value /
      # otheriwse the median index is returned. 
      return first if alist[first] < alist[median] else median


def partition(alist,first,last,median):

   leftmark = first+1
   rightmark = last

   pivotvalue = alist[median]

   done = False
   while not done:

       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
           print(alist)

       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1
           print(alist)
           
       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
           print(alist)

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)

