import sys
import re

def add_dash_to_choices(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    # 匹配行首，允许最多4个空格或任意数量的tab，然后A-D. 
    pattern = re.compile(r'^([ \t]{0,4})([A-D])\. ')
    # 匹配已经有 - A. 的行，避免重复
    dash_pattern = re.compile(r'^([ \t]{0,4})- [A-D]\. ')

    for line in lines:
        if dash_pattern.match(line):
            new_lines.append(line)
        elif pattern.match(line):
            new_line = pattern.sub(r'\1- \2. ', line)
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python add_dash_to_choices.py <文件路径>")
        sys.exit(1)
    add_dash_to_choices(sys.argv[1])
    print("处理完成！")