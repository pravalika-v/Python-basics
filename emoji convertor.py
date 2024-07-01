def emoji_convertor(message):
    words = message.split(" ")
    emojis = {
        ":-)" : "😊",
        ":-(" : "😒"
    }
    output = ""
    for word in words:
        output += emojis.get(word,word) + " "
    return output

msg = input(">")
print (emoji_convertor(msg))