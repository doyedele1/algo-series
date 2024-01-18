let flipAndInvertImage = function(image) {
    
    for (img of image) {
        flipImage(img);
        invertImage(img);
    }
    
    return image;
    
};

let flipImage = function(arr) {
    let start = 0;
    let end = arr.length - 1;

    while (start < end) {
        temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;

        start++;
        end--;
    }
};


let invertImage = function(arr) {
    for (let i = 0; i < arr.length; i++) {
        arr[i] ^= 1;
    }
};

// flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])