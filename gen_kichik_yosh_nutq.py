#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mustaqil ish: Maktabgacha ta'lim tashkilotlarida kichik yoshdagi bolalarning
nutqini o'stirish metodlari va vositalari
"""
import os, zipfile
from xml.sax.saxutils import escape

OUT = "/projects/sandbox/mustaqil-ishlar/Kichik_yosh_nutq_metodlari.docx"

PLAN = [
    "Kirish",
    "Kichik yoshdagi bolalarning nutqiy rivojlanish xususiyatlari",
    "Nutqini o'stirish metodlari tushunchasi va tasnifi",
    "Ko'rgazmali metodlar va ularning qo'llanilishi",
    "Og'zaki (verbal) metodlar va ularning qo'llanilishi",
    "Amaliy metodlar va ularning qo'llanilishi",
    "Nutqini o'stirish vositalari va ularning turlari",
    "Tarbiyachining kichik yosh bolalari nutqini o'stirishdagi roli",
    "Xulosa va foydalanilgan adabiyotlar",
]

SECTIONS = [
    [
        "Nutq — insonning eng muhim muloqot vositasi bo'lib, u tafakkur, bilim olish va ijtimoiy hayotda faoliyat ko'rsatishning asosiy qurollaridan biridir. Maktabgacha yoshdagi bolalarning nutqini o'stirish pedagogik jarayonning eng muhim yo'nalishlaridan biri hisoblanadi. Xususan, kichik yosh davri (2-4 yosh) bolaning nutqiy rivojlanishi uchun eng senzitiv, ya'ni eng qulay davr bo'lib, aynan shu davrda nutqning asosiy ko'nikmalari intensiv tarzda shakllanadi.",
        "Kichik yoshdagi bolalarning nutqiy rivojlanishi o'ziga xos xususiyatlarga ega. Bu yoshda bola atrofdagi dunyoni faol o'rganayotgan bo'lib, uning lug'ati tez sur'atda o'sadi, birinchi gaplar paydo bo'ladi va muloqotga bo'lgan ehtiyoj kuchayadi. Shu sababli maktabgacha ta'lim tashkilotlarida kichik yosh guruhlarida nutqni o'stirish ishining to'g'ri tashkil etilishi katta ahamiyatga ega.",
        "Mazkur mustaqil ishda maktabgacha ta'lim tashkilotlarida kichik yoshdagi bolalarning nutqini o'stirish metodlari va vositalari batafsil yoritiladi. Ishda ko'rgazmali, og'zaki va amaliy metodlar, nutqni rivojlantirish vositalari hamda tarbiyachining roli tahlil qilinadi. Mavzuning dolzarbligi shundaki, kichik yoshda nutqni to'g'ri va samarali rivojlantirish bolaning keyingi ta'lim muvaffaqiyatlari uchun hal qiluvchi ahamiyatga ega.",
    ],
    [
        "Kichik yoshdagi bolalarning nutqiy rivojlanishi bir qator o'ziga xos xususiyatlarga ega. 2 yoshda bolaning faol lug'ati taxminan 200-300 so'zni tashkil etadi. 3 yoshga kelib u 1000-1500 so'zga yetadi. Bu davr nutq rivojlanishining eng intensiv bosqichi hisoblanadi. Bola har kuni bir nechta yangi so'zlarni o'zlashtiradi va ularni nutqida faol qo'llay boshlaydi.",
        "Bu yoshda bolaning nutqi hali grammatik jihatdan to'liq shakllanmagan bo'ladi. Bola avval bir so'zli gaplar, keyin ikki so'zli gaplar, so'ng 3-4 so'zli oddiy gaplar tuzishni o'rganadi. Grammatik xatolar — so'z qo'shimchalarini noto'g'ri qo'llash, fe'l shakllarini aralashtirish — bu yosh uchun tabiiy holat hisoblanadi.",
        "Tovush talaffuzi jihatidan kichik yoshdagi bolalar ko'p tovushlarni hali to'g'ri talaffuz qila olmaydi. R, L, Sh, S kabi murakkab tovushlar odatda 4-5 yoshgacha to'liq shakllanmaydi. Bolalar ko'pincha murakkab tovushlarni soddalari bilan almashtiradi. Bu fiziologik jihatdan normal holat bo'lib, artikulyatsion apparatning hali to'liq yetilmaganligi bilan izohlanadi.",
        "Kichik yoshda bolaning nutqi asosan vaziyatga bog'liq (situativ) bo'ladi. Bola o'z atrofidagi narsalar, hodisalar va harakatlar haqida gapiradi. U hali mavhum tushunchalarni ifodalay olmaydi. Shuningdek, bu yoshda bola kattalar nutqiga taqlid qilish orqali ko'p narsalarni o'rganadi. Tarbiyachining va ota-onalarning nutqi bola uchun asosiy namuna bo'lib xizmat qiladi.",
        "Kichik yoshdagi bolaning nutqiy rivojlanishida hissiy komponent katta rol o'ynaydi. Bola quvonchli, qiziqarli va hissiy boy muhitda tezroq gapirishni o'rganadi. Aksincha, stress, qo'rquv yoki e'tiborsizlik nutq rivojlanishini sekinlashtirishi mumkin. Shu sababli tarbiyachi bolaga issiq, do'stona va qo'llab-quvvatlovchi muhit yaratishi zarur.",
    ],
    [
        "Nutqini o'stirish metodlari — bu bolaning nutqiy ko'nikmalarini maqsadli ravishda shakllantirish va rivojlantirish uchun qo'llaniladigan pedagogik ta'sir usullaridir. Metod — tarbiyachi va bolaning ta'limiy maqsadga erishish uchun birgalikdagi faoliyat usuli. Kichik yoshdagi bolalar bilan ishlashda to'g'ri metodlarni tanlash nutqiy rivojlanish samaradorligining asosiy sharti hisoblanadi.",
        "Maktabgacha ta'lim pedagogikasida nutqini o'stirish metodlari an'anaviy ravishda uch asosiy guruhga bo'linadi. Birinchi guruh — ko'rgazmali metodlar. Bu metodlarda bola ko'rish, eshitish va sezish orqali yangi so'zlar va tushunchalarni o'zlashtiradi. Ikkinchi guruh — og'zaki (verbal) metodlar. Bu metodlarda tarbiyachining nutqi orqali bolaning nutqiy ko'nikmalari shakllantiriladi.",
        "Uchinchi guruh — amaliy metodlar. Bu metodlarda bola bevosita harakat va faoliyat orqali nutqiy tajriba to'playdi. Har bir guruh o'ziga xos usullarni o'z ichiga oladi va kichik yoshdagi bolalar bilan ishlashda ularning barchasi birgalikda qo'llaniladi. Metodlarning to'g'ri tanlanishi va uyg'unlashtirilishi nutqiy rivojlanishning samaradorligini belgilaydi.",
        "Kichik yosh guruhlarida metodlarni tanlashda quyidagi tamoyillarga rioya qilinadi: ko'rgazmalilik tamoyili — bola eshitgan narsani ko'rishi ham kerak; hissiyotlilik — mashg'ulot bolaga qiziqarli bo'lishi shart; qisqa muddatlilik — kichik yoshdagi bola 8-10 daqiqadan ortiq e'tiborini jamlay olmaydi; takroriylik — bir xil material turli shaklda bir necha bor takrorlanishi kerak; individual yondashuv — har bir bolaning rivojlanish tezligi hisobga olinishi zarur.",
    ],
    [
        "Ko'rgazmali metodlar kichik yoshdagi bolalarning nutqini o'stirishda eng samarali va keng qo'llaniladigan metodlar hisoblanadi. Bu yoshda bola dunyoni ko'rish, ushlab ko'rish va sezish orqali o'rganadi. Ko'rgazmali metod bola uchun yangi so'zlarni real predmetlar va ularning tasvirlari bilan bog'lash imkonini beradi. Bola ko'rgan narsasining nomini tezroq eslab qoladi va nutqida qo'llaydi.",
        "Ko'rgazmali metodlarning birinchi turi — bevosita kuzatish. Tarbiyachi bolalarga real predmetlarni, hayvonlarni, o'simliklarni va hodisalarni ko'rsatib, ularning nomlarini aytadi. Masalan, sayr vaqtida daraxtlarni, qushlarni, mashinalarni ko'rsatib, ularning nomlarini bir necha bor takrorlaydi. Bola real predmetni ko'rib, uning nomini eshitib, tezroq eslab qoladi.",
        "Ikkinchi turi — rasmlar va suratlar bilan ishlash. Tarbiyachi bolalarga yorqin, yirik va tushunarli rasmlarni ko'rsatib, undagi narsalarni nomlaydi. Bu nima? Bu mushuk. Mushuk qanday qiladi? Miyov-miyov — kabi oddiy savollar orqali bolaning nutqiy faolligini oshiradi. Syujetli rasmlar bilan ishlashda oddiy voqealar tasviri ko'rsatiladi.",
        "Uchinchi turi — o'yinchoqlarni ko'rsatish va nomlash. Tarbiyachi turli o'yinchoqlarni bolalarga ko'rsatib, ularning nomlarini, ranglarini, shakllarini va harakatlarini aytadi. Bu ayiq. Ayiq katta. Ayiq jigarrang — kabi oddiy gaplar orqali bolaning lug'atini boyitadi. Shuningdek, o'yinchoqlar bilan kichik sahnalar o'ynab, bolaning bog'lanishli nutqini rivojlantiradi.",
        "To'rtinchi turi — videolar va animatsiyalar. Zamonaviy maktabgacha ta'limda qisqa bolalar multfilmlari va ta'limiy videolardan ham foydalaniladi. Biroq kichik yoshdagi bolalar uchun ekran vaqti cheklangan bo'lishi kerak va video real muloqotni almashtira olmaydi. Video qisqa, sodda va tarbiyachi izohi bilan birga ko'rsatilishi kerak. Ko'rgazmali metodlarning eng muhim sharti — har bir ko'rsatilgan narsa tarbiyachining aniq, to'g'ri va ifodali nutqi bilan birga bo'lishidir.",
    ],
    [
        "Og'zaki (verbal) metodlar — tarbiyachining nutqi orqali bolaning nutqiy ko'nikmalarini shakllantirish usullaridir. Kichik yoshdagi bolalar uchun tarbiyachining nutqi eng muhim ta'lim vositasi hisoblanadi, chunki bola nutqni atrofidagilarning gapirishini eshitish va ularga taqlid qilish orqali o'rganadi. Tarbiyachining nutqi aniq, sodda, ifodali va grammatik jihatdan to'g'ri bo'lishi shart.",
        "Og'zaki metodlarning birinchi turi — suhbat. Tarbiyachi bolalar bilan individual yoki kichik guruhda suhbat o'tkazadi. Suhbat oddiy va bolaga tanish mavzularda bo'ladi: Bugun nima kiyding? Ovqat yoqdimi? Sayrda nimalarni ko'rding? Savollar qisqa va tushunarli bo'lishi, bolaga javob berish uchun vaqt berilishi kerak.",
        "Ikkinchi turi — badiiy so'z (she'r, ertak, qo'shiq). Tarbiyachi bolalarga qisqa she'rlar, sanash o'yinlari (poteshkalar), bolalar qo'shiqlari va kichik ertaklar aytib beradi. Bu usul bolaning nutqiy eshitishini, intonatsiyani his qilishini va lug'atini rivojlantiradi. Kichik yoshdagi bolalar uchun she'rlar ritmik, qisqa va takroriy bo'lishi kerak.",
        "Uchinchi turi — so'z o'yinlari. Bu oddiy nutqiy o'yinlar bo'lib, ularda bola hayvon ovozlarini takrorlaydi, predmetlarni nomlaydi, oddiy topishmoqlar yechadi va do'stona muloqotda qatnashadi. Zanjirli savollar bolaning nutqiy faolligini oshiradi.",
        "To'rtinchi turi — hikoya qilib berish va qayta aytish. Tarbiyachi qisqa, sodda hikoyalarni aytib beradi va bolalardan oddiy savollar orqali qayta aytishni so'raydi. Kichik guruhda bola hali to'liq qayta hikoya qila olmaydi, lekin tarbiyachi boshlab bersa, bola yakuni aytishi mumkin. Bu usul bolaning bog'lanishli nutqini rivojlantirishning dastlabki bosqichidir.",
    ],
    [
        "Amaliy metodlar — bolaning bevosita faoliyati, harakati va amaliy tajribasi orqali nutqini rivojlantirish usullaridir. Kichik yoshdagi bolalar dunyoni faol harakat orqali o'rganadi, shu sababli amaliy metodlar bu yosh uchun juda samarali hisoblanadi. Bola biror narsani qilish jarayonida yangi so'zlar o'rganadi va ularni tabiiy tarzda nutqida qo'llaydi.",
        "Amaliy metodlarning birinchi turi — didaktik o'yinlar. Bu maxsus ta'limiy maqsadda tashkil etiladigan o'yinlar bo'lib, ularda bola o'yin jarayonida nutqiy ko'nikmalarni o'zlashtiradi. Masalan, Sumkada nima bor o'yinida bola qo'lini sumkaga tiqib, narsani ushlab ko'rib nomini aytadi. Kim qanday qiladi o'yinida hayvon ovozlarini takrorlaydi.",
        "Ikkinchi turi — rolli o'yinlar. Kichik yoshdagi bolalar oddiy syujetli o'yinlarga qiziqa boshlaydi. Ona va bola, Shifokor, Do'kon kabi o'yinlarda bola kattalar nutqiga taqlid qiladi, yangi so'zlarni nutqida qo'llaydi va muloqot qilishni o'rganadi. Tarbiyachi bu o'yinlarga qatnashib, bolaning nutqiy faolligini oshiradi.",
        "Uchinchi turi — barmoq o'yinlari va artikulyatsion gimnastika. Barmoq o'yinlari — bu qo'l barmoqlarining harakatlari bilan birga she'r aytilishi. Besh barmoq, Barmoqlar oilasi kabi o'yinlar bolaning mayda motorikasini va nutqini bir vaqtda rivojlantiradi. Ilmiy tadqiqotlar qo'l harakatlari va nutq markazlari orasidagi mustahkam aloqani isbotlagan.",
        "To'rtinchi turi — badiiy ijod faoliyati. Rasm chizish, plastilindan shakl yasash, applikatsiya qilish jarayonida tarbiyachi bola bilan muloqot olib boradi. Bola ijodiy faoliyat jarayonida so'zlar ishlatishni, savolga javob berishni va o'z ishini tasvirlashni o'rganadi. Beshinchi turi — harakatli o'yinlar. Yugurish, sakrash, to'p o'ynash jarayonida tarbiyachi harakatlarni nomlaydi va bola bilan muloqot qiladi.",
    ],
    [
        "Nutqini o'stirish vositalari — bolaning nutqiy rivojlanishini ta'minlovchi barcha material va nomoddiy resurslarning majmuidir. Vositalar to'g'ri tanlanganda va qo'llanganda, nutqiy rivojlanish jarayonini sezilarli darajada tezlashtiradi va samarali qiladi. Kichik yoshdagi bolalar uchun vositalar maxsus talablar asosida tanlanadi: xavfsiz, yorqin, yirik va bolaning yoshiga mos.",
        "Birinchi va eng muhim vosita — tarbiyachining nutqi. Tarbiyachining nutqi bola uchun asosiy nutqiy namuna hisoblanadi. U aniq, ravon, grammatik jihatdan to'g'ri, intonatsion boy va ifodali bo'lishi kerak. Tarbiyachi bolaga murojaat qilganda so'zlarni to'liq aytishi, shoshilmasdan gapirishi va bolaning javobini sabr bilan kutishi lozim.",
        "Ikkinchi vosita — badiiy adabiyot. Bolalar she'rlari, qisqa ertaklar, poteshkalar, qo'shiqlar va topishmoqlar bolaning lug'atini boyitadi, nutqiy eshitishini rivojlantiradi va badiiy so'zga qiziqishini uyg'otadi. Kichik yoshdagi bolalar uchun kitoblar yorqin rasmli, qisqa matnli va oddiy syujetli bo'lishi kerak.",
        "Uchinchi vosita — ko'rgazmali materiallar. Rasmlar, kartochkalar, plakatlar, o'yinchoqlar, maketlar va real predmetlar bolaning yangi so'zlarni ko'rish orqali o'zlashtirishiga yordam beradi. Syujetli rasmlar hikoya tuzishga, predmetli rasmlar esa lug'at boyitishga xizmat qiladi.",
        "To'rtinchi vosita — didaktik o'yinlar va o'yinchoqlar. Maxsus nutqiy rivojlanishga mo'ljallangan o'yinchoqlar: mushuk-sichqon o'yini, telefon, qo'g'irchoq teatri, loto, domino va boshqalar bolaning nutqiy faolligini oshiradi. Beshinchi vosita — rivojlantiruvchi muhit. Guruh xonasidagi kitob burchagi, didaktik o'yinlar javoni, teatr burchagi, tabiat burchagi va sensor burchak hammasi bola nutqini rivojlantirishga xizmat qiladi. Oltinchi vosita — texnik vositalar: audio-yozuvlar, musiqa asboblari, interaktiv o'yinchoqlar.",
    ],
    [
        "Maktabgacha ta'lim tashkilotlarida kichik yoshdagi bolalarning nutqini o'stirishda tarbiyachining roli hal qiluvchi ahamiyatga ega. Tarbiyachi — bu bola uchun eng yaqin katta inson sifatida asosiy nutqiy namuna va muloqot hamkori hisoblanadi. Uning har bir so'zi, intonatsiyasi va muomala uslubi bola nutqiga bevosita ta'sir ko'rsatadi.",
        "Tarbiyachining birinchi vazifasi — boy nutqiy muhit yaratish. U kun davomida bola bilan doimiy muloqotda bo'lishi, har bir rejim jarayonini — kiyinish, ovqatlanish, sayr, o'yin — nutqiy faoliyat bilan boyitishi kerak. Oddiy gaplar orqali bola yangi so'zlarni tabiiy muhitda o'zlashtiradi.",
        "Ikkinchi vazifasi — bolaning nutqiy faolligini rag'batlantirish. Tarbiyachi bolani gapirishga undaydi, uning har qanday nutqiy urinishini qo'llab-quvvatlaydi va hech qachon bolaning nutqidagi xatolar uchun koyimaydi. Agar bola noto'g'ri gapirsai, tarbiyachi uni to'g'rilamaydi, balki to'g'ri shaklni o'z nutqida takrorlaydi.",
        "Uchinchi vazifasi — individual yondashuvni amalga oshirish. Har bir bolaning nutqiy rivojlanishi individual tezlikda kechadi. Tarbiyachi har bir bolaning darajasini bilib, unga mos topshiriqlar berishi va sabr bilan natijani kutishi kerak.",
        "To'rtinchi vazifasi — ota-onalar bilan hamkorlik qilish. Tarbiyachi ota-onalarga bolaning nutqiy rivojlanishi haqida muntazam ma'lumot beradi, uyda qanday mashqlar bajarish mumkinligini tushuntiradi va zarurat bo'lganda mutaxassisga murojaat qilishni maslahat beradi. Beshinchi vazifasi — o'z kasbiy mahoratini doimiy oshirish.",
    ],
    [
        "Mazkur mustaqil ishda maktabgacha ta'lim tashkilotlarida kichik yoshdagi bolalarning nutqini o'stirish metodlari va vositalari har tomonlama tahlil qilindi. Tahlillar shuni ko'rsatdiki, kichik yosh davri bolaning nutqiy rivojlanishi uchun eng muhim va senzitiv davr bo'lib, bu davrda to'g'ri pedagogik ta'sir ko'rsatish katta ahamiyatga ega.",
        "Nutqini o'stirish metodlari — ko'rgazmali, og'zaki va amaliy — birgalikda qo'llanganda eng yuqori samara beradi. Kichik yoshdagi bolalar bilan ishlashda ko'rgazmalilik, hissiyotlilik, o'yin elementi va takroriylik eng muhim tamoyillar hisoblanadi. Har bir mashg'ulot bolaga qiziqarli bo'lishi va uning faol ishtirokini ta'minlashi kerak.",
        "Nutqini o'stirish vositalari — tarbiyachi nutqi, badiiy adabiyot, ko'rgazmali materiallar, didaktik o'yinlar va rivojlantiruvchi muhit — bolaning nutqiy kamolotini har tomonlama ta'minlaydi. Bu vositalarning to'g'ri tanlanishi va qo'llanilishi nutqiy rivojlanish samaradorligining asosiy sharti hisoblanadi.",
        "Xulosa qilib aytganda, kichik yoshdagi bolalarning nutqini o'stirish — bu murakkab va mas'uliyatli pedagogik jarayon bo'lib, u tarbiyachidan chuqur bilim, sabr-toqat va ijodiy yondashuvni talab qiladi. Bu jarayonning muvaffaqiyati ko'p jihatdan tarbiyachining mahoratiga, to'g'ri metodlar tanlashiga va bolaga individual yondashuvni amalga oshirishiga bog'liq.",
        "Foydalanilgan adabiyotlar:",
        "1. O'zbekiston Respublikasining \"Maktabgacha ta'lim va tarbiya to'g'risida\"gi Qonuni. — Toshkent, 2020.",
        "2. \"Ilk qadam\" maktabgacha ta'lim muassasalarining Davlat o'quv dasturi. — Toshkent, 2018.",
        "3. Sodiqova M. \"Bolalar nutqini o'stirish metodikasi\". — Toshkent, 2019.",
        "4. Raximova D. \"Kichik yoshdagi bolalar nutqini rivojlantirish\". — Toshkent, 2021.",
        "5. Ushakova O.S. \"Razvitiye rechi detey rannego vozrasta\". — Moskva, 2018.",
        "6. Yanushko Ye.A. \"Razvitiye rechi u detey rannego vozrasta\". — Moskva, 2019.",
    ],
]

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

body = []
for _ in range(4):
    body.append(make_para("", size=28))
body.append(make_para("O'ZBEKISTON RESPUBLIKASI", bold=True, size=28, align="center"))
body.append(make_para("MAKTABGACHA VA MAKTAB TA'LIMI VAZIRLIGI", bold=True, size=28, align="center"))
body.append(make_para("", size=24))
body.append(make_para("MUSTAQIL ISH", bold=True, size=40, align="center"))
body.append(make_para("", size=24))
body.append(make_para("Mavzu:", bold=True, size=28, align="center"))
body.append(make_para("Maktabgacha ta'lim tashkilotlarida kichik yoshdagi bolalarning nutqini o'stirish metodlari va vositalari", bold=True, size=28, align="center"))
for _ in range(5):
    body.append(make_para("", size=24))
body.append(make_para("Bajardi: ______________________", size=28, align="right"))
body.append(make_para("Tekshirdi: ______________________", size=28, align="right"))
for _ in range(2):
    body.append(make_para("", size=24))
body.append(make_para("Toshkent — 2026", bold=True, size=28, align="center"))
body.append(page_break())

body.append(make_para("REJA", bold=True, size=32, align="center"))
body.append(make_para("", size=20))
for i, item in enumerate(PLAN, 1):
    body.append(make_para(f"{i}. {item}", size=28))
body.append(page_break())

for idx, (heading, paragraphs) in enumerate(zip(PLAN, SECTIONS)):
    body.append(make_para(f"{idx + 1}. {heading.upper()}", bold=True, size=30, align="center"))
    body.append(make_para("", size=18))
    for p in paragraphs:
        body.append(make_body_para(p))
    if idx < len(SECTIONS) - 1:
        body.append(page_break())

sectPr = '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1134" w:right="850" w:bottom="1134" w:left="1701" w:header="708" w:footer="708" w:gutter="0"/><w:cols w:space="708"/><w:docGrid w:linePitch="360"/></w:sectPr>'
document_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>' + ''.join(body) + sectPr + '</w:body></w:document>'

content_types_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/><Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/><Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/></Types>'
rels_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/></Relationships>'
document_rels_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>'
styles_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="28"/><w:szCs w:val="28"/><w:lang w:val="uz-UZ"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:line="360" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults><w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style></w:styles>'
core_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Mustaqil ish - Kichik yosh nutq metodlari</dc:title><dc:creator>Talaba</dc:creator></cp:coreProperties>'
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
