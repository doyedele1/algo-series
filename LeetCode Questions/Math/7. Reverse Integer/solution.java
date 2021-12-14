class Solution {
    public int reverse(int x) {
        int result = 0;
        int prev = 0;
        
        while(x != 0) {
            int pop = x % 10;
            x = x / 10;
            
            result = result * 10 + pop;
            
            if((result - pop) / 10 != prev) return 0;
            prev = result;
        }
        return result;
//  Explanation

//  First iteration - 123
//  pop = 123 % 10 = 3
//  x = 123 // 10 = 12
//  result = 3
//  prev = 3

// Second iteration
//  pop = 12 % 10 = 2
//  x = 12 // 10 = 1
//  result = 32
//  prev = 32
    }
}