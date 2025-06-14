// TC: O(n), SC: O(n) where n is the number of digits in num
class Solution {
    public int minMaxDifference(int num) {
        String s = String.valueOf(num);

        // For MAX, replace the first non-9 digit with 9
        String maxVal = s;
        for (char digit : s.toCharArray()) {
            if (digit != '9') {
                maxVal = s.replace(digit, '9');
                break;
            }
        }

        // For MIN, replace the very first digit with 0
        char digitToChange = s.charAt(0);
        String minVal = s.replace(digitToChange, '0');

        return Integer.parseInt(maxVal) - Integer.parseInt(minVal);
    }
}