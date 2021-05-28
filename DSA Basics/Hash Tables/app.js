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
- Doesn't cluster outputs at specific indices, but distributes uniformly
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