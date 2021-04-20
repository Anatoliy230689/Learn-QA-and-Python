#HOMEWORK 6

import requests

# r = requests.get('http://pulse-rest-testing.herokuapp.com/books/')
# Get запрос
# print(r)
# print(r.status_code)
# print(r.headers)
# books_data = r.json()
# print(books_data)
# for i in books_data:
#     print(i['id'])


# add book
# book_data = {'title':'my kampf', 'author':'adolf hitler'}
# r = requests.post('http://pulse-rest-testing.herokuapp.com/books/', book_data)
# print(r)
# print(r.status_code)
# body = r.json()
# print(body)
# print(body['id'])


#update book
# book_id = 1579
# book_data = {'title':'My Kampf', 'author':'Adolf Hitler'}
# r = requests.put(f'http://pulse-rest-testing.herokuapp.com/books/{book_id}', book_data)
# # print(r)
# print(r.status_code)
# body = r.json()
# print(body)
# print(body['id'])


#delete book
# book_id = 1578
# book_data = {'title':'My Kampf', 'author':'Adolf Hitler'}
# r = requests.delete(f'http://pulse-rest-testing.herokuapp.com/books/{book_id}')
# # print(r)
# print(r.status_code)


#Role

# base_url = "http://pulse-rest-testing.herokuapp.com/"
# resp = requests.get(base_url+'/roles')
#
# user_list = resp.json()
# for role in user_list:
#     print(role)


#add new role
book_id = 1579
r = requests.get(f'http://pulse-rest-testing.herokuapp.com/books/{book_id}')
book = r.json()
# print(book['id'])

# role_data = {'name':"Adolf", 'type':'dictator', 'level':100, 'book':book['id']}
# base_url = "http://pulse-rest-testing.herokuapp.com/"
# resp = requests.post(base_url+'/roles', role_data)
#
# print(resp.status_code)
# body = resp.json()
# print(body)
# print(body['id'])

#update role
role_id = 136
role_data = {'name':"Adolf", 'type':'DICTATOR', 'level':100, 'book':book['id']}
base_url = "http://pulse-rest-testing.herokuapp.com/"
resp = requests.put('http://pulse-rest-testing.herokuapp.com/roles/136', role_data)

print(resp.status_code)
body = resp.json()
print(body)


