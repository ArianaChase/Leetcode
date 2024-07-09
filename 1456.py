class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        ans1 = 0
        ans2 = 0
        lastNumber1 = 0
        lastNumber2 = 0
        ans = 0
        horizontalCuts.append(h)
        verticalCuts.append(w)
        for i in sorted(horizontalCuts):
            print('this is ', i)
            if index(i) == 0:
                lastNumber1 = i
            else: 
                if i - lastNumber1 >= ans1:
                    ans1 = (i - lastNumber1) 
                    print(ans1, ' is now the answer, ', 'because ', i, ' - ', lastNumber1, ' is', (i-lastNumber1))
                    lastNumber1 = i
                else:
                    print(ans1, ' is higher than me')
                    lastNumber1 = i
                    pass
        
        for x in sorted(verticalCuts):
            if index(x) == 0:
                lastNumber2 = x
            else:
                if x - lastNumber2 >= ans2:
                    ans2 = (x - lastNumber2)
                    lastNumber2 = x
                else:
                    lastNumber2 = x

                    pass
        
        ans = ans1 * ans2
        print(ans1, ans2)
        return ans % (10**9 + 7)
