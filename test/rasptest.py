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
    file_name = "991.jpg"  # 文件名
    token = "90205a80ca66ac0a55794545fa7a8e9620321f92"
    url = "https://api.github.com/repos/inseasonzzz/uploadtest/contents/dictionary/" + file_name  # 用户名、库名、路径
    headers = {"Authorization": "token " + token}
    content = file_base64(file_data)
    data = {
            "message": "test",
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
    print("https://raw.githubusercontent.com/inseasonzzz/uploadtest/master/dictionary/" + file_name)
    # 在国内默认的down_url可能会无法访问，因此使用CDN访问


if __name__ == '__main__':
    fdata = open_file('/home/pi//5.jpg')
    upload_file(fdata)

