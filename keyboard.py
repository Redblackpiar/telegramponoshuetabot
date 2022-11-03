from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=1,
								inline_keyboard=[
									[
										InlineKeyboardButton(text="персонаж", callback_data="персонаж"),
									],
								])

ikb_menu2 = InlineKeyboardMarkup(row_width=1,
								inline_keyboard=[
									[
										InlineKeyboardButton(text="начать заново", callback_data="охранник"),
									],
								])

ikb_menu3 = InlineKeyboardMarkup(row_width=1,
								inline_keyboard=[
									[
										InlineKeyboardButton(text="правила острова", callback_data="остров жадности"),
									],
								])
