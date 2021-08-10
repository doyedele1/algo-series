class Node {
    constructor(data) {
        this.data = data
        this.left = null
        this.right = null
    }
}

class BST {
    constructor() {
        this.root = null
    }

    dfsPreOrder() {
        /* 
            Recursive steps
            - Create a variable to store the values of nodes visited
            - Store the root of the BST in a variable called current
            - Write a helper function which accepts a node
                - Push the values of the node to the variable that stores the values
                - If the node has a left child, call the helper function with the left child on the node
                - If the node has a right child, call the helper function with the right child on the node
            - Invoke the helper function with the current variable
            - Return the array of values
        */
        let values = []
        let current = this.root
        function helper(node) {
            values.push(node.data)
            if(node.left) helper(node.left)
            if(node.right) helper(node.right)
        }
        helper(current)
        return values
    }

    dfsPostOrder() {
        /* 
            Recursive steps
            - Create a variable to store the values of nodes visited
            - Store the root of the BST in a variable called current
            - Write a helper function which accepts a node
                - If the node has a left child, call the helper function with the left child on the node
                - If the node has a right child, call the helper function with the right child on the node
                - Push the values of the node to the variable that stores the values
            - Invoke the helper function with the current variable
            - Return the array of values
        */

        let values = []
        let current = this.root
        function helper(node) {
            if(node.left) helper(node.left)
            if(node.right) helper(node.right)
            values.push(node.data)
        }
        helper(current)
        return values
    }

    dfsInOrder() {
        /* 
            Recursive steps
            - Create a variable to store the values of nodes visited
            - Store the root of the BST in a variable called current
            - Write a helper function which accepts a node
                - If the node has a left child, call the helper function with the left child on the node
                - Push the values of the node to the variable that stores the values
                - If the node has a right child, call the helper function with the right child on the node
            - Invoke the helper function with the current variable
            - Return the array of values
        */

        let values = []
        let current = this.root
        function helper(node) {
            node.left && helper(node.left)
            values.push(node.data)
            node.right && helper(node.right)
        }
        helper(current)
        return values
    }
}