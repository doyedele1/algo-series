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

    insert(data) {

        /* PSEUDOCODE FOR INSERT
            - Create a new node
            - Starting at the root
                - If the root is null, set the root to the new node
                - If there is a root, check if the value of the new node is greater than or less than the value of the root
                - If the value is greater than the value of the root
                    - Check to see if there is a node to the right
                        - If there is, move to that node and repeat these steps
                        - If there isn't, add that node as the right property
                - If the value is less than the value of the root
                    - Check to see if there is a node to the left
                        - If there is, move to that node and repeat these steps
                        - If there isn't, add that node as the left property
            - Return the entire tree
        */

        var newNode = new Node(data)

        if(!this.root) {
            this.root = newNode
            return this
        }

        var current = this.root;
        
        while(true) {
            if(data === current.data) return undefined

            if(data > current.data) {
                if(!current.right) {
                    current.right = newNode
                    return this
                }
                current = current.right
            } else {
                if(!current.left) {
                    current.left = newNode
                    return this
                }
                current = current.left
            }
        }
    }


    search(data) {

        /* PSEUDOCODE FOR SEARCH 
            - Starting at the root
                -Check to see if the root is null
                    - If the root is null, return false
                - If there is a root, check to see if the value of the root is equal to the value of the data
                    - If the values are equal, return true
                - If not, check to see if the value of the root is greater than or less than the value of the root
                    - If it is greater
                        - Check to see if there is a node to the right
                            - If there is, move to that node and repeat these steps
                            - If there is not, return false
                    - If it is less
                        - Check to see if there is a node to the left
                            - If there is, move to that node and repeat these steps
                            - If there is not, return false
        */
        if(!this.root) return false

        var current = this.root

        while(true) {
            if(data === current.data) return true

            if(data > current.data) {
                if(!current.right) return false
                current = current.right
            } else {
                if(!current.left) return false
                current = current.left
            }
        }
    }
}

// var tree = new BST()
// tree.root = new Node(10)
// tree.root.left = new Node(5)
// tree.root.right = new Node(13)
// tree.root.left.left = new Node(2)
// tree.root.left.right = new Node(7)
// tree.root.right.left = new Node(11)
// tree.root.right.right = new Node(16)