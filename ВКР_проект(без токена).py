# основная рабочая программа

import telebot
from telebot import types

bot = telebot.TeleBot("ТОКЕН")
markdown = ""

# кнопка обратной связи в клаве
markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

BUT = types.KeyboardButton(text="Кнопка обратной связи 📩")
markup.add(BUT)

# информация о боте
@bot.message_handler(commands=["help"])
def send_welcome(message):
    bot.reply_to(message, "{0.first_name},\n\nменя зовут *RED-коллега*.\n\nЯ — ваш интерактивный помощник и по совместительству корпоративный бот «Красного квадрата».\n\nПомогу вам узнать информацию о нашей компании, найти коллегу и понять, по каким вопросам к нему можно обратиться, уточню организационные моменты — расскажу, как правильно взять отпуск, как заказать курьера🏃‍♂️\n\nНовым сотрудникам помогу адаптироваться к нашим условиям — расскажу о главных кабинетах, проведении первого инструктажа для новоиспеченных коллег, помогу в печати файлов, угощу в нашем телевизионном кафе🙌🏻\n\nСвои идеи или замечания можете оставить мне, нажав на встроенную кнопку обратной связи📩\n\nЕще умею общаться не только по кнопкам, но и текстом, поэтому можете мне писать✍🏻 Правда, я не до конца научился распознавать все слова и форматы, поэтому не обижайтесь, если не отвечу на ваш вопрос🤗\n\nНажмите на встроенную кнопку «Основное меню» или напишите мне /menu, и я пришлю актуальные темы, на которые сможем пообщаться.".format(
             message.from_user), parse_mode="Markdown")

# основное меню
@bot.message_handler(commands=["menu"])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="О компании 🟥", callback_data="1")
    but_2 = types.InlineKeyboardButton(text="Организационные вопросы 📎", callback_data="2")
    but_3 = types.InlineKeyboardButton(text="Для новых сотрудников 🆕", callback_data="3")
    but_4 = types.InlineKeyboardButton(text="Найти коллегу 👩🏻‍💻", callback_data="4")
    but_5 = types.InlineKeyboardButton(text="Еда в стакане 🥤", callback_data="5")
    but_6 = types.InlineKeyboardButton(text="Вакансии ✅", callback_data="6")

    markup_inline.add(but_1)
    markup_inline.add(but_2)
    markup_inline.add(but_3)
    markup_inline.add(but_4)
    markup_inline.add(but_5)
    markup_inline.add(but_6)

    bot.send_message(message.chat.id,
                 "{0.first_name},\n\nя собрал самые популярные вопросы в одном разделе и, чтобы вам было проще, разделил их на категории. Пожалуйста, выберите категорию:".format(
                     message.from_user), parse_mode="Markdown", reply_markup=markup_inline)

# категория "О компании"
@bot.callback_query_handler(func=lambda call: call.data == "1")
def get_user_info(call):
    bot.answer_callback_query(callback_query_id=call.id, text="Минуточку, готовлю новые категории")
    if call.data == "1":
        markup_inline1 = types.InlineKeyboardMarkup()
        but_1_1 = types.InlineKeyboardButton(text="Позиционирование 🟥", callback_data="1_1")
        but_1_2 = types.InlineKeyboardButton(text="Сайт ↗️", url="https://www.red-red.ru/", callback_data="1_2")
        but_1_3 = types.InlineKeyboardButton(text="О компании в цифрах 🏆", callback_data="1_3")
        but_1_4 = types.InlineKeyboardButton(text="Направления деятельности ↗️", callback_data="1_4")
        but_1_5 = types.InlineKeyboardButton(text="Ценности 🧩", callback_data="1_5")
        but_1_6 = types.InlineKeyboardButton(text="Вселенная «Красного квадрата» 🌠",
                                             url="https://cloud.mail.ru/public/cMTV/GyLLkNMxb", callback_data="1_6")

        markup_inline1.add(but_1_1)
        markup_inline1.add(but_1_2)
        markup_inline1.add(but_1_3)
        markup_inline1.add(but_1_4)
        markup_inline1.add(but_1_5)
        markup_inline1.add(but_1_6)
        bot.send_message(call.message.chat.id,
                         "{0.first_name},\nчто именно хотите узнать о компании?".format(call.from_user),
                         parse_mode="Markdown",
                         reply_markup=markup_inline1)

@bot.callback_query_handler(func=lambda call: call.data == "1_1")
def callback_query(call):
    if call.data == "1_1":
        bot.send_photo(call.message.chat.id, "https://cloud.mail.ru/public/vuWp/qc5Qoqr5D",
               caption="*Красный квадрат* — российская креативно-технологическая компания, один из лидеров в области производства мультимедиа контента.\n\nОпытная команда запускает самые популярные телевизионные проекты, организует международные культурные фестивали, деловые форумы, спортивные соревнования и масштабные церемонии. Специалисты компании создают спектакли и мюзиклы, ледовые и цирковые шоу, интерактивные музеи и тематические парки.\n\nБлагодаря консолидации лучших творческих, инженерно-технических и продюсерских ресурсов медиагруппа «Красный квадрат» входит в число признанных лидеров медиарынка и уже сегодня занимается созданием контента будущего.",
               parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "1_3")
def callback_query(call):
    if call.data == "1_3":
        bot.send_message(call.message.chat.id,
                 "*О «Красном квадрате» в цифрах*:\n\n— На данный момент в компании работает более 500 человек.\n— Реализовано более 650 проектов по всем направлениям деятельности, включая международные проекты в 14-ти странах.\n— Более 12 000 телевизионного эфира.\n— Выпустили более 450 часов сериалов.\n— Сотрудничали с более чем 17 российскими телеканалами.\n— Собрали более 600 млн просмотров на YouTube.\n— Создали более 180 документальных фильмов.\n— Отмечены 130 номинациями и 50 наградами телевизионной премии ТЭФИ, а также победами на международных фестивалях.\n— Библиотека видеофонда насчитывает более 10 000 часов контента и уникальный архив.",
                 parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "1_4")
def callback_query(call):
    if call.data == "1_4":
        bot.send_message(call.message.chat.id,
                 "Среди основных направлений деятельности «Красного квадрата» выделяются:\n\n*Мультимедиа*. Контент для аттракционов, фильмы в формате 360°, а также VR, AR, MR и другие форматы нового типа. Высочайший уровень экспертизы, самые популярные площадки с посещаемостью более 10 млн человек, внедрение новых технологий, сотрудничество с мировыми лидерами на рынке, международные награды.\n\n*Городская среда*. Создание первых в России тематических парков и аттракционов, где развлечения объединяются с образованием. Работа с общественными пространствами городов, культурным наследием страны и объектами исторической значимости.\n\n*Образование*. Запуск образовательных проектов, охватывающих все возрастные категории для развития современной медиа индустрии. Собственные студии и творческие мастерские, хакатоны, школа, академия, программа дополнительного образования, программы стажировки.\n\n*Мероприятия*. Деловые форумы, международные конгрессы и мультимедиа выставки. Реализация федеральных событий с участием первых лиц государства.\n\n*Интернет*. Производство digital-контента, задающего новые стандарты качества для российского интернет-пространства. Десятки сайтов и успешных площадок в социальных сетях, более 300 млн просмотров на YouTube.\n\n*Шоу*. Мероприятия национального масштаба: церемонии, премии, мультимедиа спектакли, масштабные постановочные шоу. Десятки реализованных авторских проектов федерального уровня. Самые сложные технические решения.\n\n*Музыка*. Собственный лейбл, музыкальная студия, продюсерский центр, акустический оркестр. Количество концертов и музыкальных шоу, организованных компанией, превышает несколько сотен.\n\n*Спорт*. Сотрудничество с федерациями и спортивными клубами, обеспечение трансляций знаковых спортивных событий. Серьезный опыт sport production на российских и международных проектах. Фильмы о спорте заслужили награды на международной арене.\n\n*Коммуникации*. Комплексные решения для поддержки и продвижения бренда. Спонсорские кампании более чем для 500 отечественных и зарубежных брендов.",
                 parse_mode="Markdown")
        medias = [types.InputMediaPhoto("https://cloud.mail.ru/public/s2zt/ZDLH9gMxt"),
          types.InputMediaPhoto("https://cloud.mail.ru/public/DHdm/1aA6SC3Ep"),
          types.InputMediaPhoto("https://cloud.mail.ru/public/KUAG/oBAkHdE1T"),
          types.InputMediaPhoto("https://cloud.mail.ru/public/Ezwg/uvVPYHe45"),
          types.InputMediaPhoto("https://cloud.mail.ru/public/s6Vh/zJLzUfG5a"),
          types.InputMediaPhoto("https://cloud.mail.ru/public/8VzQ/PwQkj7Abc"),
          types.InputMediaPhoto("https://cloud.mail.ru/public/kmG5/YmMSQ7XKZ"),
          types.InputMediaPhoto("https://cloud.mail.ru/public/AKjy/kbMVzaZKQ"),
          types.InputMediaPhoto("https://cloud.mail.ru/public/ddMG/nTBgXfySE")]
        bot.send_media_group(call.message.chat.id, medias)

@bot.callback_query_handler(func=lambda call: call.data == "1_5")
def callback_query(call):
    if call.data == "1_5":
        bot.send_photo(call.message.chat.id, "https://cloud.mail.ru/public/VwiZ/BG2MiMBWD",
               caption="*Красный квадрат — компания опережающего развития* 🟥\n\nНаши ценности:\n\n— Уважение к профессии\n— Обучение и развитие\n— Поиск инноваций\n— Внимание к истории\n— Спортивный характер\n— Осознанное отношение к природе\n— Социальная ответственность\n\n  ",
               parse_mode="Markdown")

# категория "Организационные вопросы"
@bot.callback_query_handler(func=lambda call: call.data == "2")
def get_user_info(call):
    bot.answer_callback_query(callback_query_id=call.id, text="Организованность — мой конек! Сейчас все будет😉")
    if call.data == "2":
        markup_inline2 = types.InlineKeyboardMarkup()
        but_2_1 = types.InlineKeyboardButton(text="Печать файлов в офисе 🖨", callback_data="2_1")
        but_2_2 = types.InlineKeyboardButton(text="Как правильно уйти в отпуск 🌴", callback_data="2_2")
        but_2_3 = types.InlineKeyboardButton(text="Курьер 📦", callback_data="2_3")

        markup_inline2.add(but_2_1)
        markup_inline2.add(but_2_2)
        markup_inline2.add(but_2_3)
        bot.send_message(call.message.chat.id, "{0.first_name},\nкакую категорию выберем?".format(call.from_user),
                 parse_mode="Markdown",
                 reply_markup=markup_inline2)

@bot.callback_query_handler(func=lambda call: call.data == "2_1")
def callback_query(call):
    if call.data == "2_1":
        bot.send_photo(call.message.chat.id, "http://risovach.ru/upload/2016/08/mem/1_121602134_orig_.jpg",
               caption="*Печать файлов в офисе👩🏻‍💻*\n\nЕсли вам нужно напечатать файл, то вы можете это сделать со своего рабочего компьютера. Просто нажмите на значок принтера в программе, в которой работаете, и выберите один из доступных принтеров (в названии принтера указан номер кабинета, где можно будет забрать распечатанный файл). \n\nЕсли к вашему компьютеру не подключен никакой принтер, то нужно обратиться к Инженеру отдела информационных технологий (ИТ) по внутреннему телефону +7 (495) 646-34-64 (доб. 1111) и попросить настроить печать на рабочем компьютере.\n\nТакже можете обратиться на ресепшн и попросить напечатать ваш файл. Для этого заранее можно отправить файл в письме на электронную почту reception@red-red.ru, указав в теме письма «Запрос на печать» + свою фамилию.",
               parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "2_2")
def callback_query(call):
    if call.data == "2_2":
        bot.send_message(call.message.chat.id,
                 "{0.first_name}, собираетесь в отпуск?☀️ Хорошее дело! Только не забудьте учесть несколько важных моментов:\n\nУйти в отпуск можно только в случае, если сотрудник отработал в компании уже больше полугода. Однако, также *по договоренности со своим руководителем* сотрудник может уйти в отпуск и раньше, чем через 6 месяцев.\n\nА чтобы понять, сколько дней отпуска вы можете взять, следует знать: каждый месяц сотруднику начисляются 2,33 дня отпуска. Умножайте их на количество месяцев, сколько вы работаете в компании, и в сумме получите количество дней для заслуженного отпуска!\n\nТак вот, чтобы уйти в отпуск, необходимо:\n\n1. Согласовать даты отпуска с руководителем подразделения — сделайте это как можно раньше, чтобы не возникло форс-мажорных критических ситуаций на проектах, за которые вы отвечаете.\n\n2. Обратиться к администратору проектов в своем подразделении, который поможет вам:\n\n3. Написать заявление на отпуск, это важно сделать за 4 полных дня до предполагаемой даты отпуска.\n\n4. Завизировать заявление у руководителя.\n\n5. Отнести завизированное заявление в отдел кадров в каб. 12-01.\n\nТеперь остается только дождаться начала заветного отпуска и отдохнуть за себя и всю команду «Красного квадрата»!😎\n\nОбразец заявлени на отпуск — https://cloud.mail.ru/public/xsZs/o6FDFeCGV".format(
                     call.from_user), parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "2_3")
def callback_query(call):
    if call.data == "2_3":
        bot.send_photo(call.message.chat.id, "http://risovach.ru/upload/2018/02/mem/tut_168286985_orig_.jpg",
               caption="{0.first_name},\nнужно что-то доставить в офис? А может, в типографию? В этом поможет наш курьер!\n\nЧтобы заказать курьера🏃, нужно:\n\n1. Обратиться к администратору проектов своего подразделения.\n\n2. Вместе вы создадите заявку на портале с указанием адреса, имен контактных лиц, кто отдает и забирает посылку, и их номеров телефона, а также даты и времени доставки.\n\n3. Далее вам нужно отнести свою посылку на ресепшн, уточнить, что вы оставили заявку на курьера и, конечно, поблагодарить наших менеджеров за то, что они передадут вашу посылку!".format(
                   call.from_user), parse_mode="Markdown")

# категория "Для новых сотрудников"
@bot.callback_query_handler(func=lambda call: call.data == "3")
def get_user_info2(call):
    bot.answer_callback_query(callback_query_id=call.id, text="Не переживайте, сейчас все расскажу!")
    if call.data == "3":
        markup_inline3 = types.InlineKeyboardMarkup()
        but_3_1 = types.InlineKeyboardButton(text="Как пройти в офис? 🗺", callback_data="3_1")
        but_3_2 = types.InlineKeyboardButton(text="Печать файлов в офисе 🖨", callback_data="3_2")
        but_3_3 = types.InlineKeyboardButton(text="Инструктаж для новых сотрудников ✍🏻", callback_data="3_3")
        but_3_4 = types.InlineKeyboardButton(text="Самые важные кабинеты 🧰", callback_data="3_4")

        markup_inline3.add(but_3_1)
        markup_inline3.add(but_3_2)
        markup_inline3.add(but_3_3)
        markup_inline3.add(but_3_4)
        bot.send_message(call.message.chat.id, "{0.first_name}, выберите категорию:".format(call.from_user),
                         parse_mode="Markdown", reply_markup=markup_inline3)

@bot.callback_query_handler(func=lambda call: call.data == "3_1")
def callback_query(call):
    if call.data == "3_1":
        bot.send_photo(call.message.chat.id, "https://cloud.mail.ru/public/cJpE/MWY4HcBcJ",
               caption="🟥Офис «Красного квадрата» находится по адресу ул.Академика Королева, 12, КПП 17.\n\nЗайдите в КПП и подойдите к кабинке «Красный Квадрат», которая находится справа по вашу руку. В кабинке сидит менеджер, ему нужно отдать свой паспорт и уточнить, что на вас делали заявку для прохода в офис.\n\nДалее вы с менеджером пройдете через турникеты и выйдите на улицу, пройдете по диагонали немного правее и увидите лестницу, по которой нужно подняться, и после пройти через вторые турникеты. Менеджер вам поможет и не оставит вас в беде!\n\nПосле вторых турникетов пройдите прямо по коридору до центрального коридора телецентра, где расположены лифты (5шт).\n\nНа одной из цифровых стоек рядом с лифтами нажмите цифру 12 ( именно на 12 этаже находится офис «Красного квадрата»), и на табло высветится номер лифта, к которому вы должны подойти.\n\nПосле вы подниметесь на 12 этаж на нашем суперскоростном лифте и та-даам — вы уже в офисе «Красного квадрата»!\n\nПриятного времяпрепровождения!",
               parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "3_2")
def callback_query(call):
    if call.data == "3_2":
        bot.send_photo(call.message.chat.id, "http://risovach.ru/upload/2016/08/mem/1_121602134_orig_.jpg",
               caption="*Печать файлов в офисе👩🏻‍💻*\n\nЕсли вам нужно напечатать файл, то вы можете это сделать со своего рабочего компьютера. Просто нажмите на значок принтера в программе, в которой работаете, и выберите один из доступных принтеров (в названии принтера указан номер кабинета, где можно будет забрать распечатанный файл). \n\nЕсли к вашему компьютеру не подключен никакой принтер, то нужно обратиться к Инженеру отдела информационных технологий (ИТ) по внутреннему телефону +7 (495) 646-34-64 (доб. 1111) и попросить настроить печать на рабочем компьютере.\n\nТакже можете обратиться на ресепшн и попросить напечатать ваш файл. Для этого заранее можно отправить файл в письме на электронную почту reception@red-red.ru, указав в теме письма «Запрос на печать» + свою фамилию.",
               parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "3_3")
def callback_query(call):
    if call.data == "3_3":
        bot.send_message(call.message.chat.id,
                 "*Инструктаж для новых сотрудников👨‍🚒:*\n\nЕсли вам еще не пришло сообщение от отдела кадров о прохождении инструктажа, то я расскажу тебе об этой интересной процедуре подробнее:\n\nВводный инструктаж по охране труда для сотрудников принимаемых на работу и недавно принятых *пройти нужно обязательно каждому новому сотруднику!*\n\nДля того, чтобы пройти инструктаж, вам необходимо просто прийти в четверг (именно по четвергам проходит данный инструктаж) в кабинет 12-02. Там вы прослушаете познавательную лекцию и распишитесь в журнале, закрепляя свое присутствие!\n\nОтличного провести время!",
                 parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data == "3_4")
def callback_query(call):
    if call.data == "3_4":
        bot.send_message(call.message.chat.id,
                 "*❗️Самые важные кабинеты*:\n\n{0.first_name}, представляю список самых важных кабинетов, номера кабинетов и информацию о том, где они находятся и по каким вопросам туда можно обратиться:\n\n*Ресепшн* — находится сразу у лифтов — курьерская доставка, оформление пропусков на территорию телецентра, уточнить в каком кабинете сидит сотрудник, помощь с распечаткой документов.\n\n*Отдел кадров* — 12-01 — подписание всех кадровых документов, запрос справок,  увольнение😳\n\n*Отдел секретариата* — 12-03 — отправка документов почтой России, обратиться к офис-менеджеру (заказ воды в кабинет, заказ бумаги, пригласить уборщицу, починить что-то в кабинете).\n\n*Служба информационных технологий (ИТ)* — 12-25 — по всем вопросам, связанным с компьютером, интернетом, по рабочим программам и сервисам.\n\n*Бухгалтерия* — 12-26 — узнать, была ли оплата подрядчику, сдача закрывающих документов, оформление служебных записок.\n\n*Департамент правового управления* — 12-33б и 12-36 — по всем юридическим вопросам.\n\nНадеюсь, эта информация поможет вам! А если считаете, что я что-то упустил, то смело можете написать мне, просто нажав на *кнопку обратной связи* в клавиатуре вашего устройства. Я приму во внимание любое ваше замечание или идею!".format(
                     call.from_user), parse_mode="Markdown")

# категория "Найти коллегу"
@bot.callback_query_handler(func=lambda call: call.data == "4")
def get_user_info(call):
    bot.answer_callback_query(callback_query_id=call.id, text="Секундочку, обрабатываю запрос...")
    if call.data == "4":
        markup_inline4 = types.InlineKeyboardMarkup()
        but_4_1 = types.InlineKeyboardButton(text="Дизайнерское бюро «Гранат»", callback_data="4_1")
        but_4_2 = types.InlineKeyboardButton(text="Фабрика декораций", callback_data="4_2")

        markup_inline4.add(but_4_1)
        markup_inline4.add(but_4_2)
        bot.send_photo(call.message.chat.id, "https://www.meme-arsenal.com/memes/48699c6e2834dc18536cae69626f1288.jpg",
               caption="{0.first_name},\nданная функция находится в доработке👌🏻, поэтому круг коллег, по которым можно узнать информацию, еще не полон.\n\nНо вы можете оценить, как будет работать эта функция, если отправите мне одну из этих фамилий — Звонова, Витковский, Морозова, Ляхов и я расскажу подробнее об этих сотрудниках.\n\nИли можете узнать подробности об отделах, где работают эти люди, кликнув на одну из кнопок ниже👇🏻".format(
                   call.from_user), parse_mode="Markdown", reply_markup=markup_inline4)

@bot.callback_query_handler(func=lambda call: call.data == "4_1")
def callback_query(call):
    if call.data == "4_1":
        bot.send_message(call.message.chat.id,
                 "*Гранат* — подразделение «Красного квадрата», которое отвечает за графическую составляющую различных проектов: оформление форумов, выставок и городских пространств, айдентика национальных мероприятий и министерств, создание сайтов и приложений. Команда решает амбициозные и нетривиальные задачи.",
                 parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: call.data == "4_2")
def callback_query(call):
    if call.data == "4_2":
        bot.send_message(call.message.chat.id,
                 "*Фабрика декораций* — целый парк техники, чтобы делать сложную бутафорию, высокохудожественные элементы из металла и дерева, композитов, фанеры, красить, печатать, грунтовать, собирать самые нестандартные по форме объекты. Официальный сайт — https://redsfactory.ru/.",
                 parse_mode="Markdown")

# категория "Еда в стакане"
@bot.callback_query_handler(func=lambda call: call.data == "5")
def get_user_info(call):
    bot.answer_callback_query(callback_query_id=call.id, text="Минуточку, готовлю что-то вкусное 😋")
    if call.data == "5":
        markup_inline5 = types.InlineKeyboardMarkup()
        but_5_1 = types.InlineKeyboardButton(text="Где находится кафе ❓", callback_data="5_1")
        but_5_2 = types.InlineKeyboardButton(text="Меню 🍽",
                                             url="https://ostankino.edavstakane.ru/#products_menu",
                                             callback_data="5_2")
        but_5_3 = types.InlineKeyboardButton(text="Акции кафе 🤑", callback_data="5_3")
        but_5_4 = types.InlineKeyboardButton(text="Бесплатная доставка в офис 📦", callback_data="5_4")

        markup_inline5.add(but_5_1)
        markup_inline5.add(but_5_2)
        markup_inline5.add(but_5_3)
        markup_inline5.add(but_5_4)
        bot.send_message(call.message.chat.id,
                         "{0.first_name},\nмогу рассказать вам следующее:".format(call.from_user),
                         parse_mode="Markdown", reply_markup=markup_inline5)

@bot.callback_query_handler(func=lambda call: call.data == "5_1")
def callback_query(call):
    if call.data == "5_1":
        bot.send_photo(call.message.chat.id, "https://cloud.mail.ru/public/o2bv/qiGke1puu",
                       caption="*Кафе «Еда в стакане»* находится на первом этаже АСК-1 телецентра «Останкино» возле центральных лифтов (адрес — ул. Академика Королева, 12).\n\nОриентируйтесь на яркий корнер с красивой витриной, стильным логотипом кафе и приветливыми менеджерами. На корнере можно заказать еду с собой.\n\nА за корнером есть лестница на -1 этаж, где и находится само кафе — здесь можно отдохнуть и пообедать в уютной и спокойной обстановке.\n\nБудьте как дома!",
                       parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "5_3")
def callback_query(call):
    if call.data == "5_3":
        bot.send_message(call.message.chat.id,
                         "Кажется, кто-то проголодался?\n\nКафе «Еда в стакане» предлагает особенно вкусные акции, чтобы обед был еще сытнее и приятнее:\n\n*- Бодрый перекус:* Сандвич с ветчиной и сыром + кофе = *350₽*\n\n*- Бизнес-ланч* (суп, горячее + гарнир) = *330₽*\n\nПриятного аппетита!😋",
                         parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "5_4")
def callback_query(call):
    if call.data == "5_4":
        bot.send_photo(call.message.chat.id,
                       "https://www.meme-arsenal.com/memes/2b07d0148177ca4214153d829eb7b014.jpg",
                       caption="❗️*Бесплатная доставка в офис\n\n«Еда в стакане»* — вкусная, полезная, а главное — удобная еда для тех, у кого нет времени на полноценный обед.\n\nДля самых занятых в кафе организована бесплатная ежедневная доставка на ваше рабочее место.\n\nОплата выбранного обеда производится картой на сайте — https://ostankino.edavstakane.ru\n\nМинимальная сумма заказа для доставки — 350 ₽.\n\nДоставка осуществляется с 10:00 до 18:00.\n\nПо дополнительным вопросам можно писать команде кафе в WhatsApp по номеру +7 903 210-85-76",
                       parse_mode="Markdown")

# категория "Вакансии"
@bot.callback_query_handler(func=lambda call: call.data == "6")
def get_user_info(call):
    bot.answer_callback_query(callback_query_id=call.id, text="Расскажу кое-что интересное...")
    if call.data == "6":
        markup_inline6 = types.InlineKeyboardMarkup()
        but_6_1 = types.InlineKeyboardButton(text="Sales-менеджер в «Модный подкаст»",
                                             url="https://arkhangelsk.hh.ru/vacancy/55122803?from=employer&hhtmFrom=employer",
                                             callback_data="6_1")
        but_6_2 = types.InlineKeyboardButton(text="Секретарь на ресепшн",
                                             url="https://arkhangelsk.hh.ru/vacancy/54921461?from=employer&hhtmFrom=employer",
                                             callback_data="6_2")

        markup_inline6.add(but_6_1)
        markup_inline6.add(but_6_2)
        bot.send_message(call.message.chat.id,
                         "{0.first_name}, вот последние актуальные вакансии:\n\n".format(call.from_user),
                         parse_mode="Markdown", reply_markup=markup_inline6)

# ответы бота по типу сообщений
@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text.lower() == "пока":
        bot.send_message(message.chat.id,
                         "{0.first_name}, пока! Было приятно пообщаться🤗".format(message.from_user),
                         parse_mode="Markdown")
    elif message.text.lower() == "привет":
        bot.send_message(message.chat.id,
                         "Приветствую, {0.first_name}! Меня зовут RED-коллега.\n\nПочему у меня такое имя?\n\nВо-первых, сами понимаете, цвет какой компании я символизирую 🟥.\n\nВо-вторых, мое имя расшифровывается как Responsible, Effective и Digital, что значит — ответственный, эффективный и цифровой.\n\nА в-третьих, согласитесь, красиво и лаконично!\n\nНажмите на встроенную кнопку «Основное меню» или напишите мне /menu, и я пришлю актуальные темы, на которые сможем пообщаться!\n\nА если кликните на кнопку /help, расскажу подробнее, чем могу вам помочь.".format(
                             message.from_user), parse_mode="Markdown")
    elif message.text.lower() == "как дела":
        bot.send_message(message.chat.id,
                         "Честно сказать, {0.first_name}, немного устал... Но сейчас планирую подкрепиться и закончить свои запланированные на день задачи💪🏻\n\nНадеюсь, ты тоже все успеешь🔝\n\nУдачи нам и сил!".format(
                             message.from_user), parse_mode="Markdown")
    elif message.text.lower() == "ты кто":
        bot.send_message(message.chat.id,
                         "{0.first_name},\n я — ваш интерактивный помощник и по совместительству корпоративный бот «Красного квадрата». Меня зовут RED-коллега.\n\nПочему у меня такое имя?\n\nВо-первых, вы сами понимаете, цвет какой компании я символизирую 🟥. Во-вторых, мое имя расшифровывается как Responsible, Effective и Digital, что значит — ответственный, эффективный и цифровой. А в-третьих, согласитесь, красиво и лаконично!".format(
                             message.from_user), parse_mode="Markdown")
    elif message.text.lower() == "зачем":
        bot.send_message(message.chat.id,
                         "{0.first_name},\nя помогу вам узнать информацию о нашей компании, найти коллегу и понять, по каким вопросам к нему можно обратиться, уточню организационные моменты — расскажу, как правильно взять отпуск, как заказать курьера.\n\nНовым сотрудникам помогу адаптироваться к нашим условиям — расскажу о главных кабинетах, проведении первого инструктажа для новоиспеченных коллег, помогу в печати файлов, угощу в нашем телевизионном кафе.\n\nСвои идеи или замечания можете оставить мне, нажав на кнопку обратной связи.\n\nЕще немного умею общаться текстом, поэтому можете мне писать, я постараюсь ответить на вопросы, но не обещаю, что на все — еще не до конца научился распознавать все слова и форматы.\n\nНажмите на встроенную кнопку «Основное меню» или напишите мне /menu, и я пришлю актуальные темы, на которые сможем пообщаться.".format(
                             message.from_user), parse_mode="Markdown")
    elif message.text.lower() == "чем занимаешься":
        bot.send_message(message.chat.id,
                         "{0.first_name}, конечно, работаю. Сейчас только сбегаю в «Еду в стакане», возьму бизнес-ланч, а потом обратно на свой сервер.".format(
                             message.from_user), parse_mode="Markdown")
    elif message.text.lower() == "ты где":
        bot.send_message(message.chat.id,
                         "{0.first_name}, я живу в телецентре «Останкино», там же где находится и наш офис. Не забывайте и вы заглядывать к нам на 12 этаж почаще :)".format(
                             message.from_user), parse_mode="Markdown")
    elif message.text.lower() == "кнопка обратной связи 📩":
        bot.send_message(message.chat.id,
                         "О!🤩 Кажется, я вижу, что вы хотите поделиться своими впечатлениями или рассказать о новой идее для меня или нашего корпоративного Telegram-канала? А может, есть какие-то замечания к нашей работе?🤔\n\nС радостью выслушаем вас с нашим администратором. Напишите сообщение нашей коллеге Арине — @arrr_ish, изучим вашу просьбу и обязательно ответим.\n\nСпасибо за участие! Мы очень ценим!❤️")
    elif message.text.lower() == "звонова":
        bot.send_message(message.chat.id,
                         "*Елизавета Звонова* — исполнительный директор ООО «Гранат».\n\nВ пул задач Елизаветы входит:\n\n– Осуществление разработки маркетинговой политики компании на основе анализа существующей ситуации и прогнозирования потребительского спроса на продукты компании \n\n– Определение новых рынков сбыта и сегментов потребителей\n\n– Выявление возможностей продавать больше и увеличивать занимаемую долю рынка\n\n– Изучение мнения потребителей о брендах компании, подготовка предложений по повышению конкурентоспособности и качеству продуктов\n\n– Разработка концептов и стратегии по созданию и развитию брендов компании.\n\nКонтакт для связи: zee@red-red.ru",
                         parse_mode="Markdown")
    elif message.text.lower() == "витковский":
        bot.send_message(message.chat.id,
                         "*Кирилл Витковский* — дизайн-директор ООО «Гранат».\n\nВ пул задач Кирилла входит:\n\n– Формирование дизайн-системы и контроль ее выполнения сотрудниками\n\n– Координация дизайн-команды и формирование проектных группы для работы над проектами\n\n– Арт-надзор результатов деятельности дизайн-команды\n\n– Помощь команде в текущей работе и ее обучение.\n\nКонтакт для связи: vka@red-red.ru",
                         parse_mode="Markdown")
    elif message.text.lower() == "морозова":
        bot.send_message(message.chat.id,
                         "*Алёна Морозова* — администратор проектов ООО «Гранат».\n\nВ пул задач Алёны входит:\n\n– Ведение коммуникации по задачам и этапам рабочего процесса производственного отдела с внутренними службами компании и другими производственными отделами\n\n– Выстраивание необходимых финансовых и логических процессов\n\n– Подготовка необходимой документации.\n\nКонтакт для связи: moaa@red-red.ru",
                         parse_mode="Markdown")
    elif message.text.lower() == "ляхов":
        bot.send_message(message.chat.id,
                         "*Денис Ляхов* — начальник производства медиагруппы «Красный квадрат».\n\nВ пул задач Дениса входит:\n\n– Организация необходимых производственных процессов\n\n– Руководство созданием технических заданий в сфере производственных работ\n\n– Согласование проектно-конструкторской документации.\n\nКонтакт для связи: lds@red-red.ru",
                         parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id,
                         "Упс! {0.first_name}, пока я умею общаться только по заданным темам. Нажми на встроенную кнопку «Основное меню» или напиши мне /menu, и я пришлю тебе актуальные категории!".format(
                             message.from_user), parse_mode="Markdown")

@bot.message_handler(content_types=["photo"])
def reply_to_photo(message):
    bot.send_message(message.chat.id,
                     "Вау, классная фотка!🤩 Но пока я умею общаться только по заданным темам. Поэтому нажми на встроенную кнопку «Основное меню» или напиши мне /menu, и я пришлю тебе актуальные категории!")

@bot.message_handler(content_types=["voice"])
def reply_to_audio(message):
    bot.send_message(message.chat.id,
                     "Уверен, {0.first_name}, ты записал интересное голосовое. Но пока я умею общаться только по заданным темам и не умею распознавать все слова. Поэтому нажми на встроенную кнопку «Основное меню» или напиши мне /menu, и я пришлю тебе актуальные категории!".format(
                         message.from_user), parse_mode="Markdown")

@bot.message_handler(content_types=["video"])
def reply_to_video(message):
    bot.send_message(message.chat.id,
                     "Вау, классное видео!🤩 Но пока я умею общаться только по заданным темам. Поэтому нажми на встроенную кнопку «Основное меню» или напиши мне /menu, и я пришлю тебе актуальные категории!")

@bot.message_handler(content_types=["sticker"])
def reply_to_sticker(message):
    bot.send_message(message.chat.id,
                     "Классный стикер!🤩 {0.first_name}, но пока я умею общаться только по заданным темам и не до конца умею распознавать другие форматы. Нажми на встроенную кнопку «Основное меню» или напиши мне /menu, и я пришлю тебе актуальные категории!".format(
                         message.from_user), parse_mode="Markdown")

bot.infinity_polling()
