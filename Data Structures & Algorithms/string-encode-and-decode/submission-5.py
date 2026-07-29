class Solution:
    def encode(self, strs: List[str]) -> str:
        total_word = ""
        for word in strs:
            total_word += str(len(word))+ "#" + word
        return total_word

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            word_length = int(s[i:j])   

            #build word
            word = s[j+1:j+1+word_length]

            res.append(word)

            i = j + 1 + word_length

        return res
