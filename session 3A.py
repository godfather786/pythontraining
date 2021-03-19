follower = ["amitbanga17","ramandeep18","divyjot19"]
print("follower id:", follower)
print("type of id:", type(follower))
print("follower hex id:", hex(id(follower)))


follower.append("harjot16")
follower.append("somin12")
print("follower now",follower)

del follower[1]
print("follower now",follower)