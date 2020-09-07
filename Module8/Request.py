import request

res= request.get('http://web.textfiles.com/computers/3dbasics.txt')

try:
    res.raise_for_status()
    print("status code:", res.status_code)
    print("Length of the text:", len(res.text))
    print(res.text[:103])
except Exception as exc:
    print("oh no: %"%(exc))



