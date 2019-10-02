from mypastebot import Search

# find new public pastes
pastes = Search.new()
# print the results
print(pastes['results'])

# get new public pastes as links
pastes = Search.new(linkType='link')
# print the results
print(pastes['results'])

# get new public pastes as raw links
pastes = Search.new(linkType='raw')
# print the results
print(pastes['results'])
