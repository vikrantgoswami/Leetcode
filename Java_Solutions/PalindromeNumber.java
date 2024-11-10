class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) return false;
        int divisor = 1;
        int rightDigit = 0;
        int leftDigit = 0;
        while(x/10 >= divisor) {
            divisor*=10;
        }
        while(x != 0) {
            rightDigit = x % 10;
            leftDigit =  x / divisor;
            if(rightDigit != leftDigit) return false;
            x = (x%divisor) / 10;
            divisor/=100;
        }
        return true;
    }
}