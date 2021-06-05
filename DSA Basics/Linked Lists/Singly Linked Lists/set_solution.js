class Node {
    constructor(val) {
        this.val = val
        this.next = null
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null
        this.tail = null
        this.length = 0
    }

    get(index) {
        /*  PSEUDOCODE FOR GET
            - This function should accept an index
            - If the index is less than zero or greater than or equal to the length of the list, return null
            - Loop through the list until you reach the index and return the node at that specific index
        */

        if(index < 0 || index >= this.length) return null
        var count = 0
        var current = this.head
        while(count != index) {
            current = current.next
            count++
        }
        return current
    }

    set(index, val) {
        /*  PSEUDOCODE FOR SET
            - This function should accept an index and a value
            - Use the get function to find the specific node
            - If the node is not found, return false
            - If the node is found, set the value of that node to be the value passed to the function and return true
        */
        var foundNode = this.get(index)
        if(foundNode) {
            foundNode.val = val
            return true
        }
        return false
    }
}

var list = new SinglyLinkedList()