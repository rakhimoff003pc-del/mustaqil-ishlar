#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mustaqil ish: Tabiat bilan tanishtirish metodikasi fanining predmeti, maqsad va vazifalari"""
import os, zipfile
from xml.sax.saxutils import escape

OUT = "/projects/sandbox/mustaqil-ishlar/Tabiat_metodikasi_predmeti.docx"

PLAN = [
    "Kirish",
    "Tabiat bilan tanishtirish metodikasi fanining predmeti",
    "Fanning ilmiy-nazariy asoslari",
    "Tabiat bilan tanishtirish metodikasining maqsadi",
    "Fanning asosiy vazifalari",
    "Fanning asosiy tushunchalari va kategoriyalari",
    "Fanning boshqa fanlar bilan aloqasi",
    "Fanning tadqiqot metodlari va amaliy ahamiyati",
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


SECTIONS.append([
    "Maktabgacha ta'lim tizimida bolalarni atrof-olam, xususan tabiat bilan tanishtirish muhim o'rin tutadi. Bola tabiat bilan tanishish jarayonida nafaqat bilim oladi, balki uning kuzatuvchanligi, fikrlash qobiliyati, estetik tuyg'ulari va ekologik madaniyati ham rivojlanadi. Bu jarayonni ilmiy asosda tashkil etish uchun maxsus fan - tabiat bilan tanishtirish metodikasi mavjud.",
    "Tabiat bilan tanishtirish metodikasi - bu maktabgacha yoshdagi bolalarni tabiat bilan tanishtirish jarayonining qonuniyatlarini, mazmunini, usullarini va tashkiliy shakllarini o'rganuvchi pedagogik fan sohasidir. Bu fan tarbiyachilarga bolalarni tabiat bilan ilmiy asosda, samarali va bolaning yosh xususiyatlariga mos tarzda tanishtirish imkonini beradi.",
    "Mazkur mustaqil ishda tabiat bilan tanishtirish metodikasi fanining predmeti, maqsad va vazifalari batafsil yoritiladi. Ishda fanning predmeti, ilmiy-nazariy asoslari, maqsadi, vazifalari, asosiy tushunchalari, boshqa fanlar bilan aloqasi va tadqiqot metodlari tahlil qilinadi. Mavzuning dolzarbligi shundaki, fanning predmeti va asosiy kategoriyalarini to'g'ri tushunish har bir tarbiyachi uchun kasbiy zaruratdir.",
])


SECTIONS.append([
    "Tabiat bilan tanishtirish metodikasi fanining predmeti - bu maktabgacha yoshdagi bolalarni tabiat bilan tanishtirish pedagogik jarayonidir. Fan bu jarayonning qonuniyatlarini, mazmunini, tamoyillarini, usullarini, vositalarini va tashkiliy shakllarini o'rganadi. Fanning predmeti bolaning tug'ilganidan maktabga borguncha bo'lgan davrdagi tabiat bilan tanishuvini qamrab oladi.",
    "Fanning o'rganish ob'ekti - maktabgacha yoshdagi bola va uning tabiat bilan o'zaro munosabati. Fanning predmeti esa shu munosabatni pedagogik jihatdan boshqarish, ya'ni bolani tabiat bilan maqsadli ravishda tanishtirishning shart-sharoitlari, mazmuni va usullaridir. Predmet aniq belgilanishi fanning mustaqilligini ta'minlaydi.",
    "Fanning predmeti bir nechta muhim masalalarni qamrab oladi. Birinchi masala - bolaning tabiat haqidagi tushunchalari qanday shakllanishi qonuniyatlarini o'rganish. Ikkinchi masala - har bir yosh bosqichida tabiat haqida qanday bilim berish kerakligini aniqlash. Uchinchi masala - tanishtirishning eng samarali usullari va vositalarini ishlab chiqish.",
    "To'rtinchi masala - bolada tabiatga ijobiy munosabat va ekologik madaniyatni shakllantirish yo'llarini belgilash. Beshinchi masala - tabiat bilan tanishtirishni tashkil etishning shakllari va tarbiyachining roli. Bu masalalar birgalikda fanning predmetini to'liq ochib beradi va uning ilmiy mazmunini tashkil etadi.",
    "Tabiat bilan tanishtirish metodikasi fani \"nimani o'rgatish?\" (mazmun), \"qanday o'rgatish?\" (usullar va shakllar), \"nima uchun o'rgatish?\" (maqsad) va \"qachon o'rgatish?\" (yosh bosqichlari) degan savollarga javob beradi. Bu savollar fanning asosiy kategoriyalarini tashkil etadi va uning predmetini aniqlashtirishga yordam beradi.",
])


SECTIONS.append([
    "Tabiat bilan tanishtirish metodikasi fanining ilmiy-nazariy asoslari bir nechta fundamental fanga tayanadi. Birinchi ilmiy asos - tabiiy fanlar (biologiya, ekologiya, botanika, zoologiya, geografiya). Bu fanlar tabiat, o'simliklar, hayvonlar va tabiat hodisalari haqida ilmiy bilim beradi. Tarbiyachi bu bilimlarni bolaning yoshiga moslab, sodda tarzda yetkazadi.",
    "Ikkinchi ilmiy asos - pedagogika fani. Didaktika tamoyillari, ta'lim va tarbiya nazariyasi, ta'limni tashkil etish qonuniyatlari tabiat bilan tanishtirish metodikasining pedagogik asosini tashkil etadi. Ko'rgazmalilik, izchillik, ilmiylik, yoshga moslik, onglilik kabi didaktik tamoyillar bu fanda ham qo'llaniladi.",
    "Uchinchi ilmiy asos - psixologiya fani. Bolalar psixologiyasi maktabgacha yoshdagi bolaning idroki, tafakkuri, xotirasi va qiziqishlarining xususiyatlarini o'rganadi. Bu yoshda bola ko'rgazmali-obrazli tafakkurga ega bo'lib, u tabiatni bevosita kuzatish orqali o'rganadi. Bu xususiyat tanishtirish metodlarini belgilashda hisobga olinadi.",
    "To'rtinchi ilmiy asos - falsafa. Falsafada tabiat va inson o'rtasidagi munosabat, insonning tabiatdagi o'rni va tabiat haqidagi bilimning ahamiyati masalalari o'rganiladi. Tabiatning yaxlitligi va undagi o'zaro bog'liqlik haqidagi falsafiy g'oyalar fanning metodologik asosini boyitadi.",
    "Tabiat bilan tanishtirish metodikasi fanining shakllanishida buyuk pedagoglarning g'oyalari muhim rol o'ynagan. Ya.A. Komenskiy tabiatga muvofiqlik tamoyilini ilgari surgan. K.D. Ushinskiy tabiatni \"buyuk tarbiyachi\" deb atagan. Ye.I. Tixeyeva bolalarni tabiat bilan tanishtirishning izchil metodikasini ishlab chiqqan. Bu olimlarning ilmiy merosi fanning nazariy poydevorini tashkil etadi.",
])


SECTIONS.append([
    "Tabiat bilan tanishtirish metodikasi fanining bosh maqsadi - maktabgacha yoshdagi bolalarni tabiat bilan ilmiy asosda tanishtirish jarayonini tashkil etishning samarali yo'llarini ishlab chiqish va tarbiyachilarni bu sohada zarur bilim va ko'nikmalar bilan qurollantirishdir. Bu maqsad fanning butun mazmunini belgilab beradi.",
    "Fanning maqsadi bolada tabiat haqida ilmiy tushunchalar tizimini shakllantirishning metodik asoslarini yaratishni o'z ichiga oladi. Fan har bir yosh bosqichida bolaga qanday bilim berish, uni qanday tarzda yetkazish va qanday natijaga erishish kerakligini ilmiy asoslab beradi.",
    "Maqsadning yana bir jihati - bolada tabiatga ongli va g'amxo'r munosabatni shakllantirishning metodik yo'llarini ishlab chiqishdir. Fan bolada ekologik madaniyat va tabiatga muhabbatni tarbiyalashning samarali usullarini belgilaydi. Bu zamonaviy ekologik ta'limning muhim yo'nalishi hisoblanadi.",
    "Fanning maqsadi shuningdek bo'lajak tarbiyachilarni kasbiy tayyorlash bilan bog'liqdir. Pedagogika oliy va o'rta maxsus ta'lim muassasalarida bu fan o'qitiladi. Kelajakdagi tarbiyachilar bolalarni tabiat bilan tanishtirishning nazariy asoslari va amaliy usullarini o'rganadilar va ularni amaliyotda qo'llashga tayyorlanadilar.",
    "Shunday qilib, fanning maqsadi keng qamrovli bo'lib, u bir tomondan bolalarni tabiat bilan tanishtirish jarayonini ilmiy asosda tashkil etishga, ikkinchi tomondan tarbiyachilarni bu sohada professional tayyorlashga qaratilgan. Bu maqsadga erishish bolalarning ekologik tarbiyasi va atrof-olamni bilishi sifatini oshiradi.",
])


SECTIONS.append([
    "Tabiat bilan tanishtirish metodikasi fanining vazifalari bosh maqsaddan kelib chiqqan holda aniq belgilangan. Birinchi vazifa - tabiat bilan tanishtirish mazmunini ilmiy asosda belgilash. Fan har bir yosh guruhi uchun bolaga qanday tabiiy bilim berish kerakligini, bu bilimlarning hajmi va murakkablik darajasini aniqlaydi.",
    "Ikkinchi vazifa - tabiat bilan tanishtirishning samarali metodlari va vositalarini ishlab chiqish. Fan kuzatish, tajriba, suhbat, hikoya, didaktik o'yin kabi metodlarni va ularning qo'llanilish shartlarini o'rganadi. Shuningdek, fan tabiat burchagi, ekskursiya, ko'rgazmali materiallar kabi vositalardan foydalanish yo'llarini belgilaydi.",
    "Uchinchi vazifa - tabiat bilan tanishtirishning tashkiliy shakllarini takomillashtirish. Fan mashg'ulotlar, ekskursiyalar, sayrlar, kuzatishlar, mehnat faoliyati va didaktik o'yinlar kabi tashkiliy shakllarni o'rganadi va ularni samarali tashkil etish yo'llarini ishlab chiqadi.",
    "To'rtinchi vazifa - bolaning tabiatga oid bilim va ko'nikmalarini baholash mezonlarini ishlab chiqish. Fan bolaning tabiat haqidagi tushunchalari, kuzatuvchanligi va ekologik ko'nikmalarini aniqlash usullarini belgilaydi. Beshinchi vazifa - ekologik tarbiyaning metodik asoslarini yaratish.",
    "Oltinchi vazifa - tabiat bilan tanishtirish sohasidagi ilg'or pedagogik tajribani o'rganish va umumlashtirish. Fan amaliyotdagi yutuqlarni tahlil qiladi va ularni keng joriy etish yo'llarini belgilaydi. Yettinchi vazifa - oila va maktabgacha ta'lim muassasasi hamkorligida bolaning ekologik tarbiyasini ta'minlash. Bu vazifalar birgalikda fanning amaliy yo'nalishini belgilaydi.",
])


SECTIONS.append([
    "Tabiat bilan tanishtirish metodikasi fani o'ziga xos tushunchalar va kategoriyalar tizimiga ega. Bu tushunchalar fanning ilmiy poydevorini tashkil etadi. Birinchi asosiy tushuncha - \"tabiat\". Tabiat - bu insonni o'rab turgan tirik va jonsiz olam bo'lib, u bolalarni tanishtirishning asosiy ob'ekti hisoblanadi.",
    "Ikkinchi muhim tushuncha - \"tabiiy bilim\". Bu bolaning tabiat haqidagi tasavvurlari, tushunchalari va bilimlari yig'indisidir. Tabiiy bilim bolaning yoshiga qarab oddiy tasavvurlardan murakkab tushunchalargacha rivojlanib boradi. Uchinchi tushuncha - \"ekologik tarbiya\". Bu bolada tabiatga ongli, g'amxo'r va mas'uliyatli munosabatni shakllantirish jarayonidir.",
    "To'rtinchi tushuncha - \"ekologik madaniyat\". Bu insonning tabiat bilan uyg'un munosabati, tabiatni asrash bo'yicha bilim, ko'nikma va xulq-atvor majmuidir. Beshinchi tushuncha - \"kuzatish\". Bu tabiat bilan tanishtirishning asosiy metodi bo'lib, bolaning tabiat ob'ektlarini maqsadli idrok etishidir.",
    "Oltinchi tushuncha - \"tabiat burchagi\". Bu guruh xonasida tashkil etiladigan, o'simlik va hayvonlar joylashtirilgan maxsus joy bo'lib, u bolaning tabiat bilan bevosita tanishuvini ta'minlaydi. Yettinchi tushuncha - \"ekskursiya\". Bu bolalarni tabiiy muhitga olib chiqib, tabiat bilan tanishtirishning tashkiliy shaklidir.",
    "Bu tushunchalar va kategoriyalar o'zaro bog'liq bo'lib, ular fanning yaxlit terminologik tizimini tashkil etadi. Tarbiyachi bu tushunchalarni to'g'ri bilishi va qo'llashi kerak. Asosiy tushunchalarni aniq tushunish fanni o'rganish va uni amaliyotda samarali qo'llashning muhim sharti hisoblanadi.",
])


SECTIONS.append([
    "Tabiat bilan tanishtirish metodikasi fani mustaqil fan sifatida boshqa ko'plab fanlar bilan chambarchas bog'liqdir. Bu aloqadorlik fanning interdistsiplinar xarakterini belgilaydi va uning ilmiy asosini boyitadi. Avvalo, fan tabiiy fanlar - biologiya, botanika, zoologiya, ekologiya, geografiya - bilan bog'liq.",
    "Tabiiy fanlar fanga tabiat, o'simliklar, hayvonlar va tabiat hodisalari haqida ilmiy bilim beradi. Bu bilimlar tarbiyachiga bolalarni to'g'ri va aniq tanishtirish imkonini beradi. Ekologiya fani esa tabiatdagi o'zaro bog'liqlik va inson-tabiat munosabati haqida bilim berib, ekologik tarbiyaning asosini tashkil etadi.",
    "Fan pedagogika bilan uzviy bog'liqdir. Umumiy pedagogika, didaktika va maktabgacha pedagogika fanga ta'lim va tarbiyaning umumiy qonuniyatlari, tamoyillari va usullarini taqdim etadi. Tabiat bilan tanishtirish metodikasi maktabgacha pedagogikaning xususiy metodikasi sifatida uning barcha qonuniyatlariga tayanadi.",
    "Fan psixologiya bilan ham bog'liqdir. Bolalar psixologiyasi va pedagogik psixologiya bolaning bilish jarayonlari, idroki va tafakkurining yosh xususiyatlarini tushuntiradi. Bu bilimlar tanishtirish metodlarini bolaning yoshiga moslab tanlashda zarurdir.",
    "Shuningdek, fan boshqa xususiy metodikalar - nutq o'stirish, matematik tasavvurlarni shakllantirish, tasviriy faoliyat metodikalari - bilan ham aloqadordir. Tabiat bilan tanishuv jarayonida bola nutqi rivojlanadi, matematik tushunchalar shakllanadi, tabiat go'zalligini tasviriy faoliyatda aks ettiradi. Bu fanlararo aloqadorlik bolaning yaxlit rivojlanishini ta'minlaydi.",
])


SECTIONS.append([
    "Tabiat bilan tanishtirish metodikasi fanida ilmiy tadqiqotlar olib borish uchun turli metodlardan foydalaniladi. Birinchi metod - pedagogik kuzatish. Tadqiqotchi bolalarning tabiat bilan tanishuv jarayonini, ularning tabiatga munosabatini va bilim darajasini kuzatadi va tahlil qiladi. Kuzatish tabiiy sharoitda olib boriladi.",
    "Ikkinchi metod - pedagogik eksperiment. Bu metod yangi metodikalar, usullar yoki vositalarning samaradorligini sinab ko'rish uchun qo'llaniladi. Tadqiqotchi yangi yondashuvni joriy etadi va uning natijasini an'anaviy yondashuv bilan taqqoslaydi. Eksperiment fanni rivojlantirishning muhim vositasidir.",
    "Uchinchi metod - suhbat va so'rovnoma. Tadqiqotchi bolalar, tarbiyachilar va ota-onalar bilan suhbat o'tkazib, ularning tabiat haqidagi bilimlari va munosabatlari haqida ma'lumot to'playdi. To'rtinchi metod - bolalar faoliyati mahsullarini tahlil qilish (rasmlar, ishlar). Beshinchi metod - hujjatlar tahlili (rejalar, mashg'ulot ishlanmalari).",
    "Fanning amaliy ahamiyati nihoyatda katta. Avvalo, fan tarbiyachilarga bolalarni tabiat bilan ilmiy asosda tanishtirish imkonini beradi. Fan bilimlariga ega tarbiyachi mashg'ulotlarni to'g'ri rejalashtiradi, samarali metodlar tanlaydi va bolalarning ekologik tarbiyasini ta'minlaydi.",
    "Ikkinchidan, fan bolalarning atrof-olamni bilishi, bilish qobiliyatlarining rivojlanishi va ekologik madaniyatining shakllanishiga xizmat qiladi. Uchinchidan, fan bolani maktabga tayyorlashda muhim rol o'ynaydi, chunki tabiat haqidagi bilimlar bolaning umumiy tayyorgarligining muhim qismidir. Shunday qilib, fan ham nazariy, ham amaliy jihatdan katta ahamiyatga ega.",
])


SECTIONS.append([
    "Mazkur mustaqil ishda tabiat bilan tanishtirish metodikasi fanining predmeti, maqsad va vazifalari har tomonlama tahlil qilindi. Tahlillar shuni ko'rsatdiki, bu fan mustaqil pedagogik fan bo'lib, uning aniq predmeti, maqsad va vazifalari hamda asosiy tushunchalar tizimi mavjud.",
    "Fanning predmeti - maktabgacha yoshdagi bolalarni tabiat bilan tanishtirish pedagogik jarayoni bo'lib, fan bu jarayonning qonuniyatlari, mazmuni, usullari va tashkiliy shakllarini o'rganadi. Fan tabiiy fanlar, pedagogika, psixologiya va falsafa fanlarining ilmiy yutuqlariga tayanadi.",
    "Fanning bosh maqsadi - bolalarni tabiat bilan ilmiy asosda tanishtirish jarayonini tashkil etishning samarali yo'llarini ishlab chiqish va tarbiyachilarni zarur bilim va ko'nikmalar bilan qurollantirishdir. Fanning vazifalari mazmunni belgilash, metod va vositalarni ishlab chiqish, tashkiliy shakllarni takomillashtirish va ekologik tarbiyani ta'minlashdan iborat.",
    "Xulosa qilib aytganda, tabiat bilan tanishtirish metodikasi fanining predmeti va asosiy tushunchalarini chuqur o'rganish har bir tarbiyachi uchun kasbiy zaruratdir. Bu bilimlar tarbiyachiga bolalarni tabiat bilan samarali tanishtirish, ularning bilish qobiliyatlarini rivojlantirish va ekologik madaniyatini shakllantirish imkonini beradi.",
    "Foydalanilgan adabiyotlar:",
    "1. O'zbekiston Respublikasining \"Maktabgacha ta'lim va tarbiya to'g'risida\"gi Qonuni. - Toshkent, 2020.",
    "2. \"Ilk qadam\" maktabgacha ta'lim muassasalarining Davlat o'quv dasturi. - Toshkent, 2018.",
    "3. Sodiqova M. \"Bolalarni tabiat bilan tanishtirish metodikasi\". - Toshkent, 2020.",
    "4. Yusupova N. \"Maktabgacha yoshdagi bolalarning ekologik tarbiyasi\". - Toshkent, 2021.",
    "5. Nikolayeva S.N. \"Teoriya i metodika ekologicheskogo obrazovaniya detey\". - Moskva, 2018.",
    "6. Solomennikova O.A. \"Oznakomleniye s prirodoy v detskom sadu\". - Moskva, 2017.",
])


# Bo'limlar PLAN tartibiga moslab qayta tartiblanadi
# Qo'shilish tartibi: 0=predmeti,1=xulosa,2=vazifalari,3=boshqa fanlar,
# 4=tadqiqot,5=maqsad,6=tushunchalar,7=kirish,8=nazariy asoslar
SEC_ORDERED = [
    SECTIONS[7],  # Kirish
    SECTIONS[0],  # Predmeti
    SECTIONS[8],  # Nazariy asoslari
    SECTIONS[5],  # Maqsadi
    SECTIONS[2],  # Vazifalari
    SECTIONS[6],  # Tushunchalari
    SECTIONS[3],  # Boshqa fanlar bilan aloqasi
    SECTIONS[4],  # Tadqiqot metodlari va amaliy ahamiyati
    SECTIONS[1],  # Xulosa
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
body.append(make_para("Tabiat bilan tanishtirish metodikasi fanining predmeti, maqsad va vazifalari", bold=True, size=28, align="center"))
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
core_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Mustaqil ish - Tabiat metodikasi predmeti</dc:title><dc:creator>Talaba</dc:creator></cp:coreProperties>'
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
