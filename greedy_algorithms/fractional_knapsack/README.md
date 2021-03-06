# Fractional Knapsack Problem

## Problem Description
### Task.
The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
### Input Format. 
The first line of the input contains the number π of items and the capacity π of a knapsack.
The next π lines define the values and weights of the items. The π-th line contains integers π£π and π€πβthe
value and the weight of π-th item, respectively

### Output Format. 
Output the maximal value of fractions of items that fit into the knapsack. The absolute
value of the difference between the answer of your program and the optimal value should be at most
10β3
. To ensure this, output your answer with at least four digits after the decimal point (otherwise
your answer, while being computed correctly, can turn out to be wrong because of rounding issues).

### Constraints. 
1 β€ π β€ 103 , 0 β€ π β€ 2 Β· 106 ; 0 β€ π£π β€ 2 Β· 106 , 0 < π€π β€ 2 Β· 106 for all 1 β€ π β€ π.  All the
numbers are integers.

## Sample 1.
### Input:
3 50  
60 20   
100 50    
120 30

### Output:
180.0000
### Explanation
To achieve the value 180, we take the first item and the third item into the bag.

## Sample 2.
### Input:
1 10  
500 30
### Output:
166.6667
### Explanation
Here, we just take one third of the only available item.