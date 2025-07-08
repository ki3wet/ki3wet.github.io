import os
import re

# 中文数字到阿拉伯数字的映射
digit_map = {
    '一': '1', '二': '2', '三': '3', '四': '4', '五': '5',
    '六': '6', '七': '7', '八': '8', '九': '9', '十': '10',
}

# 章节和小节的正则
chapter_pattern = re.compile(r'第([一二三四五六七八九十])章')
section_pattern = re.compile(r'第([一二三四五六七八九十])节')

# 递归重命名函数
def rename_files_and_dirs(root):
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        # 先重命名文件
        for filename in filenames:
            new_filename = filename
            # 替换章节
            new_filename = chapter_pattern.sub(lambda m: f"第{digit_map.get(m.group(1), m.group(1))}章", new_filename)
            # 替换小节
            new_filename = section_pattern.sub(lambda m: f"第{digit_map.get(m.group(1), m.group(1))}节", new_filename)
            if new_filename != filename:
                src = os.path.join(dirpath, filename)
                dst = os.path.join(dirpath, new_filename)
                print(f"Renaming file: {src} -> {dst}")
                os.rename(src, dst)
        # 再重命名文件夹
        for dirname in dirnames:
            new_dirname = dirname
            new_dirname = chapter_pattern.sub(lambda m: f"第{digit_map.get(m.group(1), m.group(1))}章", new_dirname)
            new_dirname = section_pattern.sub(lambda m: f"第{digit_map.get(m.group(1), m.group(1))}节", new_dirname)
            if new_dirname != dirname:
                src = os.path.join(dirpath, dirname)
                dst = os.path.join(dirpath, new_dirname)
                print(f"Renaming dir: {src} -> {dst}")
                os.rename(src, dst)

if __name__ == "__main__":
    # 修改为你的实务目录路径
    root_dir = os.path.join(os.path.dirname(__file__), '../docs/certificate/中级会计/实务')
    root_dir = os.path.abspath(root_dir)
    rename_files_and_dirs(root_dir) 