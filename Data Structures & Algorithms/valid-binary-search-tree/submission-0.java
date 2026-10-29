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
        return dfs(root, new int[] {Integer.MIN_VALUE, Integer.MAX_VALUE});
    }

    public boolean dfs(TreeNode node, int[] brackets) {
        if (node == null) {
            return true;
        }
        int lowerBracket = brackets[0];
        int upperBracket = brackets[1];

        boolean isNodeValid = node.val > lowerBracket && node.val < upperBracket;
        int[] nextLeftBracket = new int[] {lowerBracket, Math.min(upperBracket, node.val)};
        int[] nextRightBracket = new int[] {Math.max(lowerBracket, node.val), upperBracket};
        return isNodeValid && dfs(node.left, nextLeftBracket) && dfs(node.right, nextRightBracket);
    }
}
