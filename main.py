problems = [
  {
    "date": "2023-01-15",
    "income": "12000.00",
    "expenses": "7500.00",
    "details": "Доходы от аренды и коммунальных платежей. Расходы включают зарплаты, коммунальные услуги и расходы на обслуживание."
  },
  {
    "date": "2023-02-15",
    "income": "12500.00",
    "expenses": "7200.00",
    "details": "Доходы от аренды и коммунальных платежей. Расходы включают зарплаты, коммунальные услуги и расходы на ремонт."
  },
  {
    "date": "2023-03-15",
    "income": "13000.00",
    "expenses": "8000.00",
    "details": "Доходы от аренды и коммунальных платежей. Расходы включают зарплаты, коммунальные услуги и расходы на обслуживание зеленых зон."
  },
  {
    "date": "2023-04-15",
    "income": "13500.00",
    "expenses": "8500.00",
    "details": "Доходы от аренды и коммунальных платежей. Расходы включают зарплаты, коммунальные услуги и расходы на ремонт системы отопления."
  },
  {
    "date": "2023-05-15",
    "income": "14000.00",
    "expenses": "9000.00",
    "details": "Доходы от аренды и коммунальных платежей. Расходы включают зарплаты, коммунальные услуги и расходы на ремонт системы водоснабжения."
  }
]


import requests

url = 'http://127.0.0.1:8000/api/finances/'

for problem in problems:
    response = requests.post(url, headers={'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5ODM5MjM5LCJpYXQiOjE2Nzk3NTI4MzksImp0aSI6IjA5NjQ0ZGE4Mjg2YTRlMjlhYmU4ZjY4ZmM0ZGE0MWE5IiwidXNlcl9pZCI6MX0.wStEWSmBSv0R_yshOiDhPhkA6Op7N_6yVEM9ostGreU'}, json=problem)

