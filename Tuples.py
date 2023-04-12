filename = 'inbox.txt'
fhand = open(filename, 'r')
email_addresses = {}
for line in fhand:
    if line.startswith("From "):
        email = line.split()[1]
        email_addresses[email] = email_addresses.get(email, 0) + 1
lst = []
for key, value in email_addresses.items():
    lst.append((value,key))
lst.sort(reverse=True)
person_tuple = lst[0]
print(person_tuple[1], person_tuple[0])