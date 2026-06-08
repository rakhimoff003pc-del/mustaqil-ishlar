# -*- coding: utf-8 -*-
"""Har bir mavzuning har bir bo'limiga qo'shiladigan qo'shimcha xulosalovchi paragraf.

Format: EXTRA[(topic_num, section_index_0based)] = "matn"
"""

EXTRA = {
    # Mavzu 1
    (1, 0): "Demak, nutq insonning ijtimoiy va shaxsiy hayotining barcha tomonlarida birlamchi rol o'ynaydi. U muloqot, fikr almashish va tafakkurning quroli bo'lgani holda, bola taraqqiyotining barcha bosqichlarida hal qiluvchi omil sifatida xizmat qiladi. Tarbiyachi nutq mohiyatini chuqur anglagan holda, har bir bola bilan ish olib borishi shart.",
    (1, 1): "Shunday qilib, Nutqini o'stirish metodikasi fani — bola nutqi taraqqiyotini ilmiy asosda boshqarish, rejalashtirish va samarali rivojlantirishga xizmat qiluvchi pedagogika sohasidir. Uning boshqa fanlar bilan keng aloqasi bu fanga ko'p qirralilik baxsh etadi va uni har tomonlama boy qiladi.",
    (1, 2): "Falsafa, fiziologiya va psixologiya bir vaqtda inson nutqining mohiyatini turli tomondan ochib beradi va metodikaga mustahkam ilmiy poydevor yaratadi. Tarbiyachi bu uchta yo'nalishdagi bilimlarsiz turib bola nutqini chinakam tushuna olmaydi va uni ongli ravishda boshqara olmaydi.",
    (1, 3): "Tilshunoslik metodikaga til tizimi haqida bilim, pedagogika esa o'rgatish usullari haqida tajriba beradi. Bu ikki sohaning uyg'unligi nutq o'stirish ishini ham ilmiy, ham amaliy darajada samarali tashkil etish imkonini beradi. Yetuk tarbiyachi har ikkala sohani ham yaxshi biladi.",
    (1, 4): "Ko'p asrlik ilmiy izlanishlar va boy pedagogik tajriba zaminida fan bugungi rivojlangan holatga keldi. Uning kelajagi yangi texnologiyalar, neyropedagogika yutuqlari va integratsiyalashgan ta'lim yondashuvlari bilan bog'liq. Lekin asosiy poydevor — bola sevgisi va ona tilini hurmat qilish — har doim o'zgarmas qoladi.",

    # Mavzu 2
    (2, 0): "Demak, nutqni o'stirish maqsadi — bolada ona tilini erkin va madaniyatli qo'llay olish ko'nikmasini shakllantirish va shu orqali uni har tomonlama yetuk shaxs sifatida tarbiyalashdir. Bu maqsad bir necha o'zaro bog'liq vazifalar majmui orqali amalga oshadi.",
    (2, 1): "Lug'at va grammatik tuzilishni rivojlantirish ishi izchil, rejali va bola yoshiga mos tarzda olib borilishi kerak. Bu ikki yo'nalish bir-birini to'ldiradi: lug'atsiz grammatika ishlamaydi, grammatikasiz esa lug'at to'g'ri ifoda etilmaydi. Tarbiyachi har ikki yo'nalishni teng kuch bilan rivojlantiradi.",
    (2, 2): "Tovush madaniyati va ravon nutqni rivojlantirish nutq sifatining asosiy ko'rsatkichlaridir. Bola tovushlarni to'g'ri talaffuz qilib, fikrlarini izchil bayon eta olganidagina, uning nutqi haqiqiy ma'noda yetuk hisoblanadi. Bu vazifalar maxsus va izchil ishni talab qiladi.",
    (2, 3): "Tarbiyaviy va ma'rifiy vazifalar nutqni o'stirish ishining ma'naviy o'qini tashkil etadi. Til orqali bola nafaqat so'z, balki qadriyat, fazilat va madaniyatni ham o'zlashtiradi. Shu sababli har bir nutq mashg'uloti bir vaqtda tarbiyaviy mashg'ulot hamdir.",
    (2, 4): "Yosh xususiyatlariga muvofiq vazifalar va Davlat dasturi talablari tarbiyachining ish rejasini belgilab beradi. Lekin formal talablardan ortiq, asosiy mezon — bolaning haqiqiy taraqqiyoti va uning yetuk shaxs sifatida shakllanishidir. Pedagogik mahorat aynan shu nuqtada namoyon bo'ladi.",

    # Mavzu 3
    (3, 0): "Kichik yoshdagi bola nutqi xususiyatlarini bilish — tarbiyachi ishining poydevoridir. Bu xususiyatlar tabiiy va o'tkinchi: ular vaqt o'tishi va to'g'ri tashkil etilgan ish bilan bartaraf etiladi. Tarbiyachi sabr bilan, bola yoshiga ishonib, izchil ish olib borishi kerak.",
    (3, 1): "Asosiy metodlarning birgalikda va to'g'ri qo'llanilishi bola nutqining barcha tomonlarini bir vaqtda rivojlantiradi. Tarbiyachi har bir metodning kuchli va zaif tomonlarini bilib, ularni vaziyat va maqsadga muvofiq tanlashi kerak. Metodikadagi ijodkorlik — pedagogik mahoratning belgisidir.",
    (3, 2): "Vositalarning xilma-xilligi va sifati bola taraqqiyotini boyitadi. O'yinchoq, surat va kitob — bog'cha hayotining \"uch tayanchi\" sifatida ish ko'radi. Tarbiyachi bu vositalarni doimiy yangilab va boyitib borishi shart, chunki bola qiziqishi ham vaqt bilan o'zgaradi.",
    (3, 3): "Mashg'ulotlarning to'g'ri tashkil etilishi va kundalik tartib elementlaridan unumli foydalanish nutq ishining muvaffaqiyatini ta'minlaydi. Mashg'ulot — alohida olingan bo'lak emas, balki bog'cha hayotining bir qismidir va u barcha rejim daqiqalari bilan uzviy bog'langandir.",
    (3, 4): "Oila bilan hamkorlik bog'cha ishini ikki barobar samarali qiladi. Tarbiyachi va ota-onalar bir tilda gaplashganda, bola hayotining barcha sohalari pedagogik ta'sirga qamralib oladi. Bu — eng samarali va mantiqiy yondashuvdir.",

    # Mavzu 4
    (4, 0): "O'rta guruh bolalari yangi imkoniyatlar va yangi qiyinchiliklar davriga kiradilar. Tarbiyachining vazifasi — bu imkoniyatlarni ro'yobga chiqarish va qiyinchiliklarni yengishga yordam berishdir. Bu yoshda ishning samaradorligi keyingi yillar uchun mustahkam poydevor yaratadi.",
    (4, 1): "Lug'atni boyitish o'rta guruhda yangi sifat bosqichiga ko'tariladi. Endi muhimi nafaqat so'zlar miqdori, balki ularning aniqligi, xilma-xilligi va o'rinli qo'llanilishidir. Bu — bola nutqining yetuk darajaga yo'l olishidir.",
    (4, 2): "Grammatika va tovush madaniyati nutq sifatining ikki muhim ko'rsatkichidir. Ular ustida ish maxsus, lekin ayni paytda kundalik faoliyatga singdirilgan tarzda olib boriladi. Tarbiyachi har bir bola nutq xususiyatlariga individual yondashadi.",
    (4, 3): "Ravon nutqning ikki shakli — dialog va monolog — bog'cha hayotida o'zaro to'ldiruvchi ravishda rivojlantiriladi. Dialog ijtimoiy ko'nikmalar uchun, monolog esa aqliy taraqqiyot uchun zaruriydir. Har ikkalasi tarbiyachi e'tiborida bo'ladi.",
    (4, 4): "Mashg'ulot, kundalik faoliyat va oilaviy hamkorlik bola nutqi rivojlanishining uch poydevoridir. Bu uchtasi yagona tizim sifatida ishlaganda, bola nutqi har tomonlama va uyg'un rivojlanadi. Tarbiyachi bu uchligini doimiy nazoratda tutadi.",

    # Mavzu 5
    (5, 0): "Katta guruh bolalari maktab ostonasida turibdilar va bu davrning har bir kuni qadrli. Tarbiyachi bola taraqqiyotini chuqur tahlil qilib, har bir individual ehtiyojga javob berishi kerak. Bu yosh — bog'chaning eng mas'uliyatli davridir.",
    (5, 1): "Lug'atni chuqurlashtirish va so'z ma'nosini boyitish — katta guruhning yangi sifat bosqichidir. Bola endi nafaqat so'zlarni, balki ularning ko'p qirrali ma'nolarini, sinonimlari va antonimlarini, ko'chma ma'nolarini ham o'zlashtiradi. Bu — til boyligining haqiqiy egasi bo'lish demakdir.",
    (5, 2): "Grammatik tuzilishni mukammallashtirish va tovush tahlili savod o'rgatishga to'g'ridan-to'g'ri yo'l ochadi. Bu ish bog'chada va maktabda izchillik tamoyili asosida olib boriladi. Bog'cha tarbiyachisi maktab o'qituvchisi bilan tig'iz hamkorlikda ishlashi shart.",
    (5, 3): "Ravon nutq turlari va ijodiy hikoya — bola aqliy taraqqiyotining yorqin ko'rsatkichidir. Bola nafaqat o'rganilganni qayta aytadi, balki o'zi yangi narsa to'qib chiqaradi. Bu — ijodkorlikning kurtaklari va ularni qadrlash kerak.",
    (5, 4): "Maktabga tayyorgarlik kompleks vazifa bo'lib, u nafaqat bilim, balki xulq, motivatsiya va his-tuyg'ularni ham qamrab oladi. Tarbiyachi har bir bola tayyorgarligini individual baholaydi va kerakli yo'nalishda tuzatishlar kiritadi. Maktabga to'liq tayyor bola — bog'chaning eng katta yutug'idir.",

    # Mavzu 6
    (6, 0): "Ravon nutq tushunchasini aniq bilish tarbiyachi ishining muhim sharti hisoblanadi. Faqat tushunchani anglagan pedagog uni amalda rivojlantira oladi. Ravon nutq nazariyasini bilish — pedagogik kompetentsiyaning asosiy qismidir.",
    (6, 1): "Dialogik nutq ijtimoiy ko'nikmalar shakllanishining poydevoridir. Bog'chada dialogni rivojlantirishga ajratiladigan har bir daqiqa bola kelajagi uchun katta investitsiya hisoblanadi. Hech bir bola dialog ko'nikmalarisiz bog'chani tark etmasligi kerak.",
    (6, 2): "Monologik nutqning xilma-xil turlari bola fikrlash va nutqining barcha tomonlarini rivojlantiradi. Tasvirlash, hikoya va mulohaza — uchtasi ham muhim va bola bilan barcha turlar ustida ish olib boriladi. Bu — keng qirrali rivojlanishni ta'minlaydi.",
    (6, 3): "Surat, predmet va tabiat asosida hikoya tuzish bog'cha pedagogikasining klassik ish turlaridir. Ular bola tasavvurini, kuzatuvchanligini va nutqini birga rivojlantiradi. Tarbiyachi bu ish turlarini muntazam va xilma-xil olib boradi.",
    (6, 4): "Tarbiyachining kasbiy mahorati va xatolarni samarali bartaraf etish ko'nikmasi ravon nutqni rivojlantirishning muvaffaqiyat shartidir. Pedagog doimiy ravishda o'z ustida ishlashi va yangi metodlarni o'rganishi kerak. Bu — uzluksiz kasbiy rivojlanish jarayonidir.",

    # Mavzu 7
    (7, 0): "Dialogik nutqning psixologik-pedagogik mohiyatini tushunish tarbiyachining ish samaradorligini sezilarli darajada oshiradi. Pedagog dialogni shunchaki muloqot emas, bola taraqqiyotining quroli sifatida qarashi kerak. Bu — chuqur pedagogik yondashuvdir.",
    (7, 1): "Bola ijtimoiylashuvi dialog orqali amalga oshadi va bu bog'chaning eng muhim vazifalaridan biridir. Hech bir bilim sotsialashuvga teng kelmaydi. Bog'cha — bolaning birinchi va eng samarali \"jamiyat maktabi\"dir.",
    (7, 2): "Dialogning bola shaxsiyatiga ta'siri uzoq muddatli va chuqurdir. Bog'chada o'rganilgan dialog ko'nikmalari bolaning butun keyingi hayotida foyda keltiradi. Pedagog bu mas'uliyatni doimo his qilib turishi shart.",
    (7, 3): "Bog'chada dialogni rivojlantirishning xilma-xil yo'l va metodlari mavjud va tarbiyachi ularning barchasini bilishi va qo'llay olishi kerak. Birgina metodga tayanish samarasiz, kompleks yondashuv esa yuqori natija beradi. Bu — pedagogik ustalikning ko'rsatkichidir.",
    (7, 4): "Diagnostika va yo'naltirish — pedagogik faoliyatning ikki muhim ustunidir. Diagnostikasiz harakat ko'r-ko'rona, yo'naltirishsiz diagnostika foydasizdir. Yetuk tarbiyachi bu ikkalasini birga olib boradi va shu orqali har bir bola taraqqiyotini ta'minlaydi.",

    # Mavzu 8
    (8, 0): "Monologik nutq tushunchasi va turlarini chuqur bilish tarbiyachining samarali ish olib borishi uchun zaruriydir. Bu nazariy bilim amaliy faoliyatga ilmiy poydevor yaratadi. Pedagog nazariya va amaliyotni uyg'unlashtira olishi kerak.",
    (8, 1): "Psixologik-pedagogik asoslarni hisobga olmaslik — eng katta xato. Bola psixologiyasini tushunmagan pedagog uning nutqini ham, shaxsiyatini ham to'g'ri rivojlantira olmaydi. Psixologiya — pedagogning eng yaqin va eng zarur sherigidir.",
    (8, 2): "Tasvirlash va hikoya qilish — monologik nutqning ikki tayanch ustuni. Ularni ketma-ket va izchil o'rgatish bola nutq qobiliyatini bosqichma-bosqich rivojlantiradi. Tarbiyachi bu izchilllikka qattiq amal qilishi shart.",
    (8, 3): "Qayta hikoya va ijodiy hikoya monologning yetuk va ijodiy bosqichlaridir. Ular bola nafaqat takrorlay olishini, balki yangi narsa yarata olishini ham ko'rsatadi. Bu — bog'cha pedagogikasining yorqin natijasidir.",
    (8, 4): "Vositalarning xilma-xilligi va to'g'ri baholash — monologik nutqni rivojlantirishning kafolatidir. Boy material bazasi va aniq baholash mezonlari bo'lmagan ishda haqiqiy yutuq bo'lmaydi. Tarbiyachi bularning ikkalasiga ham e'tibor qaratadi.",

    # Mavzu 9
    (9, 0): "Lug'at va lug'at ishi tushunchalarini aniq bilish — pedagogik faoliyatning birinchi sharti. Ko'p tarbiyachilar lug'at ishini juda tor doirada tushunadilar va shu sababli uning to'liq imkoniyatlaridan foydalana olmaydilar. Nazariy bilim — amaliy yutuqning yo'lboshchisidir.",
    (9, 1): "Bola lug'atining shakllanish qonuniyatlarini bilmasdan turib, lug'at ishini ilmiy asosda olib bo'lmaydi. Har bir tarbiyachi bola yoshi bo'yicha lug'at dinamikasini, uning sifat va miqdor xususiyatlarini bilishi shart. Bu — kasbiy mas'uliyatning bir qismidir.",
    (9, 2): "Lug'at ishining to'rt asosiy vazifasi — boyitish, mustahkamlash, faollashtirish va aniqlashtirish — yagona tizim sifatida hal etiladi. Bir vazifani boshqasidan ajratib bo'lmaydi va ular bir vaqtda har bir mashg'ulotda hal qilinadi. Bu — tizimli yondashuvning afzalligidir.",
    (9, 3): "Tilshunoslik va psixologik asoslar lug'at ishini ilmiy darajaga ko'taradi. Faqat ilmiy asosga tayangan ishgina haqiqiy va barqaror natija beradi. Pedagog bu ikki sohaning yutuqlaridan doimo xabardor bo'lishi kerak.",
    (9, 4): "Lug'at ishining tamoyillari va metodlari pedagogik mahoratning amaliy ifodasidir. Tamoyillarni qo'llay olgan, metodlarni ijodiy uyg'unlashtira olgan tarbiyachigina haqiqiy yutuqqa erishadi. Bu — kasbiy ustalikning eng yuqori bosqichidir.",

    # Mavzu 10
    (10, 0): "Ta'limiy o'yin tushunchasi va tuzilishini chuqur bilmasdan turib, uni samarali qo'llab bo'lmaydi. Tarbiyachi har bir o'yinning tuzilishi, uning didaktik va o'yin vazifalarini, qoidalarini aniq tushunishi shart. Bu — pedagogik nazariyaning amaliy ifodasidir.",
    (10, 1): "Ta'limiy o'yinning lug'at boyitishdagi funksiyalari xilma-xil va kompleksdir. Birgina o'yin bir vaqtda bir necha vazifani hal qiladi va bu uning eng katta afzalligidir. Mohir tarbiyachi har bir o'yindan maksimal foyda chiqaradi.",
    (10, 2): "Lug'at o'yinlarining boy tasnifi tarbiyachiga keng tanlov imkonini beradi. Predmetli, ko'rgazmali va so'zli o'yinlar — bog'cha pedagogikasining \"uch quroli\" hisoblanadi. Tarbiyachi har birini bola yoshi va vazifaga ko'ra qo'llaydi.",
    (10, 3): "O'yinlarni puxta tashkil etish va o'tkazish ish samaradorligining kalitidir. Tasodifiy va tayyorgarliksiz o'yin — quruq vaqt o'tkazishga aylanadi. Pedagogik puxtalik — yutuqning birinchi shartidir.",
    (10, 4): "Yosh guruhlari bo'yicha o'yinlardan to'g'ri foydalanish va tarbiyachining yo'naltiruvchi roli — barcha ish samaradorligining kafolati. Tarbiyachi har bir guruhda o'z rolini aniq bilishi va uni ijodiy amalga oshirishi kerak. Bu — pedagogik mahoratning eng yorqin namoyon bo'lishidir.",

    # Mavzu 11
    (11, 0): "Ta'limiy o'yinning ta'limiy va tarbiyaviy ahamiyati shu darajada kattaki, hech bir boshqa pedagogik vosita uning o'rnini bosa olmaydi. Bog'cha hayotining markazida o'yin turishi tasodif emas, balki pedagogikaning tabiiy talabi va asoslangan tanloviga muvofiq.",
    (11, 1): "O'yin bola aqliy taraqqiyotini yagona kompleks tarzda ta'minlaydi. Boshqa hech bir faoliyat bunday keng ta'sirga ega emas. Shu sababli o'yinni \"vaqt sarflash\" deb hisoblash mutlaqo noto'g'ri va pedagogik nuqtai nazardan zararli yondashuvdir.",
    (11, 2): "O'yinning lug'at boyitishdagi samaradorligi tadqiqotlar va boy pedagogik tajribada ko'p marta tasdiqlangan. An'anaviy va zamonaviy pedagogika bu masalada bir to'xtamga keladi: o'yinsiz haqiqiy lug'at ishi mavjud emas. Bu — pedagogikaning aksiomasidir.",
    (11, 3): "Ijtimoiy-shaxsiy rivojlanish jihatidan o'yin alohida ahamiyat kasb etadi. O'yin orqali bola jamiyatga kiradi va o'zining shaxsiyatini topadi. Bu — bola hayotining eng muhim jarayonlaridan biridir va pedagog uni qo'llab-quvvatlashi shart.",
    (11, 4): "Ta'limiy o'yin samaradorligini oshirish bir qator shartlarga rioya qilish bilan bog'liq. Har bir shart muhim va ularning birortasini ham e'tibordan chetda qoldirish ish natijasini sezilarli darajada pasaytiradi. Pedagogik puxtalik — barcha shartlarni hisobga olishni talab qiladi.",

    # Mavzu 12
    (12, 0): "O'yin tushunchasi va uning bola hayotidagi o'rni — bog'cha pedagogikasining markaziy masalasi. Pedagog bu masalani chuqur anglashi va o'z ish faoliyatini shu tushunchaga muvofiq qurishi shart. Aks holda butun pedagogik faoliyat samarasiz bo'lib qoladi.",
    (12, 1): "O'yinlarning boy tasnifi va xilma-xil turlari tarbiyachiga keng pedagogik palitra beradi. Har bir tur o'z o'rniga ega va tarbiyachi ularni mohirona uyg'unlashtirib, bolaga to'liq qadrli o'yin hayoti yaratib beradi. Bu — pedagogik ustalikning yorqin ifodasidir.",
    (12, 2): "Ijodiy o'yinlar — bog'chaning yuragi. Syujetli-rolli, qurilish va dramalashtirish o'yinlari bolaga eng katta erkinlik va ijodkorlikni beradi. Tarbiyachi ularni qo'llab-quvvatlashi va boyitishi, lekin bola erkinligini bo'g'maslikka harakat qilishi shart.",
    (12, 3): "Qoidali o'yinlar bolada intizom, qoidaga rioya qilish va maqsadga intilishni shakllantiradi. Bular — kelajakdagi maktab va hayot uchun zarur fazilatlardir. Didaktik va harakatli o'yinlar har kuni bog'cha hayotida muhim o'rin tutishi kerak.",
    (12, 4): "Tarbiyachining o'yinlarni tashkil etish va boshqarishdagi roli — pedagogik mahoratning eng nozik va eng murakkab tomoni. Bu mahoratga erishish uchun yillar va yuraklar kerak, lekin natija uning sarflangan kuchlariga arziydi.",

    # Mavzu 13
    (13, 0): "Lug'atni boyituvchi o'yinlarning umumiy tasnifi va xususiyatlari — pedagogik faoliyatning nazariy poydevoridir. Bu nazariy bilimni amaliy mahorat bilan birlashtirgan tarbiyachi haqiqiy yutuqqa erishadi. Nazariya va amaliyot — pedagogning ikki qanoti.",
    (13, 1): "Predmetli o'yinlar bog'cha hayotining moddiy va eng tabiiy qismidir. Real predmet bilan o'ynagan bola so'zni butun sezgilari bilan o'zlashtiradi va bu — eng mustahkam o'rganishdir. Tarbiyachi predmetli o'yinlar uchun boy material bazasini yaratishi shart.",
    (13, 2): "Ko'rgazmali o'yinlar bolaning ko'rgazmali-obrazli fikrlashiga ideal mos keladi. Surat va kartochkalar — bog'cha pedagogikasining klassik vositalaridir va ularning roli zamonaviy texnologiyalar davrida ham kamaymagan. Aksincha, ular yangi texnik imkoniyatlar bilan boyimoqda.",
    (13, 3): "So'zli o'yinlar — lug'at ishining eng yuqori va eng yetuk bosqichi. Ular hech qanday material talab qilmaydi va istalgan vaqt va joyda o'tkazilishi mumkin. Bu — ularning eng muhim afzalligidir va shuning uchun ular oilada ham keng qo'llaniladi.",
    (13, 4): "Ko'rgazmali materiallarni mohirlik bilan tanlash, tayyorlash va qo'llash — pedagogik faoliyatning muhim qismidir. Yaxshi material ish samaradorligini bir necha barobar oshiradi, sifatsiz material esa eng yaxshi metodni ham buzib yuboradi. Pedagog bu nozikliklarga doimo e'tibor berishi shart.",
}
