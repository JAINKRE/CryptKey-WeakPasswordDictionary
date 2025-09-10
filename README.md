# CryptKey Weak Password Dictionary

[简体中文](./README-ZH-HANS.md)

This project provides a weak password dictionary dataset for [CryptKey](https://CryptKey.jeiku.net/), designed for penetration testing and security auditing scenarios. It includes commonly used weak password entries.

To use CryptKey's weak password detection feature, please download the latest database file (.db format) from the [Release](https://github.com/JAINKRE/CryptKey-WeakPasswordDictionary/releases) page of this project. CryptKey will perform localized weak password validation based on this database.

## What is a Weak Password

A weak password typically refers to one with low security that is easily guessed or cracked by automated tools. Such passwords often exhibit the following characteristics:

- Too short, usually fewer than 8 characters;
- Use common words, numerical sequences, or consecutive keyboard keys (e.g., "123456", "qwerty", "admin");
- Contain personal information such as birthdates, names, or phone numbers;
- Do not combine uppercase letters, lowercase letters, numbers, and special symbols;
- Highly similar to common words or default passwords.

Using weak passwords significantly increases the risk of unauthorized access to accounts. Therefore, detecting and alerting weak passwords is a fundamental and critical security measure in security audits and penetration testing.


## How to Use

This project provides a `TxtToDB.py` conversion script, which requires Python 3.10 or higher to run. Users can clone this repository and execute the script to automatically generate the corresponding database file compressed in tar.gz format, which can be directly loaded by CryptKey.

If you wish to use the .db format data file from this project in other applications, you can integrate it by referring to the following code example:

```python
from TxtToDB import check_passwords_with_db

# Check weak passwords example
user_passwords = ["password123", "securepass", "123456"]
matches = check_passwords_with_db(user_passwords, "dist/WeakPassword-Top15000-v2025.09.10.db")
print("Found weak passwords:", matches)
```

The output will be as follows:

```cmd
Found weak passwords: ['password123', '123456']
```


## Building a Custom Weak Password Database

If you have specific requirements for weak password detection or wish to use a custom password list, you can build your own weak password database based on this project.

Please follow these steps:

1. Save your custom weak passwords in a text file (.txt) using UTF-8 encoding, with one password per line;
2. Modify the corresponding filenames and output database names in the `create_txt_to_db` dictionary in the `TxtToDB.py` script;
3. Run the script to generate the corresponding database file.

Please note: To ensure compatibility with CryptKey, do not modify the database structure in the `create_password_db` function.

## Data Sources

The initial weak password dataset for this project is sourced from: https://github.com/wwl012345/PasswordDic

We welcome community contributions of more comprehensive or context-specific weak password lists. If you have suggestions or improvements, please submit a Pull Request to collectively enhance password security.


## License

This project is open-sourced under the MIT License.
