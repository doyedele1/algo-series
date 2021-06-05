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

    unshift(val) {
        /*  PSEUDOCODE FOR UNSHIFT
            - The function should accept a value
            - Create a new node using the value passed to the function
            - If there is no head property on the list, set the head and tail to be the newly created node
            - Otherwise set the newly created node's next property to be the current head property on the list
            - Set the head property on the list to be that newly created node
            - Increment the length of the list by 1
            - Return the linked list
        */
        var newNode = new Node(val)
        if(!this.head) {
            this.head = newNode
            this.tail = this.head
        }
        else {
            newNode.next = this.head
            this.head = newNode
        }
        this.length++
        return this
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


    insert(index, val) {
        /*  PSEUDOCODE FOR INSERT
            - If the index is less than zero or greater than the length, return false
            - If the index is the same as the length, push a new node to the end of the list
            - If the index is 0, unshift a new node to the start of the list
            - Otherwise, using the get method, access the node at the index - 1
            - Set the next property on that node to be the new node
            - Set the next property on the new node to be the previous next
            - Increment the length
            - Return true
        */
        if(index < 0 || index > this.length) return false
        if(index === this.length) return !!this.push(val)
        if(index === 0) return !!this.unshift(val)
        var newNode = new Node(val)
        var previous = this.get(index - 1)
        var temp = previous.next
        previous.next = newNode
        newNode.next = temp
        this.length++
        return true
    }
}

var list = new SinglyLinkedList()