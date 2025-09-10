# CryptKey Weak Password Dictionary

[English](./README.md)

本项目为 [CryptKey](https://CryptKey.jeiku.net/) 配套弱密码字典数据集，专为渗透测试及安全审计场景设计，收录常用弱密码条目。

如需使用 CryptKey 的弱密码检测功能，请从本项目的 [Release](https://github.com/JAINKRE/CryptKey-WeakPasswordDictionary/releases) 页面下载最新的数据库文件（.db格式）。CryptKey 将基于该数据库进行本地化弱密码校验。

## 什么是弱密码

弱密码（Weak Password）通常指那些安全性较低、容易被猜测或通过自动化工具破解的密码。这类密码往往具有以下特征：

- 长度过短，通常少于8个字符；
- 使用常见词汇、数字序列或键盘连续键位（如 “123456”、“qwerty”、“admin”）；
- 包含个人信息，如生日、姓名、电话号码等；
- 未组合使用大写字母、小写字母、数字及特殊符号；
- 与常见词汇或默认密码高度相似。

使用弱密码会显著增加账户被未授权访问的风险，因此在安全审计和渗透测试中，检测和提示弱密码是一项基础且关键的安全措施。

## 如何使用

本项目提供 `TxtToDB.py` 转换脚本，该脚本需在 Python 3.10 或更高版本环境中运行。用户可通过克隆本仓库后执行该脚本，自动生成对应的数据库文件并压缩为 tar.gz 格式，该格式可直接被 CryptKey 加载使用。

如需在其他项目中直接使用本项目的 .db 格式数据文件，可参考以下代码示例进行集成：

```python
from TxtToDB import check_passwords_with_db

# Check weak passwords example
user_passwords = ["password123", "securepass", "123456"]
matches = check_passwords_with_db(user_passwords, "dist/WeakPassword-Top15000-v2025.09.10.db")
print("Found weak passwords:", matches)
```

输出结果如下：

```cmd
Found weak passwords: ['password123', '123456']
```

## 自行构建弱密码db数据

如您有特定场景下的弱密码检测需求，或希望使用自定义密码列表，可基于本项目自行构建弱密码数据库。

请按如下步骤操作：

1. 将自定义弱密码按 UTF-8 编码格式保存为文本文件（.txt），每行一个密码；
2. 修改 `TxtToDB.py` 脚本中 `create_txt_to_db` 字典对应的文件名及输出数据库名称；
3. 运行脚本即可生成相应的数据库文件。

请注意，为确保与 CryptKey 兼容，请勿修改 `create_password_db` 函数中的数据库结构。

## 数据来源

本项目初始弱密码数据集源自： https://github.com/wwl012345/PasswordDic

我们欢迎社区贡献更全面或更针对特定场景的弱密码列表。如有建议或改进，请提交 Pull Request，共同提升密码安全性。

## License

本项目基于 MIT 许可协议开源。
