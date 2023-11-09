friends = ['Joe', 'Josh', 'Jane', 'David']
i = 0

for friend in friends:
    print(f'Dear {friend}! I would like to invite to my birthday party, because you are my favourite friend, {friend}!')

while i < len(friends):
    print(f'Dear {friends[i]}! I would like to invite to my birthday party, because you are my favourite friend, {friends[i]}!')
    i += 1

for friend in reversed(friends):
    print(f'Dear {friend}! I would like to invite to my birthday party, because you are my favourite friend, {friend}!')

while i < (len(friends)):
    print(f'Dear {friends[i]}! I would like to invite to my birthday party, because you are my favourite friend, {friends[i]}!')
    i += 1