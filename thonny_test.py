ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
#print(ramit['email'])
#print(ramit['interests'][0])
#print(ramit['friends'][0]['email'])
#print(ramit['friends'][1]['interests'][1])
def countFriends(dict):
    friends_count = 0
    for friends_count in ramit:
        if 'friends' in ramit:
            friends_count += 1
        return friends_count
print(str(countFriends(ramit)))