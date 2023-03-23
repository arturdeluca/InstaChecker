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
with open("followers.txt", "w+") as f:
    for followers in profile.get_followers():
        file = f.write(followers.username + "\n")

# confirmation
print(f"All the accounts that follow {account} have been uploaded to followers.txt")
