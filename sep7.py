'''

name = "Codegnan"
batch = 5
email_id = "saketh@codegnan.com"
print(len(email_id))

email_id = "saketh@codegnan.com"
print((email_id[7:15]))


email_ids = ['lenkalokesh2003@gmail','22u41a05c6@gmail.com','vizag2001@gmail.com','saketh@codegnan.com']
print(len(email_ids))
print(email_ids[-2:])


email_ids = ['lenkalokesh2003@gmail','22u41a05c6@gmail.com','vizag2001@gmail.com','saketh@codegnan.com']
email_ids.extend(['ksdhk@gmail.com','skdjhndk@gmail.com'])
print(email_ids)


users = {'lenkalokesh2003@gmail','22u41a05c6@gmail.com','vizag2001@gmail.com','saketh@codegnan.com','ksdhk@gmail.com','skdjhndk@gmail.com'}
print()

'''
for i in range(len(email_ids)):
    users[i+1] = email_ids[i]
print(users)

#enumerate --> it provides by default a counter object (you can store in
#desired collection)
data = dict(enumerate(email_ids,1))
print(data)

#Python --> object
#Functions --> First class objects
#Set is an Unordered collection as no indexing
