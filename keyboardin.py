from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnmain = KeyboardButton('главное меню')

# -- главное меню --
btnprofile = KeyboardButton('профиль')
btncomp = KeyboardButton('компания')
btnload = KeyboardButton('призыв')
btnbz = KeyboardButton('культ бизнесов')
btnnext = KeyboardButton('--> другое')
mainMenu =  ReplyKeyboardMarkup(resize_keyboard = True).add(btnprofile, btncomp, btnload, btnbz, btnnext)

# -- второстипенное меню --
btninfo = KeyboardButton('помощь')
btnpp = KeyboardButton('функционал')
btngg = KeyboardButton('остров жадности')
btnother = KeyboardButton('--> вернуться')
mainMenu2 =  ReplyKeyboardMarkup(resize_keyboard = True).add(btninfo, btnpp, btngg, btnother)

# -- помощь --
btn1 = KeyboardButton('киллуа как играть')
btn2 = KeyboardButton('киллуа как ввести код')
btn3 = KeyboardButton('киллуа прочее')
helpMenu =  ReplyKeyboardMarkup(resize_keyboard = True).add(btn1, btn2, btn3, btnother)

# -- призыв --
btn4 = KeyboardButton('призвать 1')
sethero =  ReplyKeyboardMarkup(resize_keyboard = True).add(btn4, btnother)

# -- культ бизнесов --
btn6 = KeyboardButton('охрана')
btn7 = KeyboardButton('телохранитель')
btn8 = KeyboardButton('ученый')
btn9 = KeyboardButton('хантер телохранитель')
btn10 = KeyboardButton('хантер ученый')
btn11 = KeyboardButton('хантер корпорация')
btn12 = KeyboardButton('--> далее')
kyltbiznes =  ReplyKeyboardMarkup(resize_keyboard = True).add(btn6, btn7, btn8, btn9, btn10, btn11, btnother, btn12)

# -- культ бизнесов2 --

btn13 = KeyboardButton('устроиться охранником')
kyltbiznes1 =  ReplyKeyboardMarkup(resize_keyboard = True).add(btn13, btnother)