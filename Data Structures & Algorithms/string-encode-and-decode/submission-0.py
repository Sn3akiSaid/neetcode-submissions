class Solution:


    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''

        sizes_list, string_output = [], ""
        for string in strs:
            sizes_list.append(len(string))

        for item in sizes_list:
            string_output += str(item)
            string_output += ","
        
        string_output += "#"

        for string in strs:
            string_output += string
        return string_output


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sizes, result, i = [], [], 0 
        while s[i] != "#":
            current = ""
            while s[i] != ",":
                current += s[i] # Collects the numbers as string
                i += 1 # Moves counter through strings characters
            sizes.append(int(current)) # Convert string of length into int and add to list of sizes
            i += 1 # Moves counter to the end of the length strings
        i += 1 # Moves counter past the "#" char

        for size in sizes:
            result.append(s[i:(i+size)]) # Starts after the "#", appends the characters up to start + size
            i += size # Moves counter to start of next string
        return result