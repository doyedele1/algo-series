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

    push(val) {
        /*  PSEUDOCODE FOR PUSH
            - This function accepts a value
            - Create a new node using the value passed to the function
            - If there is no head property on the list, set the head and tail to be the newly created node
            - Otherwise set the next property on the tail to be the new node and set the tail property on the list to be the newly created node
            - Increment the length by one
            - Return the linked list
        */
        var newNode = new Node(val)
        if(!this.head) {
            this.head = newNode
            this.tail = this.head
        } 
        else {
            this.tail.next = newNode
            this.tail = newNode
        }
        this.length++
        return this
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
}

var list = new SinglyLinkedList()

