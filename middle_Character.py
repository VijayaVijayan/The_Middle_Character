def getting_middleCharacter(word):
    length = len(word)
    mid_index = length // 2
    
    if length % 2 == 1:  
        return word[mid_index]
    else: 
        return word[mid_index - 1 : mid_index + 1]


word1 = "vijay"
word2 = "charle"

result1 = getting_middleCharacter(word1)
result2 = getting_middleCharacter(word2)

print(result1)
print(result2)
    