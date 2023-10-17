from pyuac import main_requires_admin
import subprocess

@main_requires_admin
def get_users():
    # Создает текстовый файл, который хранит в себе имена всех пользователей зарегистр. в системе.
    user_login = subprocess.check_output('net user').decode('cp866')
    with open ('login_user.txt', mode='a', encoding='utf-8') as file:
        file.write(str(file))
        file.close()
    # Создает пользователя и присваивает пароль, вы можете указать имя пользователя от которого
    # забыли пароль и присвоить другой по вашему усмотрению.
    return subprocess.check_output('net user Tresh 12345').decode('cp866')

if __name__=='__main__':
    get_users()