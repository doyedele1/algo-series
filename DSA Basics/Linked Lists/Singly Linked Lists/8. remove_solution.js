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

    pop() {
        /*  PSEUDOCODE FOR POP
            - If there are no nodes in the list, return undefined
            - Loop through the list until you reach the tail
            - Set the next property of the 2nd to last node to be null
            - Set the tail to be the 2nd to last node
            - Decrement the length of the list by 1
            - Return the values of the node removed
        */
        if(!this.head) return undefined
        
        var current = this.head
        var newTail = current
        while(current.next) {
            newTail = current
            current = current.next
        }
        this.tail = newTail
        this.tail.next = null
        this.length--
        if(this.length === 0) {
            this.head = null
            this.tail = null
        }
        return current
    }

    shift() {
        /*  PSEUDOCODE FOR SHIFT
            - If there are no nodes, return undefined
            - Store the current head property in a variable
            - Set the head property to be the current head's next property
            - Decrement the length by 1
            - Return the value of the node removed
        */
        if(!this.head) return undefined
        var currentHead = this.head
        this.head = currentHead.next
        this.length--
        if(this.length === 0) {
            this.tail = null
        }
        return currentHead
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

    remove(index) {
        /*  PSEUDOCODE FOR REMOVE
            - This function accepts an index
            - If the index is less than zero or greater than the length, return undefined
            - If the index is the same as the length - 1, pop
            - If the index is 0, shift
            - Otherwise, using the get method, access the node at the index - 1
            - Set the next property on that node to be the next of the next node
            - Decrement the length by one
            - Return the value of the node removed
        */
        if(index < 0 || index > this.length) return undefined
        if(index === this.length - 1) return !!this.pop()
        if(index === 0) return !!this.shift()
        var previousNode = this.get(index - 1)
        var removed = previousNode.next
        previousNode.next = removed.next
        this.length--
        return removed
    }
}

var list = new SinglyLinkedList()