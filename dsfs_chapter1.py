from __future__ import division

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klien"},

]

friendships = [(0,1),(0,2),(0,1),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j]) # add i as a friend of j
    users[j]["friends"].append(users[i]) # add j as a friend of i

#print (user[3]["friends"])

def numer_of_friends(user):
    """ how may friends does _user_ have?"""
    return len(user["friends"])

total_connections = sum(numer_of_friends(user) for user in users)

#print(total_connections)

num_users = len(users)
avg_connections = total_connections / num_users

# print((avg_connections))

number_friends_by_id = [(user["id"], numer_of_friends(user)) for user in users]

print(sorted(number_friends_by_id,                      # get it sorted
       key= lambda num_friends:                         # by num_friends
       num_friends, reverse=True))                      # largest to smallest

##____________________________________P2____________________________________

