#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SVN连接示例脚本 - 增强版
尝试多种连接方式和协议
"""

import requests
import subprocess

def main():
    print("=== SVN连接示例（增强版）===")
    
    # 配置信息
    username = "zhangw"
    password = "Dm123456"
    
    # 尝试不同的URL和协议
    svn_urls = [
        "https://192.168.1.189/svn/DigiPolicy_MetLife",  # 新的HTTPS地址
        "http://192.168.1.189/svn/DigiPolicy_MetLife",   # 新的HTTP地址
        "svn://192.168.1.189/DigiPolicy_MetLife"         # 新的SVN协议地址
    ]
    
    for svn_url in svn_urls:
        print(f"\n=== 测试连接: {svn_url} ===")
        
        # 1. 测试基本网络连通性（ping）
        print("\n1. 测试网络连通性（ping）:")
        try:
            # 提取IP地址
            ip = svn_url.split("://")[1].split("/")[0].split(":")[0]
            result = subprocess.run(
                ["ping", "-c", "2", ip],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                print(f"   ✓ 能ping通服务器 {ip}！")
            else:
                print(f"   ✗ 无法ping通服务器 {ip}！")
                print(f"     输出: {result.stderr[:200]}...")
        except Exception as e:
            print(f"   ✗ ping测试失败: {e}")
        
        # 2. 测试HTTP/HTTPS连接（如果适用）
        if svn_url.startswith(("http://", "https://")):
            print("\n2. 测试HTTP/HTTPS连接:")
            try:
                # 禁用证书验证，设置较短超时
                response = requests.get(
                    svn_url,
                    auth=(username, password),
                    verify=False,
                    timeout=5,
                    headers={"User-Agent": "Mozilla/5.0"}
                )
                print(f"   ✓ HTTP状态码: {response.status_code}")
                print(f"   ✓ 响应内容类型: {response.headers.get('Content-Type', '未知')}")
                if len(response.text) > 0:
                    print(f"   ✓ 响应前100字符: {response.text[:100]}...")
            except Exception as e:
                print(f"   ✗ HTTP连接失败: {e}")
        
        # 3. 尝试使用subprocess调用svn命令（如果有）
        print("\n3. 测试svn命令行工具:")
        try:
            # 检查svn命令是否存在
            which_result = subprocess.run(
                ["which", "svn"],
                capture_output=True,
                text=True,
                timeout=2
            )
            if which_result.returncode == 0:
                print(f"   ✓ svn命令路径: {which_result.stdout.strip()}")
                
                # 尝试svn info命令
                svn_result = subprocess.run(
                    [
                        "svn", "info",
                        "--username", username,
                        "--password", password,
                        "--non-interactive",
                        "--trust-server-cert",
                        svn_url
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if svn_result.returncode == 0:
                    print(f"   ✓ svn info命令执行成功！")
                    print(f"   ✓ 输出: {svn_result.stdout[:300]}...")
                else:
                    print(f"   ✗ svn info命令失败: {svn_result.returncode}")
                    print(f"     错误: {svn_result.stderr[:200]}...")
            else:
                print("   ✗ 未找到svn命令")
        except Exception as e:
            print(f"   ✗ 调用svn命令失败: {e}")
    
    print("\n=== 诊断总结 ===")
    print("1. 检查了3种可能的SVN访问协议")
    print("2. 测试了网络连通性（ping）")
    print("3. 尝试了HTTP/HTTPS连接")
    print("4. 检查了svn命令行工具")
    print("\n=== 建议 ===")
    print("1. 确认公司SVN服务器的正确访问地址和协议")
    print("2. 检查是否需要特殊的网络设置或VPN")
    print("3. 联系公司IT部门获取正确的SVN访问信息")
    print("4. 尝试使用公司提供的SVN客户端工具")
    
    print("\n=== 脚本执行结束 ===")

if __name__ == "__main__":
    main()
