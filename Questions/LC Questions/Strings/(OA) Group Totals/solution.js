function groupTotals(strArr) {

    const map = new Map();

    for(const elem of strArr) {
        let key = elem.slice(0, 1);
        let value = elem.slice(2);
        
        if (!map.has(key)) {
            map.set(key, 0);
        }
        map.set(key, +map.get(key) + +value);
    }

    let answer = "";
    answer = [...map].sort().reduce((acc, elem) => {
        if (elem[1] != 0) {
            acc = acc + elem[0] + ":" + elem[1] + ",";
            return acc;
        }
        return acc;
    }, "").slice(0, -1);
    return answer;
}

// console.log(groupTotals(["X:-1", "Y:1", "X:-4", "B:3", "X:5"]));