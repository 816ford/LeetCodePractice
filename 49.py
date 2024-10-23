strs = ["eat","tea","tan","ate","nat","bat"]



anagrams = []
output = []

dict = {}

for word in strs:
    sorted_word = "".join(sorted(word))
    print(type(sorted_word))
    if sorted_word in dict:
        dict[sorted_word].append(word)
    else:
        dict[sorted_word] = [word]

output = list(dict.values())



print(output)


