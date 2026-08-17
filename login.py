# login.py - سیستم ورود ساده

users = {
    "admin": "1234",
    "user": "5678"
}

username = input("نام کاربری: ")
password = input("رمز عبور: ")

if username in users and users[username] == password:
    print(f"✅ خوش آمدی {username}!")
else:
    print("❌ نام کاربری یا رمز عبور اشتباه است!")