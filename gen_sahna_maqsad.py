#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mustaqil ish: Sahnalashtirish faoliyatining asosiy maqsadi"""
import os, zipfile
from xml.sax.saxutils import escape

OUT = "/projects/sandbox/mustaqil-ishlar/Sahnalashtirish_asosiy_maqsadi.docx"

PLAN = [
    "Kirish",
    "Sahnalashtirish faoliyati tushunchasi va uning umumiy maqsadi",
    "Bolaning ijodiy qobiliyatlarini rivojlantirish maqsadi",
    "Bolaning nutqi va muloqot ko'nikmalarini rivojlantirish maqsadi",
    "Bolaning hissiy-emotsional olamini boyitish maqsadi",
    "Bolaning ijtimoiy va axloqiy tarbiyasi maqsadi",
    "Bolaning badiiy-estetik didini shakllantirish maqsadi",
    "Maqsadga erishishning shartlari va tarbiyachining roli",
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
    "Maktabgacha yoshdagi bolalarning har tomonlama va uyg'un rivojlanishida turli faoliyat turlari muhim o'rin tutadi. Ana shunday faoliyat turlaridan biri sahnalashtirish (teatrlashtirilgan) faoliyatdir. Bu faoliyat bolaga zavq bag'ishlaydi va ayni paytda uni har tomonlama tarbiyalaydi. Sahnalashtirish faoliyatining samaradorligi ko'p jihatdan uning maqsadini to'g'ri belgilashga bog'liq.",
    "Sahnalashtirish faoliyati - bu bolalarning badiiy asarlar, ertaklar va hikoyalar mazmunini sahna ko'rinishlari, rolli o'yinlar va dramatizatsiya orqali ifodalashidir. Bu faoliyatning asosiy maqsadi bolaning shaxsini har tomonlama rivojlantirish bo'lib, u bir nechta o'zaro bog'liq yo'nalishlarni qamrab oladi. Maqsadni aniq tushunish tarbiyachiga faoliyatni samarali tashkil etish imkonini beradi.",
    "Mazkur mustaqil ishda maktabgacha ta'lim tashkilotida sahnalashtirish faoliyatining asosiy maqsadi batafsil yoritiladi. Ishda faoliyatning umumiy maqsadi, uning ijodiy, nutqiy, hissiy, ijtimoiy va estetik yo'nalishlari hamda maqsadga erishish shartlari tahlil qilinadi. Mavzuning dolzarbligi shundaki, faoliyatning maqsadini aniq belgilash uni samarali amalga oshirishning birinchi va eng muhim shartidir.",
])

# 1. Tushunchasi va umumiy maqsadi
SECTIONS.append([
    "Sahnalashtirish faoliyati - bu adabiy asar yoki uning bir qismini sahna ko'rinishida, ya'ni harakatlar, dialoglar, mimika va imo-ishoralar orqali ifodalashga asoslangan badiiy-ijodiy faoliyatdir. Bu faoliyat teatr san'ati elementlarini bolalar faoliyatiga olib kiradi va o'yin tabiatiga ega bo'lib, bola uchun qiziqarli va jozibalidir.",
    "Maktabgacha ta'lim tashkilotida sahnalashtirish faoliyatining asosiy maqsadi - bolaning ijodiy qobiliyatlarini, nutqini, hissiy olamini, ijtimoiy ko'nikmalarini va badiiy-estetik didini rivojlantirish orqali uning shaxsini har tomonlama va uyg'un kamol toptirishdir. Bu maqsad bolaning butun shaxsiy rivojlanishini qamrab oladi.",
    "Faoliyatning asosiy maqsadi bir nechta tarkibiy qismdan iborat. Bu qismlar o'zaro bog'liq bo'lib, ular birgalikda bolaning yaxlit rivojlanishini ta'minlaydi. Maqsadning birinchi qismi - ijodiy rivojlanish, ikkinchi qismi - nutqiy rivojlanish, uchinchi qismi - hissiy rivojlanish, to'rtinchi qismi - ijtimoiy-axloqiy rivojlanish va beshinchi qismi - estetik rivojlanishdir.",
    "Sahnalashtirish faoliyatining maqsadi \"Ilk qadam\" davlat o'quv dasturining umumiy maqsadlari bilan uyg'undir. Dastur ham bolani faol, mustaqil, ijodkor va har tomonlama rivojlangan shaxs sifatida tarbiyalashni ko'zda tutadi. Sahnalashtirish faoliyati aynan shu maqsadga erishishning samarali vositalaridan biri hisoblanadi.",
    "Faoliyatning maqsadi bolaning yoshiga qarab aniqlashtiriladi. Kichik yoshda asosiy e'tibor bolada teatrga qiziqish uyg'otish va oddiy harakatlarni o'rgatishga qaratilsa, katta yoshda esa bolaning mustaqil ijodiy faoliyati, murakkab obrazlar yaratishi va to'liq sahna ko'rinishlarida ishtirok etishiga yo'naltiriladi. Shunday qilib, maqsad bolaning rivojlanish darajasiga mos ravishda murakkablashib boradi.",
])


# 2. Ijodiy qobiliyatlarni rivojlantirish maqsadi
SECTIONS.append([
    "Sahnalashtirish faoliyatining eng muhim maqsadlaridan biri - bolaning ijodiy qobiliyatlarini rivojlantirishdir. Ijodkorlik - bu inson shaxsining eng qimmatli sifatlaridan biri bo'lib, uning asoslari aynan maktabgacha yoshda shakllanadi. Sahnalashtirish faoliyati bola ijodkorligini namoyon qilishi va rivojlantirishi uchun keng imkoniyatlar yaratadi.",
    "Sahnalashtirish jarayonida bola o'z fantaziyasini faol ishga soladi. U badiiy asar qahramonini o'z tasavvurida jonlantiradi, uning qiyofasini, xatti-harakatlarini va xarakterini o'ziga xos tarzda talqin etadi. Bu jarayonda bolaning ijodiy tasavvuri rivojlanadi va u nostandart fikrlashni o'rganadi.",
    "Faoliyat bolada improvizatsiya qilish qobiliyatini rivojlantiradi. Bola tayyor andoza bo'yicha emas, balki o'z g'oyalari asosida harakat qiladi, yangi dialoglar va harakatlar o'ylab topadi. Improvizatsiya bolaning ijodiy erkinligini ta'minlaydi va uning o'ziga xos ijodiy uslubini shakllantiradi.",
    "Sahnalashtirish faoliyati bolaning badiiy obraz yaratish qobiliyatini rivojlantiradi. Bola qahramon obrazini yaratish uchun uning nutqi, harakati, mimikasi va hissiyotlari ustida ishlaydi. Bu jarayon bolaning badiiy tafakkurini va ijodiy mahoratini oshiradi. Bola obraz orqali o'z ichki olamini ifodalashni o'rganadi.",
    "Shuningdek, sahnalashtirish faoliyati bolada dekoratsiya, kostyum va atributlar yaratishda ijodiy yondashuvni rag'batlantiradi. Bola sahna ko'rinishini tayyorlashda o'z g'oyalarini taklif etadi, materiallardan ijodiy foydalanadi. Shunday qilib, ijodiy qobiliyatlarni rivojlantirish sahnalashtirish faoliyatining asosiy maqsadlaridan biri bo'lib, u bolaning kelajakdagi ijodiy salohiyatining poydevorini yaratadi.",
])

# 3. Nutqni rivojlantirish maqsadi
SECTIONS.append([
    "Sahnalashtirish faoliyatining muhim maqsadlaridan biri - bolaning nutqi va muloqot ko'nikmalarini rivojlantirishdir. Nutq bolaning aqliy va ijtimoiy rivojlanishining asosiy ko'rsatkichi bo'lib, sahnalashtirish faoliyati uni rivojlantirishning eng tabiiy va samarali vositalaridan biridir.",
    "Sahnalashtirish jarayonida bolaning lug'ati sezilarli darajada boyiydi. Bola badiiy asarlardagi yangi so'zlar, iboralar va badiiy ifodalarni o'zlashtiradi va ularni o'z nutqida qo'llaydi. Rollarni ijro etish bolaning faol lug'atini kengaytiradi va uning nutqini badiiy jihatdan boyitadi.",
    "Faoliyat bolaning dialogik va monologik nutqini rivojlantiradi. Rollarni ijro etish jarayonida bola dialoglar tuzadi, savol-javob qiladi va o'z fikrini izchil bayon etadi. Bu uning bog'lanishli nutqini shakllantiradi. Bola suhbatda faol ishtirok etishni va o'z fikrini erkin ifodalashni o'rganadi.",
    "Sahnalashtirish faoliyati bolaning nutq ifodaliligini rivojlantiradi. Bola matnni ifodali aytishni, intonatsiyadan to'g'ri foydalanishni, ovoz balandligi va sur'atini o'zgartirishni o'rganadi. U o'z nutqini hissiyot bilan boyitadi va uni ta'sirchan qiladi. Bu nutqning eng muhim sifatlaridan biri hisoblanadi.",
    "Bundan tashqari, faoliyat bolaning tovush talaffuzini yaxshilaydi va nutq nafasini rivojlantiradi. Matnlarni ifodali aytish jarayonida bola tovushlarni to'g'ri talaffuz qilishni mashq qiladi. Shuningdek, sahnalashtirish bolaning noverbal muloqot - mimika, imo-ishora, tana harakati - vositalaridan foydalanishni ham o'rgatadi. Shunday qilib, nutqni rivojlantirish sahnalashtirish faoliyatining muhim maqsadlaridan biridir.",
])


# 4. Hissiy-emotsional olamini boyitish maqsadi
SECTIONS.append([
    "Sahnalashtirish faoliyatining yana bir muhim maqsadi - bolaning hissiy-emotsional olamini boyitishdir. Hissiyotlar inson hayotida muhim o'rin tutadi va bolaning hissiy rivojlanishi uning shaxsiy kamolotining ajralmas qismi hisoblanadi. Sahnalashtirish faoliyati bolaning hissiy olamini rivojlantirish uchun keng imkoniyatlar yaratadi.",
    "Sahnalashtirish jarayonida bola turli qahramonlar qiyofasiga kiradi va ularning hissiyotlarini - quvonch, qayg'u, qo'rquv, hayrat, g'azab - his qiladi va ifodalaydi. Bu jarayonda bolaning hissiy sezgirligi rivojlanadi va u turli his-tuyg'ularni tushunishni o'rganadi. Bola hissiyotlarning xilma-xilligini va ularning ifoda usullarini o'zlashtiradi.",
    "Faoliyat bolaga o'z his-tuyg'ularini ifodalashni o'rgatadi. Ko'pincha bola o'z hissiyotlarini so'z bilan ifodalay olmaydi, lekin sahna ko'rinishida obraz orqali u ularni erkin namoyon etadi. Bu bolaning hissiy ifoda ko'nikmalarini rivojlantiradi va uning emotsional erkinligini ta'minlaydi.",
    "Sahnalashtirish faoliyati bolada empatiya - boshqalarning his-tuyg'ularini tushunish va his qilish qobiliyatini shakllantiradi. Qahramon hissiyotlarini ifodalash orqali bola boshqalarning kechinmalarini tushunishni o'rganadi. Empatiya bolaning ijtimoiy-emotsional rivojlanishining muhim asosi hisoblanadi.",
    "Bundan tashqari, sahnalashtirish faoliyati bolaning hissiy holatini muvozanatlashtiradi. Bola sahnada o'z hissiyotlarini ijobiy yo'nalishda ifodalaydi, bu uning ruhiy salomatligiga ijobiy ta'sir ko'rsatadi. Faoliyat bolaga o'z qo'rquvlari va xavotirlarini yengishga, o'ziga ishonchni mustahkamlashga yordam beradi. Shunday qilib, hissiy-emotsional olamni boyitish sahnalashtirish faoliyatining muhim maqsadlaridan biridir.",
])

# 5. Ijtimoiy va axloqiy tarbiya maqsadi
SECTIONS.append([
    "Sahnalashtirish faoliyatining muhim maqsadlaridan biri - bolaning ijtimoiy va axloqiy tarbiyasini ta'minlashdir. Sahnalashtirish jamoaviy faoliyat bo'lib, u bolada ijtimoiy ko'nikmalarni shakllantirish uchun qulay sharoit yaratadi. Bola jamoada ishlashni va boshqalar bilan hamkorlik qilishni o'rganadi.",
    "Sahnalashtirish jarayonida bola jamoa bilan birga ishlaydi. U o'z rolini jamoaning umumiy maqsadiga bo'ysundirishni, o'rtoqlari bilan kelishishni va birgalikda umumiy natijaga erishishni o'rganadi. Bu uning jamoaviylik tuyg'usini va hamkorlik ko'nikmalarini rivojlantiradi.",
    "Faoliyat bolada o'zaro hurmat, yordam berish va o'rtoqlarini qo'llab-quvvatlash kabi ijtimoiy fazilatlarni shakllantiradi. Bola o'z navbatini kutishni, boshqalarning fikrini hurmat qilishni va nizolarni tinch yo'l bilan hal etishni o'rganadi. Bu ko'nikmalar bolaning ijtimoiy hayotda muvaffaqiyatli faoliyat ko'rsatishi uchun zarurdir.",
    "Sahnalashtirish faoliyati bolaning axloqiy tarbiyasida muhim rol o'ynaydi. Badiiy asarlar va ertaklar orqali bola yaxshilik va yomonlik, halollik va aldoq, mehr va shafqatsizlik kabi axloqiy tushunchalarni o'zlashtiradi. Bola ijobiy qahramonlarga taqlid qiladi va ulardan ezgu fazilatlarni o'rganadi.",
    "Bundan tashqari, faoliyat bolada milliy va umuminsoniy qadriyatlarni shakllantiradi. O'zbek xalq ertaklari va asarlari orqali bola milliy qadriyatlarni, vatanparварlikni va xalq donishmandligini o'zlashtiradi. Shunday qilib, ijtimoiy va axloqiy tarbiya sahnalashtirish faoliyatining muhim maqsadlaridan bo'lib, u bolani jamiyatda yashashga va ezgu insoniy fazilatlarga ega bo'lishga tayyorlaydi.",
])


# 6. Badiiy-estetik didini shakllantirish maqsadi
SECTIONS.append([
    "Sahnalashtirish faoliyatining muhim maqsadlaridan biri - bolaning badiiy-estetik didini shakllantirishdir. Estetik tarbiya bolaning go'zallikni his qilish, uni qadrlash va undan zavqlanish qobiliyatini rivojlantirishni o'z ichiga oladi. Sahnalashtirish faoliyati san'at turi sifatida bolaning estetik tarbiyasiga katta hissa qo'shadi.",
    "Sahnalashtirish jarayonida bola badiiy asarning go'zalligini his qiladi. U asar mazmunining nafisligini, qahramonlar obrazlarining jozibadorligini va badiiy so'zning ta'sirchanligini idrok etadi. Bu bolaning badiiy didini shakllantiradi va unda go'zallikka intilish tuyg'usini uyg'otadi.",
    "Faoliyat bolaning teatr san'ati bilan tanishuvini ta'minlaydi. Bola teatr nima ekanligini, sahna, dekoratsiya, kostyum, aktyor mahorati haqida tushuncha hosil qiladi. Bu uning san'at olamiga kirib borishiga va madaniy saviyasining oshishiga yordam beradi. Bola san'atni tushunish va qadrlashni o'rganadi.",
    "Sahnalashtirish faoliyati bolada estetik baho berish qobiliyatini rivojlantiradi. Bola go'zal va nafis sahna ko'rinishini oddiy ko'rinishdan farqlashni, badiiy ijroni baholashni o'rganadi. U asta-sekin yuksak badiiy qiymatga ega bo'lgan asarlarni tanlashni va ulardan zavqlanishni o'rganadi.",
    "Bundan tashqari, faoliyat bolaning harakat madaniyati va plastikasini rivojlantiradi. Bola sahna harakatlarining go'zalligini, raqs va plastik harakatlarning nafisligini his qiladi va o'zlashtiradi. Shunday qilib, badiiy-estetik didni shakllantirish sahnalashtirish faoliyatining muhim maqsadlaridan bo'lib, u bolaning ma'naviy olamini boyitadi va uni go'zallikni sevadigan shaxs sifatida tarbiyalaydi.",
])

# 7. Maqsadga erishish shartlari va tarbiyachi roli
SECTIONS.append([
    "Sahnalashtirish faoliyatining asosiy maqsadiga erishish uchun bir qator shartlarga rioya qilish zarur. Birinchi shart - faoliyatni bolaning yosh xususiyatlariga moslashtirish. Har bir yosh bosqichida maqsad, mazmun va usullar bolaning rivojlanish darajasiga mos bo'lishi kerak. Bu maqsadga erishishning asosiy shartidir.",
    "Ikkinchi shart - qulay rivojlantiruvchi muhit yaratish. Guruh xonasida teatr burchagi tashkil etilib, u turli xil qo'g'irchoqlar, kostyumlar, niqoblar, dekoratsiyalar va atributlar bilan boyitilishi kerak. Bunday muhit bolaning sahnalashtirish faoliyatiga qiziqishini oshiradi va uning mustaqil faoliyatini qo'llab-quvvatlaydi.",
    "Uchinchi shart - bolalarning yoshiga mos badiiy asarlarni to'g'ri tanlash. Asarlar bolaga tushunarli, qiziqarli, badiiy jihatdan yuksak va tarbiyaviy ahamiyatga ega bo'lishi kerak. To'g'ri tanlangan asar maqsadga erishishni osonlashtiradi va bolaning rivojlanishiga ijobiy ta'sir ko'rsatadi.",
    "Maqsadga erishishda tarbiyachining roli hal qiluvchi ahamiyatga ega. Tarbiyachi faoliyatni rejalashtiradi, tashkil etadi va yo'naltiradi. U bolalarga namuna ko'rsatadi, ularning ijodiy tashabbusini rag'batlantiradi va har bir bolaning ishtirokini ta'minlaydi. Tarbiyachining mahorati va ijodiy yondashuvi faoliyat samaradorligini belgilaydi.",
    "Tarbiyachi shuningdek har bir bolaga individual yondashadi, uyatchang bolalarni qo'llab-quvvatlaydi va ularning o'ziga ishonchini mustahkamlaydi. U ota-onalar bilan hamkorlik qiladi va o'z kasbiy mahoratini doimiy oshirib boradi. Bularning barchasi sahnalashtirish faoliyatining asosiy maqsadiga to'liq erishish imkonini beradi. Shunday qilib, maqsadga erishish ko'p omillarga, ayniqsa tarbiyachining mahoratiga bog'liqdir.",
])


# 8. Xulosa
SECTIONS.append([
    "Mazkur mustaqil ishda maktabgacha ta'lim tashkilotida sahnalashtirish faoliyatining asosiy maqsadi har tomonlama tahlil qilindi. Tahlillar shuni ko'rsatdiki, sahnalashtirish faoliyatining asosiy maqsadi bolaning shaxsini har tomonlama va uyg'un rivojlantirish bo'lib, u bir nechta o'zaro bog'liq yo'nalishlarni qamrab oladi.",
    "Faoliyatning maqsadi bolaning ijodiy qobiliyatlarini rivojlantirish, nutqi va muloqot ko'nikmalarini takomillashtirish, hissiy-emotsional olamini boyitish, ijtimoiy va axloqiy tarbiyasini ta'minlash hamda badiiy-estetik didini shakllantirishni o'z ichiga oladi. Bu yo'nalishlar birgalikda bolaning yaxlit kamolotini ta'minlaydi.",
    "Sahnalashtirish faoliyatining maqsadiga erishish bir qator shartlarga - faoliyatni yoshga moslashtirish, qulay muhit yaratish, mos asarlarni tanlash - va eng muhimi tarbiyachining mahoratiga bog'liqdir. Tarbiyachi faoliyatni to'g'ri tashkil etib, har bir bolaning ishtirokini ta'minlasa, maqsadga to'liq erishish mumkin.",
    "Xulosa qilib aytganda, sahnalashtirish faoliyatining asosiy maqsadi - bolani ijodkor, nutqi rivojlangan, hissiy boy, ijtimoiy faol va estetik didga ega shaxs sifatida tarbiyalashdir. To'g'ri tashkil etilgan sahnalashtirish faoliyati bolaga zavq bag'ishlaydi, uni har tomonlama rivojlantiradi va kelajakda jamiyatga foydali, har tomonlama kamol topgan shaxsni voyaga yetkazishga zamin yaratadi.",
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
    SECTIONS[6],  # Kirish
    SECTIONS[7],  # Tushunchasi va umumiy maqsadi
    SECTIONS[2],  # Ijodiy qobiliyatlar
    SECTIONS[3],  # Nutq
    SECTIONS[4],  # Hissiy-emotsional
    SECTIONS[5],  # Ijtimoiy va axloqiy
    SECTIONS[0],  # Badiiy-estetik did
    SECTIONS[1],  # Shartlar va tarbiyachi roli
    SECTIONS[8],  # Xulosa
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
body.append(make_para("Maktabgacha ta'lim tashkilotida sahnalashtirish faoliyatining asosiy maqsadi", bold=True, size=28, align="center"))
for _ in range(6):
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
core_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Mustaqil ish - Sahnalashtirish asosiy maqsadi</dc:title><dc:creator>Talaba</dc:creator></cp:coreProperties>'
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
