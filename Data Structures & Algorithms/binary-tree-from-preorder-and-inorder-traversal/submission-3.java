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
    int preIdx = 0;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++){
            indices.put(inorder[i], i);
        }

        return helper(preorder, inorder, 0, preorder.length - 1);

    }

    public TreeNode helper(int[] preorder, int[] inorder, int l, int r) {
        if(r < l) return null;

        int rootVal = preorder[preIdx++];
        int inRootIdx = indices.get(rootVal);
        TreeNode root = new TreeNode(rootVal);

        root.left = helper(preorder,inorder, l, inRootIdx- 1);
        root.right = helper(preorder,inorder, inRootIdx + 1, r);

        return root;

    }
}
