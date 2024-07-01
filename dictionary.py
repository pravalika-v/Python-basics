phone_no = input("Phone number: ")
plist = ""
number_mapping = {
    "1":"one ", "2":"Two ", 
    "3":"Three ", "4":"Four ", "5":"Five ", "6":"Six ", "7":"Seven ", 
    "8":"Eight ", "9":"Nine ", "0":"Zero "
}
for ch in phone_no:
    plist += number_mapping[ch]
print(plist)