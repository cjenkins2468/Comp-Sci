read_file = open('inbox.txt', 'r')
hours = {}
for line in read_file:
    if line.startswith("From "):
        time = line.split()[5]
        hour = time.split(":")[0]
        hours[hour] = hours.get(hour, 0) + 1
lst = []
for key, value in hours.items():
    int(key)
    lst.append((key,value))
lst.sort(reverse=False)
print(lst)
for t in lst:
    print(t[0], t[1])

