/*
    - No index
    - Connected via nodes with a next pointer
    - Random access is not allowed
    - Arrays (skyscrapers with elevators). Linked lists (skyscrapers with no elevators)
*/

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
        if(this.length === 1) {
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


    reverse() {
        /*  PSEUDOCODE FOR REVERSE
            - Swap the head and tail
            - Create a variable called next
            - Create a variable called previous
            - Create a variable called node and initialize it to the head property
            - Loop through the list
            - Set next to be the next property on whatever node is
            - Set the next property on the node to be whatever previous is
            - Set the previous to tbe value of the node variable
            - Set the node variable to be the value of the next variable
        */
        var node = this.head
        this.head = this.tail
        this.tail = node
        var next
        var previous = null
        for(var i = 0; i < this.length; i++) {
            next = node.next
            node.next = previous
            previous = node
            node = next
        }
        return this
    }

    // print() {
    //     var arr = []
    //     var current = this.head
    //     while(current) {
    //         arr.push(current.val)
    //         current = current.next
    //     }
    //     console.log(arr)
    // }
}

var list = new SinglyLinkedList()