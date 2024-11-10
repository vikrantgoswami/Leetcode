import java.util.*;

class LongestConsSequence {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> setOfNums = new HashSet<Integer>();
        int maxLengOfSubseq = 0;

        // making a set out of the list
        for (int num : nums) {
            setOfNums.add(num);
        }

        for (Integer num : setOfNums) {
            if (!setOfNums.contains(num - 1)) {
                // previous number to this number is not present in the set
                // this means this number is not part of a sequence rather a starting point for
                // a sequence
                int currSubseqLen = 1;
                int numInSeq = num;

                // now we'll calculate the length of subsequence formed starting with the
                // current element
                while (setOfNums.contains(numInSeq + 1)) {
                    numInSeq += 1;

                    // increase curr subseq length when each subsequent number is present in set
                    currSubseqLen += 1;
                }
                maxLengOfSubseq = Math.max(maxLengOfSubseq, currSubseqLen);
            }
        }
        return maxLengOfSubseq;

    }
}