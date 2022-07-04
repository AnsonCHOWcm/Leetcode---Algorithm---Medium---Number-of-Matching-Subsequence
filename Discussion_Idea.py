class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        waiting_list = collections.defaultdict(list)

        for w in map(iter, words):
            waiting_list[next(w)].append(w)

        for c in s:

            for w in waiting_list.pop(c, ()):
                waiting_list[next(w, None)].append(w)

        return (len(waiting_list[None]))
