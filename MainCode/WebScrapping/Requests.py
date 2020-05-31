import requests
res = requests.get('https://web.bii.a-star.edu.sg/~liangzhu/2017/11/02/linuxcommandline/automatetheboringstuffwithpython_new.pdf')
res.status_code
res.raise_for_status()
print(res.text[:500])