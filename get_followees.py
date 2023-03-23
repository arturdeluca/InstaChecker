import instaloader

L = instaloader.Instaloader()

username = "your_username"
password = "your_password"

L.login(username, password)

# acccount that will be targeted
account = "account_being_targeted"
profile = instaloader.Profile.from_username(L.context, account)

# creates a file calles 'followers.txt' with all user's followers.
# every interaction it re-writes it ('w+').
with open("followees.txt", "w+") as f:
    for followees in profile.get_followees():
        file = f.write(followees.username + "\n")

# confirmation
print(f"All the people that {account} follows have been uploaded to followees.txt")
