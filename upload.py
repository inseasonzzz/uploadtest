import requests
import base64
import json


# 读取文件
def open_file(file_path):
    with open(file_path, 'rb+') as f:
        return f.read()


# 将文件转换为base64编码，上传文件必须将文件以base64格式上传
def file_base64(data):
    data_b64 = base64.b64encode(data).decode('utf-8')
    return data_b64


# 上传文件
def upload_file(file_data):
    file_name = "6.png"  # 文件名
    token = "c69b4429ea675066192b2aac7a4fea27f59bcf22"
    url = "https://api.github.com/repos/inseasonzzz/littlepic/contents/test/" + file_name  # 用户名、库名、路径
    headers = {"Authorization": "token " + token}
    content = file_base64(file_data)
    data = {
            "message": "testpic",
            "committer": {
            "name": "inseasonzzz",
            "email": "qq1457098613@163.com"
        },
        "content": content
    }
    data = json.dumps(data)
    req = requests.put(url=url, data=data, headers=headers)
    req.encoding = "utf-8"
    re_data = json.loads(req.text)
    print(re_data)
    #print(re_data['content']['sha'])
    print("https://raw.githubusercontent.com/inseasonzzz/littlepic/master/test/" + file_name)
    # 在国内默认的down_url可能会无法访问，因此使用CDN访问


if __name__ == '__main__':
    fdata = open_file('C://Users/Eazon/Desktop//100.png')
    upload_file(fdata)

