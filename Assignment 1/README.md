# Assignment 1

# Insertion Sort

## General Complexity

Insertion Sort can be thought of as playing a card game. Assume we have a dealer has a deck [7, 2, 4, 9, 6]. Every time you get a card you, you need to insert it in the right position.

First, you get 7, you keep it, then you get 2, and you insert it before 7, then you get 4, and you insert it between 2 and 7, and so on till everything is sorted. Every time you get a card, you insert it in the right position.

7 is the first item we assume its in the right position. Next item is 2, for that we look at all the items we&#39;ve seen so far (7), and check if they are greater than 2, then shift them to the right to make space for 2. To do this, we store 2 in a temporary variable, and store 7 in the position of 2. Our deck now becomes [7, 7, 4, 9, 6]. And then we store the temporary variable (2) at the original position of 7. Now our deck becomes [2, 7, 4, 9, 6]. For every step, we pick one item from the unsorted part of the array and insert it at the correct position of the sorted part.

## Big O

We need to iterate over the input array and read one item at a time  Best and worst cast  O(n)

Then we need to iterate over the items that we&#39;ve sorted and shift them if required  Best case (if items are already sorted)  O(1), worst case (array sorted in descending order)  O(n)

Time complexity  Best case **O(n)**

Time complexity  Worst case **O(n****2****)**

## Complexity Classification

**Linear** , for the best case, and **Quadratic** for the worst case. The complexity classification is **P** because the algorithm can solve the decision problem in polynomial time.

# Traveling Salesman Problem

## General Complexity

The Traveling Salesman Problem is essentially finding the shortest route to visit a number of locations ones from an origin and return to said origin. There are several solutions to this problem, and they range from **exact** solutions (which provide a globally optimal path exists for a small number of cities but as cities grow, the computation time grows faster) to **approximate** solutions (which trades a little bit of distance for less computation time).

For this solution, we start by selecting a node to be the starting node (S). Then, we store the optimal value from S to every other node. Doing this solves paths with exactly 2 nodes. We would need to save the set of visited nodes, and the last visited node. Then we would expand to visit all other unvisited nodes from the last visited node getting the minimum cost.

## Big O

First approach is using the brute force method, where you have to compute or visit every possible node or city. This means that we have to try all possible permutations of node orderings and see which gives the minimum weight **O(n!).**

Using Dynamic programming, the time complexity is exponential because there are exponential number of subsets O(2n) and for each subset we are going through every vertex and we&#39;re checking what should be the vertex before that vertex O(2n)  Doing this gives us a time complexity of **O(n****2 ****2**** n****)**.

## Complexity Classification

The complexity classification is **NP Hard** because it&#39;s almost impossible to solve in polynomial time and it is at least as hard as the hardest problem in NP.

# Finding the Sum of all Values in a 3-D Array

## General Complexity

A 3-D array has an array withing an array within an array. To find the sum of all the values in a 3d array, we would need to traverse all the elements in the array.

## Big O

Since we need to traverse all the elements in the 3d array, we would need to have 3 nested loops which gives us a time complexity of O(n3)

## Complexity Classification

Since our big O is O(n3) our classification name is going to be cubic. The complexity classification is **P** because the algorithm can solve the decision problem in polynomial time.

# Radix Sort

## General Complexity

Radix sort can only be used to count numbers. If we are dealing with unsorted numbers then we know that there are 10 digits from 0 to 9, so we&#39;ll need 10 buckets for sort the numbers from the least significant digit to the most significant digit. Counting sort is used as a subroutine to sort. First, find the number with the largest number of digits, if there are N digits in the biggest number then we will need to perform N iterations. The remaining numbers in the array will be padded with leading zeros so they all have N digits. Then take the 10 buckets 0-9 and sort the numbers using the least significant digit to the most significant digit. After sorting is complete, the leading zeros will be removed, and your array will be sorted.

## Big O

To get the complexity of the Radix sort, we gave to factor in the complexity of the counting sort. Counting sort has a linear time complexity of O(n+k) where k is the range of keys from 1 to k and in worse case of O(n2) when elements are in range of 1 to n2. For Radix sort, we&#39;ll need to define some variables: n = length of the array, d = number of digits, b = number representation (e.g., base 10). Each step-in radix sort takes O(n+b), and that needs to be repeated d times (for the number of digits). Which makes the time complexity **O(d(n+b))**. One more thing to note is that the value of b can come down to making a tradeoff between time and space because the larger value we choose for b, the more space is required for the counting sort step and at the same time a larger b would imply a smaller d, which would take less time to sort the array.

## Complexity Classification

The classification name is **linear**. The complexity classification is **P** because the algorithm can solve the decision problem in polynomial time.

# Brute Force Password Cracker

## General Complexity

A brute force password cracker looks through all possible combinations of password. I use itertools.product() to loop through every combination of letters and numbers of fixed string length. Itertools product finds the Cartesian product which is the set of all combinations of elements from multiple sets. Adding repeat argument makes it possible to check variable length of passwords not just 2. First, a loop is used to iterate over the range of the password length (i); inside that loop, there&#39;s going to be another loop that iterates over all possible combinations of numbers and letters with length i till we find the password match.

## Big O

Finding the big O of this is a bit complicated because I&#39;m not sure about the computation that goes into the itertools product. Since I know what the output is supposed to look like, since we are looking for all possible combinations of length of 1 (A-Z or a-z or 0-9 = 26+26+10 = 62) to length of p. E.x. let&#39;s assume password is &#39;pass&#39;: 62 \* 62 \* 62 \* 62 = 624 or 62n. where n is the password length

In summary the time complexity would be the product of the two loops, which is equal to O(n\*62n)

## Complexity Classification

The classification name of this is going to be **exponential**. The complexity classification is **NP** because it is a decision problem that can be verified in polynomial time and the total possible outcomes is very large.

# Video Link URL

https://youtu.be/0rJPH4tpm7c