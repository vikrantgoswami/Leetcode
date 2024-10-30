class Solution {
    //Given a string s, find the length of the longest substring without repeating characters.
    public int lengthOfLongestSubstring(String s) {
        Set<Character> visitedChars = new HashSet<Character>();
        int res = 0;
        int l = 0;
        int n = s.length();

        for(int r=0; r<n; r++){
            while(visitedChars.contains(s.charAt(r))){
                visitedChars.remove(s.charAt(l));
                l+=1;
            }
            visitedChars.add(s.charAt(r));
            res = Math.max(res, r-l+1);
        }
        return res;
    }
}