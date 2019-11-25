#include <stdio.h>

/*二叉树结构定义*/
typedef struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
} BiNode, *LinkNode, *BiTree;

/*二叉树转双链表*/
void BST2DLL(BiNode *root, LinkNode *tail) {
    if (root == NULL)
        return;

    /*将左子树转为双链表*/
    if (root->left)
        BST2DLL(root->left, tail);

    /*将左子树转化的双链表与根节点相连*/
    root->left = *tail;
    if (*tail)
        (*tail)->right = root;

    /*更新tail信息*/
    *tail = root;

    /*将右子树转为双链表并连接*/
    if (root->right)
        BST2DLL(root->right, tail);
}

/*求中位数*/
void Median(BiTree tree) {
    /*中序遍历，构建双链表*/
    LinkNode tail = NULL;
    BST2DLL(tree, &tail);

    /*非空判断*/
    if (tail == NULL) {
        printf("BST is NULL");
        return;
    }

    /*快慢指针，求中位数*/
    LinkNode fast = tail;
    LinkNode slow = tail;
    while (fast != NULL) {
        if (fast->left == NULL) {
            printf("median is %d", slow->val);
            return;
        }
        else if (fast->left != NULL && fast->left->left == NULL) {
            printf("median is %d", (slow->val + slow->left->val) / 2);
            return;
        }
        else {
            fast = fast->left->left;
            slow = slow->left;
        }
    }
}

int main() {
    BiNode node1, node2, node3, node4;

    node1.val = 10;
    node1.left = &node2;
    node1.right = &node3;

    node2.val = 6;
    node2.left = &node4;
    node2.right = NULL;

    node3.val = 14;
    node3.left = NULL;
    node3.right = NULL;

    node4.val = 4;
    node4.left = NULL;
    node4.right = NULL;

    Median(&node1);

    return 0;
}



