# sort the dict based on number's
dict1 = {'India': 2, 'Us': 1, 'Uk': 3, 'Loser': 5}
dd = {}
for k, v in sorted(dict1.items(), key=lambda item: item[1]):
    dd[k] = v
print(dd)
print({k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])})

# count the frequency of each element in a list.
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
frequency = {}
for i in nums:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)