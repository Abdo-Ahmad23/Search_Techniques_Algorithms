class MergeSortAsc():
    def merge_sort(arr:list):## Divide and conquer
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        left_sorted = MergeSortAsc.merge_sort(left_half)
        right_sorted = MergeSortAsc.merge_sort(right_half)

        return MergeSortAsc.merge(left_sorted ,  right_sorted)

    def merge(left:int ,  right:int):
        sorted_array=list()
        i=j=0

        # Compare values from both {right & left}
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        # Task remaining from left
        while i < len(left):
            sorted_array.append(left[i])
            i += 1

        # Task remaining from right
        while j < len(right):
            sorted_array.append(right[j])
            j += 1

        return sorted_array
class MergeSortDes():
    def merge_sort(arr:list):## Divide and conquer
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        left_sorted = MergeSortDes.merge_sort(left_half)
        right_sorted = MergeSortDes.merge_sort(right_half)

        return MergeSortDes.merge(left_sorted ,  right_sorted)

    def merge(left:int ,  right:int):
        sorted_array=list()
        i=j=0

        # Compare values from both {right & left}
        while i<len(left) and j<len(right):
            if left[i] > right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        # Task remaining from left
        while i < len(left):
            sorted_array.append(left[i])
            i += 1

        # Task remaining from right
        while j < len(right):
            sorted_array.append(right[j])
            j += 1

        return sorted_array

class BinarySearch():
    def isFound(arr:list , target:int)->bool:
        arr = MergeSortAsc.merge_sort(arr)
        left  ,  right = 0  ,  len(arr) - 1
        while left <= right:
            mid = ( left + right ) >> 1
            if arr[mid]  ==  target:
                return True
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def indexOfElementAfterSorting(arr:list,target:int)->int:
        if BinarySearch.isFound(arr,target):
            arr = MergeSortAsc.merge_sort(arr)
            left  ,  right = 0  ,  len(arr) - 1
            while left <= right:
                mid = ( left + right ) >> 1
                if arr[mid]  ==  target:
                    return mid
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        else:
            return -1

arr=[1,2,3,5,6,0]
target=1
print(BinarySearch.isFound(arr,target))
print(BinarySearch.indexOfElementAfterSorting(arr,target))