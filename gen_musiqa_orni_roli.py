#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mustaqil ish: Bolalar hayotida musiqaning o'rni va roli
"""
import os, zipfile
from xml.sax.saxutils import escape

OUT = "/projects/sandbox/mustaqil-ishlar/Bolalar_hayotida_musiqa.docx"

PLAN = [
    "Kirish",
    "Musiqaning inson va bola hayotidagi umumiy ahamiyati",
    "Musiqaning bola hissiy-emotsional rivojlanishidagi roli",
    "Musiqaning bola aqliy va nutqiy rivojlanishidagi o'rni",
    "Musiqaning bola axloqiy va estetik tarbiyasidagi roli",
    "Musiqaning bola jismoniy rivojlanishi va sog'lig'idagi o'rni",
    "Musiqaning bolaning kundalik hayotidagi o'rni",
    "Oilada va maktabgacha ta'limda musiqadan foydalanish",
    "Xulosa va foydalanilgan adabiyotlar",
]

SECTIONS = [
    [
        "Musiqa - insoniyat yaratgan eng go'zal va ta'sirchan san'at turlaridan biri bo'lib, u kishi hayotining barcha jabhalarini qamrab oladi. Inson tug'ilganidan boshlab musiqa bilan hamroh bo'ladi: onaning allasi, bolalik qo'shiqlari, bayram kuylari - bularning barchasi insonni musiqa olamiga olib kiradi. Ayniqsa, bolalik davrida musiqaning o'rni va roli beqiyosdir.",
        "Bola hayotida musiqa shunchaki ko'ngilochar vosita emas, balki uning shaxsiy kamoloti, hissiy boyligi va ma'naviy rivojlanishining muhim omilidir. Musiqa bolaning his-tuyg'ulariga ta'sir ko'rsatadi, uning ichki olamini boyitadi, atrofdagi go'zallikni his qilishga o'rgatadi va uni har tomonlama rivojlantiradi. Shu sababli bola hayotida musiqaning o'rnini to'g'ri tushunish katta ahamiyatga ega.",
        "Mazkur mustaqil ishda bolalar hayotida musiqaning o'rni va roli har tomonlama yoritiladi. Ishda musiqaning bola hayotidagi umumiy ahamiyati, uning hissiy, aqliy, nutqiy, axloqiy, estetik va jismoniy rivojlanishidagi roli, kundalik hayotdagi o'rni hamda oila va maktabgacha ta'limda musiqadan foydalanish masalalari tahlil qilinadi. Mavzuning dolzarbligi shundaki, musiqaning bola hayotidagi rolini anglash uni tarbiyaviy maqsadlarda samarali qo'llash imkonini beradi.",
    ],
    [
        "Musiqa insoniyat tarixining eng qadimgi san'at turlaridan biri bo'lib, u barcha xalqlar va madaniyatlarda mavjud. Musiqa insonning his-tuyg'ularini ifodalash, muloqot qilish va o'zini namoyon qilishning o'ziga xos tili hisoblanadi. U so'zsiz ham insonga ta'sir ko'rsatadi, uning kayfiyatini o'zgartiradi va ruhiy holatiga ta'sir qiladi.",
        "Bola hayotida musiqa juda erta paydo bo'ladi. Hatto ona qornidagi homila ham tovushlarni eshitadi va musiqaga munosabat bildiradi. Tug'ilgan chaqaloq onaning allasini eshitib tinchlanadi, uxlaydi. Bu musiqaning bola hayotidagi dastlabki va eng tabiiy ko'rinishidir. Alla - bu nafaqat bolani uxlatish vositasi, balki ona va bola o'rtasidagi ilk hissiy bog'lanish vositasidir.",
        "Bola o'sib borgan sari musiqaning uning hayotidagi o'rni kengayadi. Bola musiqaga jonli munosabat bildiradi: quvnoq musiqa eshitganda jilmayadi, harakatlanadi, sekin musiqa esa uni tinchlantiradi. Bu bolaning musiqani tabiiy ravishda his qilishidan dalolat beradi. Musiqaga bo'lgan bu tabiiy moyillik har bir bolada mavjud bo'lib, uni rivojlantirish kerak.",
        "Musiqa bolaning butun shaxsiga - uning hissiyotlari, tafakkuri, irodasi va xulq-atvoriga ta'sir ko'rsatadi. U bolaning ichki olamini boyitadi, unda nozik tuyg'ularni shakllantiradi va atrofdagi olamni go'zal idrok etishga o'rgatadi. Shu ma'noda musiqa bolaning har tomonlama rivojlanishining muhim omili hisoblanadi.",
        "Zamonaviy ilmiy tadqiqotlar musiqaning bola rivojlanishiga ko'p qirrali ijobiy ta'sirini isbotlagan. Musiqa nafaqat bolaning estetik tarbiyasiga, balki uning aqliy, nutqiy, jismoniy va ijtimoiy rivojlanishiga ham hissa qo'shadi. Shu sababli musiqa bola hayotining ajralmas va muhim qismi sifatida e'tirof etiladi.",
    ],
    [
        "Musiqaning bola hissiy-emotsional rivojlanishidagi roli nihoyatda katta. Musiqa - bu his-tuyg'ular tili bo'lib, u bolaning emotsional olamiga bevosita ta'sir ko'rsatadi. Bola musiqa tinglash orqali turli hissiyotlarni - quvonch, qayg'u, tantanavorlik, hayajon - his qilishni o'rganadi. Bu uning hissiy sezgirligini rivojlantiradi va emotsional olamini boyitadi.",
        "Musiqa bolaga o'z his-tuyg'ularini tushunishga va ifodalashga yordam beradi. Ko'pincha bola o'z hissiyotlarini so'z bilan ifodalay olmaydi, lekin musiqa orqali u ularni his qiladi va namoyon etadi. Masalan, quvnoq musiqada bola raqsga tushadi, sakraydi, sekin musiqada esa tinchlanadi, o'ylaydi. Shunday qilib, musiqa bolaning hissiy ifoda vositasi bo'lib xizmat qiladi.",
        "Musiqa bolaning kayfiyatini boshqarishda muhim rol o'ynaydi. Tinch va yoqimli musiqa bolani tinchlantiradi, uning hayajonini bosadi va uyquga tayyorlaydi. Quvnoq va ritmik musiqa esa bolaning kayfiyatini ko'taradi, unga g'ayrat va quvonch bag'ishlaydi. Tarbiyachilar va ota-onalar bu xususiyatdan foydalanib, bolaning emotsional holatini muvofiqlashtiradi.",
        "Musiqa bolada empatiya - boshqalarning his-tuyg'ularini tushunish va his qilish qobiliyatini shakllantiradi. Musiqa qahramonlarining hissiyotlarini his qilish orqali bola boshqalarning kechinmalarini tushunishni o'rganadi. Bu uning ijtimoiy-emotsional rivojlanishi uchun muhim asos bo'ladi.",
        "Shuningdek, musiqa bolaning psixologik holatiga ijobiy ta'sir ko'rsatadi. Musiqa terapiyasi bolalardagi xavotir, qo'rquv va stress holatlarini yengillashtirishda samarali vosita sifatida qo'llaniladi. Yoqimli musiqa bolaga xotirjamlik va xavfsizlik hissini beradi, uning ruhiy salomatligini mustahkamlaydi. Shunday qilib, musiqa bolaning hissiy-emotsional rivojlanishida hal qiluvchi rol o'ynaydi.",
    ],
    [
        "Musiqaning bola aqliy rivojlanishidagi o'rni ilmiy jihatdan isbotlangan. Musiqa tinglash va idrok etish jarayonida bolaning diqqati, xotirasi va tafakkuri faol ishlaydi. Bola musiqani diqqat bilan tinglashni, uning qismlarini farqlashni va eslab qolishni o'rganadi. Bu uning bilish jarayonlarini rivojlantiradi.",
        "Musiqa bolaning xotirasini rivojlantiradi. Qo'shiqlarni yodlash, kuylarni eslab qolish va ularni qayta ijro etish bolaning musiqaviy va umumiy xotirasini mustahkamlaydi. Bola she'r va qo'shiq matnlarini yodlash orqali o'z xotira hajmini oshiradi. Bu keyinchalik o'quv faoliyatida muhim ahamiyatga ega bo'ladi.",
        "Ilmiy tadqiqotlar musiqa va matematik qobiliyatlar o'rtasidagi bog'liqlikni aniqlagan. Musiqa ritmi, tempi va tuzilishini idrok etish bolada matematik tafakkurni - sanoq, tartib, nisbat tushunchalarini rivojlantiradi. Musiqa bilan shug'ullanadigan bolalar matematik masalalarni yaxshiroq yechishlari kuzatilgan.",
        "Musiqaning bola nutqiy rivojlanishidagi o'rni alohida ahamiyatga ega. Qo'shiq kuylash bolaning talaffuzini yaxshilaydi, nutq nafasini rivojlantiradi va artikulyatsion apparatni mustahkamlaydi. Qo'shiq matnlari orqali bola yangi so'zlar o'rganadi va lug'at boyligini oshiradi. Ritmik mashqlar va sanash o'yinlari nutq ritmini his qilishga yordam beradi.",
        "Bundan tashqari, musiqa fonematik eshitishni - tovushlarni quloq bilan farqlash qobiliyatini rivojlantiradi. Bu qobiliyat bolaning savodxonlikka tayyorgarligi uchun muhim asos hisoblanadi. Tovushlarning balandligi, davomiyligi va tembrini farqlash keyinchalik harflar va so'zlarni o'rganishda yordam beradi. Shunday qilib, musiqa bolaning aqliy va nutqiy rivojlanishiga har tomonlama ijobiy ta'sir ko'rsatadi.",
    ],
    [
        "Musiqaning bola axloqiy tarbiyasidagi roli muhim ahamiyatga ega. Musiqa orqali bolada ezgu tuyg'ular - mehr, muhabbat, vatanparварlik, do'stlik, halollik - shakllanadi. Qo'shiqlar va musiqa asarlari mazmuni orqali bola yaxshilik va yomonlikni, go'zallik va xunuklikni farqlashni o'rganadi. Musiqa bolaning qalbiga ezgulik urug'larini ekadi.",
        "Xalq musiqasi va milliy qo'shiqlar bolada vatanga muhabbat va milliy g'ururni shakllantiradi. Bola o'z xalqining musiqaviy merosi - allalar, xalq qo'shiqlari, milliy kuylar - bilan tanishib, o'z madaniyatini qadrlashni o'rganadi. Bu uning milliy o'zligini anglashi va vatanparварlik tuyg'ularining shakllanishiga zamin yaratadi.",
        "Jamoaviy musiqaviy faoliyat - birgalikda kuylash, raqs va musiqaviy o'yinlar - bolada jamoaviylik, hamkorlik va o'zaro hurmat tuyg'ularini tarbiyalaydi. Bola jamoa bilan uyg'un harakat qilishni, o'z navbatini kutishni va birgalikda go'zal natijaga erishishni o'rganadi. Bu uning ijtimoiy axloqiy sifatlarini shakllantiradi.",
        "Musiqaning bola estetik tarbiyasidagi roli markaziy o'rinni egallaydi. Musiqa - bu go'zallik san'ati bo'lib, u bolada go'zallikni his qilish va undan zavqlanish qobiliyatini shakllantiradi. Bola musiqa orqali nafis tuyg'ularni, badiiy didni va estetik ideallarni o'zlashtiradi. Bu uning butun hayoti davomida go'zallikka intilishining asosini yaratadi.",
        "Musiqa bolada badiiy did va estetik baho berish qobiliyatini rivojlantiradi. Bola turli xarakterdagi musiqani tinglab, ularni farqlashni, go'zal va nafis musiqani his qilishni o'rganadi. U asta-sekin yuksak badiiy qiymatga ega bo'lgan musiqani tanlashni o'rganadi. Shunday qilib, musiqa bolaning axloqiy va estetik tarbiyasida tengsiz rol o'ynaydi va uning ma'naviy olamini boyitadi.",
    ],
    [
        "Musiqaning bola jismoniy rivojlanishidagi o'rni ham sezilarli darajada muhimdir. Musiqaga mos harakatlar, raqs va ritmik gimnastika bolaning harakat koordinatsiyasini, chaqqonligini va plastikligini rivojlantiradi. Musiqa ritmiga moslashib harakat qilish bolaning vaqt va makonda mo'ljal olish qobiliyatini oshiradi.",
        "Musiqa jo'natmasida bajariladigan jismoniy mashqlar bolaga qiziqarli va jozibali bo'ladi. Quvnoq musiqa bolaning harakat faolligini oshiradi, unga g'ayrat va quvonch bag'ishlaydi. Ertalabki gimnastikani musiqa jo'natmasida o'tkazish bolaning kayfiyatini ko'taradi va mashqlarni samaraliroq bajarishga yordam beradi.",
        "Ritmik harakatlar va raqs bolaning mushaklarini mustahkamlaydi, gavda holatini to'g'rilaydi va nafas tizimini rivojlantiradi. Musiqaga mos harakatlanish jarayonida bolaning butun tanasi faol ishlaydi. Bu uning jismoniy chiniqishiga va sog'lig'ining mustahkamlanishiga hissa qo'shadi.",
        "Musiqaning bola sog'lig'iga ijobiy ta'siri ilmiy jihatdan tasdiqlangan. Yoqimli musiqa bolaning asab tizimini tinchlantiradi, stress va zo'riqishni yengillashtiradi. Musiqa terapiyasi bolalarning psixologik va jismoniy salomatligini mustahkamlashda qo'llaniladi. Tinch musiqa bolaning yaxshi uxlashiga va dam olishiga yordam beradi.",
        "Nafas mashqlari bilan birga olib boriladigan qo'shiq kuylash bolaning nafas tizimini rivojlantiradi va o'pka hajmini oshiradi. To'g'ri nafas olish bolaning umumiy sog'lig'i uchun muhimdir. Shunday qilib, musiqa bolaning jismoniy rivojlanishi va sog'lig'ini mustahkamlashda ham muhim rol o'ynaydi. Musiqa va harakatning uyg'unligi bolaning har tomonlama jismoniy kamolotiga xizmat qiladi.",
    ],
    [
        "Musiqa bolaning kundalik hayotining ajralmas qismi bo'lishi kerak. Bola kun davomida turli vaziyatlarda musiqa bilan hamroh bo'lishi mumkin. Ertalab bola quvnoq musiqa jo'natmasida uyg'onadi va ertalabki gimnastikani bajaradi. Bu unga kun davomida g'ayrat va ijobiy kayfiyat bag'ishlaydi.",
        "Kun davomida musiqa bolaning turli faoliyatlariga hamroh bo'ladi. O'yin vaqtida musiqa bolaning ijodiy faoliyatini rag'batlantiradi. Tasviriy faoliyat vaqtida tinch musiqa bolaning ilhomini oshiradi va diqqatini jamlashga yordam beradi. Mehnat faoliyati vaqtida ritmik musiqa ishni qiziqarli qiladi.",
        "Dam olish va uyqu vaqtida tinch, yoqimli musiqa bolani tinchlantiradi va uyquga tayyorlaydi. Alla va sekin kuylar bolaning asab tizimini bo'shashtirib, sokin uyquni ta'minlaydi. Bu bolaning to'liq dam olishi va sog'lig'i uchun muhimdir.",
        "Bayram va tantanali kunlarda musiqa alohida o'rin tutadi. Bayramlarda bolalar kuylaydi, raqsga tushadi va musiqaviy sahna ko'rinishlarini namoyish etadi. Bu bolaning hayotiga quvonch va tantanavorlik bag'ishlaydi, unda ijobiy xotiralar qoldiradi. Bayramlar bolaning musiqaviy tajribasini boyitadi.",
        "Musiqaning kundalik hayotda tabiiy o'rin egallashi bolada musiqaga muhabbat va qiziqishni shakllantiradi. Bola musiqani hayotning ajralmas qismi sifatida qabul qiladi va undan zavqlanishni o'rganadi. Bu uning butun hayoti davomida musiqaga bo'lgan ijobiy munosabatining asosini yaratadi. Shu sababli musiqani bolaning kundalik hayotiga oqilona kiritish muhim ahamiyatga ega.",
    ],
    [
        "Bola hayotida musiqaning o'rni oila va maktabgacha ta'lim muassasasida birgalikda ta'minlanadi. Oila - bu bolaning musiqa bilan dastlabki tanishuvi ro'y beradigan joy. Onaning allasi, ota-onaning kuylagan qo'shiqlari va oilada yangraydigan musiqa bolaning musiqaviy tarbiyasining ilk asoslarini yaratadi.",
        "Oilada bolaning musiqaviy rivojlanishi uchun qulay muhit yaratish muhimdir. Ota-onalar bola bilan birga qo'shiq kuylashi, musiqa tinglashi, raqsga tushishi va musiqaviy o'yinlar o'ynashi mumkin. Bola uchun yoqimli, yoshiga mos musiqa tanlash va uni muntazam tinglatish bolaning musiqaviy didini shakllantiradi.",
        "Ota-onalar bolaning musiqaga qiziqishini qo'llab-quvvatlashi va rag'batlantirishi kerak. Agar bola kuylashni yoki raqsga tushishni xohlasa, ota-onalar buni qo'llab-quvvatlashi lozim. Bolani musiqaga majburlash emas, balki unga musiqadan zavqlanish imkonini berish muhimdir.",
        "Maktabgacha ta'lim muassasasida musiqaviy tarbiya tizimli va professional tarzda olib boriladi. Musiqa rahbari va tarbiyachilar bolalarning musiqaviy qobiliyatlarini rivojlantiradi, ularga musiqaviy bilim va ko'nikmalar beradi. Musiqa mashg'ulotlari, bayramlar va kundalik faoliyatda musiqadan foydalanish bolaning musiqaviy tajribasini boyitadi.",
        "Oila va maktabgacha ta'lim muassasasining uyg'un hamkorligi bolaning musiqaviy rivojlanishini ta'minlaydi. Tarbiyachilar ota-onalarga bolaning musiqaviy tarbiyasi bo'yicha tavsiyalar beradi, uyda qanday musiqa tinglatish va qanday faoliyat o'tkazish mumkinligini tushuntiradi. Bu hamkorlik bolaning musiqa olamiga to'liq kirib borishini ta'minlaydi va uning hayotida musiqaning munosib o'rin egallashiga zamin yaratadi.",
    ],
    [
        "Mazkur mustaqil ishda bolalar hayotida musiqaning o'rni va roli har tomonlama tahlil qilindi. Tahlillar shuni ko'rsatdiki, musiqa bola hayotining ajralmas va muhim qismi bo'lib, u bolaning butun shaxsiy kamolotiga ko'p qirrali ijobiy ta'sir ko'rsatadi.",
        "Musiqa bolaning hissiy-emotsional rivojlanishida hal qiluvchi rol o'ynaydi - u bolaning hissiy olamini boyitadi, kayfiyatini boshqaradi va empatiyani shakllantiradi. Aqliy va nutqiy rivojlanishda esa musiqa diqqat, xotira, tafakkur va nutq ko'nikmalarini rivojlantiradi. Shuningdek, musiqa matematik qobiliyatlar va savodxonlikka tayyorgarlikka ham hissa qo'shadi.",
        "Musiqa bolaning axloqiy va estetik tarbiyasida muhim o'rin tutadi - u ezgu tuyg'ularni, vatanparварlikni, badiiy did va go'zallikni his qilish qobiliyatini shakllantiradi. Jismoniy rivojlanishda esa musiqa harakat koordinatsiyasini, chaqqonlikni va sog'liqni mustahkamlaydi. Musiqa bolaning kundalik hayotiga tabiiy ravishda kiritilishi kerak.",
        "Xulosa qilib aytganda, musiqa - bu bolaning ma'naviy olamini boyitadigan, uni har tomonlama rivojlantiradigan va hayotiga go'zallik hamda quvonch bag'ishlaydigan tengsiz vositadir. Oila va maktabgacha ta'lim muassasasining uyg'un hamkorligida bolaning hayotida musiqaning munosib o'rin egallashini ta'minlash har bir kattaning muhim vazifasidir. Musiqa bolalik davridan boshlab insonni hamroh qilib, uning butun hayotini boyitadi.",
        "Foydalanilgan adabiyotlar:",
        "1. O'zbekiston Respublikasining \"Maktabgacha ta'lim va tarbiya to'g'risida\"gi Qonuni. - Toshkent, 2020.",
        "2. \"Ilk qadam\" maktabgacha ta'lim muassasalarining Davlat o'quv dasturi. - Toshkent, 2018.",
        "3. Nazarova M. \"Maktabgacha ta'limda musiqaviy tarbiya metodikasi\". - Toshkent, 2020.",
        "4. Qodirova R. \"Bolalar musiqaviy tarbiyasi\". - Toshkent, 2019.",
        "5. Vetlugina N.A. \"Muzykalnoye razvitiye rebyonka\". - Moskva, 2018.",
        "6. Radynova O.P. \"Muzykalnoye vospitaniye doshkolnikov\". - Moskva, 2017.",
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
body.append(make_para("Bolalar hayotida musiqaning o'rni va roli", bold=True, size=28, align="center"))
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
core_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Mustaqil ish - Bolalar hayotida musiqaning orni</dc:title><dc:creator>Talaba</dc:creator></cp:coreProperties>'
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
