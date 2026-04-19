class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = defaultdict(list)

        for string in strs:
            # Create empty frequency table
            count = [0] * 26 # a, b, ..., z

            for char in string:
                # Using ascii find the count of current char
                # Add 1 in the frequency table at the position of character 
                count[ord(char) - ord("a")] += 1

            # Key of hashset is now an array (tuple) of frequency tables
            # Append the string as the value of specific frequency table keys
            # dict deals with matching frequency table keys
            hashset[tuple(count)].append(string)

        return list(hashset.values())