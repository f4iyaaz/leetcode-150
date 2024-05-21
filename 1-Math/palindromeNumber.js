/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    num = x.toString()
    let arr = num.split("")
    if((arr.length % 2) != 0) {
        let p1 = ""
        let p2 = ""
        mid = Math.floor(arr.length / 2)
        for(let i = 0; i <= mid; i++) {
            p1 += arr[i]
        }
        for(let i = arr.length-1; i >= mid; i--) {
            p2 += arr[i]
        }
        if(p1 == p2) {
            return true
        }
        else {
            return false
        }
    }
    else {
        mid = arr.length / 2
        let p3 = ""
        let p4 = ""
        for(let i = 0; i < mid; i++) {
            p3 += arr[i]
        }
        for(let i = arr.length-1; i >= mid; i--) {
            p4 += arr[i]
        }
        if(p3 == p4) {
            return true
        }
        else {
            return false
        }
    }
};

console.log(isPalindrome(10))