import json

#global variables with some sample messages to show order of elements is not important
mention = "@"
link = "http"
emot = "("

#lists storing each type
Mentions = []
Links = []
Emoticons = []

message = 'This is a working chat message mention is @user and @user2 link is http.hello.com and emoticon is (o_o) (yay) '
#message = '(o.o) wow @texas what is up with the weather? => https.weather.com/texas'
#message = 'hello (wave) '

#test to show individual words in message
# and how many words there are
print(message.split())
size = len(message.split())
print(size)

#increments through length of list (split message)
spot = 0
mentCount = 0
while spot != size:
        if mention in message.split()[spot]:
            print('mention: ', message.split()[spot])
            Mentions.append(message.split()[spot])
            mentCount = mentCount+1
            spot = spot+1
        else:
            spot = spot+1

print(Mentions)
spot = 0
linkCount = 0
while spot != size:
    if link in message.split()[spot]:
        print('link: ', message.split()[spot])
        Links.append(message.split()[spot])
        linkCount = linkCount + 1
        spot = spot + 1
    else:
        spot = spot+1

spot = 0
emotCount = 0
while spot != size:
    if emot in message.split()[spot]:
        print('emoticon: ', message.split()[spot])
        Emoticons.append(message.split()[spot])
        emotCount = emotCount + 1
        spot = spot + 1
    else:
        spot = spot+1


#object
msg = {
    "mention " : Mentions,
    "link " : Links,
    "emoticon " : Emoticons,
    "Other word count" : size-mentCount-linkCount-emotCount
}

# convert into JSON:
y = json.dumps(msg)

#JSON string:
print(y)