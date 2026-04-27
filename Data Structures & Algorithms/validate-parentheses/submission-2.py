class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Hashmap mapping 
        closeToOpen = { ")": "(",
                        "]": "[",
                        "}": "{" }

        for c in s:
            # Check if char in string matches a closing KEY from hashmap
            if c in closeToOpen:
                # Check IF the stack is not empty AND the top value in stack is the matching opening VALUE
                if stack and stack[-1] == closeToOpen[c]:
                    # Then remove the last element from stack (LIFO)
                    stack.pop()
                # If they don't match or the stack is empty -> parentheses don't match
                else:
                    return False
            # If not in closeToOpen (keys) closing parentheses, must be open parenthesis
            else:
                # Add it to the stack and keep going
                stack.append(c)
        # In the end can only return True if the stack is empty
        return True if not stack else False