let validAnagram = function(s, t) {
    if(s.length !== t.length) {
        return false
    }
    
    let freqCounter = {}
    
    for(let i = 0; i < s.length; i++) {
        if(freqCounter[s[i]] > 0) {
            freqCounter[s[i]]++
        }
        else {
            freqCounter[s[i]] = 1
        }
    }
    
    for(let i = 0; i < t.length; i++) {
        if(!(freqCounter[t[i]])) {
            return false
        }
        else {
            freqCounter[t[i]] -= 1
        }
    }
    return true
    
};
    

validAnagram("anagram","nagaram") // return true
validAnagram("cat", "tac") // return true
validAnagram("listen", "silent") // return true
validAnagram("program", "function") // return false