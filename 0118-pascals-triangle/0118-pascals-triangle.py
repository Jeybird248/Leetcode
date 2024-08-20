class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        
        def binomialCoeff(n, k) :
            res = 1
            if (k > n - k) :
                k = n - k
            for i in range(0 , k) :
                res = res * (n - i)
                res = res // (i + 1)

            return res


        for line in range(0, numRows) :
            arr = []
            for i in range(0, line + 1) :
                arr.append(binomialCoeff(line, i))
            output.append(arr)
                
        return output