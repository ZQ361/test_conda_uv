import sys
import platform

print("=" * 50)
print("环境验证报告")
print("=" * 50)
print(f"Python 版本: {sys.version}")
print(f"Python 路径: {sys.executable}")
print(f"操作系统: {platform.platform()}")
print(f"当前环境: {sys.prefix}")
print("=" * 50)

# 检查是否在 conda 环境中
if "conda" in sys.prefix:
    print("✅ 当前在 Conda 虚拟环境中")
else:
    print("⚠️  当前在全局 Python 环境中")