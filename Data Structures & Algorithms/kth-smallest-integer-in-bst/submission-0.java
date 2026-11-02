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
    private int counter = 0;
    private int res = Integer.MIN_VALUE;

    public int kthSmallest(TreeNode root, int k) {
        helper(root, k);

        return res;
    }

    private void helper(TreeNode node, int k) {
        if (node == null) {
            return;
        }

        helper(node.left, k);
        counter++;
        if (counter == k) {
            res = node.val;
            return;
        }
        helper(node.right, k);
    }
}
