"""
There are N strings. Each string's length is no more than 20 characters.
There are also Q queries. For each query, you are given a string, and
you need to find out how many times this string occurred previously.
"""


strings = {}

num_strings = int(input().strip())
for i in range(num_strings):
    string = input().strip()
    strings[string] = strings.get(string, 0) + 1

num_queries = int(input().strip())
for j in range(num_queries):
    query = input().strip()
    print(strings.get(query, 0))
