#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python文件操作示例
功能：演示文件的创建、写入、读取、修改等基本操作
"""

import os

def main():
    print("=== Python文件操作示例 ===")

    # 定义文件名
    filename = "test_file.txt"
    print(f"\n1. 文件名: {filename}")

    # ------------------------
    # 1. 创建并写入文件
    # ------------------------
    print("\n2. 创建并写入文件...")
    try:
        # 准备要写入的数据列表，方便统计行数
        lines_to_write = [
            "Hello, Python!\n",
            "这是一个文件操作示例。\n",
            "当前时间: 2024年1月\n",
            "文件操作是Python的基础功能。\n",  # 添加逗号，分隔第4行和第5行
            "文件操作是Python的基础功能111。\n"  # 现在这是独立的第5个元素
        ]
        
        # 写入文本数据
        with open(filename, 'w', encoding='utf-8') as f:
            # 使用writelines写入列表，自动处理每行
            f.writelines(lines_to_write)
        
        # 动态统计并输出写入的行数
        write_count = len(lines_to_write)
        print(f"   ✓ 文件创建成功！已写入{write_count}行数据")
    except Exception as e:
        print(f"   ✗ 文件创建失败: {e}")
        return

    # ------------------------
    # 2. 读取文件内容
    # ------------------------
    print("\n3. 读取文件内容...")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        print("   ✓ 文件内容:")
        print("   " + content.replace('\n', '\n   '))
    except Exception as e:
        print(f"   ✗ 文件读取失败: {e}")
        return

    # ------------------------
    # 3. 追加写入数据
    # ------------------------
    print("\n4. 追加写入数据...")
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write("\n--- 追加内容 ---\n")
            f.write("这是追加的第1行数据。\n")
            f.write("这是追加的第2行数据。\n")
        print("   ✓ 追加数据成功！")
    except Exception as e:
        print(f"   ✗ 追加数据失败: {e}")
        return

    # ------------------------
    # 4. 逐行读取文件
    # ------------------------
    print("\n5. 逐行读取文件...")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print(f"   ✓ 共 {len(lines)} 行数据:")
        for i, line in enumerate(lines, 1):
            print(f"   第 {i} 行: {line.rstrip()}")
    except Exception as e:
        print(f"   ✗ 逐行读取失败: {e}")
        return

    # ------------------------
    # 5. 修改文件内容
    # ------------------------
    print("\n6. 修改文件内容...")
    try:
        # 读取所有内容
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 修改第3行
        if len(lines) >= 3:
            lines[2] = "修改后的内容: 2024年1月9日\n"

        # 写入修改后的内容
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lines)

        # 显示修改后的内容
        with open(filename, 'r', encoding='utf-8') as f:
            modified_content = f.read()
        print("   ✓ 文件修改成功！")
        print("   修改后的内容:")
        print("   " + modified_content.replace('\n', '\n   '))
    except Exception as e:
        print(f"   ✗ 文件修改失败: {e}")
        return

    # ------------------------
    # 6. 获取文件信息
    # ------------------------
    print("\n7. 获取文件信息...")
    try:
        # 获取文件大小（字节）
        file_size = os.path.getsize(filename)

        # 获取文件创建时间
        import time
        create_time = os.path.getctime(filename)
        create_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(create_time))

        print(f"   ✓ 文件名: {filename}")
        print(f"   ✓ 文件大小: {file_size} 字节")
        print(f"   ✓ 创建时间: {create_time_str}")
        print(f"   ✓ 文件路径: {os.path.abspath(filename)}")
    except Exception as e:
        print(f"   ✗ 获取文件信息失败: {e}")

    # ------------------------
    # 7. 清理临时文件
    # ------------------------
    print("\n8. 清理临时文件...")
    try:
        os.remove(filename)
        print(f"   ✓ 临时文件已删除: {filename}")
    except Exception as e:
        print(f"   ✗ 文件删除失败: {e}")

    print("\n=== 文件操作示例完成 ===")
    print("你已经学会了Python的基本文件操作！")
    print("\n核心知识点:")
    print("- 使用 open() 函数打开文件")
    print("- 'w' 模式: 创建并写入（覆盖原有内容）")
    print("- 'r' 模式: 读取文件内容")
    print("- 'a' 模式: 追加写入数据")
    print("- 使用 with 语句自动关闭文件")
    print("- 支持中文编码 (encoding='utf-8')")

def main1():
    print("=== main ===")

if __name__ == "__main__":
    main()
    main1()
