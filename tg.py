import requests
TOKEN = "5644081136:AAG0l0HKCIvG1QMOBbD4StGxFiiJTgmTcbQ"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())

# import requests
# TOKEN = "5644081136:AAG0l0HKCIvG1QMOBbD4StGxFiiJTgmTcbQ"
# chat_id = "2118205691"
# message = "hello from Edgari bot"
# url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
# print(requests.get(url).json()) # this sends the message