//导入必要的包
import requests
import execjs
inport os

//指定node运行的环境变量
os.environ("NODE.PATH"] = "/usr/local/lib/node_modules/"

//读取拼接的JS文件
with open('v20.js', mode = 'r', encoding='utf-8') as f: 
	js = f.read()
JS = execjs.compile(js)

url = "http://xxxxxx"

//执行JS文件中的方法，获取加密参数
signature = JS.call("get.sign", url)

print(signature)

final_url = f"{url}&_signature={signature}"
res = requests.get( 
	url=final_url, 
	headers = {
      "user-agent":"XXX"
	  }
	  )
	  
print(res.text)
