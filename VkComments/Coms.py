import vk_api
import time

print("Скрипт на НакруткУ Комментариев.")
print("Создатель https://vk.com/chmotie")
print("группа https://vk.com/scripts_xxx")
print("Что бы продолжить пиши 1")


xyi = input("-> ")

if xyi == "1":
    owner = input("Введите цифровой ID страницы ")
    postid = input("введите ид поста")
    token = input("введите токен: ")
    kolvo = input("Введите кол-во постов")
    delay = input("введите задержку желательно 5 сек")
    message = input("текст комментария ")
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    sex = 0 
while int(sex) < int(kolvo):
    try:
        vk.wall.createComment(owner_id=owner,post_id=postid,message=message)
        sex += 1
        time.sleep(int(delay))
    except vk_api.exceptions.Captcha as captcha:
          continue