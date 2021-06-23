/* 
    - Popping and reversing are much easier with doubly linked lists compared to singly linked lists
    - More memory is used up in doubly linked lists
*/

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

    push(val) {
        /* 
            - Create a new node with the value passed to the function
            - If the head property is null, set the head and tail to be the newly created node
            - If not, set the next property on the tail to be the new node
            - Set the previous property on the new node to be the old tail
            - Set the tail to be the new node
            - Increment length by one
            - Return the list
        */

        var newNode = new Node(val)
        if(this.length === 0) {
            this.head = newNode
            this.tail = newNode
        }

        else {
            this.tail.next = newNode
            newNode.prev = this.tail
            this.tail = newNode
        }
        this.length++
        return this
    }
}

