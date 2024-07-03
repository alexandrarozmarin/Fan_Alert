followers = '''username1's profile picture
username1
name1
username2's profile picture
username2
name2
username3's profile picture
username3
name3
username4's profile picture
username4
· #
name4
username5's profile picture
username5
·
name5
'''

following = '''username1's profile picture
username1
name1
username2's profile picture
username2
name2
username3's profile picture
username3
name3
'''

split_followers = followers.splitlines()
split_following = following.splitlines()

for person in split_followers:
    if "profile picture" in person:
        split_followers.remove(person)
    if person == "·":
        split_followers.remove(person)
    
for person in split_following:
    if "profile picture" in person:
        split_following.remove(person)

fan_alert = []

for person in split_following:
    if person not in split_followers:
        fan_alert.append(person)

print(fan_alert)
