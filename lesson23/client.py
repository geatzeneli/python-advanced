import requests
from script import User
api_url="http://127.0.0.1:8000/user"
from typing import Dict


user_data:Dict[str,str|int]={"id":1, "name":"John","age":23,"email":"test@test.com","gender":"Female"}
response=requests.post(api_url,json=user_data)
print(response.status_code)

