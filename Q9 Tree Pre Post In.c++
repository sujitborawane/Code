#include <stdio.h>
#include <stdlib.h>
struct Node {
    int key;
    struct Node* left;
    struct Node* right;
};
struct Node* newNode(int item) {
    struct Node* temp = (struct Node*) malloc(sizeof(struct Node));
    temp->key = item;
    temp->left = temp->right = NULL;
    return temp;
}
struct Node* insert(struct Node* node, int key) {
    if (node == NULL) {
        return newNode(key);
    }
    if (key < node->key) {
        node->left = insert(node->left, key);
    } else if (key > node->key) {
        node->right = insert(node->right, key);
    }
    return node;
}
void inorder(struct Node* root) {
    if (root != NULL) {
        inorder(root->left);  
        printf("%d ", root->key); 
        inorder(root->right); 
    }
}
void preorder(struct Node* root) {
    if (root != NULL) {
        printf("%d ", root->key);  
        preorder(root->left); 
        preorder(root->right);
    }
}
void postorder(struct Node* root) {
    if (root != NULL) {
        postorder(root->left);  
        postorder(root->right); 
        printf("%d ", root->key); 
    }
}
int main() {
    struct Node* root = NULL;
    int n, i,  value;
    printf("Enter the number of elements to insert into the BST: ");
    scanf("%d", &n);
    printf("Enter %d elements: \n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &value);
        root = insert(root, value);
    }
    printf("\nIn-order Traversal: ");
    inorder(root);
    printf("\n");
	printf("Pre-order Traversal: ");
    preorder(root);
    printf("\n");
    printf("Post-order Traversal: ");
    postorder(root);
    printf("\n");
    return 0;
}

