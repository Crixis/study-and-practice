"""Given two non-negative integers low and high. 
Return the count of odd numbers between low and high (inclusive).
Constraints: 0 <= low <= high <= 10^9
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:  
        count=0
        if low>=0 and high<=10**9 and low<high:
            for num in range(low, high+1):
                if num%2 != 0:
                    count+=1
        return count


"""Input:
Hello World

Output:
wORLD hELLO

The function is expected to return a STRING

The function accepts STRING sentence as parameter."""

def reverse_words_order_and_swap_cases(sentence):
    mystr = ''
    for i in sentence:
        if i.isspace():
            mystr+= " "
        else:
            if i.isupper():
                mystr+= i.lower()
            if i.islower():
                mystr+= i.upper()
    words = list(reversed(mystr.split()))
    mywords = " ".join(words)
    return mywords
    
out = reverse_words_order_and_swap_cases("Hello World")
print(out)