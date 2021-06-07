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