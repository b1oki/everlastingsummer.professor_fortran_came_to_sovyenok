init -1000 python:
    translation["fortran"] = {}
    translation["fortran"]["english"] = "'Professor Fortran in Sovyonok' only in Russian"
    translation["fortran"][None] = u"Профессор Фортран в Совёнке"
init:
    $ mods["fortran"] = translation["fortran"][_preferences.language]
    #$ mod_tags["fortran"] = ["gameplay:vn","protagonist:male","character:Professor Fortran"]
    $ pr = Character(u'Профессор Фортран', color="#6a5acd")
    $ p1_forget_about_muka = False
    $ p1_take_muka = False
    $ p1_take_breakfast = False
    $ p1_meet_el_morning = False
    $ p1_drop_muka = False
    $ p1_tell_mz = False
label fortran:
    scene black with dissolve
    pause(1)
    if _preferences.language == None:
        jump fortran_ru
    else:
        jump fortran_en
label fortran_en:
    narrator "Sorry, but we have no English translation. You can play in Russian."
    menu:
        "Play Russia":
            narrator "Let's play, Comrade!"
            jump fortran_ru
        "Return to Main Menu":
            narrator "Good luck!"
            return
    return
label fortran_ru:
    jump fortran_ru_p1
    return
label fortran_ru_p1:
    $ persistent.sprite_time = 'sunset'
    $ sunset_time()
    play music music_list["my_daily_life"] fadein 5
    show blink
    scene bg int_house_of_mt_sunset
    show mt normal pioneer at center
    show unblink
    mt "Доброе утро, Семён! Пора учавствовать в общественной деятельности."
    th "Это в какой? Уборка территории? А может, спасение мира?"
    th "Ага, это Сара Коннор, а меня прислали в прошлое спасти от развала Советский Союз."
    mt "Сегодня к нам должен приехать профессор из Москвы."
    mt "Нам нужно подготовиться к его приезду."
    mt "Мы приготовим праздничный торт."
    th "Неужели снова продукты по всему лагерю собирать?"
    mt "Электроник и Шурик очень ждут профессора, и они вызвались помочь."
    mt "Шурик пошел за дрожжами, Электроник принесет сахар. Девочки собирают ягоды. "
    stop music fadeout 3
    mt "А ты принесешь муки. Она там же, в библиотеке. Всё, мне пора!"
    play sound sfx_open_dooor_campus_1
    hide mt with dissolve
    play music music_list["my_daily_life"] fadein 5
    narrator "Ольга Дмитриевна спешно удалилась."
    th "Дела делами, а для начала нужно проснуться."
    scene bg ext_house_of_mt_sunset with fade
    narrator "Погода была превосходная. Впрочем, когда она здесь такой не была?"
    scene bg ext_washstand_day with dissolve
    stop music fadeout 3
    th "И что же это за профессор такой?"
    scene bg ext_washstand2_day with fade
    play sound sfx_open_water_sink
    th "Самое удивительно, что он смог вытащить Электроника и Шурика из берлоги!"
    stop sound
    play sound sfx_water_sink_stream
    th "Особенно Шурик, это более невероятное событие, чем его пропажа. Тогда он её объяснил поисками деталей."
    th "Забавно, кажется, будто торт каждый раз приурочен к выходу Шурика из здания кружка, а не к чему-то ещё."
    scene bg ext_washstand_day with dissolve
    stop sound
    play sound sfx_stomach_growl
    narrator "Холодная вода привела меня в чувства, но, в то же время, напомнила о необходимости питаться."
    stop sound
    play sound sfx_dinner_horn_processed
    narrator "Очень кстати."
    th "Просьба вожатой… Пропускать завтрак из-за какого-то профессора?!"
    menu:
        "Все равно библиотека по дороге":
            $ p1_forget_about_muka = False
            jump fortran_ru_p1_library
        "Война войной, а обед по расписанию":
            $ p1_forget_about_muka = True
            jump fortran_ru_p1_dining_hall
    return
label fortran_ru_p1_library:
    scene bg ext_library_day with fade
    stop music fadeout 3
    stop sound
    play sound sfx_knocking_door_2
    th "Что же, не в первый раз. Хоть не мешки с сахаром таскать! До сих пор не понял, почему муку хранят в библиотеке."
    mz "Открыто."
    stop sound
    play sound sfx_open_door_squeak_2
    scene bg int_library_day
    show mz bukal glasses pioneer close at center
    with fade
    stop sound
    play ambience ambience_library_day
    mz "Чего тебе?"
    me "Я пришел за мукой. Ольга Дмитриевна торт затеяла."
    mz "Опять Шурик за водкой убежал и не вернулся?"
    me "Нет. Какой-то гость в лагерь приедет."
    mz "Жди здесь, сейчас принесу."
    hide mz with dspr
    th "Предлагать помощь я не стал, она и в прошлый раз отказалась от неё. А я не настаиваю."
    narrator "Через несколько минут Женя вернулась с небольшим мешком."
    show mz normal glasses pioneer close at center with dspr
    mz "Забирай! Еще пара тортов, и всю муку изведут."
    mz "А что за гость, не слышал?"
    if p1_meet_el_morning == True:
        menu:
            "Рассказать":
                $ p1_tell_mz = True
                me "Профессор Фортран, изучает компьютеры и роботов. Приехал смотреть на робота Электроника."
                show mz bukal glasses pioneer close at center with dspr
                mz "Чего это столичному профессору сдались эти…"
            "Промолчать":
                me "Только, что он профессор из Москвы. Даже имени не знаю."
    else:
        me "Только, что он профессор из Москвы. Даже имени не знаю."
    show mz normal glasses pioneer close at center with dspr
    mz "Ладно."
    if p1_take_breakfast == False:
        me "Спасибо. А ты не идешь на завтрак?"
    else:
        me "Спасибо. А почему тебя на завтраке не было?"
    mz "Это ты полдня спишь, а нормальные люди с утра завтракают. Иди давай!"
    $ p1_take_muka = True
    stop ambience
    play music music_list["afterword"] fadein 5
    scene bg ext_library_day with fade
    if p1_take_breakfast == False:
        th "Так ведь завтра недавно объявили…"
    narrator "Мука кажется пушинкой, в сравнении с тем мешком сахара, что я тащил в столовую после спасения Шурика."
    jump fortran_ru_p1_dining_hall
    return
label fortran_ru_p1_dining_hall:
    scene bg ext_dining_hall_near_sunset with dissolve
    if p1_take_muka == False:
        narrator "Никуда мука за полчаса не денется, а вот я от голода настрадаюсь."
    else:
        narrator "Хоть вес у мешка был небольшой, но руки всё равно устали."
    if p1_take_breakfast == False:
        $ p1_take_breakfast = True
        scene bg int_dining_hall_people_day
        show un normal pioneer at right
        show sl normal pioneer at left
        with fade
        sl "Привет, Семён! Слышал про профессора? Говорят, в компьютерах разбирается."
        un "Мы всем лагеремм к его прибытию торт готовим."
        if p1_forget_about_muka == True:
            sl "Кстати, Семён, ты же должен был муку принести."
            show sl serious pioneer at left
            me "Ну… Я решил сначала подкрепиться, чтоб хватило сил."
            sl "Семён, не забудь за ним сходить. Скоро Электроник принесет сахар."
            sl "А все остальные продукты уже на месте. Не задерживайся! Профессор приедет днем."
            sl "Я пойду, мы с Леной уже позавтракали."
            hide sl
            hide un
            with dspr
        else:
            sl "Вижу, Семён, ты муку принес. Давай я отнесу на кухню."
            $ p1_drop_muka = True
            hide sl with dspr
            un "Ладно, я уже позавтракала. Приятного аппетита!"
            hide un with dspr
        narrator "Я нашел место у окна. На завтрак был привычный рацион пионера."
        th "Надо было распросить Славю о профессоре."
    else:
        scene bg int_dining_hall_day with fade
        narrator "Я отнес мешок на кухню."
        $ p1_drop_muka = True
        if p1_meet_el_morning == False:
            narrator "Повариха сказала, что не хватает только сахара."
        else:
            narrator "Повариха сказала, что остальные продукты уже принесли."
    if p1_meet_el_morning == False:
        $ p1_meet_el_morning = True
        scene bg ext_dining_hall_near_sunset
        show el normal pioneer far at center
        with fade
        narrator "На выходе из столовой я столкнулся с измученным Электроником."
        el "Привет, Семён!"
        me "Привет! А расскажи мне, кого ждем в гости."
        show el grin pioneer at center with dspr
        el "Как это кого. Сам профессор Фортран! Выдающийся ученый. Гений!"
        narrator "Электроник оживился. Или дело в том, что он отдохнул от тяжелого мешка, или дело в профессоре."
        me "А чем он занимается?"
        el "Он работал над МЭСМ и Эльбрусом! Сейчас его институт проводит исследования роботов."
        el "Мы с Шуриком собираемся учиться и работать у него. Его заинтересовал наш проект и он приехал в Совёнок."
        show el smile pioneer at center with dspr
        me "Это тот киборг, что в вашем кружке?"
        el "Именно. А профессор Фортран поможет нам его доработать. Когда он увидит нашу работу, он поймет, что мы пригодимся в его институте!"
        show el normal pioneer at center with dspr
        stop music fadeout 3
        stop sound
        play music music_list["a_promise_from_distant_days"] fadein 5
        hide el with dspr
        narrator "Электроник потащил мешок в столовую."
        th "Что-то я не помню, что бы в СССР создали робота."
        $ persistent.sprite_time = 'day'
        $ day_time()
        scene bg ext_square_day with fade
        th "Скорее всего, мир Совёнка не совпадает с моей реальностью."
        th "Что еще, кроме наличия института по созданию роботов, здесь отличается от {i}моего{/i} мира…"
    else:
        $ persistent.sprite_time = 'day'
        $ day_time()
        scene bg ext_square_day with fade
    if p1_drop_muka == True:
        narrator "Поручение Ольги Дмитриевной выполнено, теперь можно отдохнуть."
        jump fortran_ru_p2
    else:
        narrator "Теперь можно выполнить поручение Ольги Дмитриевной и принести муку."
        jump fortran_ru_p1_library
    return
label fortran_ru_p2:
    jump fortran_ru_continue
    return
label fortran_ru_continue:
    scene black with fade
    "..." "Продолжение следует…"
    return