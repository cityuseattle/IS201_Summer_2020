import requests

res= requests.get('https://www.google.com')

try:
    res.raise_for_status()
    print("status code:", res.status_code)
    print("Length of the text:", len(res.text))
    print(res.text[:103])
except Exception as exc:
    print("oh no: %" %(exc))





    