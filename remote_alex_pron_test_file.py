import requests
email = 'lector3@lectonik.ru'
pswd = '12345678'
auth_token = [
            '74401a74765709d07a59b4775f93458e86dfbd44',  # superuser
            '06dff0ef6857526a14d587a4192bd00a6c1dd86d',
            '',
            '',
            ]
add_profile_data = {
  "first_name": "Трофим",
  "last_name": "Бенеславский",
  "middle_name": "",
  "birth_date": "1975-07-10",
  "city": "Москва",
  "description": "Профессор МФЮА",
#   "latitude": 50.0211349,
#   "longitude": 37.0211349
}
modify_profile_data = {
  # "first_name": "Эдуард",
  # "last_name": "Суровый",
  # "middle_name": "",
  # "birth_date": "1980-06-02",
  # "city": "Пермь",
  # "rating": 0,
  "is_lecturer": True,
  # "is_project_admin": False,
  # "is_customer": False,
  # "is_verified": False,
  # "description": "Профессор ПГУ",
  # "latitude": 52.0211349,
  # "longitude": 33.0217634
}

add_lecture_data = {
  "id": 1,
  "name":"Донорство. Проблема нехватки крови",
  "date":"2022-11-28",
  "duration": 60,
  "description":"Рассматриваются вопросы о проблемах нехватки крови",
  # "lecturer_name":"Эдуард Суровый",
}
delete_lecture_data = {
  "id": 18,
}
delete_lecture_data_list = {
  "id_list": [11, 'dfg', 56]
}




# r = requests.post('https://dev.lectonic.ru/api/auth/signup/', data={'email': email,'password':pswd})
# r = requests.post('https://dev.lectonic.ru/api/auth/login/', data={'email': email,'password':pswd})
# r = requests.post('https://dev.lectonic.ru/api/auth/logout/', headers={'Authorization': auth_token[0]})


# r = requests.post('https://dev.lectonic.ru/api/workrooms/profile/', 
#     headers={'Authorization': auth_token[1]},
#     data = add_profile_data)

# r = requests.patch('https://dev.lectonic.ru/api/workrooms/profile/', 
#     headers={'Authorization': auth_token[1]},
#     data = modify_profile_data)

# r = requests.post('https://dev.lectonic.ru/api/workrooms/lecturer/lecture/', 
#     headers={'Authorization': auth_token[1]},
#     data = add_lecture_data)

# r = requests.delete('https://dev.lectonic.ru/api/workrooms/lecturer/lecture/', 
#     headers={'Authorization': auth_token[1]},
#     data = delete_lecture_data)

r = requests.patch('https://dev.lectonic.ru/api/workrooms/lecturer/lecture/', 
    headers={'Authorization': auth_token[1]},
    data = add_lecture_data)

# r = requests.delete('https://dev.lectonic.ru/api/workrooms/lecturer/lecture/delete-multiple/', 
#     headers={'Authorization': auth_token[1]},
#     data = delete_lecture_data_list)

# r = requests.get('https://dev.lectonic.ru/api/workrooms/lecturer/lecture/', 
#     headers={'Authorization': auth_token[3]}
#     )

# r = requests.get('https://dev.lectonic.ru/api/workrooms/lecturer/lecture/?id=20', 
#     headers={'Authorization': auth_token[1]}
#     )

print (r.text)