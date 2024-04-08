class Solution:
    def checkValidString(self, s: str) -> bool:
        left_balance = 0
        right_balance = 0
        n = len(s) # Length of the string

        # First pass: check from left to right treating asterisks as open brackets
        for i in range(n):
            if s[i] == '(' or s[i] == '*': # Increment left balance for open brackets and asterisks
                left_balance += 1
            else: # Decrement left balance for close brackets
                left_balance -= 1

            # Perform the same operations for the corresponding character from the right end of the string
            if s[n - 1 - i] == ')' or s[n - 1 - i] == '*':
                right_balance += 1
            else:
                right_balance -= 1

            # More right brackets than left brackets and asterisks OR More left brackets than right brackets and asterisks
            if left_balance < 0 or right_balance < 0:
                return False
        return True # If the balance remains non-negative throughout the string, it's valid
                    