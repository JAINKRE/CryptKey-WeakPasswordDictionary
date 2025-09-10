import sqlite3
import tarfile
import os

def create_password_db(text_file, db_file):
    if os.path.exists(db_file):
        os.remove(db_file)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE passwords (password TEXT PRIMARY KEY)')
    batch_size = 10000
    batch = []
    with open(text_file, 'r', encoding='utf-8') as f:
        for line in f:
            batch.append((line.strip(),))
            if len(batch) >= batch_size:
                cursor.executemany('INSERT OR IGNORE INTO passwords VALUES (?)', batch)
                batch = []
        if batch:
            cursor.executemany('INSERT OR IGNORE INTO passwords VALUES (?)', batch)
    
    conn.commit()
    conn.close()

def check_passwords_with_db(user_passwords, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    weak_passwords = []
    for password in user_passwords:
        cursor.execute('SELECT 1 FROM passwords WHERE password = ?', (password,))
        if cursor.fetchone():
            weak_passwords.append(password)
    
    conn.close()
    return weak_passwords


if __name__ == '__main__':

    version = "2025.09.10"

    output_folder = "dist"
    os.makedirs(output_folder, exist_ok=True)

    create_txt_to_db = {
        "WeakPassword-14M.txt":"WeakPassword-14M.db",
        "WeakPassword-Top15000.txt":"WeakPassword-Top15000.db",
        "Passwd-Top1000.txt":"Passwd-Top1000.db",
        "Passwd-EN-Top10000.txt":"Passwd-EN-Top10000.db",
        "Passwd-CN-Top10000.txt":"Passwd-CN-Top10000.db",
    }

    # Automatically iterate and create all databases
    for text_file, db_file in create_txt_to_db.items():
        if os.path.exists(text_file):
            db_name_without_ext = os.path.splitext(db_file)[0]
            versioned_db_file = f"{db_name_without_ext}-v{version}.db"
            output_db_path = os.path.join(output_folder, versioned_db_file)
            
            print(f"Processing {text_file} -> {output_db_path}")
            create_password_db(text_file, output_db_path)
        else:
            print(f"Warning: File {text_file} does not exist, skipping processing.")

    # Package each generated db file into its own tar.gz archive
    for db_file in create_txt_to_db.values():
        db_name_without_ext = os.path.splitext(db_file)[0]
        versioned_db_file = f"{db_name_without_ext}-v{version}.db"
        db_path = os.path.join(output_folder, versioned_db_file)
        
        if os.path.exists(db_path):
            archive_name = f"{db_name_without_ext}-v{version}.tar.gz"
            archive_path = os.path.join(output_folder, archive_name)
            
            with tarfile.open(archive_path, "w:gz") as tar:
                tar.add(db_path, arcname=versioned_db_file)
            
            # Remove the db file after packaging
            os.remove(db_path)
            
            print(f"Packaged {versioned_db_file} into {archive_path} and removed the original db file")
        else:
            print(f"Warning: {db_path} not found, skipping packaging")

    # Check weak passwords example
    #user_passwords = ["password123", "securepass", "123456"]
    #matches = check_passwords_with_db(user_passwords, "WeakPassword-14M.db")
    #print("Found weak passwords:", matches)
