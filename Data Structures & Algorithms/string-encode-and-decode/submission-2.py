class Solution:

    def encode(self, strs: List[str]) -> str:
        string_output = ""

        for string in strs:
            # Add length of string to output string
            # Add separator and the actual string
            string_output += str(len(string)) + "#" + string

        return string_output


    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s): 
            j = i
            while s[j] != "#": 
                j += 1 
            length = int(s[i:j]) # Takes the strings and converts to int adding to the length
            i = j + 1 # Moves counter i over the '#'
            j = i + length # moves string counter over to the end of word
            result.append(s[i:j]) # Appends the range of chars to a string

            i = j # Resets the i counter to start at the same position as j
            
        return result