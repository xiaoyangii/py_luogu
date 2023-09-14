import json
import requests as req
import urllib.error
import re
from bs4 import BeautifulSoup
from headers_config import *

baseUrl = "https://www.luogu.com.cn/problem/list"
baseUrl1 = "https://www.luogu.com.cn/problem/"
baseUrl2 = "https://www.luogu.com.cn/problem/solution/"

def get_pid(url, params):
    res = req.get(url + "&_contentOnly=1", headers = headers)
    # res = req.get(baseUrl, headers = headers, params=params)
    jsonText = res.text
    loader = json.loads(jsonText)
    map = loader["currentData"]["problems"]
    total = map["count"]
    pro = map["result"]
    return total, pro


def getProSlu(pid):
    res_solu = req.get(baseUrl2 + pid, headers = headers) # 获取题解
    html = res_solu.text
    # text = str(urllib.parse.unquote(html, encoding='unicode_escape')) # 题解解码
    bs = BeautifulSoup(html,"html.parser")
    core = str(bs.select("script")[0])
    return core

def getPro(pid):
    res = req.get(baseUrl1 + pid, headers = headers)   # 获取题目
    html = res.text
    bs = BeautifulSoup(html,"html.parser")
    core = str(bs.select("article")[0])
    return core, html
  
# getProName(content)函数通过正则表达式re获得<h1>标签里面的题目名称并返回
def getProName(content):
    pattern = re.compile(r"<h1>(.*?)</h1>")
    result = pattern.findall(content)
    return result[0]
