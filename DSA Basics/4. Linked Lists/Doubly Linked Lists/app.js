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
        if(!this.head) {
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
            poppedNode.prev = null
        }
        this.length--
        return poppedNode
    }


    shift() {
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
            poppedNode.prev = null
        }
        this.length--
        return poppedNode
    }
}

