newphrase = "rainstorm"
# 01234567 We are using THIS version
# 123456789 college board version.

shortphrase = newphrase[3:len(newphrase)-3]
 # index 3 which is "n" is inclusive
# index len(newphrase)-3 which is exclusive
print(shortphrase) #prints "nst"

#collegeboard version [4:len(newphase)-6]
#explain why len(newphase)-3 = 9-3 = 6
#Why does it end with 6?
#because the last index is not included