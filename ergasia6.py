import instaloader
from statistics import mode

def most_common(users):
    return mode(users)

L = instaloader.Instaloader()

PROFILE = input("Input the instagram name: ")

posts = instaloader.Profile.from_username(L.context, PROFILE).get_posts()

users = []



i = 1
for post in posts:
    comments = post.get_comments()
    for comment in comments:
        users.append(comment.owner.username)
    if i == 100:
        break
    i += 1

print("The user that made the most comments is: " + most_common(users))
