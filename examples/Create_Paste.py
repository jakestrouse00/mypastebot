from mypastebot import Create

# get the token
token = Create.getToken()
# create the paste
paste = Create.makePaste(text='This is the text of our new paste', title='This is the title of the paste', format='1', token=token)
# print the pastebin link
print("Link: " + paste['link'])
# print the pastebin raw link
print("Raw Link: " + paste['raw'])
