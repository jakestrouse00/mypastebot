# MyPasteBot
A simple Pastebin.com package to create guest pastes, find new public pastes and more!

## prerequisites
requests==2.22.0

## Installation
```cmd
python -m pip install mypastebot
```
### Methods

#### Create a New Guest Paste
```python
from mypastebot import Create

token = Create.getToken()
paste = Create.makePaste(text='This is the text of our new paste', title='This is the title of the paste', format='1', token=token)
print("Link: " + paste['link'])
print("Raw Link: " + paste['raw'])
```
 
 #### Find Pastes Using Keyword
 ```python
from mypastebot import Search

# max limit is 15
pastes = Search.find(term='Python', limit=10)

print(pastes['results'])

# find most recent pastes

pastes = Search.find(term='Python', limit=10, sortType='date')

print(pastes['results'])
```

#### Find Newest Public Pastes
```python
from mypastebot import Search


pastes = Search.new()
print(pastes['results'])

# get new public pastes as links
pastes = Search.new(linkType='link')
print(pastes['results'])

# get new public pastes as raw links
pastes = Search.new(linkType='raw')
print(pastes['results'])
```
