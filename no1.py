"""
遍历文件夹下所有文件并合并输出到某文件
使用命令：python 该文件 需要执行任务的文件路径（该参数不可省略）
作者：mythSun
"""

import argparse
import os
from glob import glob

# 传入参数接收变量 此种方式必须传参执行
parse = argparse.ArgumentParser()
parse.add_argument("file_path")
args = parse.parse_args()
# 检查最终file_path
print(args.file_path)
# 输入参数就是下面使用的input_path，此处把其注释，方便测试
# input_path = args.file_path

# 此处填好自己的路径，注意最后的"/",win下是双斜杠，此处方便测试，暂时写死
input_path = "F:\\pythontest\\"
# 最终存入的文件名
out_path = 'output.txt'
# 构造输出的路径，和输入路径在同一个文件夹下，如果该文件夹内没有这个文件会自动创建
output_path = os.path.join(input_path, out_path)
# 如果存在最终输出文件，先删除，防止叠加
if os.path.exists(output_path):
    os.remove(output_path)
whole_file = []
# 最终遍历的名字中带a1的文件
id_file = input_path + 'a1*'
len_file = len(glob(id_file))
print(len_file)
for file in glob(id_file):
    whole_file.append(file)
# 检查最终whole_file
print(whole_file)
content = []
# 对于每一个路径，将其打开之后，使用readlines获取全部内容
for w in whole_file:
    with open(w, 'rb') as f:
        content = content + f.readlines()
# 将内容写入文件
with open(output_path, 'wb') as f:
    f.writelines(content)
