# open both documents so it is possible to access data and compare between them
with open("followees.txt", "r") as f:
    followees = f.read().splitlines()

with open("followers.txt", "r") as b:
    followers = b.read().splitlines()

print("The follow accounts are not following you back:")
print()
print()

i = 1
# comparing both set of data
# if the element is in the "followees" doc (meaning that the account targeted follows him)
# it also should be in the "followers" doc (meaning that the other account follows the target account back)
# otherwise, its name should be printed to confirm that that element does not follow you back

for element in followees:
    if element not in followers:
        print(i, element)
        print("------------------------------")
        i += 1
