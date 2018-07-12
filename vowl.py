list1=['a','e','i','o','u','A','E','I','O','U']
let=input()
if let in list1:
    print("Vowel")
elif(ord(let)>=65 and ord(let)<=90 or ord(let)>=97 and ord(let)<=122):
    print("Consonant")
else:
    print("invalid")
