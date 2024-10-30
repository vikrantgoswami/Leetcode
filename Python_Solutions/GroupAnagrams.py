class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #approach would be to sort the words in list
        #store the words in a map with key the sorted value & value a list of anagrams
        #finally we return the list of values of the map

        words_map = {}
        result    = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in words_map.keys():
                existing_list = words_map.get(sorted_word)
                existing_list.append(word)
                words_map[sorted_word] = existing_list
            else:
                words_map[sorted_word] = [word]

        for value in words_map.values():
            result.append(value)

        return result