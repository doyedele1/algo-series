'''
    - Greedy algorithm is an algorithm that makes a greedy (optimal) choice at every single step in the solution of the problem.
    - The greedy choice is defined by some rule.
    - Greedy Algorithm Properties (when to use a greedy algorithm to solve a problem)
        - Greedy choice property: A global (or overall) optimal solution can be reached by choosing the optimal choice at every step.
        - Optimal substructure: A problem has an optimal substructure if an optimal solution to the entire problem contains the optimal solutions to the sub-problems.
    - Examples: Fractional Knapsack Problem, Dijkstra's Algorithm, Minimum Spanning Tree (MST) Problem, etc.
'''

'''
    Greedy Approach for a fractional knapsack problem
        - Calculate the ratio (value/weight) of each item in the knapsack
        - Sort the items by the ratio in descending order
        - Take the item with the highest ratio and add them until we can't add the next item as whole
        - At the end, add the next item as much (fraction) as we can

    Algorithm Greedy(a, n):
    for i = 1 to n do:
        x = select(a)
        if feasible(x) then:
            solution = solution + x
'''