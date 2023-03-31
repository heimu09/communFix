problems = [
  {
    "name": "Иван Иванов",
    "role": "Сантехник",
    "phone": "+7-900-123-45-67",
    "email": "ivanov@example.com"
  },
  {
    "name": "Петр Петров",
    "role": "Электрик",
    "phone": "+7-900-987-65-43",
    "email": "petrov@example.com"
  },
  {
    "name": "Анна Смирнова",
    "role": "Управляющий",
    "phone": "+7-900-555-35-35",
    "email": "smirnova@example.com"
  },
  {
    "name": "Сергей Кузнецов",
    "role": "Дежурный по дому",
    "phone": "+7-900-777-88-99",
    "email": "kuznetsov@example.com"
  },
  {
    "name": "Ольга Морозова",
    "role": "Консультант по вопросам ЖКХ",
    "phone": "+7-900-222-44-66",
    "email": "morozova@example.com"
  }
]

import requests

url = 'https://3327-217-196-25-57.in.ngrok.io/api/contacts/'

for problem in problems:
    response = requests.post(url, headers={'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5ODM5MjM5LCJpYXQiOjE2Nzk3NTI4MzksImp0aSI6IjA5NjQ0ZGE4Mjg2YTRlMjlhYmU4ZjY4ZmM0ZGE0MWE5IiwidXNlcl9pZCI6MX0.wStEWSmBSv0R_yshOiDhPhkA6Op7N_6yVEM9ostGreU'}, json=problem)

