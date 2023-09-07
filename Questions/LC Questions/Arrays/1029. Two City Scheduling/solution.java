/*
    Explanation:
        - We have to pick equal number of cities A and B
        Initially,
        - Can we see if we can send all candidates to city A?
        - Now, which of the candidates can we send to B? We will pick the candidate for which we gained the maximum (the most negative number)
        
        --> (A-B) = by sending person to city A, the company would lose A-B

        [[10,20],[30,200],[400,50],[30,20]]
        -10, -170, 350, 10
        Sorting returns (-170, -10, 10, 350)

        
        TC - O(nlogn) because of sorting the input array
        SC - O(logn). Quick Sort algorithm is used in Java
 */

class Solution {
    public int twoCitySchedCost(int[][] costs) {
      Arrays.sort(costs, new Comparator<int[]>() {
        @Override
        public int compare(int[] o1, int[] o2) {
          return o1[0] - o1[1] - (o2[0] - o2[1]);
        }
      });
  
      int res = 0;
      int n = costs.length / 2;
      for (int i = 0; i < n; ++i) res += costs[i][0] + costs[i + n][1];
      return res;
    }
}