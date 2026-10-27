# Q1. Find the Frequency of Each Word in a Sentence

from solutions import word_frequency

# Given input
sentence1 = "python is easy and python is powerful"
print(word_frequency(sentence1))

# Q2. Find the Frequency of Each Character in a Word

from solutions import char_freq

#Given input

sentence1 = "banana"
print(char_freq(sentence1))

# Q3. Find the First Non-Repeating Character in a Word

from solutions import first_non_repe

#Given input

sentence1 = "swwiiss"
print(first_non_repe(sentence1))

## Q4. Check Whether Two Strings Are Anagrams

from solutions import anagrams

#Given input
s1 = "listen"
s2 = "silent"
print(anagrams(s1,s2))

## Q5. Find the First Repeating Character in a String

from solutions import repe_char

#Given input
sentence  = "programming"
print(repe_char(sentence))

## Q6. Move All Zeros to the End of a List

from solutions import move_zeros
#Given input
l = [0, 3, 0, 1, 2, 0, 4]
print(move_zeros(l))

## Q7. Find the Second Highest Distinct Number in a List

from solutions import second_largest
#Given input
l = [10, 20, 40, 30, 40, 20]
print(second_largest(l))

## Q8. Remove Duplicates Without Changing the Original Order

from solutions import remove_dupli
#Given input
l = [4, 2, 4, 5, 2, 7, 5]
print(remove_dupli(l))

## Q9. Find the Missing Number from 1 to N

from solutions import missing_values
#Given input
nums = [1, 2, 4, 5, 6]
N = 6

print(missing_values(nums,N))

## Q10. Find Two Numbers Whose Sum Equals a Target

from solutions import sum_target
# #Given input
nums = [2, 7, 11, 15]
target = 9
print(sum_target(nums,target))

## Q11. Find the Number Closest to Zero
from solutions import closest_to_zero
# #Given input
nums = [-8, -3, 2, 5, -2]
print(closest_to_zero(nums))

## Q12. Find Common Elements Between Two Lists
from solutions import common_ele
# #Given input
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

print(common_ele(list1,list2))

## Q13. Rotate a List to the Right by K Positions


from solutions import rotate_right
# #Given input
nums = [1, 2, 3, 4, 5]
K = 2
print(rotate_right(nums,K))

## Q14. Find the Maximum Sum of Two Consecutive Elements

from solutions import max_consecutive_sum
# #Given input
nums = [4, 7, 2, 9, 5]
print(max_consecutive_sum(nums))

## Q15. Find All Pairs of Numbers Whose Sum Equals a Target

from solutions import find_pairs
# #Given input
nums = [2, 4, 3, 5, 7, 8, 1]
target = 9


print(find_pairs(nums,target))
