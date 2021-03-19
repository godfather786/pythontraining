rohan_followers = {"amit", "ram", "alok", "mohit", "divyjot", "harjot"}
amit_followrs={"rohan", "divyjot","harjot","massi"}

mutual_followers = rohan_followers.intersection(amit_followrs)

print("rohan")
print(rohan_followers)

print("amit")
print(amit_followrs)

print("Mutual followers for rohan and amit")
print(mutual_followers)