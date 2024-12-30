# str = input()
# vowel_substring = []
# const_substring = []
# vowels = "AEIOU"
# for i in range(len(str)):
#     if str[i] in vowels:
#          for j in range(i+1, len(str) + 1):
#             vowel_substring.append(str[i:j])
#     else:
#         for j in range(i+1, len(str) + 1):
#             const_substring.append(str[i:j])


# uniq_vowel_sub = list(set(vowel_substring))
# uniq_const_sub = list(set(const_substring))
# sum_v = 0
# sum_c = 0
# for i in uniq_vowel_sub:
#     sum_v = sum_v + str.count(i)
# for j in uniq_const_sub:
#     sum_c = sum_c + str.count(j)

# if sum_v > sum_c:
#     print('Kevin', sum_v)
# elif sum_v < sum_c:
#     print('Stuart', sum_c)
# else:
#     print('Draw')
# print('vowel_substring:',vowel_substring)
# print('uniq_vowel_sub: ',uniq_vowel_sub)

# print('const_substring: ',const_substring)
# print('unique_const_substring: ',uniq_const_sub)





# sum = 0
# print('substring:',substring)
# uniq_sub = set(substring)
# print('uniq_sub: ',uniq_sub)
# for i in uniq_sub:
#     sum = sum + str.count(i)
#     print('i:',i)
#     print('str.count(i):',str.count(i))
#     print('sum:',sum)

# print(sum)
# print(substring)



str = input()

vowels = 'AEIOU'
kevin_score = stuart_score =  0
for i in list(range(len(str))):
    if str[i] in vowels:
        kevin_score  += len(str) - i
    else:
        stuart_score += len(str) - i

if(kevin_score > stuart_score):
    print('Kevin',kevin_score)
elif(stuart_score > kevin_score):
    print('Stuart', stuart_score)
else:
    print('Draw')

