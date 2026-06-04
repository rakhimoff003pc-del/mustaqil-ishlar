#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mustaqil ish: Sahnalashtirish faoliyatining vazifalari, shakllari va tamoyillari"""
import os, zipfile
from xml.sax.saxutils import escape

OUT = "/projects/sandbox/mustaqil-ishlar/Sahnalashtirish_vazifa_shakl_tamoyil.docx"

PLAN = [
    "Kirish",
    "Sahnalashtirish faoliyatining vazifalari haqida umumiy tushuncha",
    "Sahnalashtirish faoliyatining ta'limiy va rivojlantiruvchi vazifalari",
    "Sahnalashtirish faoliyatining tarbiyaviy vazifalari",
    "Teatr - sahnalashtirish faoliyatining shakllari haqida tushuncha",
    "Teatr turlari va sahnalashtirish faoliyatining asosiy shakllari",
    "Teatr - sahnalashtirish faoliyatining tamoyillari",
    "Faoliyatni tashkil etishda tarbiyachining roli",
    "Xulosa va foydalanilgan adabiyotlar",
]

SECTIONS = []


def make_para(text, bold=False, size=28, align=None, before=120, after=120):
    align_xml = f'<w:jc w:val="{align}"/>' if align else ""
    bold_xml = '<w:b/>' if bold else ""
    safe = escape(text)
    return ('<w:p><w:pPr>' f'<w:spacing w:before="{before}" w:after="{after}" w:line="360" w:lineRule="auto"/>' f'{align_xml}' '<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>' f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>{bold_xml}</w:rPr>' '</w:pPr><w:r><w:rPr>' '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>' f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>{bold_xml}</w:rPr>' f'<w:t xml:space="preserve">{safe}</w:t></w:r></w:p>')

def make_body_para(text):
    safe = escape(text)
    return ('<w:p><w:pPr>' '<w:spacing w:before="0" w:after="120" w:line="360" w:lineRule="auto"/>' '<w:ind w:firstLine="709"/>' '<w:jc w:val="both"/>' '<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>' '<w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>' '</w:pPr><w:r><w:rPr>' '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>' '<w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>' f'<w:t xml:space="preserve">{safe}</w:t></w:r></w:p>')

def page_break():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


# 0. Kirish
SECTIONS.append([
    "Maktabgacha yoshdagi bolalarning har tomonlama va uyg'un rivojlanishida turli faoliyat turlari muhim o'rin tutadi. Ana shunday faoliyat turlaridan biri teatr - sahnalashtirish faoliyatdir. Bu faoliyat bolaga zavq bag'ishlaydi va ayni paytda uni har tomonlama tarbiyalaydi. Sahnalashtirish faoliyatining samaradorligi uning vazifalari, shakllari va tamoyillarini to'g'ri belgilashga bog'liqdir.",
    "Teatr - sahnalashtirish faoliyati bolalarning badiiy asarlar mazmunini sahna ko'rinishlari, rolli o'yinlar va dramatizatsiya orqali ifodalashidir. Bu faoliyat aniq vazifalarga ega bo'lib, turli shakllarda amalga oshiriladi va muayyan tamoyillarga asoslanadi. Bu uch jihatni - vazifalar, shakllar va tamoyillar - chuqur tushunish faoliyatni samarali tashkil etishning asosiy sharti hisoblanadi.",
    "Mazkur mustaqil ishda maktabgacha ta'lim tashkilotida sahnalashtirish faoliyatining vazifalari, teatr - sahnalashtirish faoliyatining shakllari va uning tamoyillari batafsil yoritiladi. Ishda faoliyatning ta'limiy, rivojlantiruvchi va tarbiyaviy vazifalari, turli teatr shakllari hamda asosiy tamoyillar tahlil qilinadi. Mavzuning dolzarbligi shundaki, bu masalalarni bilish tarbiyachiga faoliyatni samarali tashkil etish imkonini beradi.",
])

# 1. Vazifalari haqida umumiy tushuncha
SECTIONS.append([
    "Sahnalashtirish faoliyatining vazifalari - bu faoliyat orqali erishilishi kerak bo'lgan aniq natijalar va maqsadlardir. Vazifalar faoliyatning umumiy maqsadidan kelib chiqadi va uni amaliy jihatdan aniqlashtiradi. To'g'ri belgilangan vazifalar tarbiyachiga faoliyatni rejalashtirish, tashkil etish va natijalarini baholashda yo'l-yo'riq vazifasini bajaradi.",
    "Sahnalashtirish faoliyatining vazifalari pedagogikada an'anaviy ravishda uch asosiy guruhga bo'linadi. Birinchi guruh - ta'limiy vazifalar, ya'ni bolaga bilim va ko'nikmalar berish bilan bog'liq vazifalar. Ikkinchi guruh - rivojlantiruvchi vazifalar, ya'ni bolaning aqliy, nutqiy, ijodiy va jismoniy qobiliyatlarini rivojlantirish bilan bog'liq vazifalar.",
    "Uchinchi guruh - tarbiyaviy vazifalar, ya'ni bolaning shaxsiy sifatlari, axloqiy fazilatlari va hissiy olamini shakllantirish bilan bog'liq vazifalar. Bu uch guruh vazifalar bir-biri bilan uzviy bog'liq bo'lib, ular birgalikda amalga oshiriladi. Faoliyat jarayonida bola bir vaqtning o'zida bilim oladi, qobiliyatlarini rivojlantiradi va tarbiyalanadi.",
    "Vazifalar bolaning yosh xususiyatlariga qarab aniqlashtiriladi. Har bir yosh bosqichida vazifalarning mazmuni va murakkablik darajasi bolaning rivojlanish darajasiga mos bo'lishi kerak. Kichik yoshda oddiy vazifalar - teatrga qiziqish uyg'otish, oddiy harakatlarni o'rgatish - qo'yilsa, katta yoshda murakkab vazifalar - mustaqil obraz yaratish, sahna ko'rinishini tayyorlash - belgilanadi.",
    "Sahnalashtirish faoliyatining vazifalarini aniq belgilash faoliyatning samaradorligini ta'minlaydi. Tarbiyachi har bir mashg'ulot yoki sahna ko'rinishi uchun aniq vazifalar qo'yadi va ular asosida ish olib boradi. Vazifalarga erishilganligini baholash esa faoliyatni doimiy takomillashtirib borish imkonini beradi. Shunday qilib, vazifalar faoliyatning asosini tashkil etadi.",
])


# 2. Ta'limiy va rivojlantiruvchi vazifalar
SECTIONS.append([
    "Sahnalashtirish faoliyatining ta'limiy vazifalari bolaga muayyan bilim va ko'nikmalarni berish bilan bog'liqdir. Birinchi ta'limiy vazifa - bolani teatr san'ati bilan tanishtirish. Bola teatr nima ekanligi, sahna, dekoratsiya, kostyum, aktyor mahorati haqida dastlabki tushunchalarga ega bo'ladi. U teatrga tomoshabin va ishtirokchi sifatida munosabatda bo'lishni o'rganadi.",
    "Ikkinchi ta'limiy vazifa - bolani badiiy asarlar bilan tanishtirish. Sahnalashtirish jarayonida bola ertaklar, hikoyalar va she'rlar mazmunini chuqur o'zlashtiradi, qahramonlar va voqealar bilan tanishadi. Bu uning badiiy adabiyot haqidagi bilimlarini boyitadi. Uchinchi ta'limiy vazifa - bolaga obraz yaratish, rol ijro etish va sahnada harakatlanish ko'nikmalarini o'rgatish.",
    "Sahnalashtirish faoliyatining rivojlantiruvchi vazifalari bolaning turli qobiliyatlarini rivojlantirish bilan bog'liqdir. Birinchi rivojlantiruvchi vazifa - bolaning nutqini rivojlantirish. Faoliyat jarayonida bolaning lug'ati boyiydi, dialogik va monologik nutqi rivojlanadi, talaffuzi va nutq ifodaliligi yaxshilanadi.",
    "Ikkinchi rivojlantiruvchi vazifa - bolaning ijodiy qobiliyatlarini rivojlantirish. Bola fantaziya, ijodiy tasavvur, improvizatsiya va obraz yaratish qobiliyatlarini egallaydi. Uchinchi rivojlantiruvchi vazifa - bolaning bilish jarayonlarini (diqqat, xotira, tafakkur) rivojlantirish. Bola matnni yodlash, rolni eslab qolish va voqealar ketma-ketligini tushunish orqali bu jarayonlarni rivojlantiradi.",
    "To'rtinchi rivojlantiruvchi vazifa - bolaning harakat madaniyati va plastikasini rivojlantirish. Bola harakatlar, mimika va imo-ishoralar orqali obraz yaratishni o'rganadi, bu uning harakat koordinatsiyasi va plastikligini rivojlantiradi. Shunday qilib, ta'limiy va rivojlantiruvchi vazifalar bolaga bilim berish bilan birga uning qobiliyatlarini har tomonlama rivojlantirishga xizmat qiladi.",
])

# 3. Tarbiyaviy vazifalar
SECTIONS.append([
    "Sahnalashtirish faoliyatining tarbiyaviy vazifalari bolaning shaxsiy sifatlari, axloqiy fazilatlari va hissiy olamini shakllantirish bilan bog'liqdir. Bu vazifalar bolani komil inson sifatida tarbiyalashga qaratilgan bo'lib, sahnalashtirish faoliyatining eng muhim jihatlaridan birini tashkil etadi.",
    "Birinchi tarbiyaviy vazifa - bolada axloqiy fazilatlarni shakllantirish. Badiiy asarlar va ertaklar orqali bola yaxshilik va yomonlik, halollik, mehr-shafqat, do'stlik kabi axloqiy tushunchalarni o'zlashtiradi. Bola ijobiy qahramonlarga taqlid qiladi va ulardan ezgu fazilatlarni o'rganadi. Bu uning axloqiy ongini shakllantiradi.",
    "Ikkinchi tarbiyaviy vazifa - bolada ijtimoiy ko'nikmalar va jamoaviylikni shakllantirish. Sahnalashtirish jamoaviy faoliyat bo'lib, bola hamkorlik qilishni, o'z navbatini kutishni, o'rtoqlarini qo'llab-quvvatlashni va jamoa bilan birga ishlashni o'rganadi. Bu uning ijtimoiy hayotga moslashuvini ta'minlaydi.",
    "Uchinchi tarbiyaviy vazifa - bolada hissiy madaniyatni shakllantirish. Bola turli qahramonlar hissiyotlarini ifodalash orqali o'z his-tuyg'ularini tushunishni, ularni boshqarishni va boshqalarning kechinmalarini his qilishni (empatiya) o'rganadi. To'rtinchi tarbiyaviy vazifa - bolada o'ziga ishonch va omma oldida o'zini erkin tutish ko'nikmasini shakllantirish.",
    "Beshinchi tarbiyaviy vazifa - bolada milliy va estetik qadriyatlarni shakllantirish. O'zbek xalq ertaklari va asarlari orqali bola milliy qadriyatlarni, vatanparварlikni va xalq donishmandligini o'zlashtiradi. Shuningdek, bolada go'zallikni his qilish va san'atga muhabbat tuyg'ulari shakllanadi. Shunday qilib, tarbiyaviy vazifalar bolani har tomonlama kamol topgan, axloqli va madaniyatli shaxs sifatida tarbiyalashga xizmat qiladi.",
])


# 4. Shakllari haqida tushuncha
SECTIONS.append([
    "Teatr - sahnalashtirish faoliyatining shakllari deganda bu faoliyatni amalga oshirishning turli usullari va ko'rinishlari tushuniladi. Faoliyat shakllari bolaning yoshi, imkoniyatlari va faoliyatning maqsadiga qarab tanlanadi. To'g'ri tanlangan shakl faoliyatning samaradorligini oshiradi va bolaning qiziqishini ta'minlaydi.",
    "Teatr - sahnalashtirish faoliyatining shakllarini ikki katta guruhga bo'lish mumkin. Birinchi guruh - bolalarning o'zlari ishtirok etadigan faoliyat shakllari (dramatizatsiya o'yinlari). Bunda bolalar bevosita aktyor sifatida qatnashadi, qahramon rolini o'zlari ijro etadi. Ikkinchi guruh - rejissyorlik o'yinlari, bunda bola qo'g'irchoq yoki figuralar yordamida sahna ko'rinishini namoyish etadi.",
    "Faoliyat shakllari shuningdek tashkiliy jihatdan ham farqlanadi. Maxsus mashg'ulotlar shaklida sahnalashtirish - bu tarbiyachi tomonidan rejalashtirilgan va o'tkaziladigan mashg'ulotlardir. Mustaqil teatrlashtirilgan o'yinlar - bu bolalarning erkin faoliyat vaqtida o'z xohishlariga ko'ra o'ynaydigan o'yinlaridir. Bayram va o'yin-kulgilar esa tayyorlangan sahna ko'rinishlarini namoyish etish shaklidir.",
    "Faoliyat shakllari bolaning yoshiga qarab murakkablashib boradi. Kichik yoshda asosan oddiy shakllar - stol usti teatri, tarbiyachi ishtirokidagi oddiy dramatizatsiya - qo'llaniladi. Katta yoshda esa murakkab shakllar - mustaqil dramatizatsiya, to'liq sahna ko'rinishlari, musiqali spektakllar - joriy etiladi.",
    "Faoliyatning turli shakllaridan foydalanish bolaning sahnalashtirish faoliyatini boyitadi va uni har tomonlama rivojlantiradi. Tarbiyachi turli shakllarni uyg'unlashtirib qo'llaydi, bu esa faoliyatni qiziqarli va xilma-xil qiladi. Shakllarning to'g'ri tanlanishi va qo'llanilishi faoliyatning maqsad va vazifalariga erishishni ta'minlaydi.",
])

# 5. Teatr turlari va asosiy shakllar
SECTIONS.append([
    "Teatr - sahnalashtirish faoliyatining asosiy shakllaridan biri dramatizatsiya o'yinlaridir. Bunda bolalarning o'zlari qahramon rolini bajaradi, badiiy asar mazmunini harakat, dialog va mimika orqali ifodalaydi. Dramatizatsiya o'yinlari bolaning ijodiy qobiliyatlarini, nutqini va hissiy olamini eng faol rivojlantiradigan shakl hisoblanadi.",
    "Ikkinchi muhim shakl - qo'g'irchoq teatri. Bunda bola qo'g'irchoqlar yordamida sahna ko'rinishini namoyish etadi. Qo'g'irchoq teatrining turli ko'rinishlari mavjud: barmoq teatri (qo'g'irchoqlar barmoqlarga kiydiriladi), qo'lqop teatri (bibabo), soyali teatr (figuralar soyasi ekranga tushiriladi) va marionetkalar (iplar yordamida boshqariladigan qo'g'irchoqlar).",
    "Uchinchi shakl - stol usti teatri. Bunda kichik o'yinchoqlar, figuralar yoki rasmlar yordamida stol ustida sahna ko'rinishi namoyish etiladi. Bu shakl kichik yoshdagi bolalar uchun qulay bo'lib, ularning nutqi va tasavvurini rivojlantiradi. Stol usti teatri qog'oz figuralar, yog'och yoki plastik o'yinchoqlar yordamida tashkil etiladi.",
    "To'rtinchi shakl - flanelegraf teatri, bunda figuralar maxsus matoli taxtaga yopishtirilib, voqea hikoya qilinadi. Beshinchi shakl - niqobli teatr, bunda bolalar qahramon niqoblarini kiyib, sahna ko'rinishini o'ynaydi. Oltinchi shakl - musiqali sahna ko'rinishlari, bunda sahnalashtirish qo'shiq, raqs va musiqa bilan boyitiladi.",
    "Har bir teatr turi va shakli o'ziga xos imkoniyatlarga ega bo'lib, bolaning muayyan qobiliyatlarini rivojlantiradi. Masalan, qo'g'irchoq teatri uyatchang bolalar uchun qulay, chunki bola qo'g'irchoq ortida o'zini erkinroq his qiladi. Dramatizatsiya esa bolaning aktyorlik mahoratini va o'ziga ishonchini rivojlantiradi. Shunday qilib, turli shakllarning birgalikda qo'llanilishi bolaning sahnalashtirish faoliyatini har tomonlama boyitadi.",
])


# 6. Tamoyillari
SECTIONS.append([
    "Teatr - sahnalashtirish faoliyati muayyan tamoyillarga asoslanadi. Bu tamoyillar faoliyatni ilmiy va pedagogik jihatdan to'g'ri tashkil etishning asosiy qoidalari bo'lib, ularga rioya qilish faoliyatning samaradorligini ta'minlaydi. Birinchi tamoyil - ixtiyoriylik tamoyili. Bola sahnalashtirish faoliyatida o'z xohishi bilan ishtirok etishi kerak, uni majburlash mumkin emas.",
    "Ikkinchi tamoyil - yoshga moslik tamoyili. Faoliyatning mazmuni, shakli va murakkablik darajasi bolaning yosh xususiyatlariga mos bo'lishi kerak. Badiiy asarlar bolaning yoshiga, idrok imkoniyatlariga va qiziqishlariga muvofiq tanlanadi. Uchinchi tamoyil - bosqichmalik va izchillik tamoyili. Faoliyat oddiydan murakkabga qarab izchil olib boriladi.",
    "To'rtinchi tamoyil - individuallik tamoyili. Har bir bolaning qobiliyatlari, qiziqishlari va imkoniyatlari hisobga olinadi. Tarbiyachi har bir bolaga uning imkoniyatlariga mos rol beradi va uni qo'llab-quvvatlaydi. Beshinchi tamoyil - ijodiy faollik tamoyili. Bola tayyor andoza bo'yicha emas, balki o'z ijodiy g'oyalari asosida harakat qilishi rag'batlantiriladi.",
    "Oltinchi tamoyil - emotsionallik tamoyili. Faoliyat bolada ijobiy hissiyotlar uyg'otishi, unga zavq bag'ishlashi kerak. Bola sahnalashtirish jarayonidan quvonish va lazzatlanishi lozim. Yettinchi tamoyil - badiiylik tamoyili. Sahnalashtirish uchun yuksak badiiy qiymatga ega bo'lgan asarlar tanlanadi va ular badiiy jihatdan to'g'ri ifodalanadi.",
    "Sakkizinchi tamoyil - tizimlilik tamoyili. Sahnalashtirish faoliyati tasodifiy emas, balki muntazam va tizimli olib borilishi kerak. To'qqizinchi tamoyil - hamkorlik tamoyili, ya'ni faoliyat bolalar, tarbiyachi va ota-onalar hamkorligida amalga oshiriladi. Bu tamoyillarning barchasi birgalikda sahnalashtirish faoliyatini samarali tashkil etish va uning maqsad hamda vazifalariga erishish imkonini beradi.",
])

# 7. Tarbiyachining roli
SECTIONS.append([
    "Teatr - sahnalashtirish faoliyatini tashkil etishda tarbiyachining roli hal qiluvchi ahamiyatga ega. Tarbiyachi bu faoliyatning tashkilotchisi, yo'naltiruvchisi va ilhomlantiruvchisi sifatida ishtirok etadi. Uning mahorati va ijodiy yondashuvi faoliyatning vazifalariga erishishni, to'g'ri shakl va tamoyillarni qo'llashni ta'minlaydi.",
    "Tarbiyachining birinchi vazifasi - faoliyatni rejalashtirish va tashkil etish. U bolalarning yoshiga mos badiiy asarlarni tanlaydi, faoliyat shaklini belgilaydi, mashg'ulotlarni rejalashtiradi va zarur jihozlarni tayyorlaydi. Tarbiyachi teatr burchagini tashkil etadi va uni qo'g'irchoqlar, niqoblar, kostyumlar bilan boyitadi.",
    "Tarbiyachining ikkinchi vazifasi - bolalarga namuna ko'rsatish va ularni o'rgatish. Tarbiyachi ifodali o'qiydi, obrazlarni namoyish etadi va bolalarga obraz yaratishni, rol ijro etishni o'rgatadi. Uning ifodali nutqi va hissiy ijrosi bolalar uchun asosiy namuna bo'lib xizmat qiladi.",
    "Tarbiyachining uchinchi vazifasi - tamoyillarga rioya qilgan holda har bir bolaning ishtirokini ta'minlash. Tarbiyachi ixtiyoriylik, individuallik va ijodiy faollik tamoyillariga amal qiladi, har bir bolaga mos rol beradi va uyatchang bolalarni rag'batlantiradi. U bolaning ijodiy tashabbusini qo'llab-quvvatlaydi.",
    "Tarbiyachining to'rtinchi vazifasi - ota-onalar bilan hamkorlik qilish va o'z kasbiy mahoratini doimiy oshirib borish. Tarbiyachi ota-onalarni bolaning sahnalashtirish faoliyatiga jalb etadi, bayramlar va sahna ko'rinishlariga taklif qiladi. Shunday qilib, tarbiyachining mahorati, ijodiy yondashuvi va mas'uliyati teatr - sahnalashtirish faoliyatining samaradorligini va bolaning rivojlanishini ta'minlaydi.",
])

# 8. Xulosa
SECTIONS.append([
    "Mazkur mustaqil ishda maktabgacha ta'lim tashkilotida sahnalashtirish faoliyatining vazifalari, teatr - sahnalashtirish faoliyatining shakllari va tamoyillari har tomonlama tahlil qilindi. Tahlillar shuni ko'rsatdiki, bu uch jihat birgalikda sahnalashtirish faoliyatini samarali tashkil etishning asosini tashkil etadi.",
    "Sahnalashtirish faoliyatining vazifalari uch guruhga - ta'limiy, rivojlantiruvchi va tarbiyaviy vazifalarga - bo'linadi. Bu vazifalar birgalikda bolaga bilim berish, uning qobiliyatlarini rivojlantirish va uni komil inson sifatida tarbiyalashga xizmat qiladi. Vazifalar bolaning yosh xususiyatlariga qarab aniqlashtiriladi.",
    "Teatr - sahnalashtirish faoliyatining shakllari xilma-xil bo'lib, ularga dramatizatsiya o'yinlari, qo'g'irchoq teatri, stol usti teatri, soyali teatr va musiqali sahna ko'rinishlari kiradi. Faoliyat esa ixtiyoriylik, yoshga moslik, individuallik, ijodiy faollik, emotsionallik va badiiylik kabi tamoyillarga asoslanadi.",
    "Xulosa qilib aytganda, sahnalashtirish faoliyatining vazifalari, shakllari va tamoyillarini chuqur bilish va ularga amal qilish faoliyatni samarali tashkil etishning asosiy shartidir. To'g'ri tashkil etilgan teatr - sahnalashtirish faoliyati bolani har tomonlama rivojlantiradi va uning ijodkor, nutqi rivojlangan, hissiy boy va ijtimoiy faol shaxs sifatida shakllanishiga zamin yaratadi.",
    "Foydalanilgan adabiyotlar:",
    "1. O'zbekiston Respublikasining \"Maktabgacha ta'lim va tarbiya to'g'risida\"gi Qonuni. - Toshkent, 2020.",
    "2. \"Ilk qadam\" maktabgacha ta'lim muassasalarining Davlat o'quv dasturi. - Toshkent, 2018.",
    "3. Nazarova M. \"Maktabgacha ta'limda teatrlashtirilgan faoliyat metodikasi\". - Toshkent, 2020.",
    "4. Qodirova R. \"Bolalar teatri va sahnalashtirish\". - Toshkent, 2019.",
    "5. Maxaneva M.D. \"Teatralizovannye zanyatiya v detskom sadu\". - Moskva, 2018.",
    "6. Artyomova L.V. \"Teatralizovannye igry doshkolnikov\". - Moskva, 2017.",
])


# Bo'limlarni PLAN tartibiga moslab qayta tartiblash
SEC_ORDERED = [
    SECTIONS[7],  # Kirish
    SECTIONS[8],  # Vazifalar haqida umumiy tushuncha
    SECTIONS[5],  # Ta'limiy va rivojlantiruvchi vazifalar
    SECTIONS[6],  # Tarbiyaviy vazifalar
    SECTIONS[3],  # Shakllari haqida tushuncha
    SECTIONS[4],  # Teatr turlari va asosiy shakllar
    SECTIONS[0],  # Tamoyillari
    SECTIONS[1],  # Tarbiyachining roli
    SECTIONS[2],  # Xulosa
]

body = []
for _ in range(4):
    body.append(make_para("", size=28))
body.append(make_para("O'ZBEKISTON RESPUBLIKASI", bold=True, size=28, align="center"))
body.append(make_para("MAKTABGACHA VA MAKTAB TA'LIMI VAZIRLIGI", bold=True, size=28, align="center"))
body.append(make_para("", size=24))
body.append(make_para("MUSTAQIL ISH", bold=True, size=40, align="center"))
body.append(make_para("", size=24))
body.append(make_para("Mavzu:", bold=True, size=28, align="center"))
body.append(make_para("Maktabgacha ta'lim tashkilotida sahnalashtirish faoliyatining vazifalari. Teatr - sahnalashtirish faoliyatining shakllari va tamoyillari", bold=True, size=28, align="center"))
for _ in range(5):
    body.append(make_para("", size=24))
body.append(make_para("Bajardi: ______________________", size=28, align="right"))
body.append(make_para("Tekshirdi: ______________________", size=28, align="right"))
for _ in range(2):
    body.append(make_para("", size=24))
body.append(make_para("Toshkent - 2026", bold=True, size=28, align="center"))
body.append(page_break())

body.append(make_para("REJA", bold=True, size=32, align="center"))
body.append(make_para("", size=20))
for i, item in enumerate(PLAN, 1):
    body.append(make_para(f"{i}. {item}", size=28))
body.append(page_break())

for idx, (heading, paragraphs) in enumerate(zip(PLAN, SEC_ORDERED)):
    body.append(make_para(f"{idx + 1}. {heading.upper()}", bold=True, size=30, align="center"))
    body.append(make_para("", size=18))
    for p in paragraphs:
        body.append(make_body_para(p))
    if idx < len(SEC_ORDERED) - 1:
        body.append(page_break())


sectPr = '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1134" w:right="850" w:bottom="1134" w:left="1701" w:header="708" w:footer="708" w:gutter="0"/><w:cols w:space="708"/><w:docGrid w:linePitch="360"/></w:sectPr>'
document_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>' + ''.join(body) + sectPr + '</w:body></w:document>'

content_types_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/><Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/><Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/></Types>'
rels_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/></Relationships>'
document_rels_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>'
styles_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="28"/><w:szCs w:val="28"/><w:lang w:val="uz-UZ"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:line="360" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults><w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style></w:styles>'
core_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Mustaqil ish - Sahnalashtirish vazifa shakl tamoyil</dc:title><dc:creator>Talaba</dc:creator></cp:coreProperties>'
app_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"><Application>Microsoft Office Word</Application></Properties>'

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml', content_types_xml)
    z.writestr('_rels/.rels', rels_xml)
    z.writestr('word/_rels/document.xml.rels', document_rels_xml)
    z.writestr('word/document.xml', document_xml)
    z.writestr('word/styles.xml', styles_xml)
    z.writestr('docProps/core.xml', core_xml)
    z.writestr('docProps/app.xml', app_xml)

print(f"Created: {OUT}")
print(f"Size: {os.path.getsize(OUT)} bytes")
