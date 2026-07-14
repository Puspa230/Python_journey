str = "I am Puspita.\nI am a python developer."
print(str)

#String concatination
str1 = "Good"
str2 = "luck"

print(str1 + "_" + str2)

#Functions
#length of String
str3 = "Publishers of Odisha"
ch = len(str3)
print(ch)

#String Slicing
print(str3[0:3])
print(str3[-3:len(str3)])

#endswith
str3_endswith_sha = str3.endswith("sha")
print(str3_endswith_sha)

#capitalize
capitalize_str3 = str3.capitalize()
print(capitalize_str3)

#replace
new_str = str3.replace("of","in")
print(new_str)

#find
find_str = str3.find("r")
print(find_str)

#count
count_the_occurance_of_substr = str3.count("Odisha")
print(count_the_occurance_of_substr)




