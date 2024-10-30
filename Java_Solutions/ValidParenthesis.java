class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> bracketsMap = new HashMap<>();
        bracketsMap.put(')','(');
        bracketsMap.put(']','[');
        bracketsMap.put('}','{');
        Stack<Character> bracketStack = new Stack<Character>();

        for (char bracket : s.toCharArray()){
            if (bracketsMap.containsValue(bracket)){
                bracketStack.push(bracket);
            }
            else{
                if (bracketStack.size() >=1 && bracketStack.peek() == bracketsMap.get(bracket)) {
                    bracketStack.pop();
                }
                else{
                    return false;
                }
            }
        }
        return bracketStack.size() == 0;
    }
}