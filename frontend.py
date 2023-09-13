import tkinter as tk
import tkinter.font as tkfont
from tkinter import scrolledtext # 导入 scrolledtext 模块
import sys
from getPid import get_pid
from main import *

# 难度选项和对应的difficulty值
difficulty_options = {
    "暂无评定": 0,
    "入门": 1,
    "普及-": 2,
    "普及/提高-": 3,
    "普及+/提高": 4,
    "提高+/省选-": 5,
    "省选/NOI-": 6,
    "NOI/NOI+/CTSC": 7
}

type_options = {
    "洛谷": "B%7CP",
    "主题库": "P",
    "入门与面试": "B",
    "CodeForces": "CF",
    "SPOJ": "SP",
    "AtCoder": "AT",
    "UVA": "UVA",
}

# 创建主窗口
root = tk.Tk()
root.title("洛谷题库爬取")
root.geometry("1000x800")  # 设置窗口大小为1000x800
root.configure(bg="white")  # 设置背景颜色为白色

# 设置字体样式
font_style = tkfont.Font(family="微软雅黑", size=18)
font_style_warning = tkfont.Font(family="微软雅黑", size=18, weight="bold")

# 设置行列空白间隔
root.rowconfigure(0, pad=20)
root.rowconfigure(1, pad=20)
root.rowconfigure(2, pad=20)
root.rowconfigure(3, pad=20)
root.columnconfigure(0, pad=10)
root.columnconfigure(1, pad=10)

# 创建类型值Label，设置宽度以对齐其他标签
type_label = tk.Label(root, text="类型:", font=font_style, bg="white", width=6)
type_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

# 创建单选按钮
selected_type = tk.StringVar()
column_counter = 1

for type_key in type_options.keys():
    if type_key == "洛谷":
        type_button = tk.Radiobutton(root, text="      洛谷      ", variable=selected_type, value=type_key, font=font_style,
                                 indicatoron=0, bg="white", selectcolor="#E0F7FF", highlightthickness=0)
    else:
        type_button = tk.Radiobutton(root, text=type_key, variable=selected_type, value=type_key, font=font_style,
                                 indicatoron=0, bg="white", selectcolor="#E0F7FF", highlightthickness=0)
    type_button.grid(row=0, column=column_counter, padx=10, pady=10, sticky="w")
    column_counter += 1
selected_type.set("洛谷")  # 默认选择洛谷

# 创建一个 Frame 用于包含关键词 Label 和输入框
keyword_frame = tk.Frame(root, bg="white")
keyword_frame.grid(row=1, column=0, columnspan=24, padx=10, pady=10, sticky="ew")

# 创建关键词 Label，设置宽度以对齐其他标签
keyword_label = tk.Label(keyword_frame, text="关键字:", font=font_style, bg="white", width=6)
keyword_label.pack(side="left", padx=(0, 10), pady=10)

# 创建关键词输入框，并增加宽度、边框
keyword_entry = tk.Entry(keyword_frame, font=font_style, width=25, borderwidth=2, relief="solid")  # 增大宽度并添加边框
keyword_entry.pack(side="left", padx=20, pady=10)

# 创建关键词提示信息 Label，设置宽度以对齐其他标签
keyword_label = tk.Label(keyword_frame, text="多个关键词以顿号(、)分开！！！", font=font_style_warning, bg="white", width=30, fg="red")
keyword_label.pack(side="left", padx=(0, 10), pady=10)

# 创建难度值输入框，并增加宽度和高度以及font_style样式，设置宽度以对齐其他标签
difficulty_label = tk.Label(root, text="难度:", font=font_style, bg="white", width=6)
difficulty_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
selected_difficulty = tk.StringVar()
difficulty_menu = tk.OptionMenu(root, selected_difficulty, *difficulty_options.keys())
difficulty_menu.config(width=7, height=1, font=font_style)  # 设置宽度、高度和样式
difficulty_menu.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# 创建一个 Frame 用于包含文本区域
text_frame = tk.Frame(root, bg="white")
text_frame.grid(row=5, column=0, columnspan=5, padx=10, pady=10, sticky="ew")

# 创建一个 Frame 用于包含文本区域
text_frame = tk.Frame(root, bg="white")
text_frame.grid(row=5, column=0, columnspan=5, padx=10, pady=10, sticky="ew")

# 创建一个Text组件用于显示控制台输出
output_text = scrolledtext.ScrolledText(text_frame, font=font_style, width=30, height=10, bg="#E0F7FF", relief="solid", bd=2)
output_text.pack()

# 创建一个函数来将标准输出重定向到文本区域
def redirect_output():
    sys.stdout.write = output_text.insert("end", str)  # 重定向标准输出
    sys.stderr.write = output_text.insert("end", str)  # 重定向标准错误


# 创建一个函数来获取用户输入并构建URL
def get_url():
    keyword = keyword_entry.get() # 获得用户输入的关键词
    if keyword:
        keywords = keyword.replace("、", "-")  # 如果有关键词，就分割
    else:
        keywords = "无关键词"  # 如果没有关键词，就默认无关键词，用于生成文件夹名称
    difficulty = difficulty_options[selected_difficulty.get()] if selected_difficulty.get() else ""  # 如果没有选择难度，就默认为""
    if difficulty == "":
        difficult = "全部"  # 如果没有选择难度，就默认为返回全部，用于生成文件夹名称
    else:
        difficult = selected_difficulty.get()  # 如果有选择难度，就用选择的难度，用于生成文件夹名称
    type_value = type_options[selected_type.get()]  # 获得用户选择的类型，用于构建URL
    # 构建文件名
    doc_parts = [difficult, keywords]
    doc_name = '-'.join(doc_parts)
    # 构建URL
    params = {"difficulty": difficulty, "type": type_value, "page": 1, "_contentOnly": 1}
    url = f"https://www.luogu.com.cn/problem/list?type={type_value}&difficulty={difficulty}&keyword={keyword}&page=1"
    return url, params, doc_name

def main():
    url, params, doc_name = get_url()
    total, arr_pro = get_pid(url, params)
    get_problem(doc_name, total, arr_pro)
    
    
# 创建一个按钮，当用户点击时调用get_numby_problems函数，使其与上面的难度选择器对齐并适当增加宽高
search_button = tk.Button(root, text=" 搜索 ", command=main, font=font_style, width=8, height=1)
search_button.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# 运行tkinter应用程序
root.mainloop()