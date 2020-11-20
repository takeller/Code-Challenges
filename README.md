#### The purpose of this repo is to organize code challenges I complete. Each challenge with have the original problem statement, a link to the test file, and a link to my solution. 

<details>
  <summary>Directions Reducer</summary>
  
   #### Problem Statement: 
   `Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).`  
    
    
   [Tests](fake link)    
   [Solution](https://github.com/takeller/Code-Challenges/blob/main/directions/directions_reducer.js)
</details>

<details>
  <summary>String Compression</summary>
      
   #### Problem Statement: 
   `Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the 'compressed' string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters.`   
    
    
   [Tests](https://github.com/takeller/Code-Challenges/blob/main/string_compression/test_string_compression.py)    
   [Solution](https://github.com/takeller/Code-Challenges/blob/main/string_compression/string_compression.py)
</details>

<details>
  <summary>Payload Target</summary>
      
   #### Problem Statement: 

Write a method that takes two parameters, payload and target. Search through a payload of unique integer values (positive, negative, or 0) to find any two numbers that add together to equal the target (which could also be positive or negative or 0).

When you find a set of numbers that add up to your target value, you can stop processing.

If found, return an array of those two values, otherwise return an empty array if no matching values are found.

For example, if your payload of numbers contained a 10 and a 5 you could return those numbers if your target was 15. Likewise, if you had -3 and 18, those would also add together to be a target of 15.

Be careful that you don't find the same number twice in your payload; for example if your payload contains a 4 and your target is 8, your answer should not indicate that it found 4 twice.

Solve this any way you can, then optimize to run in O(n) time and 1x space complexity.

    
    
   [Tests](Fake Link)    
   [Solution](https://github.com/takeller/Code-Challenges/blob/main/payload_target/payload_target.rb)
</details>

<details>
  <summary>Persistence</summary>
      
   #### Problem Statement: 
   `Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the 'compressed' string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters.`   
    
    
   [Tests](https://github.com/takeller/Code-Challenges/blob/main/persistence/test_persistence.py)    
   [Solution](https://github.com/takeller/Code-Challenges/blob/main/persistence/persistence.py)
</details>

<details>
  <summary>Roman Numeral To Integer</summary>
      
   #### Problem Statement: 
   `Write a recursive function that converts an integer into a string such that the number is represented in Roman Numerals in the most efficient way.
eg, the number 4 could be written as 'IIII' but it's more efficient to use 'IV' since that's a shorter string
Assume no number is greater than 4,000
Here are the Roman Numeral equivalents you'll need to know:
M=1000, CM=900, D=500, CD=400,
C=100, XC=90, L=50, XL=40,
X=10, IX=9, V=5, IV=4, I=1 `  
    
    
   [Tests](Fake Link)    
   [Solution](https://github.com/takeller/Code-Challenges/blob/main/roman_to_integer/recursion_challenge.rb)
</details>

<details>
  <summary>Snail</summary>
      
   #### Problem Statement: 
   `Given an n x n array, write a method that returns the array elements arranged from outermost elements to the middle element, traveling clockwise.`
   ```ruby
const array_matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

snail(array_matrix) 
#=> [1, 2, 3, 6, 9, 8, 7, 4, 5]
```
   [Tests](Fake Link)    
   [Solution](https://github.com/takeller/Code-Challenges/blob/main/snail/snail_challenge.rb)
</details>

<details>
  <summary>Equal Sides of an Array</summary>
      
   #### Problem Statement: 
   ```You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

For example:

Let's say you are given the array {1,2,3,4,3,2,1}: Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}: Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

Last one:
You are given the array {20,10,-80,10,10,15,35}
At index 0 the left side is {}
The right side is {10,-80,10,10,15,35}
They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
Index 0 is the place where the left side and right side are equal.

Note: Please remember that in most programming/scripting languages the index of an array starts at 0.

Input:
An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

Output:
The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.

Note:
If you are given an array with multiple answers, return the lowest correct index.
```
   [Tests](https://github.com/takeller/Code-Challenges/blob/main/equal_sides_of_an_array/test_equal_sides.py)    
   [Solution](https://github.com/takeller/Code-Challenges/blob/main/equal_sides_of_an_array/equal_sides.py)
</details>

<details>
  <summary>Greed is Good</summary>
      
   #### Problem Statement: 
   ```Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
In some languages, it is possible to mutate the input to the function. This is something that you should never do. If you mutate the input, you will not be able to pass all the tests.
```
   [Tests](https://github.com/takeller/Code-Challenges/blob/main/equal_sides_of_an_array/test_equal_sides.py)    
   [Solution](https://github.com/takeller/Code-Challenges/blob/main/equal_sides_of_an_array/equal_sides.py)
</details>
