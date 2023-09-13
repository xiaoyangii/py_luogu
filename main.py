import requests as req
import time
import re
import os
from headers_config import *
from getPid import *

savePath = "E:\\桌面\\py_luogu\\problem\\"

proName = ""
proSoluName = ""
arr_problems = []

def get_problem(doc_name, total, arr_pro):
    if total == 0:
      print("未找到相关题目或当前筛选条件下无题目！！！请重新筛选")
      return
    else:
      print(f"共找到{format(total)}个相关题目")

    if not isexist(name=doc_name, path=savePath):    # 检查是否存在该分类的文件夹，如果不存在则创建
      os.makedirs("problem" + "\\" + doc_name)
    
    for i in range(total):
      print(f"正在爬取{format(arr_pro[i]['pid'])}...", end="")

      core, html = getPro(arr_pro[i]["pid"])
      core1 = getProSlu(arr_pro[i]["pid"])

      proName = getProName(core)              # 获取题目名称

      if html.find("Exception") == -1:        # 洛谷中没找到该题目或无权查看的提示网页中会有该字样
        problemMD2 = getMD(core1, "solu")     # 获取题解
        problemMD = getMD(core, "pro")        # 获取题目
        print("爬取成功！正在保存...",end="")

        path = arr_pro[i]["pid"] + "-" + proName   # 题号-题目名称
        saveData(problemMD, doc_name + "\\", path, path + ".md")
        saveData(problemMD2, doc_name + "\\", path, path + "-题解" + ".md")
        print("保存成功!")
      else:
        print("该题目不存在或无权查看")
      hasSave = i
      if i == 49:
        break
      time.sleep(random.randint(1,3))
    print("爬取完毕")
    print("共爬取{format(hasSave)}个题目!!!")


# 将html转换为markdown
def getMD(core, type):
    md = str(core)
    if type == "solu":
      type_index = md.find("type") # 查找"type"之前的内容的索引位置
      # 截取"type"之前的内容
      if type_index != -1:
          content_before_type = md[:type_index]
      else:
          content_before_type = md
      content_before_type = content_before_type[:-3]
      md = re.sub("<h1>", "# ", md)
      md = re.sub("<h2>", "## ", md)
      md = re.sub("<h3>", "#### ", md)
      md = re.sub("</?[a-zA-Z]+[^<>]*>", "", md)
    else:
      md = re.sub("<h1>","# ",md)
      md = re.sub("<h2>","## ",md)
      md = re.sub("<h3>","#### ",md)
      md = re.sub("</?[a-zA-Z]+[^<>]*>","",md)
    return md

def saveData(data, doc_name, pathh, filename):
    if not isexist(name=pathh, path=savePath + doc_name):
      os.makedirs("problem" + "\\" + doc_name + pathh)
    cfilename = savePath + doc_name + pathh + "\\" + filename
    file = open(cfilename,"w",encoding="utf-8")
    for d in data:
        file.writelines(d)
    file.close()
  
def isexist(name, path=None):
    '''
    :param name: 需要检测的文件或文件夹名
    :param path: 需要检测的文件或文件夹所在的路径，当path=None时默认使用当前路径检测
    :return: True/False 当检测的文件或文件夹所在的路径下有目标文件或文件夹时返回Ture,
            当检测的文件或文件夹所在的路径下没有有目标文件或文件夹时返回False
    '''
    if path is None:
      path = os.getcwd()
    if os.path.exists(path + '\\' + name):
      print("Under the path: " + path + '\n' + name + " is exist")
      return True
    else:
      if (os.path.exists(path)):
          print("Under the path: " + path + '\n' + name + " is not exist")
      else:
          print("This path could not be found: " + path + '\n')
      return False


