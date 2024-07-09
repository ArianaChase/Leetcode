class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words) #the biggest number of len(word)
        ans = []
        for i in range(max_len):
            ver_word = ''
            for word in words:
                if i < len(word):
                    print('yeet')
                    ver_word += word[i]
                else: 
                    ver_word += ' '

            ans.append(ver_word.rstrip())

        return ans

