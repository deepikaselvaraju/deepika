c=input()
if(ord(c)>=65 and ord(c)<=90) or (ord(c)>=97 and ord(c)<=122):
  if(c==chr(65) or c==chr(69) or c==chr(73) or c==chr(79) or c==chr(85) or c==chr(97) or c==chr(101) or c==chr(105) or c==chr(111) or c==chr(117)):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
