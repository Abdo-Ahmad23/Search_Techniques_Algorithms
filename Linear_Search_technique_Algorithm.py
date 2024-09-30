class LinearSearch():
    def isFound(arr:list,target:int)->bool:
        for i in arr:
            if i ==target:
                return True
        return False
    def indexOfElement(arr:list,target:int)->int:
        if LinearSearch.isFound(arr,target):
            for i in range(len(arr)):
                if target==arr[i]:
                    return i
        else:
            return -1

arr=[1,2,3,5,6,0]
target=1
print(LinearSearch.isFound(arr,target))
print(LinearSearch.indexOfElement(arr,target))