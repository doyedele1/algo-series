/* 

Hash tables or hash maps are used to store key-value pairs.

They are like arrays, but the keys are not ordered.

Unlike arrays, hash tables are fast for all of the following operations:
    finding values,
    adding new values,
    removing values

Python has Dictionaries. JS has Objects and Maps, Java, Go & Scala have Maps, Ruby has Hashesx.

What makes a good hash?
- Fast (constant time)
- Doesn't cluster outputs at specific indices, but distributes keys uniformly
- Deterministic (same input yields same output)

*/

// HASH FUNCTION
function hash(key, arrayLen) {
    let total = 0

    for(let char of key) {
        // map "a" to 1, "b" to 2, "c" to 3, etc.
        let value = char.charCodeAt(0) - 96
        total = (total + value) % arrayLen
    }
    return total
}

hash("pink", 10) // 0
hash("orangered", 10) // 7
hash("cyan", 10) // 3

// IMPROVED HASH FUNCTION
function hash(key, arrayLen) {
    let total = 0
    let WEIRD_PRIME = 3
    for(let i = 0; i < Math.min(key.length, 100); i++) {
        let char = key[i]
        let value = char.charCodeAt(0) - 96
        total = (total * WEIRD_PRIME + value) % arrayLen
    }
    return total
}

/* DEALING WITH COLLISIONS

- Separate Chaining - use a nested array or linked lists to store the values at each index in the array.
Here, we can store multiple key-value pair at each index.

- Linear Probing - when we find a collision, we search through the array to find the next empty slot
Here, we store a single key-value at each index.

*/

// A HASH TABLE CLASS
class HashTable {
    constructor(size = 53) {
        this.keyMap = new Array(size)
    }

    _hash(key) {
        let total = 0
        let WEIRD_PRIME = 31
        for(let i = 0; i < Math.min(key.length, 100); i++) {
            let char = key[i]
            let value = char.charCodeAt(0) - 96
            total = (total * WEIRD_PRIME + value) % this.keyMap.length;
        }
        return total
    }

    /* SET METHOD
    - Accepts a key and a value
    - Hashes the key
    - Stores the key-value pair in the hash table array via separate chaining
    */
    set(key, value) {
        let index = this._hash(key)
        if(!this.keyMap[index]) {
            this.keyMap[index] = []
        }
        this.keyMap[index].push([key, value])
    }

    /* GET METHOD
    - Accepts a key
    - Hashes the key
    - Retrieves the key-value pair in the hash table
    - If the key isn't found, return undefined
    */
    get(key) {
        let index = this._hash(key)
        if(this.keyMap[index]) {
            for(let i = 0; i < this.keyMap[index].length; i++) {
                if(this.keyMap[index][i][0] === key) {
                    return this.keyMap[index][i][1]
                }
            }
        }
        return undefined
    }

    /* KEYS METHOD
    - Loops through the hash table array and returns an array of keys in the table
    */
    keys() {
        let keysArr = []
        for(let i = 0; i < this.keyMap.length; i++) {
            if(this.keyMap[i]) {
                for(let j = 0; j < this.keyMap[i].length; j++) {
                    if(!keysArr.includes(this.keyMap[i][j][0])) {
                        keysArr.push(this.keyMap[i][j][0])
                    }
                }
            }
        }
        return keysArr
    }

    /* VALUES METHOD
    - Loops through the hash table array and returns an array of values in the table
    */
    values() {
        let valuesArr = []
        for(let i = 0; i < this.keyMap.length; i++) {
            if(this.keyMap[i]) {
                for(let j = 0; j < this.keyMap[i].length; j++) {
                    if(!valuesArr.includes(this.keyMap[i][j][1])) {
                        valuesArr.push(this.keyMap[i][j][1])
                    }
                }
            }
        }
        return valuesArr
    }
}

let ht = new HashTable(17)
ht.set("maroon", "#800000")
ht.set("yellow", "#FFFF00")
ht.set("olive", "#808000")
ht.set("salmon", "#FA8072")
ht.set("lightcoral", "#F08080")
ht.set("mediumvioletred", "#C71585")

// for duplicate data
ht.set("plum", "#DDA0DD")
ht.set("purple", "#DDA0DD")
ht.set("violet", "#DDA0DD")

ht.get("olive")

ht.values()
ht.keys()

/* BIG O of Hash Tables
    Average case
        - Insert: O(1)
        - Deletion: O(1)
        - Access: O(1)
        - Searching for a key: 0(1)
        - Searching for a value: 0(n)
*/