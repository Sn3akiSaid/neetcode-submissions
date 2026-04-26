class Solution:
    def isValid(self, s: str) -> bool:
        # Brute force solution
        bracket = "()"
        curly = "{}"
        square = "[]"

        while bracket in s or curly in s or square in s:
        # There will always be at least one instance of a bracket type present,
        # so the while loo replaces that bracket type with empty space.
        # In the case s="([{}])" it finds curly first and removes it but then
        # square comes up and removes that and so on.
        # In the s="()[]{}" it finds all and simultaneously removes them
            s = s.replace(bracket, '')
            s = s.replace(curly, '')
            s = s.replace(square, '')
        # Check if s is empty
        return s == ''
