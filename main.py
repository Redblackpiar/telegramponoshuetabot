from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery
import json
import os
import random
import time
from handler import keyboardin as nav
from handler import keyboard as key
TOKEN_Telegram = "5721796054:AAG97pca0p_DmJVuSL7lTkHJKXIICdXEjvM"

profile = {
	"name": "player",
	"character": "None",
	"strong": 0,
	"Coins": 0,
	"gold": 0,
	"goldsvitok": 0,
	"hp": 0,
	"def": 0,
	"speed": 0,
	"damage": 0,
	"lvl": 0,
	"exp": 0,
	"exp2": 100,
	"comm": 0,
}

profile_boss = {
	"scoreplayer": 1,
	"scoreboss": 0,
	"winner": 0
}
comm = ["1"]
sticker_rando = ["CAACAgQAAxkBAAEGMTNjV6cqnCl-jecnWCBFjlNq-EN-2AAC0lwAAuOnXQUmQdLVbac6RSoE", "CAACAgQAAxkBAAEGMTFjV6SnVmAFqXa4nRjBNF02fraylgACylwAAuOnXQXQZO0YnrumdSoE", "CAACAgQAAxkBAAEGMSZjV59GEqWltSkUV1CDhBiFtZBG5QAC0FwAAuOnXQXEW3k2DFr1jyoE", "CAACAgQAAxkBAAEGMSRjV58_p-0uj1I19obLsLYqiDxLcgACylwAAuOnXQXQZO0YnrumdSoE", "CAACAgQAAxkBAAEGMOxjV4kjXgOGjrgAAbloI6HlDzR_EJ8AAvhcAALjp10FfuOQzv9zLm4qBA", "CAACAgQAAxkBAAEGMOpjV4kdxqRm2vvXmp5IK8U-S0NiKQACF10AAuOnXQWDM-dLML1pnyoE"]
rando = ["1","1","1","1","1","1","1","2","2","2","2","2","3","3","3","4","4","4","4","4","4","4","4","4","5","5","5","5","5","6","6","6","6","6","6","6","6","6","7","7","7","8","8","8","8","9","9","9","9","9","9","10","11","11","11","12","12","12","12","12","13","13","13","13","13","14"]
client = Bot(TOKEN_Telegram, parse_mode="HTML")
dp = Dispatcher(client)
@dp.message_handler()
async def mess(message: Message):
	content = str(message.text).split(" ")
	user_Id = str(message.from_user.id)
	user_name = message.from_user['username']
	chatId = message.chat.id
	if content[0][0] == "/":
		if content[0][1:] == "start":
			await client.send_sticker(chat_id=message.from_user.id, sticker=r"CAACAgQAAxkBAAEGMOxjV4kjXgOGjrgAAbloI6HlDzR_EJ8AAvhcAALjp10FfuOQzv9zLm4qBA")
			time.sleep(2)
			await client.send_message(chat_id=chatId, text=f"привет, я киллуа золдик, я помогу тебе освоиться в этом месте, чтобы вызвать меня скажи: киллуа помоги\n(перед тем как начать игру напиши /register )")

	if content[0][0] == "/":
		if content[0][1:] == "register":
			reg = os.listdir()
			if str(f"{user_Id}.json") not in reg:
				with open(f"{user_Id}.json", "w") as file:
					json.dump(profile, file)
					await client.send_sticker(chat_id=message.from_user.id, sticker=r"CAACAgQAAxkBAAEGMTFjV6SnVmAFqXa4nRjBNF02fraylgACylwAAuOnXQXQZO0YnrumdSoE")
					time.sleep(2)
					await client.send_message(chat_id=chatId, text="регестрация прошла успешно", reply_markup = nav.mainMenu)
					with open(f"{user_Id}1.json", "w") as boss:
						json.dump(profile_boss, boss)
					with open("logs.json", "r") as log:
						logs_compl = json.load(log)
					logs_compl["logs"] += int(1)
					with open("logs.json", "w") as logs:
						json.dump(logs_compl, logs)

	if content[0] == "киллуа":
		if content[1] == "помоги":
			await client.send_sticker(chat_id=message.from_user.id, sticker=r"CAACAgQAAxkBAAEGMSZjV59GEqWltSkUV1CDhBiFtZBG5QAC0FwAAuOnXQXEW3k2DFr1jyoE")
			time.sleep(2)
			await client.send_message(chat_id=chatId, text="я могу помочь с этим:\n1. как играть\n2. как ввести код\n3. прочее\n4. доскональная инструкция(например: киллуа как играть)")

	if content[0] == "помощь":
		await client.send_sticker(chat_id=message.from_user.id, sticker=r"CAACAgQAAxkBAAEGMSZjV59GEqWltSkUV1CDhBiFtZBG5QAC0FwAAuOnXQXEW3k2DFr1jyoE")
		time.sleep(2)
		await client.send_message(chat_id=chatId, text="я могу помочь с этим:\n1. как играть\n2. как ввести код\n3. прочее\n4. доскональная инструкция(например: киллуа как играть)", reply_markup = nav.helpMenu)

	if content[0] == "киллуа":
		if content[1] == "как":
			if content[2] == "играть":
				await client.send_sticker(chat_id=message.from_user.id, sticker="CAACAgQAAxkBAAEGMTNjV6cqnCl-jecnWCBFjlNq-EN-2AAC0lwAAuOnXQUmQdLVbac6RSoE")
				time.sleep(2)
				await client.send_message(chat_id=chatId, text="краткая инструкция:\n1. устройся на работу для заработка - культ бизнесов\n2. участвуй на арене - командой: арена(в данной версии отсуствует)\n3. участвуй на небесной арене - командой: небесная арена(в данной версии отсуствует)")

			elif content[2] == "ввести":
				if content[3] == "код":
					await client.send_sticker(chat_id=message.from_user.id, sticker=random.choice(sticker_rando))
					time.sleep(2)
					await client.send_message(chat_id=chatId, text="скоро - в том смысле что кодов еще нету")

		elif content[1] == "прочее":
			await client.send_sticker(chat_id=message.from_user.id, sticker=random.choice(sticker_rando))
			time.sleep(2)
			await client.send_message(chat_id=chatId, text="прочее:\n1. профиль - показывает ваш профиль\n2. статистика - показывает всю статистику вашего аккаунта\n3. /update - показывает версию функций")

	if content[0] == "профиль":
		with open(f"{user_Id}.json", "r") as file:
			profile_load = json.load(file)
		name = profile_load["name"]
		character = profile_load["character"]
		strong = profile_load["strong"]
		Coins = profile_load["Coins"]
		await client.send_message(chat_id=chatId, text=f"ваш профиль:\nимя: {name}\nперсонаж: {character}\nмонеты: {Coins}", reply_markup=key.ikb_menu)

	if content[0] == "призыв":
		with open(f"{user_Id}.json", "r") as file:
			profile_load = json.load(file)
		gold = profile_load["gold"]
		await client.send_message(chat_id=chatId, text="одиночный призыв - 250 золота\n10 призывов за раз - 2000 золота\nчтобы совершить призыв: призвать 1 или призвать 10", reply_markup = nav.sethero)

	if content[0] == "призвать":
		if content[1] == "1":
			with open(f"{user_Id}.json", "r") as file:
				profile_load = json.load(file)
				gold = profile_load["gold"]
			if profile_load["gold"] >= 249:
				if profile_load["character"] != "None":
					await client.send_message(chat_id=chatId, text="у вас уже есть персонаж")
				elif profile_load["character"] == "None":
					profile_load["gold"] -= int(250)
					with open(f"{user_Id}.json", "w") as file:
						json.dump(profile_load, file)
					if random.choice(rando) == "1":
						photo = open("gon.jpg", "rb")
						await client.send_photo(chat_id=message.chat.id, photo=photo)
						await client.send_message(chat_id=chatId, text="вы получили персонажа:\nимя: гон фрикс\nздоровье: 500\nзащита: 50\nурон: 10\nскорость: 16\nуровень: 1\nопыт: 0/100\n\nчтобы совершить эволюцию нужен 100 уровень")
						profile_load["character"] = "gon"
						profile_load["hp"] += int(500)
						profile_load["def"] += int(50)
						profile_load["speed"] += int(16)
						profile_load["damage"] += int(10)
						profile_load["lvl"] += int(1)
						profile_load["exp"] += int(0)
						with open(f"{user_Id}.json", "w") as file:
							json.dump(profile_load, file)
					elif random.choice(rando) == "2":
						photo = open("killya.jpg", "rb")
						await client.send_photo(chat_id=message.chat.id, photo=photo)
						await client.send_message(chat_id=chatId, text="вы получили персонажа:\nимя: киллуа золдик\nздоровье: 300\nзащита: 150\nурон: 25\nскорость: 26\nуровень: 1\nопыт: 0/100\n\nчтобы совершить эволюцию нужен 100 уровень")
						profile_load["character"] = "killya"
						profile_load["hp"] += int(300)
						profile_load["def"] += int(150)
						profile_load["speed"] += int(26)
						profile_load["damage"] += int(25)
						profile_load["lvl"] += int(1)
						profile_load["exp"] += int(0)
						with open(f"{user_Id}.json", "w") as file:
							json.dump(profile_load, file)
					elif random.choice(rando) == "3":
						photo = open("kyrapika.jpg", "rb")
						await client.send_photo(chat_id=message.chat.id, photo=photo)
						await client.send_message(chat_id=chatId, text="вы получили персонажа:\nимя: курапика курута\nздоровье: 500\nзащита: 75\nурон: 30\nскорость: 18\nуровень: 1\nопыт: 0/100\n\nчтобы совершить эволюцию нужен 100 уровень")
						profile_load["character"] = "kyrapika"
						profile_load["hp"] += int(500)
						profile_load["def"] += int(75)
						profile_load["speed"] += int(18)
						profile_load["damage"] += int(30)
						profile_load["lvl"] += int(1)
						profile_load["exp"] += int(0)
						with open(f"{user_Id}.json", "w") as file:
							json.dump(profile_load, file)
					elif random.choice(rando) == "4":
						photo = open("leorio.jpg", "rb")
						await client.send_photo(chat_id=message.chat.id, photo=photo)
						await client.send_message(chat_id=chatId, text="вы получили персонажа:\nимя: Леорио Паладинайт\nздоровье: 1000\nзащита: 10\nурон: 20\nскорость: 12\nуровень: 1\nопыт: 0/100")
						profile_load["character"] = "leorio"
						profile_load["hp"] += int(1000)
						profile_load["def"] += int(10)
						profile_load["speed"] += int(12)
						profile_load["damage"] += int(20)
						profile_load["lvl"] += int(1)
						profile_load["exp"] += int(0)
						with open(f"{user_Id}.json", "w") as file:
							json.dump(profile_load, file)
					elif random.choice(rando) == "5":
						photo = open("ving.jpg", "rb")
						await client.send_photo(chat_id=message.chat.id, photo=photo)
						await client.send_message(chat_id=chatId, text="вы получили персонажа:\nимя: винг\nздоровье: 250\nзащита: 170\nурон: 45\nскорость: 16\nуровень: 1\nопыт: 0/100")
						profile_load["character"] = "ving"
						profile_load["hp"] += int(250)
						profile_load["def"] += int(170)
						profile_load["speed"] += int(16)
						profile_load["damage"] += int(45)
						profile_load["lvl"] += int(1)
						profile_load["exp"] += int(0)
						with open(f"{user_Id}.json", "w") as file:
							json.dump(profile_load, file)
					elif random.choice(rando) == "6":
						photo = open("zushi.jpg", "rb")
						await client.send_photo(chat_id=message.chat.id, photo=photo)
						await client.send_message(chat_id=chatId, text="вы получили персонажа:\nимя: зуши\nздоровье: 500\nзащита: 150\nурон: 25\nскорость: 10\nуровень: 1\nопыт: 0/100")
						profile_load["character"] = "zushi"
						profile_load["hp"] += int(500)
						profile_load["def"] += int(150)
						profile_load["speed"] += int(10)
						profile_load["damage"] += int(25)
						profile_load["lvl"] += int(1)
						profile_load["exp"] += int(0)
						with open(f"{user_Id}.json", "w") as file:
							json.dump(profile_load, file)
					elif random.choice(rando) == "7":
						photo = open("satotz.jpg", "rb")
						await client.send_photo(chat_id=message.chat.id, photo=photo)
						await client.send_message(chat_id=chatId, text="вы получили персонажа:\nимя: сатоц\nздоровье: 1200\nзащита: 150\nурон: 20\nскорость: 50\nуровень: 1\nопыт: 0/100")
						profile_load["character"] = "satotz"
						profile_load["hp"] += int(1200)
						profile_load["def"] += int(150)
						profile_load["speed"] += int(50)
						profile_load["damage"] += int(20)
						profile_load["lvl"] += int(1)
						profile_load["exp"] += int(0)
						with open(f"{user_Id}.json", "w") as file:
							json.dump(profile_load, file)
					elif random.choice(rando) == "8":
						photo = open("kalluto.jpg", "rb")
						await client.send_photo(chat_id=message.chat.id, photo=photo)
						await client.send_message(chat_id=chatId, text="вы получили персонажа:\nимя: каллуто золдик\nздоровье: 300\nзащита: 250\nурон: 50\nскорость: 16\nуровень: 1\nопыт: 0/100")
						profile_load["character"] = "kalluto"
						profile_load["hp"] += int(300)
						profile_load["def"] += int(250)
						profile_load["speed"] += int(16)
						profile_load["damage"] += int(50)
						profile_load["lvl"] += int(1)
						profile_load["exp"] += int(0)
						with open(f"{user_Id}.json", "w") as file:
							json.dump(profile_load, file)
					elif random.choice(rando) == "9":
						photo = open("colt.jpg", "rb")
						await client.send_photo(chat_id=message.chat.id, photo=photo)
						await client.send_message(chat_id=chatId, text="вы получили персонажа:\nимя: кольт\nздоровье: 500\nзащита: 100\nурон: 10\nскорость: 10\nуровень: 1\nопыт: 0/100")
						profile_load["character"] = "colt"
						profile_load["hp"] += int(500)
						profile_load["def"] += int(100)
						profile_load["speed"] += int(10)
						profile_load["damage"] += int(10)
						profile_load["lvl"] += int(1)
						profile_load["exp"] += int(0)
						with open(f"{user_Id}.json", "w") as file:
							json.dump(profile_load, file)
					elif random.choice(rando) == "10":
						photo = open("illumi.jpg", "rb")
						await client.send_photo(chat_id=message.chat.id, photo=photo)
						await client.send_message(chat_id=chatId, text="вы получили персонажа:\nимя: иллуми золдик\nздоровье: 5000\nзащита: 450\nурон: 125\nскорость: 50\nуровень: 1\nопыт: 0/100")
						profile_load["character"] = "illumi"
						profile_load["hp"] += int(5000)
						profile_load["def"] += int(450)
						profile_load["speed"] += int(50)
						profile_load["damage"] += int(125)
						profile_load["lvl"] += int(1)
						profile_load["exp"] += int(0)
						with open(f"{user_Id}.json", "w") as file:
							json.dump(profile_load, file)
					elif random.choice(rando) == "11":
						photo = open("silva.jpg", "rb")
						await client.send_photo(chat_id=message.chat.id, photo=photo)
						await client.send_message(chat_id=chatId, text="вы получили персонажа:\nимя: сильва золдик\nздоровье: 3250\nзащита: 675\nурон: 85\nскорость: 125\nуровень: 1\nопыт: 0/100")
						profile_load["character"] = "silva"
						profile_load["hp"] += int(3250)
						profile_load["def"] += int(675)
						profile_load["speed"] += int(125)
						profile_load["damage"] += int(85)
						profile_load["lvl"] += int(1)
						profile_load["exp"] += int(0)
						with open(f"{user_Id}.json", "w") as file:
							json.dump(profile_load, file)
					elif random.choice(rando) == "12":
						photo = open("gin.gif", "rb")
						await client.send_photo(chat_id=message.chat.id, photo=photo)
						await client.send_message(chat_id=chatId, text="вы получили персонажа:\nимя: джин фрикс\nздоровье: 1250\nзащита: 500\nурон: 35\nскорость: 250\nуровень: 1\nопыт: 0/100")
						profile_load["character"] = "gin"
						profile_load["hp"] += int(1250)
						profile_load["def"] += int(500)
						profile_load["speed"] += int(250)
						profile_load["damage"] += int(35)
						profile_load["lvl"] += int(1)
						profile_load["exp"] += int(0)
						with open(f"{user_Id}.json", "w") as file:
							json.dump(profile_load, file)
					elif random.choice(rando) == "13":
						photo = open("pity.jpg", "rb")
						await client.send_photo(chat_id=message.chat.id, photo=photo)
						await client.send_message(chat_id=chatId, text="вы получили персонажа:\nимя: нефирпиту(королевский страж)\nздоровье: 6000\nзащита: 654\nурон: 66\nскорость: 50\nуровень: 1\nопыт: 0/100")
						profile_load["character"] = "pity"
						profile_load["hp"] += int(6000)
						profile_load["def"] += int(654)
						profile_load["speed"] += int(50)
						profile_load["damage"] += int(66)
						profile_load["lvl"] += int(1)
						profile_load["exp"] += int(0)
						with open(f"{user_Id}.json", "w") as file:
							json.dump(profile_load, file)
					elif random.choice(rando) == "14":
						photo = open("meruem.jpg", "rb")
						await client.send_photo(chat_id=message.chat.id, photo=photo)
						await client.send_message(chat_id=chatId, text="вы получили персонажа:\nимя: меруэм(король)\nздоровье: 10000\nзащита: 1000\nурон: 250\nскорость: 550\nуровень: 1\nопыт: 0/100")
						profile_load["character"] = "meruem"
						profile_load["hp"] += int(10000)
						profile_load["def"] += int(1000)
						profile_load["speed"] += int(550)
						profile_load["damage"] += int(250)
						profile_load["lvl"] += int(1)
						profile_load["exp"] += int(0)
						with open(f"{user_Id}.json", "w") as file:
							json.dump(profile_load, file)

	if content[0] == "шанс":
		if content[1] == "призыва":
			await client.send_message(chat_id=chatId, text="COMMON:\n\nгон(форма 1) - 70%\nкиллуа(форма 1) - 50%\nкурапика(форма 1) - 30%\nлиорио - 90 %\n\nUNCOMMON:\n\nвинг - 50%\nзуши - 90%\n\nRARE:\n\nсатоц - 10%\nкаллуто золдик - 15%\nкольт - 25%\n\nLEGENDARY:\n\nиллуми золдик - 1%\nсильва золдик - 0.5%\nджин фрикс - 5%\nнеферпиту - 5.6%\nмеруэм - 0.001%")

	if content[0] == "компания":
		with open(f"{user_Id}.json", "r") as file:
			profile_load = json.load(file)
		if profile_load["character"] == "None":
			await client.send_message(chat_id=chatId, text="у вас нету персонажа")
		with open(f"{user_Id}1.json", "r") as boss:
			profile_boss1 = json.load(boss)
		if random.choice(comm) == "1":
			if profile_load["comm"] <= 10000000:
				hp1 = random.randint(1, 50)
				def1 = random.randint(1, 25)
				damage1 = random.randint(1, 10)
				speed1 = random.randint(1, 6)
				await client.send_message(chat_id=chatId, text=f"ваш противник:\nимя: dummy\nздровье: {hp1}\nзащита: {def1}\nурон: {damage1}\nскорость: {speed1}\n\n производиться сражение(пожалуста подождите)")
				time.sleep(5)
				profile_boss1["scoreplayer"] = 0
				profile_boss1["scoreboss"] = 0
				with open(f"{user_Id}1.json",  "w") as boss:
					json.dump(profile_boss1, boss)
				if hp1 <= profile_load["hp"]:
					profile_boss1["scoreplayer"] += int(1)
					with open(f"{user_Id}1.json",  "w") as boss:
						json.dump(profile_boss1, boss)
						print(hp1)

				elif hp1 >= profile_load["hp"]:
					profile_boss1["scoreboss"] += int(1)
					with open(f"{user_Id}1.json",  "w") as boss:
						json.dump(profile_boss1, boss)

				if def1 <= profile_load["def"]:
					profile_boss1["scoreplayer"] += int(1)
					with open(f"{user_Id}1.json",  "w") as boss:
						json.dump(profile_boss1, boss)
						print(def1)

				elif def1 >= profile_load["def"]:
					profile_boss1["scoreboss"] += int(1)
					with open(f"{user_Id}1.json",  "w") as boss:
						json.dump(profile_boss1, boss)

				if damage1 <= profile_load["damage"]:
					profile_boss1["scoreplayer"] += int(1)
					with open(f"{user_Id}1.json",  "w") as boss:
						json.dump(profile_boss1, boss)
						print(damage1)

				elif damage1 >= profile_load["damage"]:
					profile_boss1["scoreboss"] += int(1)
					with open(f"{user_Id}1.json",  "w") as boss:
						json.dump(profile_boss1, boss)

				if speed1 <= profile_load["speed"]:
					profile_boss1["scoreplayer"] += int(1)
					with open(f"{user_Id}1.json",  "w") as boss:
						json.dump(profile_boss1, boss)
						print(speed1)

				elif speed1 >= profile_load["speed"]:
					profile_boss1["scoreboss"] += int(1)
					with open(f"{user_Id}1.json",  "w") as boss:
						json.dump(profile_boss1, boss)

				if profile_boss1["scoreboss"] <= profile_boss1["scoreplayer"]:
					await client.send_message(chat_id=chatId, text=f"@{user_name} выиграл бой c dummy")
					profile_load["comm"] += int(1)
					with open(f"{user_Id}.json",  "w") as boss:
						json.dump(profile_load, boss)
				elif profile_boss1["scoreboss"] <= profile_boss1["scoreplayer"]:
					await client.send_message(chat_id=chatId, text=f"@{user_name} проиграл бой с dummy")

	if content[0] == "культ":
		if content[1] == "бизнесов":
			await client.send_message(chat_id=chatId, text=f"1. охрана\n2. телохранитель\n3. ученый\n4. хантер телохранитель\n5. хантер ученый\n6. хантер корпорация", reply_markup = nav.kyltbiznes)

	if content[0][0] == "/":
		if content[0][1:] == "update":
			await client.send_sticker(chat_id=message.from_user.id, sticker=r"CAACAgQAAxkBAAEGO6BjW8LvXayzF3Hs382M4jUNY3u0LwAC8VwAAuOnXQWwJ5X4QEXmWSoE")
			time.sleep(2)
			await client.send_message(chat_id=chatId, text="1. профиль - версия 1\n2. призыв/призвать - версия 1(бета)\n3. шанс призыва - версия 1(бета)\n4. компания - версия 1(бета)\n5. работы - версия 1(бета)")

	if content[0] == "охрана":
		await client.send_message(chat_id=chatId, text=f"специально для {user_name}, подробнее про работу: охранником\nзаработок: 100 монет и 5 золота в минуту\nпрокачка бизнеса не возможна\nполучение опыта не возможна")

	if content[0] == "телохранитель":
		await client.send_message(chat_id=chatId, text=f"специально для {user_name}, подробнее про работу: телохранителем\nвзнос: 500 монет\nзаработок: 400 монет и 10 золота в минуту\nпрокачка бизнеса не возможна\nполучение опыта персонажа: 10 опыта на главного персонажа(будет работать в будущем)")

	if content[0] == "ученый":
		await client.send_message(chat_id=chatId, text=f"специально для {user_name}, подробнее про работу: ученый\nвзнос: 2500 монет\nзаработок: 1000 монет и 50 золота в минуту\nпрокачка бизнеса не возможна\nполучение опыта персонажа: 20 опыта на главного персонажа(будет работать в будущем)")

	if content[0] == "хантер":
		if content[1] == "телохранитель":
			await client.send_message(chat_id=chatId, text=f"специально для {user_name}, подробнее про работу: хантер телохранитель\nвзнос: 12500 монет\nзаработок: 5000 монет и 500 золота в минуту\nпрокачка бизнеса не возможна\nполучение опыта персонажа: 50 опыта на главного персонажа(будет работать в будущем)")

	if content[0] == "хантер":
		if content[1] == "ученый":
			await client.send_message(chat_id=chatId, text=f"специально для {user_name}, подробнее про работу: хантер ученый\nвзнос: 15500 монет\nзаработок: 5500 монет и 510 золота в минуту\nпрокачка бизнеса не возможна\nполучение опыта персонажа: 80 опыта на главного персонажа(будет работать в будущем)")

	if content[0] == "хантер":
		if content[1] == "корпорация":
			await client.send_message(chat_id=chatId, text=f"специально для {user_name}, подробнее про работу: хантер\nвзнос: 155000 монет\nзаработок: 50000 монет и 1000 золота в минуту\nпрокачка бизнеса не возможна(прокачка будет в будущем)\nполучение опыта персонажа: 100 опыта на главного персонажа(будет работать в будущем)")

	if content[0] == "устроиться":
		if content[1] == "охранником":
			with open(f"{user_Id}.json", "r") as file:
				profile_load = json.load(file)
			await client.send_message(chat_id=chatId, text=f"@{user_name} стал охранником\nвы получите вознаграждение через 1 минуту")
			time.sleep(60)
			await client.send_message(chat_id=chatId, text=f"@{user_name} получает 100 монет и 5 золота за работу охранником\n\n(эта работа одноразовая, пожалуйста устройтесь заново)", reply_markup = key.ikb_menu2)
			profile_load["Coins"] += int(100)
			profile_load["gold"] += int(5)
			with open(f"{user_Id}.json", "w") as file:
				json.dump(profile_load, file)

	if content[0] == "функционал":
		await client.send_message(chat_id=chatId, text="на данный момент, функционал мал\nработает лишь одна работа охранником\nработает призыв\nработает компания\nи остольное по мелочи")

	if content[0] == "-->":
		if content[1] == "другое":
			await client.send_message(chat_id=chatId, text="клавиатура обновлена", reply_markup = nav.mainMenu2)

	if content[0] == "-->":
		if content[1] == "вернуться":
			await client.send_message(chat_id=chatId, text="клавиатура обновлена", reply_markup = nav.mainMenu)

	if content[0] == "-->":
		if content[1] == "далее":
			await client.send_message(chat_id=chatId, text="клавиатура обновлена", reply_markup = nav.kyltbiznes1)

	if content[0] == "остров":
		if content[1] == "жадности":
			await client.send_message(chat_id=chatId, text=f"специально для @{user_name}\nостров жадности будет доступен лишь хантерам\nпри победе вы получите x2 всего золота которое есть у вас\nвсего в одной игре может быть 50-500 учасников\nпри поражении вы потеряте 1500 золота", reply_markup = key.ikb_menu3)

	@dp.callback_query_handler(text="персонаж")
	async def send_message(call: CallbackQuery):
		user_Id = str(message.from_user.id)
		with open(f"{user_Id}.json", "r") as file:
			profile_load = json.load(file)
		character = profile_load["character"]
		hp = profile_load["hp"]
		defend = profile_load["def"]
		damage = profile_load["damage"]
		speed = profile_load["speed"]
		lvl = profile_load["lvl"]
		exp = profile_load["exp"]
		await call.message.answer(f"ваш персонаж: {character}\nздоровье: {hp}\nзащита: {defend}\nурон: {damage}\nскорость: {speed}\nуровень: {lvl}\nопыт: {exp}/100")

	@dp.callback_query_handler(text="охранник")
	async def send_message(call: CallbackQuery):
		user_Id = str(message.from_user.id)
		with open(f"{user_Id}.json", "r") as file:
			profile_load = json.load(file)
			await client.send_message(chat_id=chatId, text=f"@{user_name} стал охранником\nвы получите вознаграждение через 1 минуту")
			time.sleep(60)
			await client.send_message(chat_id=chatId, text=f"@{user_name} получает 100 монет и 5 золота за работу охранником\n\n(эта работа одноразовая, пожалуйста устройтесь заново)", reply_markup = key.ikb_menu2)
			profile_load["Coins"] += int(100)
			profile_load["gold"] += int(5)
			with open(f"{user_Id}.json", "w") as file:
				json.dump(profile_load, file)

	@dp.callback_query_handler(text="остров жадности")
	async def send_message(call: CallbackQuery):
		await client.send_message(chat_id=chatId, text=f"специально для @{user_name}, правила острова: \n чтобы выиграть нужно собрать все карты либо остаться последним в живых. \n чтобы найти карты, их можно покупать либо забирать у мертвых игроков либо находить на локациях игры. \n что будет если вы проиграете, вы получите увечия через которые не сможете играть в компании и т.д, так же потеряете 1500 золота")


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)