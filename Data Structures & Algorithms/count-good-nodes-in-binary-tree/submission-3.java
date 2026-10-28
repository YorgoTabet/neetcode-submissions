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
        return helper(root, root.val);
    }

    public int helper(TreeNode node, int max) {
        if(node == null) {
            return 0;
        } else {
            int newMax = Math.max(max, node.val);
            int nodeCount = newMax == node.val ? 1: 0;
            return nodeCount + helper(node.left, newMax) + helper(node.right, newMax);
        }
    }
}
