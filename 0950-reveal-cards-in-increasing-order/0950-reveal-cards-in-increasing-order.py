from collections import deque
from array import array
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        st = deque()
        st.append(deck[n - 1])
        # print(st)
        for i in range(n - 2, -1, -1):
            st.appendleft(st.pop())
            st.appendleft(deck[i])
            # print(st)
        # revealed = []
        # while st:
        #     revealed.append(st.popleft())
        # return revealed        
        return array('i',st)