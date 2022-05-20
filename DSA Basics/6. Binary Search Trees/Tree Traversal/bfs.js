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

    BFS() {
        /* 
            Iterative steps
            - Create a queue and a variable to store the values of nodes visited
            - Place the root node in the queue
            - Loop as long as there is anything in the queue
                - Dequeue a node from the queue and push the value of the node into the variable that stores the nodes
                - If there is a left property on the node dequeued, push it into the queue
                - If there is a right property on the node dequeued, push it into the queue
            - Return the variable that stores the values of the nodes
        */
        let node = this.root
        let queue = []
        let visited = []

        queue.push(node)
        while(queue.length) {
            node = queue.shift()
            visited.push(node.data)
            if(node.left) queue.push(node.left)
            if(node.right) queue.push(node.right)
        }
        return visited
    }
}