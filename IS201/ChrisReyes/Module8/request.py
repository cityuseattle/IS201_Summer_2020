import requests

res= requests.get('http://web.textfiles.com/computers/3dbasics.txt')

try:
    res.raise_for_status()
    print("status Code:", res.status_code)
    print("Length of the text:", len(res.txt))
    print(res.txt[:103])
except Exception as exc:
    print("OH no: %s" %(exc))
