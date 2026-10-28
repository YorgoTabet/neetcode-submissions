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
    public int goodNodes(TreeNode root) {
        return 1 + helper(root.left, root.val) + helper(root.right, root.val);
    }

    public int helper(TreeNode root, int max) {
        if(root == null) {
            return 0;
        } else {
            int newMax = Math.max(max, root.val);
            int nodeCount = newMax == root.val ? 1: 0;
            return nodeCount + helper(root.left, newMax) + helper(root.right, newMax);
        }
    }
}
