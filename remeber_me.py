import json

def get_stored_username():
    file_name = 'username.json'
    try:
        with open(file_name) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("请输入姓名")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("wlecome back!" + username)
    else:
        username = input("what is your name?")
        with open(file_name, 'w') as f_obj:
            json.dump(username,f_obj)
            print("We will remeber you when you come back!"+ username)



get_new_username()
