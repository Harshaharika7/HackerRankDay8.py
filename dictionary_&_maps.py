# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read number of entries
n = int(input())

# Initialize phone book dictionary
phone_book = {}

# Read entries into the dictionary
for _ in range(n):
    entry = input().split()
    name = entry[0]
    phone = entry[1]
    phone_book[name] = phone

# Read and respond to queries
try:
    while True:
        query = input()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
except EOFError:
    pass
