class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        Set<Character> numSet = new HashSet<>();
        int res = 0;

        for(int i = 0; i < s.length(); i++) {
            while(numSet.contains(s.charAt(i))) {
                numSet.remove(s.charAt(l));
                l++;
            }

            numSet.add(s.charAt(i));
            res = Math.max(i - l + 1, res);
        }

        return res;
        
    }
}