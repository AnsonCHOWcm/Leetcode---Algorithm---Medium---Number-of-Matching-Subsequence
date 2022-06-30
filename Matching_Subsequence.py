class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        res = 0

        s_len = len(s)

        index = 0

        while index < len(words):

            word = words[index]

            w_len = len(word)

            w_index = 0
            s_index = 0

            while w_index < w_len and s_index < s_len:

                if word[w_index] == s[s_index]:
                    w_index += 1

                s_index += 1

            if w_index == w_len:
                res += 1
                while index < len(words) - 1 and words[index + 1] == words[index]:
                    res += 1
                    index += 1
            else:
                while index < len(words) - 1 and words[index + 1] == words[index]:
                    index += 1

            index += 1

        return res

