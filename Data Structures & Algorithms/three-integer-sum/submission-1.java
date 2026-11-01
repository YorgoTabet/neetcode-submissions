class Solution {
  public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> res = new ArrayList<>();

    for (int i = nums.length - 1; i >= 2; i--) {
      int target = nums[i];
      if (target < 0) break;
      if (i < nums.length - 1 && nums[i] == nums[i + 1]) continue;

      int l = 0;
      int r = i - 1;
      while (l < r) {
        int total = nums[l] + nums[r] + target;
        if (total == 0) {
          res.add(List.of(nums[l], nums[r], target));
          l++;
          r--;
          while (l < r && nums[l] == nums[l - 1]) l++;
        } else if (total > 0) {
          r--;
        } else {
          l++;
        }
      }
    }
    return res;
  }
}