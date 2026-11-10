class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numbers = new HashSet<>();
        int res = 0;

        for (int i : nums) {
            numbers.add(i);
        }

        for (int i : numbers) {
            int count = 0;
            int smaller = i - 1;
            if (!numbers.contains(smaller)) {
                while (numbers.contains(i + count)) {
                    count++;
                }
                res = Math.max(res, count);
            }
        }

        return res;
    }
}