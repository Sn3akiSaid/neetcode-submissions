/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 // Overloaded constructors - take whichever version is called
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */


 // TreeNode is an object where each integer value val has a representative left or right state
 // initial value is central - no left or right
 // subsequent values accrue their 

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {

        // Check if current node final (leaf)
        if (!root) return nullptr;
        
        // swaps the dereferenced pointers currently stored in each dereferenced pointer
        swap(root->left, root->right);
        
        // recursive call setting left node as root
        invertTree(root->left);
        // recursive call setting right node as root
        invertTree(root->right);

        return root;
    }
};
