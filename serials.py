import asyncio
import logging
from aiogram import Bot, Dispatcher, types
import emoji


logging.basicConfig(level=logging.INFO)

bot = Bot(token='5668613394:AAH1aukTC8IAunHwapb2ToLMZm_fNqYONpo')

dp = Dispatcher(bot)


kb = [types.KeyboardButton(text='Зарубежные')]
kb1 = [types.KeyboardButton(text='Российские')]

a = [types.KeyboardButton(text='Комедия' + '😂')]
b = [types.KeyboardButton(text='Ужасы' + '😱')]
c = [types.KeyboardButton(text='Детективы' + '🕵')]
d = [types.KeyboardButton(text='Фантастика' + '🔥')]
e = [types.KeyboardButton(text='Мелодрамы' + '😊')]

a1 = [types.KeyboardButton(text='Кoмедия' + '😂')]
b1 = [types.KeyboardButton(text='Ужaсы' + '😱')]
c1 = [types.KeyboardButton(text='Дeтективы' + '🕵')]
d1 = [types.KeyboardButton(text='Фaнтастика' + '🔥')]
e1 = [types.KeyboardButton(text='Мeлодрамы' + '😊')]

tb = [types.KeyboardButton(text='Да, давай')]
tb1 = [types.KeyboardButton(text='Нет, не надо')]
tb2 = [types.KeyboardButton(text='Да, давай!')]
tb3 = [types.KeyboardButton(text='Да, давай!!')]
tb4 = [types.KeyboardButton(text='Да, давай!!!')]
tb5 = [types.KeyboardButton(text='Да, давай!!!!')]

t1 = [types.KeyboardButton(text='Да, дaвaй')]
t2 = [types.KeyboardButton(text='Да, дaвaй!')]
t3 = [types.KeyboardButton(text='Да, дaвaй!!')]
t4 = [types.KeyboardButton(text='Да, дaвaй!!!')]
t5 = [types.KeyboardButton(text='Да, дaвaй!!!!')]

s0 = [types.KeyboardButton(text='')]


sr = types.ReplyKeyboardMarkup([kb, kb1])

sr1 = types.ReplyKeyboardMarkup([a, b, c, d, e])

sr2 = types.ReplyKeyboardMarkup([a1, b1, c1, d1, e1])

sr3 = types.ReplyKeyboardMarkup([tb, tb1])

sr4 = types.ReplyKeyboardMarkup([tb2, tb1])

sr5 = types.ReplyKeyboardMarkup([tb3, tb1])

sr6 = types.ReplyKeyboardMarkup([tb4, tb1])

sr7 = types.ReplyKeyboardMarkup([tb5, tb1])

sr13 = types.ReplyKeyboardMarkup([t1, tb1])

sr14 = types.ReplyKeyboardMarkup([t2, tb1])

sr15 = types.ReplyKeyboardMarkup([t3, tb1])

sr16 = types.ReplyKeyboardMarkup([t4, tb1])

sr17 = types.ReplyKeyboardMarkup([t5, tb1])

s20 = types.ReplyKeyboardMarkup([s0])


@dp.message_handler(commands=['start'])
async def hello(message: types.message):
    await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGAAE4Yz1xCzP_G31-DbI2y9MPU40IV5YAApcAAztgJBSz41Uh62ze2SoE'),
    await message.answer('Привет! Я чат-бот по поиску сериалов' + emoji.emojize(' 🍿'))
    await bot.send_message(message.chat.id, 'Какие сериалы предпочитаете?', reply_markup=sr)


@dp.message_handler(text='Зарубежные')
async def foreign(message: types.message):
    await message.answer('Хорошо! Выберете жанр' + emoji.emojize(' :thumbs_up:'), reply_markup=sr2)


@dp.message_handler(text='Российские')
async def russian(message: types.message):
    await message.answer('Хорошо! Выберете жанр' + emoji.emojize(' :thumbs_up:'), reply_markup=sr1)


@dp.message_handler(text='Комедия' + '😂')
async def seas(message: types.message):
    await message.answer('https://interny.tnt-online.ru/'),
    await message.answer('https://ctc.ru/projects/serials/voroniny/video/24-sezon/'),
    await message.answer('https://kino.mail.ru/series_758364_kuhnya/')
    await bot.send_message(message.chat.id, 'Хотите видеть рейтинг и отзывы на эти сериалы?',
                           reply_markup=sr3)


@dp.message_handler(text='Ужасы' + '😱')
async def seas(message: types.message):
    await message.answer('https://ctc.ru/projects/serials/pischeblok/'),
    await message.answer('https://kino.mail.ru/series_919820_pereval_dyatlova/'),
    await bot.send_message(message.chat.id, 'Хотите видеть рейтинг и отзывы на эти сериалы?',
                           reply_markup=sr4)


@dp.message_handler(text='Детективы' + '🕵')
async def seas(message: types.message):
    await message.answer('https://www.5-tv.ru/projects/1000117/sled/films/'),
    await message.answer('https://ayaznal.ru/video/vip/498/serialy/russkie/nevskij'),
    await message.answer('https://tv4.myserial.online/8157-mazhor-2014-7-9.html')
    await bot.send_message(message.chat.id, 'Хотите видеть рейтинг и отзывы на эти сериалы?',
                           reply_markup=sr5)


@dp.message_handler(text='Фантастика' + '🔥')
async def seas(message: types.message):
    await message.answer('https://kino.tricolor.tv/series/watch/chernobyl-zona-otchuzhdeniya-final-2019/season-1/'),
    await message.answer('https://ctc.ru/projects/serials/vyzhit-posle/'),
    await message.answer('https://kino.mail.ru/cinema/movies/719312_temnii_mir_ravnovesie/')
    await bot.send_message(message.chat.id, 'Хотите видеть рейтинг и отзывы на эти сериалы?',
                           reply_markup=sr6)


@dp.message_handler(text='Мелодрамы' + '😊')
async def seas(message: types.message):
    await message.answer('https://kino.mail.ru/series_916913_skoraya_pomosch/seasons_4/'),
    await message.answer('https://kino.mail.ru/series_828742_dom_s_liliyami/'),
    await message.answer('https://www.justwatch.com/ru/сериал/noven-kii')
    await bot.send_message(message.chat.id, 'Хотите видеть рейтинг и отзывы на эти сериалы?',
                           reply_markup=sr7)


@dp.message_handler(text='Кoмедия' + '😂')
async def comedy(message: types.message):
    await message.answer('https://kino.mail.ru/series_761379_klinika/'),
    await message.answer('https://doramy.club/27325-1-policejskaya-akademiya.html'),
    await message.answer('https://hd.kinopoisk.ru/film/42136048353b48cfa4225742c71e341e/?content_tab=series&episode=1&season=1')
    await bot.send_message(message.chat.id, 'Хотите видеть рейтинг и отзывы на эти сериалы?',
                           reply_markup=sr13)


@dp.message_handler(text='Ужaсы' + '😱')
async def horror(message: types.message):
    await message.answer('https://kinogo.biz/8380-krik.html'),
    await message.answer('https://www.afisha.ru/movie/261342/seasons/'),
    await message.answer('https://kinogo.biz/8682-shtamm-1.html')
    await bot.send_message(message.chat.id, 'Хотите видеть рейтинг и отзывы на эти сериалы?',
                           reply_markup=sr14)


@dp.message_handler(text='Дeтективы' + '🕵')
async def detective(message: types.message):
    await message.answer('https://kinogo.biz/8862-kak-izbezhat-nakazanija-za-ubijstvo-1.html'),
    await message.answer('https://www.afisha.ru/movie/263354/seasons/'),
    await message.answer('https://kino.mail.ru/series_767480_lyuter/')
    await bot.send_message(message.chat.id, 'Хотите видеть рейтинг и отзывы на эти сериалы?',
                           reply_markup=sr15)


@dp.message_handler(text='Фaнтастика' + '🔥')
async def fantastic(message: types.message):
    await message.answer('https://allserial.xyz/1714-lyucifer-z65.html'),
    await message.answer('https://zetflix.ru.net/serials/akademija-ambrella/'),
    await message.answer('https://teenwolf-online.com/sezon-1/')
    await bot.send_message(message.chat.id, 'Хотите видеть рейтинг и отзывы на эти сериалы?',
                           reply_markup=sr16)


@dp.message_handler(text='Мeлодрамы' + '😊')
async def melodrama(message: types.message):
    await message.answer('https://turk-ru.ru/postuchi-v-moyu-dver322/'),
    await message.answer('https://doramy.site/1711-silachka-do-bon-sun.html'),
    await message.answer('https://zetflix.ru.net/serials/heartbreak-high/')
    await bot.send_message(message.chat.id, 'Хотите видеть рейтинг и отзывы на эти сериалы?',
                           reply_markup=sr17)


@dp. message_handler(text='Да, давай')
async def yes(message: types.message):
    await message.answer('Интерны: Я досмотрела 14 сезон — и как будто с близкими и любимыми родственниками попрощалась. Он столько раз выручал меня, когда на душе было тяжело. Спасибо большое всем актерам и создателям сериала. Я от всей души вам выражаю благодарность и восхищение за ваш талант и за поддержку в трудные минуты. Рейтинг: 7,5/10' + '⭐')
    await message.answer('Воронины: Хочу поделиться впечатлениями от просмотра сериала "Воронины". Сериал легкий к просмотру его хочется смотреть и смотреть. Нравоучения отца к сыновьям понятны. Глава молодого семейства разрывается между мамой и женой, и не всегда ему получается угодить обоим. Мать - типичная свекровь: властная, жалеющая своих детей, и во всем учащая невестку. Юмор в сериале довольно легкий, не пошлый и очень смешной. Рейтинг: 6/10' + '⭐')
    await message.answer('Кухня: Комедийный сериал "Кухня" я смотрел несколько раз. Но он мне настолько понравился, что пересматривал его еще 2 или 3 раза. Этот сериал надо смотреть с чувством иронии, ведь не зря он комедийный.мВ сериале стоит отметить и музыкальное сопровождение. Музыка добавляет сюжету чувственности.Я советую посмотреть этот сериал тем, кто хочет непринужденно провести время, отдохнут, и посмеяться. Рейтинг: 8,6/10' + '⭐')
    await message.answer('Приятного просмотра' + '❤')
    await message.answer('Для возвращения на главную нажмите сюда: /start')


@dp.message_handler(text='Да, давай!')
async def yes(message: types.message):
    await message.answer('Пищеблок: Сериал «Пищеблок» очень необычный, особенно для российского кинематографа. Этот сериал поразил меня своей атмосферой пионерского лагеря, Советского союза, лета и беззаботного детства. Сколько бы не ругали наши ужастики, но они наши, с нашими ценностями и героями, поэтому и воспринимаются роднее. Понравилась игра всех актёров без исключения. Сериал советую к просмотру любителям жанров мистики и детектива, страшных моментов мало, но это не портит сериал. Рейтинг: 7,5/10' + '⭐')
    await message.answer('Перевал Дятлова: Отличный сериал, смотрю с удовольствием! Впечатления от увиденного только хорошие. Было и мрачно, и детективно, и загадочно. И актеры неплохо их сыграли. Качественная, даже скажу - изобретательная съемка позволяет глубже погрузится в историю и сюжет. Пейзажи тоже на отлично. Всем любителям жанра - советую! Рейтинг: 7,7/10' + '⭐')
    await message.answer('Приятного просмотра' + '❤')
    await message.answer('Для возвращения на главную нажмите сюда: /start')


@dp.message_handler(text='Да, давай!!')
async def yes(message: types.message):
    await message.answer('След: Во время просмотра получила невероятное количество удовольствие, эмоций разного характера.Истории действительно необычные и поданы зрителям по всем правилам хорошего кино. Каждая серия - это совершенно новая история о совершенном или только планируемом преступлении. Сериал очень динамичный с продуманным закрученным сюжетом, смотрится на одном дыхании. Рейтинг: 9,6/10' + '⭐')
    await message.answer('Невский: Сюжет хороший, по типажу актёры подобраны на 100% согласно своей роли. Сериал Невский рассказывает о жизни в целом, со всеми своими взлётами, падениями и неожиданными поворотами, но, через жизненную историю одного героя. Этот сериал идеален для всех, кто воспринимает этот мир как взрослый серьёзный человек, и кому надоели сериалы с глупым юмором американского направления. Рейтинг: 9,2/10' + '⭐')
    await message.answer('След: Актерский состав очень хороший, подобраны изумительно. Сюжет интересный. Как богатенький папа отправляет своего сына работать, устав от его гулянок. И не просто работать, а в полицию, где его не возлюбили сразу и есть за что. Как оказалось это только на пользу и сын превращается в человека.Многие тут увидят себя и взглянут со стороны.К просмотру рекомендую, интересный сериал. Рейтинг: 8,8/10' + '⭐')
    await message.answer('Приятного просмотра' + '❤')
    await message.answer('Для возвращения на главную нажмите сюда: /start')


@dp.message_handler(text='Да, давай!!!')
async def yes(message: types.message):
    await message.answer('ЧЗО: Отличный сериал! Подкупило качество ЧЗО. Прекрасные молодые актеры, очень органично существующие в рамках своих персонажей. Шведскому режиссеру удался пресловутый «взгляд со стороны», итогом чего стало отсутствие свойственных нашему кино древнерусской тоски и дидактики. Рейтинг: 7,5/10' + '⭐')
    await message.answer('Выжить после: Сюжет злободневный и актуальный, очень волнуют все герои, все их события и перипетии, заботы и проблемы. В сериале есть и любовь, и дружба, и предательство, и самопожертвование, и жестокость. События развиваются стремительно, совершенно непредсказуемо и неожиданно. Смотрится на одном дыхании. Актёры все великолепны и талантливы! Рейтинг: 8/10' + '⭐')
    await message.answer('Тёмный мир: Обалденный сериал про приключения российских студентов в карельской глуши. Замечательно все - сценарий , актерские работы, спецэффекты, динамика... Рейтинг: 9.7/10' + '⭐')
    await message.answer('Приятного просмотра' + '❤')
    await message.answer('Для возвращения на главную нажмите сюда: /start')


@dp.message_handler(text='Да, давай!!!!')
async def yes(message: types.message):
    await message.answer('Скорая помощь: Фильм бесподобный! Смотрится легко и захватывает с первого кадра. Подбор актёров выше всяческих похвал! Это единственный сериал, где нет героев второго плана. Понятно, что фильм завязан на судьбе героя Гоши Куценко, но всё сделано, так что забываешь об этом и начинаешь переживать за судьбы абсолютно всех героев этого сериала. Рейтиг: 7,1/10' + '⭐')
    await message.answer('Дом с лилиями: Исторически наполняет и передает дух прошлого. Показана послевоенная разруха, сталинские репрессии, становление коммунистического строя, работа партийной элиты и многое другое. Это несомненно очень интересно - заглянуть в прошлое, посмотреть как жили наши предки. Рейтинг: 6,5/10' + '⭐')
    await message.answer('Новенький. Новенький - интересный сериал о жестоких реалиях современной молодёжи! Он снят на актуальную тему, имеет интересный сюжет и качественное исполнение. Сериал раскрывает одну из больших проблем нашего времени. показывает разные проблемные семьи. Дети часто остаются один на один со своими проблемами, боятся и не хотят рассказывать взрослым, а взрослым часто нет до них дела. Сериал заставляет взглянуть на проблему с разных углов. Рейтинг: 7,6/10' + '⭐')
    await message.answer('Приятного просмотра' + '❤')
    await message.answer('Для возвращения на главную нажмите сюда: /start')


@dp.message_handler(text='Нет, не надо')
async def no(message: types.message):
    await message.answer('Хорошо! Приятного просмотра' + '❤')
    await message.answer('Для возвращения на главную нажмите сюда: /start')


@dp.message_handler(text='Да, дaвaй!')
async def yes(message: types.message):
    await message.answer('Крик: «Кому-то нравится спорт… Мне же по душе серийные убийцы». В первой серии видны отсылки к всем частям франшизы и это очень радует. Вы увидите и знакомые пейзажи, вечерники студентов, парня-рассказчика, который все знает о ужасах и увидите как ведется съемка в реальном времени одной из героинь, увидите отсылку на убийц из первой части. Рейтинг: 6,8/10' + '⭐')
    await message.answer('Нулевой: Сериал просто поражает самыми разными сезонами, в которых задумки идут по расходящимся направлениям — и как же это качественно снято! При всех мелких недостатках, очень пугающие сюжеты содержат в себе и достаточно глубокие концептуальные мысли. Рейтинг: 8,7/10' + '⭐')
    await message.answer('Штамм: В сериале Штамм представлен оригинальный взгляд на вампиризм - как на вирус. Съемки масштабные - видно, что бюджет выделили серьезный. Сюжeт cepиaлa тoжe дocтaтoчнo непредсказуемый и бывают такие пoвopoты иcтopии, кoтopыx вы вpяд ли oжидaли бы. Кaк и чeм зaкoнчилcя ceзoн - нe cкaжу, нo поверьте, cepиaл "Штaмм" cтoит пocмoтpeть. Рейтинг: 8,4/10' + '⭐')
    await message.answer('Приятного просмотра' + '❤')
    await message.answer('Для возвращения на главную нажмите сюда: /start')


@dp.message_handler(text='Да, дaвaй')
async def yes(message: types.message):
    await message.answer('Клиника: Сериал нереально классный. Нужно досмотреть до конца хотя бы одну серию. Дальше – просто невозможно оторваться. Юмор здесь своеобразный, скажем американский. Через время втягиваешься и смеешься до упаду. Рейтинг: 8,6/10' + '⭐')
    await message.answer('Полицейская академия: Этот сериал, сериал девяностых годов. В то время наверно это был единственный фильм, который был такой смешной. Все герои этого сериала очень смешные они тем, что постоянно попадают в какие-то интересные ситуации, где им сами же и приходится постоянно выпутываться. Рекомендую к просмотру. Рейтиг: 8,7/10' + '⭐')
    await message.answer('Бесстыжие: Сколько уже прошло сезонов, а интерес к сериалу не угас ни на грош! Реальная жизнь всегда притягивает. А этот сериал и есть повествование о настоящей, реальной жизни. как будто в замочную скважину соседей подглядываешь. Актеры просто потрясающие! Один Фрэнк со своими фразочками чего стоит. Рейтинг: 9/10' + '⭐')
    await message.answer('Приятного просмотра' + '❤')
    await message.answer('Для возвращения на главную нажмите сюда: /start')


@dp.message_handler(text='Да, дaвaй!!')
async def yes(message: types.message):
    await message.answer('Как избежать наказания за убийство: "Как избежать наказание за убийство" - увлекательный сериал о сильной женщине, жизненной несправедливости, системе, где процветает равноправие, порабощена социальная яма, а жизнь не является способом выжить.. Рейтинг: 4,7/5' + '⭐')
    await message.answer('Побег. Майкл Скофилд: Сериал "Побег" был одним из первых, который я посмотрел и переключился с фильмов на сериалы. Все сезоны смотрел с удовольствием. Два брата, один из которых попадает в тюрьму и осужден на казнь, а второй ставит задачу его оттуда вытащить любой ценой.Смотрится на одном дыхании. Продуманный сюжет, харизматичные актеры. Рейтинг: 4,8/5' + '⭐')
    await message.answer('Лютер: Я всей душой люблю ЛЮТЕРА, просто потому,что ОН ЕСТЬ. ЗАМЕЧАТЕЛЬНЫЙ ДЕТЕКТИВНЫЙ СЕРИАЛ, стоящий на ровне с другими британскими шедеврами. Рейтинг: 4,8/5' + '⭐')
    await message.answer('Приятного просмотра' + '❤')
    await message.answer('Для возвращения на главную нажмите сюда: /start')


@dp.message_handler(text='Да, дaвaй!!!')
async def yes(message: types.message):
    await message.answer('Люцифер: Слышала о этом сериале часто но что то название не интриговало вообще. Желания смотреть было 0, и поэтому когда он попался я решила включить чисто.. пока занимаюсь делами думаю пусть идет. НО делами я особо не позанималась а исчезла (выпала) из жизни на 3 дня. Да, ровно столько мне понадобилось что б посмотреть 4 сезона. Повезло, что уже 4 сезона вышло и осталось подождать только одного). 4 сезон, когда сериалом теперь занимается нетфликс, вообще вырос на уровень. Рейтинг: 4,5/5' + '⭐')
    await message.answer('Академия амбрелла: Изначально, когда узнала об этом сериале подумала, что очередная фигня, на которую даже время тратить не стоит. Но информация о нем мне стала попадаться все чаще и я все решилась его посмотреть.И что хочу сказать, зря я его не посмотрела раньше. Он настолько классный, что его можно посмотреть буквально за пару день, не отрывая глаз. Там так необычно разворачивается сам сюжет сериала, что я немного удивилась, так как в обычных сериалах или фильмах такого не встретишь. Рейтинг: 9.0/10' + '⭐')
    await message.answer('Волчонок: Сериал "Волчонок" раньше казался мне подростковым. Почему в этот раз решила начать смотреть? Узнала, что там снимается Томас из "Бегущий в лабиринте" - актер Дилан О Брайан. Фильм се понравился, решила узнать о его фильмографии побольше. Рейтинг: 4.5/5' + '⭐')
    await message.answer('Приятного просмотра' + '❤')
    await message.answer('Для возвращения на главную нажмите сюда: /start')


@dp.message_handler(text='Да, дaвaй!!!!')
async def yes(message: types.message):
    await message.answer('Постучись в мою дверь: Я никогда не смотрела турецкие сериалы, а после дикой популярности «Великолепного века», меня такие сериалы вообще перестали привлекать. Но в начале октября, было скучно и на сайте Кинопоиск, в подборке популярных сериалов попался «Постучись в мою дверь». Понравились актеры на заставке, описание читать не стала, решила смотреть. И каково было моё удивление, когда я поняла, что это турецкий ромком. Рейтинг: 4,2/5' + '⭐')
    await message.answer('Силачка До Бон Су: Прекрасная красивая дорама про отношения в основном, с правильной мыслью, которую я увидела, все надо делать, и делать во время, если не признаешься в своих чувствах, то ничего не изменится. Рейтинг: 4,7/5' + '⭐')
    await message.answer('Школа разбитых сердец: Этот сериал вышел совсем недавно и на него нет пока что отзывов :( ' + '⭐')
    await message.answer('Приятного просмотра' + '❤')
    await message.answer('Для возвращения на главную нажмите сюда: /start')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
