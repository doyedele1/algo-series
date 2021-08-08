class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BST {
    constructor() {
        this.root = null;
    }

    insert(data) {
    /** PSEUDOCODE FOR INSERT
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
     **/
        
    }
}

var tree = new BST();
tree.root = new Node(10);
tree.root.left = new Node(5);
tree.root.right = new Node(13);
tree.root.left.left = new Node(2);
tree.root.left.right = new Node(4);
tree.root.right.left = new Node(14);
tree.root.right.right = new Node(16);