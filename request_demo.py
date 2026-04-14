import requests, json

# Send Request
m_headers = {'x-user': 'test_user', 'x-taste': '1,1,2,1,1,1'}
x = requests.post('https://backlog.raymon8331.workers.dev/upload', headers=m_headers)

# return status code
print(x.status_code)

# desc
print(x.reason)

# Content
print(x.content)
data = json.loads(x.content.decode("utf-8"))
print(data)