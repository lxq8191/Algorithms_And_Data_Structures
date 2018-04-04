/**
public class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }

}
*/
public class Solution {
    public int TreeDepth(TreeNode root) {
        int depth = 0; 
        if(root==null) return 0;
        else{
            return 1+(TreeDepth(root.left)>TreeDepth(root.right)?TreeDepth(root.left):TreeDepth(root.right));
        }
    }
}