a = {"Ironman", "Captain", "Thor", "Loki"}
b = {"Batman", "Superman", "Wonder Woman"}
c = {"Thor", "Loki"}
#isdisjoint

print(a.isdisjoint(c))

#issubset

print(c.issubset(a))

#issuperset

print(a.issuperset(c))

#update

a.update(b)
print(a)

#clear

a.clear()
print(a)