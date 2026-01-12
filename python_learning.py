#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python学习基础文件
包含：基本语法、数据类型、条件语句、循环、函数等
适合初学者学习和做简单作业
"""

# =========================================
# 1. 基本输出和注释
# =========================================
print("=== Python学习基础文件 ===")
print("Hello, Python!")  # 单行注释

# 多行注释使用三个双引号或单引号
"""
这是多行注释
用于解释代码块
"""

# =========================================
# 2. 变量和数据类型
# =========================================
print("\n=== 2. 变量和数据类型 ===")

# 整数
age = 25
print(f"年龄: {age}, 类型: {type(age)}")

# 浮点数
height = 1.75
print(f"身高: {height}, 类型: {type(height)}")

# 字符串
name = "张三"
print(f"姓名: {name}, 类型: {type(name)}")

# 布尔值
has_book = True
print(f"有书: {has_book}, 类型: {type(has_book)}")

# 空值
empty_value = None
print(f"空值: {empty_value}, 类型: {type(empty_value)}")

# =========================================
# 3. 常用数据结构
# =========================================
print("\n=== 3. 常用数据结构 ===")

# 列表 (List) - 有序可变
fruits = ["苹果", "香蕉", "橙子"]
print(f"列表: {fruits}")
fruits.append("葡萄")  # 添加元素
print(f"添加后: {fruits}")
print(f"第一个元素: {fruits[0]}")

# 元组 (Tuple) - 有序不可变
coordinates = (100, 200)
print(f"元组: {coordinates}")
print(f"x坐标: {coordinates[0]}")

# 字典 (Dictionary) - 键值对
student = {
    "name": "李四",
    "age": 20,
    "major": "计算机科学"
}
print(f"字典: {student}")
print(f"专业: {student['major']}")

# 集合 (Set) - 无序唯一
colors = {"红", "绿",  "绿色", "蓝", "蓝","红"}  # 重复元素会被自动去重
print(f"集合: {colors}")
print(f"集合大小: {len(colors)}")

# =========================================
# 4. 条件语句
# =========================================
print("\n=== 4. 条件语句 ===")

score = 85
if score >= 90:
    print(f"分数: {score}, 等级: 优秀")
elif score >= 80:
    print(f"分数: {score}, 等级: 良好")
elif score >= 60:
    print(f"分数: {score}, 等级: 及格")
else:
    print(f"分数: {score}, 等级: 不及格")

# =========================================
# 5. 循环语句
# =========================================
print("\n=== 5. 循环语句 ===")

# for循环遍历列表
print("for循环遍历水果列表:")
for fruit in fruits:
    print(f"- {fruit}")

# for循环遍历字典
print("\nfor循环遍历学生字典:")
for key, value in student.items():
    print(f"{key}: {value}")

# while循环
print("\nwhile循环计数:")
counter = 0
while counter < 5:
    print(f"计数: {counter}")
    counter += 1

# =========================================
# 6. 函数定义和调用
# =========================================
print("\n=== 6. 函数定义和调用 ===")

# 定义函数
def greet(name, greeting="你好"):
    """
    问候函数
    :param name: 姓名
    :param greeting: 问候语，默认为"你好"
    :return: 问候字符串
    """
    return f"{greeting}, {name}!"

# 调用函数
print(greet("王五"))
print(greet("赵六", "早上好"))

# 计算两个数的和
def add(a, b):
    """计算两个数的和"""
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

# =========================================
# 7. 输入和输出
# =========================================
print("\n=== 7. 输入和输出 ===")

# 输入示例（注释掉，避免运行时阻塞）
# user_name = input("请输入你的姓名: ")
# print(f"你好, {user_name}!")

# 格式化输出
print(f"{name}今年{age}岁，身高{height}米")
print("{}今年{}岁，身高{:.2f}米".format(name, age, height))

# =========================================
# 8. 异常处理
# =========================================
print("\n=== 8. 异常处理 ===")

try:
    result = 10 / 0
    print(f"结果: {result}")
except ZeroDivisionError:
    print("错误: 不能除以零")
except Exception as e:
    print(f"发生了其他错误: {e}")
finally:
    print("异常处理结束")

# =========================================
# 9. 类和面向对象
# =========================================
print("\n=== 9. 类和面向对象 ===")

class Person:
    """Person类"""
    
    def __init__(self, name, age):
        """构造方法"""
        self.name = name
        self.age = age
    
    def introduce(self):
        """自我介绍方法"""
        return f"我叫{self.name}，今年{self.age}岁"

# 创建对象
person = Person("小明", 18)
print(person.introduce())

# =========================================
# 10. 导入模块
# =========================================
print("\n=== 10. 导入模块 ===")

# 导入内置模块
import math
print(f"π的值: {math.pi}")
print(f"2的平方根: {math.sqrt(2)}")

# 从模块导入特定函数
from random import randint
random_number = randint(1, 100)
print(f"随机数(1-100): {random_number}")

# =========================================
# 11. 作业示例
# =========================================
print("\n=== 11. 作业示例 ===")

# 作业1: 编写一个函数，计算列表中所有元素的和
def sum_list(numbers):
    """计算列表中所有元素的和"""
    total = 0
    for num in numbers:
        total += num
    return total

# 测试作业1
numbers = [1, 2, 3, 4, 5]
print(f"列表{numbers}的和: {sum_list(numbers)}")

# 作业2: 编写一个函数，判断一个数是否为偶数
def is_even(number):
    """判断一个数是否为偶数"""
    return number % 2 == 0

# 测试作业2
print(f"4是偶数: {is_even(4)}")
print(f"5是偶数: {is_even(5)}")

print("\n=== Python学习基础文件结束 ===") 