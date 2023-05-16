# dicts1 = {"a": "Bob", "b": "Alice", "c": "Carol"}
# print(dicts1)
# print(type(dicts1))

# dicts2 = {1: "Bob", "b": True, "c": 1024}
# print(dicts2)

# dicts1 = {"a": "Bob", "b": "Alice", "c": "Carol"}
# print(dicts1["a"])
# print(dicts1["c"])
#
# dicts1["d"] = "Dave"
# print(dicts1)
# dicts1["a"] = "Python"
# print(dicts1)
#
# del dicts1["b"]
# print(dicts1)

dicts1 = {"a": "Bob", "b": "Alice", "c": "Carol"}
print(len(dicts1))
print(dicts1.keys())
print(dicts1.values())
print(dicts1.items())
print("a" in dicts1)
print("x" in dicts1)
dicts1.clear()
print(dicts1)