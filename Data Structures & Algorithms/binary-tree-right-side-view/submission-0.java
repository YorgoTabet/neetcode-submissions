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
    public List<Integer> rightSideView(TreeNode root) {
        if(root == null) return new ArrayList<>();
        Queue<TreeNode> queue = new ArrayDeque<>();
        List<Integer> res = new ArrayList<>();

        queue.offer(root);
    
        while(!queue.isEmpty()){
            int iterations = queue.size();

            for (int i = 0; i < iterations ; i++){
                TreeNode node = queue.poll();
                if(node.left != null) queue.offer(node.left);
                if(node.right != null) queue.offer(node.right);
                
                if(i == iterations - 1) res.add(node.val);
            }
        
        }

        return res;
    }
}
