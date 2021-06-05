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

    /*  PSEUDOCODE FOR SHIFT
            - If there are no nodes, return undefined
            - Store the current head property in a variable
            - Set the head property to be the current head's next property
            - Decrement the length by 1
            - Return the value of the node removed
    */
    shift() {
        if(!this.head) return undefined
        var currentHead = this.head
        this.head = currentHead.next
        this.length--
        if(this.length === 0) {
            this.tail = null
        }
        return currentHead
    }
}

var list = new SinglyLinkedList()