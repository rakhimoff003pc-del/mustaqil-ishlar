#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mustaqil ish: Maktabgacha ta'lim tashkilotida sahnalashtirish faoliyatining maqsad va vazifalari"""
import os, zipfile
from xml.sax.saxutils import escape

OUT = "/projects/sandbox/mustaqil-ishlar/Sahnalashtirish_faoliyati.docx"

PLAN = [
    "Kirish",
    "Sahnalashtirish faoliyati tushunchasi va mohiyati",
    "Sahnalashtirish faoliyatining asosiy maqsadi",
    "Sahnalashtirish faoliyatining vazifalari",
    "Sahnalashtirish faoliyatining turlari",
    "Sahnalashtirish faoliyatining bola rivojlanishidagi ahamiyati",
    "Sahnalashtirish faoliyatini tashkil etish shakllari va bosqichlari",
    "Tarbiyachining sahnalashtirish faoliyatidagi roli",
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
    "Maktabgacha yoshdagi bolalarning har tomonlama va uyg'un rivojlanishida turli faoliyat turlari muhim o'rin tutadi. Ana shunday faoliyat turlaridan biri sahnalashtirish (teatrlashtirilgan) faoliyatdir. Sahnalashtirish faoliyati bolaning ijodiy qobiliyatlarini, nutqini, hissiy olamini va ijtimoiy ko'nikmalarini rivojlantirishga xizmat qiladigan samarali pedagogik vositadir.",
    "Sahnalashtirish faoliyati - bu bolalarning badiiy asarlar, ertaklar va hikoyalar mazmunini sahna ko'rinishlari, roli o'yinlari va dramatizatsiya orqali ifodalashidir. Bu faoliyat o'yin va san'atni o'zida birlashtirib, bolaga zavq bag'ishlaydi va ayni paytda uni tarbiyalaydi. Maktabgacha ta'lim tashkilotlarida sahnalashtirish faoliyatini to'g'ri tashkil etish katta ahamiyatga ega.",
    "Mazkur mustaqil ishda maktabgacha ta'lim tashkilotida sahnalashtirish faoliyatining asosiy maqsadi va vazifalari batafsil yoritiladi. Ishda sahnalashtirish faoliyatining mohiyati, maqsadi, vazifalari, turlari, bola rivojlanishidagi ahamiyati, tashkil etish shakllari va tarbiyachining roli tahlil qilinadi. Mavzuning dolzarbligi shundaki, to'g'ri tashkil etilgan sahnalashtirish faoliyati bolaning ijodiy va shaxsiy kamoloti uchun mustahkam asos yaratadi.",
])

# 1. Tushunchasi va mohiyati
SECTIONS.append([
    "Sahnalashtirish faoliyati - bu adabiy asar yoki uning bir qismini sahna ko'rinishida, ya'ni harakatlar, dialoglar, mimika va imo-ishoralar orqali ifodalashga asoslangan badiiy-ijodiy faoliyatdir. Bu faoliyat teatr san'ati elementlarini bolalar faoliyatiga olib kiradi va bolani badiiy obraz yaratish jarayoniga jalb etadi. Sahnalashtirish faoliyati o'yin tabiatiga ega bo'lib, bola uchun qiziqarli va jozibalidir.",
    "Sahnalashtirish faoliyatining mohiyati shundan iboratki, bola badiiy asar qahramoni qiyofasiga kiradi, uning xatti-harakatlarini, his-tuyg'ularini va nutqini ifodalaydi. Bu jarayonda bola nafaqat asar mazmunini chuqur o'zlashtiradi, balki o'zining ijodiy qobiliyatlarini ham namoyon etadi. Bola obraz orqali o'z hissiyotlarini ifodalashni va boshqalarning kechinmalarini tushunishni o'rganadi.",
    "Sahnalashtirish faoliyati ikki muhim tomonni o'zida birlashtiradi: o'yin va san'at. O'yin tomoni shundaki, bola rolga kirib, xayoliy vaziyatda harakat qiladi, bu unga zavq bag'ishlaydi. San'at tomoni esa bolaning badiiy obraz yaratishi, uni ifodali va ta'sirchan tarzda namoyish etishidir. Bu ikki tomonning uyg'unligi sahnalashtirish faoliyatining o'ziga xosligini belgilaydi.",
    "Sahnalashtirish faoliyati badiiy adabiyot bilan uzviy bog'liqdir. Bola sahnalashtirish uchun ertak, hikoya yoki she'rni avval tinglaydi, uning mazmunini tushunadi va qahramonlar bilan tanishadi. Keyin u bu asarni sahna ko'rinishida ifodalaydi. Shu tariqa sahnalashtirish bolaning badiiy adabiyotga qiziqishini oshiradi va uni chuqur idrok etishga yordam beradi.",
    "Sahnalashtirish faoliyati bolaning yoshiga qarab turli darajada murakkablashib boradi. Kichik yoshda bola oddiy harakatlarni takrorlaydi, katta yoshda esa to'liq sahna ko'rinishlarida ishtirok etadi, rollarni mustaqil ijro etadi va hatto o'z syujetlarini o'ylab topadi. Bu faoliyat bolaning ijodiy rivojlanishi bilan birga takomillashib boradi.",
])


# 2. Asosiy maqsadi
SECTIONS.append([
    "Maktabgacha ta'lim tashkilotida sahnalashtirish faoliyatining asosiy maqsadi - bolaning ijodiy qobiliyatlarini rivojlantirish, uning badiiy-estetik didini shakllantirish, nutqi va hissiy olamini boyitish hamda ijtimoiy ko'nikmalarini takomillashtirishdir. Bu maqsad bolaning har tomonlama va uyg'un rivojlanishiga xizmat qiladi.",
    "Maqsadning birinchi jihati - bolaning ijodiy salohiyatini ro'yobga chiqarishdir. Sahnalashtirish faoliyatida bola o'z fantaziyasini ishga soladi, obraz yaratadi, harakatlar va dialoglar o'ylab topadi. Bu uning ijodiy fikrlashini va tashabbuskorligini rivojlantiradi. Bola o'zini erkin ifoda etish imkoniyatiga ega bo'ladi.",
    "Maqsadning ikkinchi jihati - bolada badiiy-estetik did va go'zallikni his qilish tuyg'usini shakllantirishdir. Sahnalashtirish jarayonida bola badiiy asarning go'zalligini, qahramonlar obrazlarining nafisligini va san'atning ta'sirchanligini his qiladi. Bu uning estetik tarbiyasiga hissa qo'shadi.",
    "Maqsadning uchinchi jihati - bolaning nutqini va muloqot ko'nikmalarini rivojlantirishdir. Rollarni ijro etish jarayonida bola o'z nutqini ifodali, ravon va to'g'ri qilishni o'rganadi. U dialoglar tuzadi, intonatsiyani his qiladi va o'z fikrini erkin ifodalashni o'rganadi.",
    "Maqsadning to'rtinchi jihati - bolada ijtimoiy ko'nikmalar va hissiy intellektni rivojlantirishdir. Sahnalashtirish jamoaviy faoliyat bo'lib, bola boshqalar bilan hamkorlik qilishni, o'z rolini jamoaning umumiy maqsadiga bo'ysundirishni o'rganadi. Shuningdek, bola qahramonlar hissiyotlarini ifodalash orqali o'z hissiy olamini boyitadi va empatiyani rivojlantiradi. Shunday qilib, sahnalashtirish faoliyatining maqsadi keng qamrovli bo'lib, u bolaning ijodiy, estetik, nutqiy va ijtimoiy rivojlanishini ta'minlaydi.",
])

# 3. Vazifalari
SECTIONS.append([
    "Maktabgacha ta'lim tashkilotida sahnalashtirish faoliyatining vazifalari bosh maqsaddan kelib chiqqan holda aniq belgilangan. Birinchi vazifa - bolada badiiy asarlarga va teatr san'atiga qiziqish uyg'otish. Bola ertaklar, hikoyalar va she'rlarni sevib tinglashi, ularni sahnalashtirishda ishtirok etishni xohlashi kerak. Bu qiziqish barcha sahnalashtirish faoliyatining asosi hisoblanadi.",
    "Ikkinchi vazifa - bolaning ijodiy qobiliyatlarini rivojlantirish. Bu vazifa bolada fantaziya, ijodiy tasavvur, obraz yaratish va improvizatsiya qilish qobiliyatlarini shakllantirishni o'z ichiga oladi. Bola qahramon obrazini o'ziga xos tarzda talqin etishni va ifodalashni o'rganadi.",
    "Uchinchi vazifa - bolaning nutqini rivojlantirish. Sahnalashtirish jarayonida bolaning lug'ati boyiydi, dialogik va monologik nutqi rivojlanadi, talaffuzi yaxshilanadi va nutqning intonatsion ifodaliligi shakllanadi. Bola matnni ifodali aytishni va o'z nutqini hissiyot bilan boyitishni o'rganadi.",
    "To'rtinchi vazifa - bolada hissiy-emotsional sohani rivojlantirish. Bola turli qahramonlar hissiyotlarini - quvonch, qayg'u, qo'rquv, hayrat - ifodalash orqali o'z hissiy olamini boyitadi. U o'z his-tuyg'ularini boshqarishni va boshqalarning hissiyotlarini tushunishni o'rganadi.",
    "Beshinchi vazifa - bolada ijtimoiy ko'nikmalar va jamoaviylikni shakllantirish. Sahnalashtirish jamoaviy faoliyat bo'lib, bola hamkorlik qilishni, o'z navbatini kutishni va jamoa bilan birga ishlashni o'rganadi. Oltinchi vazifa - bolada harakat madaniyati va plastikani rivojlantirish. Bola harakatlar orqali obraz yaratishni, mimika va imo-ishoralardan foydalanishni o'rganadi. Yettinchi vazifa - bolada o'ziga ishonch va omma oldida o'zini erkin tutish ko'nikmasini shakllantirish.",
])


# 4. Turlari
SECTIONS.append([
    "Maktabgacha ta'lim tashkilotlarida sahnalashtirish faoliyatining bir nechta turlari mavjud. Bu turlar bolaning yoshi, imkoniyatlari va faoliyatning maqsadiga qarab tanlanadi. Birinchi tur - dramatizatsiya o'yinlari. Bunda bolalarning o'zlari qahramon rolini bajaradi, badiiy asar mazmunini harakat, dialog va mimika orqali ifodalaydi. Bola bevosita aktyor sifatida ishtirok etadi.",
    "Ikkinchi tur - qo'g'irchoq teatri. Bunda bola qo'g'irchoqlar yordamida sahna ko'rinishini namoyish etadi. Qo'g'irchoq teatrining turli ko'rinishlari mavjud: barmoq teatri, qo'lqop teatri, soyali teatr, stol usti teatri. Qo'g'irchoq teatri ayniqsa uyatchang bolalar uchun qulay, chunki bola qo'g'irchoq ortida o'zini erkinroq his qiladi.",
    "Uchinchi tur - stol usti teatri. Bunda kichik o'yinchoqlar, figuralar yoki rasmlar yordamida stol ustida sahna ko'rinishi namoyish etiladi. Bu tur kichik yoshdagi bolalar uchun mos bo'lib, ularning nutqi va tasavvurini rivojlantiradi.",
    "To'rtinchi tur - soyali teatr. Bunda yorug'lik va ekran yordamida figuralarning soyasi orqali sahna ko'rinishi namoyish etiladi. Bu tur bolaning tasavvurini rivojlantiradi va unga sehrli muhit yaratadi. Beshinchi tur - flanelegraf teatri, bunda figuralar maxsus matoli taxtaga yopishtiriladi.",
    "Oltinchi tur - bibabo teatri (qo'lqop qo'g'irchoqlari) va marionetkalar. Bu turlarda maxsus qo'g'irchoqlardan foydalaniladi. Yettinchi tur - musiqali sahna ko'rinishlari va ertaklar, bunda sahnalashtirish musiqa, qo'shiq va raqs bilan boyitiladi. Har bir tur o'ziga xos imkoniyatlarga ega bo'lib, ularning barchasi birgalikda bolaning sahnalashtirish faoliyatini boyitadi va uni har tomonlama rivojlantiradi.",
])

# 5. Bola rivojlanishidagi ahamiyati
SECTIONS.append([
    "Sahnalashtirish faoliyati bolaning rivojlanishida ko'p qirrali ahamiyatga ega. Avvalo, bu faoliyat bolaning nutqiy rivojlanishiga kuchli ta'sir ko'rsatadi. Rollarni ijro etish, dialoglar tuzish va matnni ifodali aytish jarayonida bolaning lug'ati boyiydi, nutqi ravon va ifodali bo'ladi. Bola to'g'ri talaffuz qilishni va nutq intonatsiyasidan foydalanishni o'rganadi.",
    "Sahnalashtirish faoliyati bolaning hissiy-emotsional rivojlanishiga ijobiy ta'sir ko'rsatadi. Bola turli qahramonlar qiyofasiga kirib, ularning hissiyotlarini his qiladi va ifodalaydi. Bu uning hissiy olamini boyitadi, o'z his-tuyg'ularini tushunish va ifodalash qobiliyatini rivojlantiradi. Shuningdek, bola boshqalarning kechinmalarini tushunishni - empatiyani o'rganadi.",
    "Sahnalashtirish faoliyati bolaning ijodiy qobiliyatlarini rivojlantiradi. Bola obraz yaratish, harakatlar va dialoglar o'ylab topish, improvizatsiya qilish jarayonida o'z fantaziyasini va ijodiy tafakkurini ishga soladi. Bu uning ijodiy salohiyatini ro'yobga chiqaradi va nostandart fikrlashga o'rgatadi.",
    "Sahnalashtirish faoliyati bolaning ijtimoiy rivojlanishiga hissa qo'shadi. Jamoaviy sahna ko'rinishlarida bola hamkorlik qilishni, o'z rolini jamoaning umumiy maqsadiga bo'ysundirishni, o'rtoqlarini qo'llab-quvvatlashni o'rganadi. Bu uning ijtimoiy ko'nikmalarini va jamoaviylik tuyg'usini shakllantiradi.",
    "Bundan tashqari, sahnalashtirish faoliyati bolada o'ziga ishonchni mustahkamlaydi va omma oldida o'zini erkin tutishni o'rgatadi. Bola sahnada chiqish qilish orqali uyatchanligini yengadi, o'z imkoniyatlariga ishonadi. Faoliyat shuningdek bolaning xotirasini, diqqatini va harakat koordinatsiyasini rivojlantiradi. Shunday qilib, sahnalashtirish faoliyati bolaning barcha rivojlanish sohalariga ijobiy ta'sir ko'rsatadigan kompleks pedagogik vositadir.",
])


# 6. Tashkil etish shakllari va bosqichlari
SECTIONS.append([
    "Maktabgacha ta'lim tashkilotida sahnalashtirish faoliyati turli shakllar orqali tashkil etiladi. Birinchi shakl - maxsus mashg'ulotlar. Bu mashg'ulotlarda tarbiyachi bolalarni teatr san'ati bilan tanishtiradi, ularga obraz yaratish, harakat va nutq ustida ishlashni o'rgatadi. Mashg'ulotlar bolaning yoshiga mos tarzda tashkil etiladi.",
    "Ikkinchi shakl - mustaqil teatrlashtirilgan o'yinlar. Bunda bolalar erkin faoliyat vaqtida o'z xohishlariga ko'ra sahna ko'rinishlarini o'ynaydi. Tarbiyachi bunda bolalarga zarur jihozlar va sharoit yaratadi, lekin ularning mustaqilligini cheklamaydi. Uchinchi shakl - bayramlar va o'yin-kulgilar, bunda bolalar tayyorlangan sahna ko'rinishlarini namoyish etadi.",
    "Sahnalashtirish faoliyatini tashkil etish bir necha bosqichda amalga oshiriladi. Birinchi bosqich - badiiy asar bilan tanishtirish. Tarbiyachi bolalarga ertak yoki hikoyani ifodali o'qib beradi, uning mazmunini tushuntiradi va qahramonlar bilan tanishtiradi. Bola asarni chuqur idrok etishi kerak.",
    "Ikkinchi bosqich - asar mazmuni ustida ishlash. Tarbiyachi bolalar bilan asar mazmunini muhokama qiladi, qahramonlarning xarakteri va xatti-harakatlarini tahlil qiladi. Uchinchi bosqich - rollarni taqsimlash va ular ustida ishlash. Bolalar rollarni tanlaydi, o'z qahramonining nutqi, harakati va hissiyotlarini mashq qiladi. Tarbiyachi bunda har bir bolaga yordam beradi.",
    "To'rtinchi bosqich - sahna ko'rinishini tayyorlash. Bolalar dekoratsiya, kostyum va atributlarni tayyorlashda ishtirok etadi, sahna ko'rinishini birgalikda mashq qiladi. Beshinchi bosqich - sahna ko'rinishini namoyish etish. Bolalar tayyorlangan ko'rinishni tomoshabinlar - boshqa bolalar yoki ota-onalar - oldida namoyish etadi. Oltinchi bosqich - tahlil va muhokama, bunda bolalar o'z chiqishlarini muhokama qiladi. Bu bosqichlar izchil amalga oshirilib, sahnalashtirish faoliyatining samaradorligini ta'minlaydi.",
])

# 7. Tarbiyachining roli
SECTIONS.append([
    "Maktabgacha ta'lim tashkilotida sahnalashtirish faoliyatini amalga oshirishda tarbiyachining roli hal qiluvchi ahamiyatga ega. Tarbiyachi bu faoliyatning tashkilotchisi, yo'naltiruvchisi va ilhomlantiruvchisi sifatida ishtirok etadi. Uning mahorati, ijodiy yondashuvi va teatr san'atiga bo'lgan munosabati bolalarning sahnalashtirish faoliyatiga qiziqishini belgilaydi.",
    "Tarbiyachining birinchi vazifasi - sahnalashtirish faoliyatini rejalashtirish va tashkil etish. U bolalarning yoshiga mos badiiy asarlarni tanlaydi, mashg'ulotlarni rejalashtiradi, zarur jihoz va materiallarni tayyorlaydi. Tarbiyachi sahnalashtirish uchun teatr burchagini tashkil etadi va uni turli jihozlar bilan boyitadi.",
    "Tarbiyachining ikkinchi vazifasi - bolalarga namuna ko'rsatish. Tarbiyachi o'zi ifodali o'qiydi, qahramonlar obrazlarini namoyish etadi va bolalarga obraz yaratishni o'rgatadi. Tarbiyachining ifodali nutqi va hissiy ijrosi bolalar uchun asosiy namuna bo'lib xizmat qiladi.",
    "Tarbiyachining uchinchi vazifasi - har bir bolaning ishtirokini ta'minlash va uni qo'llab-quvvatlash. Tarbiyachi har bir bolaga uning imkoniyatlariga mos rol beradi, uyatchang bolalarni rag'batlantiradi va ularning o'ziga ishonchini mustahkamlaydi. U bolaning har bir urinishini qadrlaydi va ijobiy muhit yaratadi.",
    "Tarbiyachining to'rtinchi vazifasi - bolalarning ijodiy tashabbusini rag'batlantirish. Tarbiyachi bolalarga tayyor andoza bermaydi, balki ularning o'z obrazlarini yaratishiga, improvizatsiya qilishiga imkon beradi. Beshinchi vazifasi - ota-onalar bilan hamkorlik qilish va o'z kasbiy mahoratini doimiy oshirib borish. Tarbiyachining mahorati va ijodiy yondashuvi sahnalashtirish faoliyatining samaradorligini va bolalarning rivojlanishini ta'minlaydi.",
])


# 8. Xulosa
SECTIONS.append([
    "Mazkur mustaqil ishda maktabgacha ta'lim tashkilotida sahnalashtirish faoliyatining asosiy maqsadi va vazifalari har tomonlama tahlil qilindi. Tahlillar shuni ko'rsatdiki, sahnalashtirish faoliyati maktabgacha ta'limning muhim tarkibiy qismi bo'lib, u bolaning har tomonlama va uyg'un rivojlanishida katta o'rin tutadi.",
    "Sahnalashtirish faoliyatining asosiy maqsadi - bolaning ijodiy qobiliyatlarini rivojlantirish, badiiy-estetik didini shakllantirish, nutqi va hissiy olamini boyitish hamda ijtimoiy ko'nikmalarini takomillashtirishdir. Bu maqsad aniq belgilangan vazifalar - qiziqish uyg'otish, ijodkorlikni rivojlantirish, nutqni boyitish, hissiy va ijtimoiy sohalarni shakllantirish - orqali amalga oshiriladi.",
    "Sahnalashtirish faoliyati turli shakllarda - dramatizatsiya o'yinlari, qo'g'irchoq teatri, stol usti teatri, soyali teatr - amalga oshiriladi. Bu faoliyat bolaning nutqiy, hissiy, ijodiy va ijtimoiy rivojlanishiga ijobiy ta'sir ko'rsatadi. Tarbiyachining mahorati va ijodiy yondashuvi bu faoliyatning samaradorligini ta'minlaydi.",
    "Xulosa qilib aytganda, sahnalashtirish faoliyati - bu o'yin va san'atni o'zida birlashtirgan, bolaning ijodiy salohiyatini ro'yobga chiqaradigan va uning shaxsini har tomonlama rivojlantiradigan muhim pedagogik vositadir. To'g'ri tashkil etilgan sahnalashtirish faoliyati bolaga zavq bag'ishlaydi, uni tarbiyalaydi va kelajakda ijodkor, o'ziga ishongan va har tomonlama rivojlangan shaxs sifatida shakllanishiga zamin yaratadi.",
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
    SECTIONS[7],  # Tushunchasi va mohiyati
    SECTIONS[2],  # Asosiy maqsadi
    SECTIONS[3],  # Vazifalari
    SECTIONS[4],  # Turlari
    SECTIONS[5],  # Bola rivojlanishidagi ahamiyati
    SECTIONS[0],  # Tashkil etish shakllari va bosqichlari
    SECTIONS[1],  # Tarbiyachining roli
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
body.append(make_para("Maktabgacha ta'lim tashkilotida sahnalashtirish faoliyatining asosiy maqsadi va vazifalari", bold=True, size=28, align="center"))
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
core_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Mustaqil ish - Sahnalashtirish faoliyati</dc:title><dc:creator>Talaba</dc:creator></cp:coreProperties>'
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
