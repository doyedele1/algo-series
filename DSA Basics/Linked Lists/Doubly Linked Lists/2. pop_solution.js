class Node {
    constructor(val) {
        this.val = val
        this.prev = null
        this.next = null
    }
}

class DoublyLinkedList {
    constructor() {
        this.head = null
        this.tail = null
        this.length = 0
    }

    pop() {
        /* 
            - If there is no head, return undefined
            - Store the current tail in a variable to return it later
            - If the length is 1, set the head and tail to be null
            - Update the tail to be the previous node
            - Set the new tail's next to null
            - Decrement length by one
            - Return the value removed
        */

        if(!this.head) return undefined
        
        poppedNode = this.tail

        if(this.length === 1) {
            this.head = null
            this.tail = null
        }
        else {
            this.tail = poppedNode.prev
            this.tail.next = null
        }
        this.length--
        return poppedNode
    }
}

