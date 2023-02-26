from aiogram import Bot, Dispatcher, executor, types
import datetime as dt

token = 'enter a tocken here :)'
bot = Bot(token=token)
dp = Dispatcher(bot=bot)

data = {
    'Сычёв': {
        0: ['08:30 - 10:00', '14:00 - 15:30'],
        1: ['08:30 - 10:00', '10:15 - 11:45', '12:15 - 13:45', '14:00 - 15:30'],
        2: ['10:15 - 11:45', '12:15 - 13:45', '14:00 - 15:30'],
        3: ['08:30 - 10:00', '10:15 - 11:45', '12:15 - 13:45', '14:00 - 15:30'],
        4: ['08:30 - 10:00', '10:15 - 11:45', '14:00 - 15:30']
    },
    'Французова': {
        0: ['08:30 - 10:00', '14:00 - 15:30'],
        1: ['08:30 - 10:00', '10:15 - 11:45', '12:15 - 13:45', '14:00 - 15:30'],
        2: ['10:15 - 11:45', '12:15 - 13:45', '14:00 - 15:30'],
        3: ['08:30 - 10:00', '10:15 - 11:45', '12:15 - 13:45', '14:00 - 15:30'],
        4: ['08:30 - 10:00', '10:15 - 11:45', '14:00 - 15:30']
    },
    'Сафронова': {
        0: ['08:30 - 10:00', '14:00 - 15:30'],
        1: ['08:30 - 10:00', '10:15 - 11:45', '12:15 - 13:45', '14:00 - 15:30'],
        2: ['10:15 - 11:45', '12:15 - 13:45', '14:00 - 15:30'],
        3: ['08:30 - 10:00', '10:15 - 11:45', '12:15 - 13:45', '14:00 - 15:30'],
        4: ['08:30 - 10:00', '10:15 - 11:45', '14:00 - 15:30']
    },
    'Редькин': {
        0: ['08:30 - 10:00', '14:00 - 15:30'],
        1: ['08:30 - 10:00', '10:15 - 11:45', '12:15 - 13:45', '14:00 - 15:30'],
        2: ['10:15 - 11:45', '12:15 - 13:45', '14:00 - 15:30'],
        3: ['08:30 - 10:00', '10:15 - 11:45', '12:15 - 13:45', '14:00 - 15:30'],
        4: ['08:30 - 10:00', '10:15 - 11:45', '14:00 - 15:30']
    }
}


@dp.message_handler(commands=['start'])
async def start_handler(message: types.message):
    starts_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Сычёв', 'Французова', 'Сафронова', 'Редькин']
    for button in buttons:
        starts_markup.add(button)

    await message.reply('Привет!'
                        '\nЯ помогу тебе узнать, когда преподователь свободен.'
                        '\nНажми на кнопку нужного преподователя',
                        reply_markup=starts_markup)


@dp.message_handler(content_types=['text'])
async def another_handler(message: types.message):
    today_is = dt.datetime.today().weekday()
    output_string = 'Расписание преподователя на сегодня: '

    if message.text == 'Сычёв' or message.text == 'Французова' or message.text == 'Сафронова' \
            or message.text == 'Редькин':
        if today_is > 4:
            time = 0
        else:
            time = today_is
        for i in data[message.text][time]:
            output_string += '\n' + i
        await message.reply(output_string)

    else:
        await message.reply('Я тебя не понимаю')


if __name__ == '__main__':
    executor.start_polling(dp)
