import requests,base64,random,time,json

def creat_file(strx=''):
    randx=random.randint(1000, 9999)
    fn= ''+ time.strftime("%Y%m%d%H%M%S", time.localtime())+str(randx)+'.txt'
    with open(fn, 'a+') as f:
        f.write(fn + '\n')  # 加\n换行显示
        f.write(strx)
    return fn

def fn_base64(fn):
    # 打开本地图片，并转化为base64
    f = open(fn, 'rb')
    fnb64 = base64.b64encode(f.read()).decode('utf-8')
    return fnb64

tokens='6b987297b89c4f8e0'#

fn=creat_file('sxs')
url = "https://api.github.com/repos/[user]/[proj]/contents/[path]/"+ fn
# d = {
   "message": "my commit message",
   "committer": {
     "name": "user",
     "email": "user@163.com"
   },
   "content": fn_base64(fn)
 }


headers = {"Authorization": 'token '+tokens} # 前两行会在后面的代码中忽略掉不写
r = requests.put(url=url,data=json.dumps(d), headers=headers)
rs=r.status_code
if rs==201:
    print('sucess')
#出现422错误，有可能是文件在项目中已经存在了。