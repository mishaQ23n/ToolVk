import vk_api
import time
import os
import colorama
import random
from colorama import Fore, Back,Style
from vk_api.utils import get_random_id
colorama.init()

priva = [
"""

██████╗░░█████╗░░██████╗░██████╗██╗██╗░░░░░██╗░░██╗░█████╗░███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██║██║░░░░░██║░██╔╝██╔══██╗██╔════╝
\033[32m██████╔╝███████║╚█████╗░╚█████╗░██║██║░░░░░█████═╝░███████║█████╗░░
██╔══██╗██╔══██║░╚═══██╗░╚═══██╗██║██║░░░░░██╔═██╗░██╔══██║██╔══╝░░
██║░░██║██║░░██║██████╔╝██████╔╝██║███████╗██║░╚██╗██║░░██║██║░░░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░


                            Создатель: @chmotie
                            Группа: @scripts_xxx 
                            Version: 0.1
1)Включить рассылку
"""
]

print(priva[0])
vibor = input("->")
if vibor == "1":
	token = input("Token:")
	vk_session = vk_api.VkApi(token=token)
	vk = vk_session.get_api()
friends = vk.friends.get()['items']
for pas in friends:
	try:
		vk.messages.send(user_id=pas,message="ку-ку, братишка",random_id=get_random_id())
		time.sleep(2)
		friends = vk.friends.get()['items']
	except vk_api.exceptions.ApiError:
		continue
