import requests
email = 'admin@lectonik.ru'
pswd = '12345678'
auth_token = [
            '74401a74765709d07a59b4775f93458e86dfbd44',  # superuser
            'e577670c4fe8dd3b25e97f011d41b3feb23589dd',
            '94d92271074d949bc8c4a54200022721f2664503',
            ]
add_profile_data = {
  "first_name": "Николай",
  "last_name": "Николаев",
  "middle_name": "",
  "birth_date": "1970-02-18",
  "city": "Москва",
  "description": "Мое описание",
#   "latitude": 50.0211349,
#   "longitude": 37.0211349
}
modify_profile_data = {
#   "first_name": "Иван",
#   "last_name": "Иванов",
#   "middle_name": "Иванович",
#   "birth_date": "1960-02-18",
#   "city": "Москва",
#   "rating": 0,
  "is_lecturer": True,
#   "is_project_admin": False,
#   "is_customer": False,
#   "is_verified": False,
#   "description": "Мое описание",
#   "latitude": 50.0211349,
#   "longitude": 37.0211349
}

add_lecture_data = {
  "name":"Python.Начало",
  "date":"2022-02-23",
  "duration": 120,
  "description":"Лекция по Python для начинающих",
  "lecturer_name":"Данила Козловкий",
}


# r = requests.post('https://dev.lectonik.ru/api/auth/signup/', data={'email': email,'password':pswd})


# r = requests.post('http://127.0.0.1:8000/api/auth/signup/', data={'email': email,'password':pswd})
# r = requests.post('http://127.0.0.1:8000/api/auth/login/', data={'email': email,'password':pswd})
# r = requests.post('http://127.0.0.1:8000/api/auth/logout/', headers={'Authorization': auth_token[0]})

# r = requests.post('http://127.0.0.1:8000/api/workrooms/lecturer/addlecture/', headers={'Authorization': auth_token[0]},
#                                                                             data ={'name':'Python.Основы', 'description':'Вводная лекция. Введение в python'})

# r = requests.get('http://127.0.0.1:8000/api/workrooms/lecturer/lectures-list/', 
#     headers={'Authorization': auth_token[1]}
#     )

# r = requests.post('http://127.0.0.1:8000/api/workrooms/profile/', 
#     headers={'Authorization': auth_token[1]},
#     data = add_profile_data)

# r = requests.patch('http://127.0.0.1:8000/api/workrooms/profile/', 
#     headers={'Authorization': auth_token[1]},
#     data = modify_profile_data)

r = requests.post('http://127.0.0.1:8000/api/workrooms/lecturer/lecture/', 
    headers={'Authorization': auth_token[1]},
    data = add_lecture_data)

# r = requests.get('http://127.0.0.1:8000/api/workrooms/lecturer/lecture/', 
#     headers={'Authorization': auth_token[0]}
#     )

print (r.text)