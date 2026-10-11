class Solution:
    def binarySearch(self, arr: List[int], target:int) -> bool:
        l,r = 0, len(arr) - 1

        while l <= r:
            mid = math.floor((r-l) / 2 + l)

            if(arr[mid] == target):
                return True
            if(target < arr[mid]):
                r = mid - 1
            else:
                l = mid + 1

        return False

    def binarySearchInRange(self, arr: List[List[int]], target:int) -> Optional[int]:
        m_length = len(arr)
        n_length = len(arr[0]) - 1
        
        l,r = 0, len(arr) - 1


        while l <= r:
            mid = math.floor((r-l) / 2 + l)
            
            if(target >= arr[mid][0] and target <= arr[mid][n_length]):
                return mid
            if(target < arr[mid][0]):
                r = mid - 1
            else:
                l = mid + 1

        return None

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = self.binarySearchInRange(matrix, target)
    
        return  self.binarySearch(matrix[m], target) if m is not None else False




