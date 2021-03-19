# set {}
name1 ="rohan"
name2 ="alok"
print(name1, type(name1), hex(id(name1)))
print(name2, type(name2), hex(id(name2)))

follower = {"amitbanga17","ramandeep18","divyjot19"}
print("follower id:", follower)
print("type of id:", type(follower))
print("follower hex id:", hex(id(follower)))

follower.add("mohan")
follower.add("ram")
follower.add("sham")
print("total is",follower)
print("total follower:", len(follower))

follower.remove("sham")
print("total is",follower)
print("total follower:", len(follower))
