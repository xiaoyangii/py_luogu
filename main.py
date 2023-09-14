import requests as req
import time
import re
import os
from headers_config import *
from getPid import *

savePath = "E:\\桌面\\py_luogu\\problem\\"

proName = ""

def get_problem(doc_name, total, arr_pro):
    hasSave = 0
    if total == 0:
      print("未找到相关题目或当前筛选条件下无题目！！！请重新筛选")
      return
    else:
      print(f"共找到{format(total)}个相关题目")

    if not isexist(name=doc_name, path=savePath):    # 检查是否存在该分类的文件夹，如果不存在则创建
      os.makedirs("problem" + "\\" + doc_name)
    
    for i in range(total):
      if i == 50:
        break
      print(f"正在爬取{format(arr_pro[i]['pid'])}...", end="")

      core, html = getPro(arr_pro[i]["pid"])
      core1 = getProSlu(arr_pro[i]["pid"])

      proName = getProName(core)              # 获取题目名称

      if html.find("Exception") == -1:        # 洛谷中没找到该题目或无权查看的提示网页中会有该字样
        problemMD2 = getMD(core1, "solu")     # 获取题解
        problemMD = getMD(core, "pro")        # 获取题目
        print("爬取成功！")
        print("正在保存...",end="")

        path = arr_pro[i]["pid"] + "-" + proName   # 题号-题目名称
        if str(path).find('/') >= 0:
          path = path.replace('/', ' ')
        print(path)
        saveData(problemMD, doc_name + "\\", path, path + ".md")
        saveData(problemMD2, doc_name + "\\", path, path + "-题解" + ".md")
        print("保存成功!")
        hasSave = hasSave+1
      else:
        print("该题目不存在或无权查看")
      print("--------------------------------------------")
      time.sleep(random.randint(0,2))
    print("爬取完毕")
    print(f"共爬取{format(hasSave)}个题目!!!")
    print("------------------------------------------------")


# 将html转换为markdown
def getMD(core, type):
    md = str(core)
    if type == "solu":
      index = md.index('"')
      pos = md.index('"', index + 1)
      md = md[index + 1: pos]
      text = urllib.parse.unquote(md)
      datas = json.loads(text)
      solutions = datas["currentData"]["solutions"]["result"]
      if len(solutions) > 0:
        solu = solutions[0]
        md = solu["content"]
        return md
      return "本题暂无题解"
    else:
      md = re.sub("<h1>","# ",md)
      md = re.sub("<h2>","## ",md)
      md = re.sub("<h3>","#### ",md)
      md = re.sub("</?[a-zA-Z]+[^<>]*>","",md)
    return md

def saveData(data, doc_name, pathh, filename):
    if not isexist(name=pathh, path=savePath + doc_name, types_name=filename):
      os.makedirs("problem" + "\\" + doc_name + pathh)
    cfilename = savePath + doc_name + pathh + "\\" + filename
    file = open(cfilename,"w",encoding="utf-8")
    for d in data:
        file.writelines(d)
    file.close()
  
def isexist(name, path=None, types_name=""):
    '''
    :param name: 需要检测的文件或文件夹名
    :param path: 需要检测的文件或文件夹所在的路径，当path=None时默认使用当前路径检测
    :return: True/False 当检测的文件或文件夹所在的路径下有目标文件或文件夹时返回Ture,
            当检测的文件或文件夹所在的路径下没有有目标文件或文件夹时返回False
    '''
    if path is None:
      path = os.getcwd()
    if os.path.exists(path + '\\' + name):
      print("Under the path: " + path + '\n' + types_name + " 存在")
      return True
    else:
      if (os.path.exists(path)):
          print("Under the path: " + path + '\n' + types_name + " 不存在，已创建")
      else:
          print("This path could not be found: " + path + '\n')
      return False

