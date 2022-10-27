n, k = map(int, input().split())

A = [0 for _ in range(n)]
for i in range(n):
	A[i] = list(map(int, input().split()))

# 2 2 | 1 1
# 2 x | 1 1
# - - - - -
# 3 3 | y 4
# 3 3 | 4 4

#행렬이 2x2일때 까지 분할정복할꺼임
def findK(A,startRow,endRow,startCol,endCol,k):
    # startElem 가 k라면 
    if A[startRow][startCol] == k:
        return [startRow, startCol]
    # endElem 가 k라면
    if A[endRow][endCol] == k:
        return [endRow, endCol]
    
    # 2x2행렬일 때 k 조사
    while endRow - startRow <= 1 :
        # startElem의 오른쪽이 k라면
        if A[startRow][endCol] == k:
            return [startRow,endCol]
        # endElem의 왼쪽이 k라면
        if A[endRow][startCol] == k:
            return [endRow, startCol]
        # 찾는게 없다면 
        else:
            return
    #X,Y's elem 좌표 생성
    xRow = startRow + (endRow - startRow) // 2                                          
    xCol = startCol + (endCol - startCol) // 2
    yRow, yCol = xRow+1, xCol+1
    
    #X,Y's elem 가 k 인지 조사하는 함수 선언
    def checkXY(A, xRow, xCol, yRow, yCol, k):
        # X.value == k 인가?
        if A[xRow][xCol] == k :
            return[xRow, xCol]
        # Y.value == k 인가?
        if A[yRow][yCol] == k:
            return[yRow, yCol]
        # 없다면 null 을 리턴하고 종료 
        return
    # checkXY 함수 선언 종료
    
    result = checkXY(A, xRow, xCol, yRow, yCol, k)
    # 만약리턴값이 null 값이 아니라면 결과를 반환
    if result: return result
    
    # X.value > k 인가?
    if A[xRow][xCol] > k:
        # 4 분 면에 있을 수 없다.
        # 1,2,3 분면에 대해 분할정복
        result = findK(A, startRow, xRow, yCol, endCol, k)
        if result: return result # 1 분면 
        
        result = findK(A, startRow, xRow, startCol, xCol, k)
        if result: return result # 2 분면
        
        result = findK(A, yRow, endRow, startCol, xCol, k)       
        if result: return result# 3 분면
    
    # Y.value < k 인가?
    if A[yRow][yCol] < k:
        # 2 분 면에 있을 수 없다.
        # 1,3,4 분면에 대해 분할정복
        result = findK(A, startRow, xRow, yCol, endCol, k)
        if result: return result # 1 분면
        
        result = findK(A, yRow, endRow, startCol, xCol, k) 
        if result: return result # 3 분면
        
        result = findK(A, yRow, endRow, yCol, endCol, k) 
        if result: return result # 4 분면
        
    
    # X.value < k < Y.value 인가?
    if (A[xRow][xCol]< k) and (k < A[yRow][yCol]):
        #2,4 분 면에 있을 수 없다.
        result = findK(A, startRow, xRow, yCol, endCol, k)  
        if result: return result  # 1 분면
        
        result = findK(A, yRow, endRow, startCol, xCol, k) 
        if result: return result  # 3 분면
    
    return [-1,-1]
#findK 종료


index = findK(A,0,n-1,0,n-1,k)
print(f"({index[0]}, {index[1]})")


# 4 -10
# -24 - 9 - 8 18
# -21 - 7 3 19
# -20 - 4 7 22
# -10 - 2 15 25
