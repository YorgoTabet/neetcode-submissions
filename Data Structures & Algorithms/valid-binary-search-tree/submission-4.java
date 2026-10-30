/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isValidBST(TreeNode root) {
      return helper(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean helper(TreeNode node, long min, long max) {
        if(node == null) return true;
        boolean nodeIsValid = min < node.val && node.val < max;
        if(!nodeIsValid) return false;

        boolean isValidLeft = helper(node.left, min, node.val);
        boolean isValidRight = helper(node.right, node.val, max);

        return nodeIsValid && isValidLeft && isValidRight;

    }
}
