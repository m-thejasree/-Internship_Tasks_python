## Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    words = sentence.split()
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result

## Q2. Find the Frequency of Each Character in a Word

def char_freq(word):
    d = {}
    for i in word:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

##Q3. Find the First Non-Repeating Character in a Word


def first_non_repe(word):
    d = {}
    for i in word:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i,j in d.items():
        if j == 1:
            return i
    return None

## Q4. Check Whether Two Strings Are Anagrams

def anagrams(str1,str2):
    if sorted(str1) == sorted(str2) and len(str1) == len(str2):
        return True
    return False

## Q5. Find the First Repeating Character in a String

def repe_char(word):
    d = {}
    for i in word:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i,j in d.items():
        if j > 1:
            return i
    return None

## Q6. Move All Zeros to the End of a List

def move_zeros(list1):
    result = []

    for i in list1:
        if i != 0:
            result.append(i)

    for i in list1:
        if i == 0:
            result.append(i)

    return result


# Q7. Find the Second-Largest Distinct Number

def second_largest(list1):
    unique = sorted(set(list1))

    if len(unique) < 2:
        return None

    return unique[-2]

## Q8. Remove Duplicates Without Changing the Original Order

def remove_dupli(list1):
    result = []
    for i in list1:
        if i not in result:
            result.append(i)
    return result

## Q9. Find the Missing Number from 1 to N

def missing_values(nums,n):
    for i in range(1,n+1):
        if i not in nums:
            return i

# Q10. Find Two Numbers Whose Sum Equals a Target

def sum_target(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]

    return []

## Q11. Find the Number Closest to Zero

def closest_to_zero(nums):
    closest = nums[0]

    for i in nums:
        if abs(i) < abs(closest):
            closest = i
        elif abs(i) == abs(closest) and i > closest:
            closest = i

    return closest

## Q12. Find Common Elements Between Two Lists

def common_ele(list1, list2):
    result = []
    for i in list1:
        if i in list2 and i not in result:
            result.append(i)
    return result

## Q13. Rotate a List to the Right by K Positions

def rotate_right(nums, K):
    if len(nums) == 0:
        return nums

    K = K % len(nums)

    return nums[-K:] + nums[:-K] if K != 0 else nums

## Q14. Find the Maximum Sum of Two Consecutive Elements

def max_consecutive_sum(nums):
    max_sum = nums[0] + nums[1]

    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

## Q15. Find All Pairs of Numbers Whose Sum Equals a Target

def find_pairs(nums, target):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = sorted([nums[i], nums[j]])

                if pair not in result:
                    result.append(pair)

    result.sort(key=lambda pair: pair[0])

    return result