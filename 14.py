class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_len = min(len(word) for word in strs)
        ans = ''
        lastWord = ''
        for i in range(max_len):
            print('new round ', i)
            counter = 0
            while counter < len(strs):
                for word in strs:
                    if lastWord != '':   
                        if word[i] == lastWord[i]:
                            counter += 1
                            lastWord = word
                            print(counter, " similarity ", "both have ", word[i])
                        elif word == lastWord:
                            ans+= word[i]
                            print('only one word')
                            return ans
                        else:
                            print('no more similarities: ', ans)
                            return ans    
                    else:
                        lastWord = word  
                        print('first word')
            ans += word[i]
            print('one prefix confirmed')
        return ans 
   
