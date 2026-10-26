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
    private TreeNode answer;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        answer = new TreeNode();

        helper(root, p, q);

        return answer;
    }
    private boolean helper(TreeNode node, TreeNode p, TreeNode q) {
        if (node == null)
            return false;
        boolean found = node.val == p.val || node.val == q.val;

        boolean foundInLeft = helper(node.left, p, q);
        boolean foundInRight = helper(node.right, p, q);

        boolean inChildren = foundInLeft && foundInRight;

        if (inChildren || (found && (foundInLeft || foundInRight))) {
            answer = node;
        }
        return foundInLeft || foundInRight || found;
    }
}
