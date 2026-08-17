# login_secure.py
import hashlib

users = {
    "admin": hashlib.sha256("1234".encode()).hexdigest(),
    "user": hashlib.sha256("5678".encode()).hexdigest()
}

username = input("نام کاربری: ")
password = hashlib.sha256(input("رمز عبور: ").encode()).hexdigest()

if username in users and users[username] == password:
    print(f"✅ خوش آمدی {username}!")
else:
    print("❌ اطلاعات وارد شده اشتباه است!")