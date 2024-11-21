grocery = {}
while True:
    try:
        item = input().lower()
        if item == "done":  # Use "done" to exit instead of relying on EOFError
            break
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        break

for key in sorted(grocery.keys()):
    print( grocery[key],key.upper(),)
