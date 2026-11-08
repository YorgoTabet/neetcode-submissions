class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        Set<Character> charSet = new HashSet<>();
        int res = 0;

        for(int i = 0; i < s.length(); i++) {
            while(charSet.contains(s.charAt(i))) {
                charSet.remove(s.charAt(l));
                l++;
            }

            charSet.add(s.charAt(i));
            res = Math.max(charSet.size(), res);
        }

        return res;
        
    }
}