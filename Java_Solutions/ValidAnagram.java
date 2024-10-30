class Solution {
    public boolean isAnagram(String s, String t) {
        // for s & t to be anagrams -> they should've same length and same frequency of
        // each character
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> char_count = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (char_count.containsKey(s.charAt(i))) {
                char_count.put(s.charAt(i), char_count.get(s.charAt(i)) + 1);
            } else {
                char_count.put(s.charAt(i), 1);
            }
            if (char_count.containsKey(t.charAt(i))) {
                char_count.put(t.charAt(i), char_count.get(t.charAt(i)) - 1);
            } else {
                char_count.put(t.charAt(i), -1);
            }
        }

        for (int i = 0; i < s.length(); i++) {
            if (char_count.get(s.charAt(i)) != 0) {
                return false;
            }
        }

        return true;
    }
}