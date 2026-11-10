class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numbers = new HashSet<>();
        Set<Integer> seen = new HashSet<>();
        int res = 0;

        for (int i : nums) {
            numbers.add(i);
        }

        for( int i : nums) {
            if(seen.contains(i)) continue;

            int count = 1;
            // smaller count
            int smaller = i -1;
            int larger = i + 1;
            while(numbers.contains(smaller)) {
                count++;
                seen.add(smaller);
                smaller--;
                }
            while(numbers.contains(larger)) {
                count++;
                seen.add(larger);
                larger++;
                }
            res = Math.max(res, count);
        }

        return res;

    }
}


// build a set of the numbers 
// for each number, check if we have the number less than it
// if not directly under it discard the number
// if directly under it, increase count and set the number to be checked
// caveat to think about, number can be the largest, the smallest or in the middle
// find the number that doesn't have a larger but has a lower, or the opposite so you can test from it 