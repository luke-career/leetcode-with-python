class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        p = 0
        while tickets[k] > 0:
            if(tickets[p] > 0):
                tickets[p] -= 1
                count += 1
            p = (p + 1) % len(tickets)

        return count