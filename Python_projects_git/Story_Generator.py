import random
when = ['A few months ago', 'day before yesterday', 'that night', 'A long time ago', 'On 20th Jan']
who = ['a duck', 'an lion', 'a zebra', 'a tiger', 'a dog']
name = ['Ali', 'Miriam', 'daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university', 'seminar', 'school', 'laundry']
happened = ['made a lot of friends', 'Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))