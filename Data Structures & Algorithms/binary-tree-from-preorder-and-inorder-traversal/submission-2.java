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
    Map<Integer, Integer> indices = new HashMap<>();
    int preIndex = 0;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++){
            indices.put(inorder[i], i);
        }

        return helper(preorder, inorder, 0, preorder.length - 1);

    }

    public TreeNode helper(int[] preorder, int[] inorder, int l, int r) {
        if(r < l) return null;

        int currentRoot = preorder[preIndex++];
        int inIndex = indices.get(currentRoot);
        TreeNode root = new TreeNode(currentRoot);

        root.left = helper(preorder,inorder, l, inIndex- 1);
        root.right = helper(preorder,inorder, inIndex + 1, r);

        return root;

    }
}
