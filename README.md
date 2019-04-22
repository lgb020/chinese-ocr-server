# 本地OCR识别服务 Demo

### 环境: 
Linux & Python 2.X & Tensorflow 1.3 & Keras & Flask

### 识别部分：
运行 chinese_ocr 目录下setup.sh文件安装识别所需环境（前提有Python 2.X）

注：GPU条件下直接运行即可；CPU条件下须注释setup.sh文件中GPU相关操作，解开CPU相关操作再运行。

### 服务部分：
运行 flask_server.py 启动本地服务。

### Python客户端示例：
```
myurl="http://127.0.0.1:5000/Rec_Interface/file"
img_info = {'image_path':'xxx.jpg'}
r = requests.post(myurl, data=img_info)
print(json.loads(r.text))
```

## 参考：[YCG09](https://github.com/YCG09/chinese_ocr)
