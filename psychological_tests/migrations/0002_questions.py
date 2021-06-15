from django.db import migrations


def forwards(apps, schema_editor):
    PSM25Question = apps.get_model('psychological_tests', 'PSM25Question')
    TailorQuestion = apps.get_model('psychological_tests', 'TailorQuestion')
    EmotionalBurnoutQuestion = apps.get_model('psychological_tests', 'EmotionalBurnoutQuestion')

    PSM25Question.objects.bulk_create([
        PSM25Question(question_text='Обычно я спокоен и вывести меня из этого состояния нелегко'),
        PSM25Question(question_text='Мои нервы расстроены не более, чем у других людей'),
        PSM25Question(question_text='У меня редко бывают запоры'),
        PSM25Question(question_text='У меня редко бывают головные боли'),
        PSM25Question(question_text='Я редко устаю'),
        PSM25Question(question_text='Я почти всегда чувствую себя счастливым'),
        PSM25Question(question_text='Я уверен в себе'),
        PSM25Question(question_text='Я практически никогда не краснею'),
        PSM25Question(question_text='Я человек смелый'),
        PSM25Question(question_text='Я краснею не чаще, чем другие'),
        PSM25Question(question_text='Я редко ощущаю сильное сердцебиение'),
        PSM25Question(question_text='Обычно мои руки теплые (не очень боятся холода)'),
        PSM25Question(question_text='Я застенчив не более, чем другие'),
        PSM25Question(question_text='Мне не хватает чувства уверенности в своих силах'),
        PSM25Question(question_text='Порою мне кажется, что я ни на что не годен'),
        PSM25Question(question_text='Бывают периоды беспокойства, не могу усидеть на месте'),
        PSM25Question(question_text='Меня часто беспокоит желудок'),
        PSM25Question(question_text='Не хватит духа вынести предстоящие трудности'),
        PSM25Question(question_text='Хочется быть счастливым, как другие'),
        PSM25Question(question_text='Кажется, передо мной трудности, которые мне не преодолеть'),
        PSM25Question(question_text='Мне снятся кошмарные сны'),
        PSM25Question(question_text='Когда волнуюсь, дрожат руки'),
        PSM25Question(question_text='У меня беспокойный сон, часто просыпаюсь'),
        PSM25Question(question_text='Меня часто тревожат возможные неудачи'),
        PSM25Question(question_text='Иногда испытываю страх, когда опасности нет'),
        PSM25Question(question_text='Мне трудно сосредоточиться на задании'),
        PSM25Question(question_text='Простую работу делаю часто с напряжением'),
        PSM25Question(question_text='Я легко прихожу в замешательство'),
        PSM25Question(question_text='Почти все время испытываю неясную тревогу'),
        PSM25Question(question_text='Я склонен принимать всерьез даже пустяки'),
        PSM25Question(question_text='Я часто переживаю и плачу'),
        PSM25Question(question_text='У меня бывают приступы тошноты и рвоты'),
        PSM25Question(question_text='Расстройство желудка у меня почти каждый месяц'),
        PSM25Question(question_text='Я боюсь, что при волнении сильно покраснею'),
        PSM25Question(question_text='Мне обычно трудно сосредоточиться на чем-то важном'),
        PSM25Question(
            question_text='Меня постоянно беспокоит желание улучшить свое материальное положение, хотя оно не хуже других'),
        PSM25Question(question_text='Нередко думаю, о чем не хотел бы поделиться с другими, стыдно'),
        PSM25Question(question_text='Иногда из-за переживаний теряю сон'),
        PSM25Question(question_text='Когда волнуюсь, иногда сильно потею'),
        PSM25Question(question_text='Я иногда сильно потею, даже в холодные дни'),
        PSM25Question(question_text='Временами из-за волнения никак не могу заснуть'),
        PSM25Question(question_text='Я человек легко возбудимый'),
        PSM25Question(question_text='Иногда чувствую себя бесполезным человеком'),
        PSM25Question(question_text='Нередко из-за волнения могу легко выйти из себя'),
        PSM25Question(question_text='Я часто ощущаю смутную тревогу'),
        PSM25Question(question_text='Я чувствительнее многих своих товарищей'),
        PSM25Question(question_text='Почти все время испытываю чувство голода'),
        PSM25Question(question_text='Часто кажется, что меня преследуют болезни'),
        PSM25Question(question_text='Часто кажется, что за мной кто-то наблюдает'),
        PSM25Question(question_text='Ожидание всегда меня нервирует'),
    ])

    TailorQuestion.objects.bulk_create([
        TailorQuestion(question_text='Я напряжен и взволнован (взвинчен)'),
        TailorQuestion(question_text='У меня ком в горле, и (или) я ощущаю сухость во рту'),
        TailorQuestion(question_text='Я перегружен работой. Мне совсем не хватает времени'),
        TailorQuestion(question_text='Я проглатываю пищу или забываю поесть'),
        TailorQuestion(
            question_text='Я обдумываю свои идеи снова и снова; я меняю свои планы; мои мысли постоянно повторяются'),
        TailorQuestion(question_text='Я чувствую себя одиноким, изолированным и непонятым'),
        TailorQuestion(
            question_text='Я страдаю от физического недомогания; у меня болит голова, напряжены мышцы шеи, боли в спине, спазмы в желудке'),
        TailorQuestion(question_text='Я поглощен мыслями, измучен или обеспокоен'),
        TailorQuestion(question_text='Меня внезапно бросает то в жар, то в холод'),
        TailorQuestion(question_text='Я забываю о встречах или делах, которые должен сделать или решить'),
        TailorQuestion(question_text='Я легко могу заплакать'),
        TailorQuestion(question_text='Я чувствую себя уставшим'),
        TailorQuestion(question_text='Я крепко стискиваю зубы'),
        TailorQuestion(question_text='Я не спокоен'),
        TailorQuestion(question_text='Мне тяжело дышать, и (или) у меня внезапно перехватывает дыхание'),
        TailorQuestion(
            question_text='Я имею проблемы с пищеварением и с кишечником (боли, колики, расстройства или запоры)'),
        TailorQuestion(question_text='Я взволнован, обеспокоен или смущен'),
        TailorQuestion(question_text='Я легко пугаюсь; шум или шорох заставляет меня вздрагивать'),
        TailorQuestion(question_text='Мне необходимо более чем полчаса для того, чтобы уснуть'),
        TailorQuestion(
            question_text='Я сбит с толку; мои мысли спутаны; мне не хватает сосредоточенности, и я не могу сконцентрировать внимание'),
        TailorQuestion(question_text='У меня усталый вид; мешки или круги под глазами'),
        TailorQuestion(question_text='Я чувствую тяжесть на своих плечах'),
        TailorQuestion(
            question_text='Я встревожен. Мне необходимо постоянно двигаться; я не могу устоять на одном месте'),
        TailorQuestion(question_text='Мне трудно контролировать свои поступки, эмоции, настроения или жесты'),
        TailorQuestion(question_text='Я напряжен'),
    ])

    EmotionalBurnoutQuestion.objects.bulk_create([
        EmotionalBurnoutQuestion(
            question_text='Организационные недостатки на работе постоянно заставляют нервничать, переживать, напрягаться.'),
        EmotionalBurnoutQuestion(question_text='Сегодня я доволен своей профессией не меньше, чем в начале карьеры.'),
        EmotionalBurnoutQuestion(
            question_text='Я ошибся в выборе профессии или профиля деятельности (занимаю не свое место).'),
        EmotionalBurnoutQuestion(
            question_text='Меня беспокоит то, что я стал хуже работать (менее продуктивно, качественно, медленнее).'),
        EmotionalBurnoutQuestion(
            question_text='Теплота взаимодействия с партнерами очень зависит от моего настроения - хорошего или плохого.'),
        EmotionalBurnoutQuestion(question_text='От меня как профессионала мало зависит благополучие партнеров.'),
        EmotionalBurnoutQuestion(
            question_text='Когда я прихожу с работы домой, то некоторое время (часа 2—3) мне хочется побыть наедине, чтобы со мной никто не общался.'),
        EmotionalBurnoutQuestion(
            question_text='Когда я чувствую усталость или напряжение, то стараюсь поскорее решить проблемы партнера (свернуть взаимодействие).'),
        EmotionalBurnoutQuestion(
            question_text='Мне кажется, что эмоционально я не могу дать партнерам того, что требует профессиональный долг.'),
        EmotionalBurnoutQuestion(question_text='Моя работа притупляет эмоции.'),
        EmotionalBurnoutQuestion(
            question_text='Я откровенно устал от человеческих проблем, с которыми приходится иметь дело на работе.'),
        EmotionalBurnoutQuestion(
            question_text='Бывает, я плохо засыпаю (сплю) из-за переживаний, связанных с работой.'),
        EmotionalBurnoutQuestion(question_text='Взаимодействие с партнерами требует от меня большого напряжения'),
        EmotionalBurnoutQuestion(question_text='Работа с людьми приносит все меньше удовлетворения.'),
        EmotionalBurnoutQuestion(question_text='Я бы сменил место работы, если бы представилась возможность.'),
        EmotionalBurnoutQuestion(
            question_text='Меня часто расстраивают то, что я не могу должным образом оказать партнеру профессиональную поддержку, услугу, помощь.'),
        EmotionalBurnoutQuestion(
            question_text='Мне всегда удается предотвратить влияние плохого настроения на деловые контакты.'),
        EmotionalBurnoutQuestion(
            question_text='Меня очень огорчает, если что-то не ладится в отношениях с деловым партнером.'),
        EmotionalBurnoutQuestion(
            question_text='Я настолько устаю на работе, что дома стараюсь общаться как можно меньше.'),
        EmotionalBurnoutQuestion(
            question_text='Из-за нехватки времени, усталости или напряжения часто уделяю внимание партнеру меньше, чем положено.'),
        EmotionalBurnoutQuestion(question_text='Иногда самые обычные ситуации общения на работе вызывают раздражение.'),
        EmotionalBurnoutQuestion(question_text='Я спокойно воспринимаю обоснованные претензии партнеров. '),
        EmotionalBurnoutQuestion(question_text='Общение с партнерами побудило меня сторониться людей.'),
        EmotionalBurnoutQuestion(
            question_text='При воспоминании о некоторых коллегах по работе или партнерах у меня портится настроение.'),
        EmotionalBurnoutQuestion(question_text='Конфликты или разногласия с коллегами отнимают много сил и эмоций.'),
        EmotionalBurnoutQuestion(
            question_text='Мне все труднее устанавливать или поддерживать контакты с деловыми партнерами.'),
        EmotionalBurnoutQuestion(question_text='бстановка на работе мне кажется очень трудной, сложной.'),
        EmotionalBurnoutQuestion(
            question_text='У меня часто возникают тревожные ожидания, связанные с работой: что-то должно случиться, как бы не допустить ошибки, смогу ли сделать все, как надо, не сократят ли и т.п.'),
        EmotionalBurnoutQuestion(
            question_text='Если партнер мне не приятен, я стараюсь ограничить время общения с ним или меньше уделять ему внимания.'),
        EmotionalBurnoutQuestion(
            question_text='В общении на работе я придерживаюсь принципа: «не делай людям добра, не получишь зла».'),
        EmotionalBurnoutQuestion(question_text='Я охотно рассказываю домашним о своей работе.'),
        EmotionalBurnoutQuestion(
            question_text='Бывают дни, когда мое эмоциональное состояние плохо сказывается на результатах работы (меньше делаю, снижается качество, случаются конфликты).'),
        EmotionalBurnoutQuestion(
            question_text='Порой я чувствую, что надо проявить к партнеру эмоциональную отзывчивость, но не могу.'),
        EmotionalBurnoutQuestion(question_text='Я очень переживаю за свою работу.'),
        EmotionalBurnoutQuestion(
            question_text='Партнерам по работе отдаёшь внимания и заботы больше, чем получаешь от них признательности.'),
        EmotionalBurnoutQuestion(
            question_text='При мысли о работе мне обычно становится не по себе: начинает колоть в области сердца, повышается давление, появляется головная боль.'),
        EmotionalBurnoutQuestion(
            question_text='У меня хорошие (вполне удовлетворительные) отношения с непосредственным руководителем.'),
        EmotionalBurnoutQuestion(question_text='Я часто радуюсь, видя, что моя работа приносит пользу людям.'),
        EmotionalBurnoutQuestion(question_text='Последнее время (или как всегда) меня преследуют неудачи в работе.'),
        EmotionalBurnoutQuestion(
            question_text='Некоторые стороны (факты) моей работы вызывают глубокое разочарование, повергают в уныние.'),
        EmotionalBurnoutQuestion(
            question_text='Бывают дни, когда контакты с партнерами складываются хуже, чем обычно. '),
        EmotionalBurnoutQuestion(
            question_text='Я разделяю деловых партнеров (субъектов деятельности) на «хороших» и «плохих».'),
        EmotionalBurnoutQuestion(
            question_text='Усталость от работы приводит к тому, что я стараюсь сократить общение с друзьями и знакомыми.'),
        EmotionalBurnoutQuestion(
            question_text='Я обычно проявляю интерес к личности партнера помимо того, что касается дела. '),
        EmotionalBurnoutQuestion(
            question_text='Обычно я прихожу на работу отдохнувшим, со свежими силами, в хорошем настроении. '),
        EmotionalBurnoutQuestion(
            question_text='Я иногда ловлю себя на том, что работаю с партнерами автоматически, без души.'),
        EmotionalBurnoutQuestion(
            question_text='По работе встречаются настолько неприятные люди, что невольно желаешь им чего-нибудь плохого.'),
        EmotionalBurnoutQuestion(
            question_text='После общения с неприятными партнерами у меня бывает ухудшение физического или психического самочувствия.'),
        EmotionalBurnoutQuestion(
            question_text='На работе я испытываю постоянные физические или психологические перегрузки.'),
        EmotionalBurnoutQuestion(question_text='Успехи в работе вдохновляют меня.'),
        EmotionalBurnoutQuestion(
            question_text='Ситуация на работе, в которой я оказался, кажется безысходной (почти безысходной). '),
        EmotionalBurnoutQuestion(question_text='Я потерял покой из-за работы.'),
        EmotionalBurnoutQuestion(
            question_text='На протяжении последнего года была жалоба (были жалобы) в мой адрес со стороны партнера(ов). '),
        EmotionalBurnoutQuestion(
            question_text='Мне удается беречь нервы благодаря тому, что многое из происходящего с партнерами я не принимаю близко к сердцу.'),
        EmotionalBurnoutQuestion(question_text='Я часто с работы приношу домой отрицательные эмоции.'),
        EmotionalBurnoutQuestion(question_text='Я часто работаю через силу. '),
        EmotionalBurnoutQuestion(question_text='Прежде я был более отзывчивым и внимательным к партнерам, чем теперь.'),
        EmotionalBurnoutQuestion(
            question_text='В работе с людьми руководствуюсь принципом: не трать нервы, береги здоровье.'),
        EmotionalBurnoutQuestion(
            question_text='Иногда иду ни работу с тяжелым чувством: как все надоело, никого бы не видеть и не слышать.'),
        EmotionalBurnoutQuestion(question_text='После напряженного рабочего дня я чувствую недомогание.'),
        EmotionalBurnoutQuestion(question_text='Контингент партнеров, с которым я работаю, очень трудный.'),
        EmotionalBurnoutQuestion(
            question_text='Иногда мне кажется, что результаты моей работы не стоят тех усилий, которые я затрачиваю.'),
        EmotionalBurnoutQuestion(question_text='Если бы мне повезло с работой, я был бы более счастлив.'),
        EmotionalBurnoutQuestion(question_text='Я в отчаянии из-за того, что на работе, у меня серьезные проблемы.'),
        EmotionalBurnoutQuestion(
            question_text='Иногда я поступаю со своими партнерами так, как не хотел бы, чтобы поступали со мной.'),
        EmotionalBurnoutQuestion(
            question_text='Я осуждаю партнеров, которые рассчитывают на особое снисхождение, внимание.'),
        EmotionalBurnoutQuestion(
            question_text='Чаще всего после рабочего дня у меня нет сил, заниматься домашними делами.'),
        EmotionalBurnoutQuestion(question_text='Обычно я тороплю время: скорей бы рабочий день кончился.'),
        EmotionalBurnoutQuestion(
            question_text='Состояния, просьбы, потребности партнеров обычно меня искренне волнуют.'),
        EmotionalBurnoutQuestion(
            question_text='Работая с людьми, я обычно как бы ставлю экран, защищающий от чужих страданий и отрицательных эмоций.'),
        EmotionalBurnoutQuestion(question_text='Работа с людьми (партнерами) очень разочаровала меня.'),
        EmotionalBurnoutQuestion(question_text='Чтобы восстановить силы, я часто принимаю лекарства.'),
        EmotionalBurnoutQuestion(question_text='Как правило, мой рабочий день проходит спокойно и легко.'),
        EmotionalBurnoutQuestion(
            question_text='Мои требования к выполняемой работе выше, чем то, чего я достигаю в силу обстоятельств.'),
        EmotionalBurnoutQuestion(question_text='Моя карьера сложилась удачно.'),
        EmotionalBurnoutQuestion(question_text='Я очень нервничаю из-за всего, что связано с работой.'),
        EmotionalBurnoutQuestion(
            question_text='Некоторых из своих постоянных партнеров я не хотел бы видеть и слышать.'),
        EmotionalBurnoutQuestion(
            question_text='Я одобряю коллег, которые полностью посвящают себя людям (партнерам), забывая о собственных интересах.'),
        EmotionalBurnoutQuestion(
            question_text='Моя усталость на работе обычно мало сказывается (никак не сказывается) в общении с домашними и друзьями.'),
        EmotionalBurnoutQuestion(
            question_text='Если предоставляется случай, я уделяю партнеру меньше внимания, но так, чтобы он этого не заметил.'),
        EmotionalBurnoutQuestion(question_text='Меня часто подводят нервы в общении с людьми на работе.'),
        EmotionalBurnoutQuestion(
            question_text='Ко всему (почти ко всему), что происходит на работе, я утратил интерес, живое чувство.'),
        EmotionalBurnoutQuestion(
            question_text='Работа с людьми плохо повлияла на меня как профессионала — обозлила, сделала нервным, притупила эмоции.'),
        EmotionalBurnoutQuestion(question_text='Работа с людьми явно подрывает мое здоровье.'),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('psychological_tests', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards)
    ]
