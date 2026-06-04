#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mustaqil ish: Bolalarni tabiat bilan tanishtirishning nazariy asoslari"""
import os, zipfile
from xml.sax.saxutils import escape

OUT = "/projects/sandbox/mustaqil-ishlar/Tabiat_bilan_tanishtirish.docx"

PLAN = [
    "Kirish",
    "Tabiat tushunchasi va uning tarkibiy qismlari",
    "Bolalarni tabiat bilan tanishtirishning nazariy asoslari",
    "Bolalarni tabiat bilan tanishtirishning maqsad va vazifalari",
    "Tabiat bilan tanishtirishning mazmuni va yo'nalishlari",
    "Bolalarni tabiat bilan tanishtirish metodlari va vositalari",
    "Ekologik tarbiya va tabiatga muhabbatni shakllantirish",
    "Tarbiyachining bolalarni tabiat bilan tanishtirishdagi roli",
    "Xulosa va foydalanilgan adabiyotlar",
]

SECTIONS = []


SECTIONS.append([
    "Tabiat - inson hayotining asosi va uning ajralmas qismi bo'lib, u kishini o'rab turgan butun moddiy olamni qamrab oladi. Bola dunyoga kelgan kunidan boshlab tabiat bilan o'zaro ta'sirda bo'ladi: u quyosh nurini his qiladi, qushlar sayrashini eshitadi, gullarni ko'radi va o'simliklarning hidini sezadi. Bolalarni tabiat bilan tanishtirish maktabgacha ta'limning muhim yo'nalishlaridan biri hisoblanadi.",
    "Maktabgacha yosh - bolaning atrof-olamni faol o'rganish, undagi narsa va hodisalarga qiziqish bilan qaraydigan davridir. Aynan shu davrda bolada tabiatga muhabbat, unga g'amxo'rlik qilish va ekologik madaniyatning asoslari shakllanadi. Tabiat bilan tanishuv bolaning bilim doirasini kengaytiradi, uning kuzatuvchanligini, fikrlash qobiliyatini va estetik tuyg'ularini rivojlantiradi.",
    "Mazkur mustaqil ishda maktabgacha ta'limda bolalarni tabiat bilan tanishtirishning nazariy asoslari va tabiat haqidagi tushuncha batafsil yoritiladi. Ishda tabiat tushunchasi, tanishtirishning nazariy asoslari, maqsad va vazifalari, mazmuni, metodlari, ekologik tarbiya hamda tarbiyachining roli tahlil qilinadi. Mavzuning dolzarbligi shundaki, bugungi kunda ekologik muammolar keskinlashayotgan bir paytda bolalarda tabiatga ongli munosabatni shakllantirish muhim ahamiyat kasb etmoqda.",
])


SECTIONS.append([
    "Tabiat - bu insonni o'rab turgan, uning ishtirokisiz mavjud bo'lgan butun moddiy olamdir. Tabiat keng ma'noda butun koinotni, tor ma'noda esa Yer yuzidagi tirik va jonsiz olamni anglatadi. Tabiat tushunchasi inson yashaydigan muhitni, undagi barcha narsa va hodisalarni o'z ichiga oladi. Bolalarni tabiat bilan tanishtirishda aynan shu keng tushuncha asos qilib olinadi.",
    "Tabiat ikki asosiy qismga bo'linadi: tirik tabiat va jonsiz tabiat. Tirik tabiatga o'simliklar, hayvonlar, qushlar, hasharotlar, baliqlar va insonning o'zi kiradi. Tirik organizmlar nafas oladi, oziqlanadi, o'sadi, ko'payadi va harakatlanadi. Bola tirik tabiat bilan tanishganda jonli mavjudotlarning hayoti, ehtiyojlari va ularga g'amxo'rlik qilish haqida tushunchaga ega bo'ladi.",
    "Jonsiz tabiatga quyosh, oy, yulduzlar, havo, suv, tuproq, toshlar, qum va boshqa jonsiz narsalar kiradi. Jonsiz tabiat tirik organizmlarning yashashi uchun zarur sharoit yaratadi. Masalan, quyosh issiqlik va yorug'lik beradi, suv va havo barcha tirik mavjudotlar uchun hayotiy zarurdir. Bola jonsiz tabiat bilan tanishganda tabiat hodisalarini va ularning ahamiyatini tushunadi.",
    "Tabiatdagi barcha narsalar o'zaro bog'liq va bir-biriga ta'sir ko'rsatadi. O'simliklar quyosh nuri, suv va tuproqsiz o'sa olmaydi. Hayvonlar o'simliklar va boshqa hayvonlar bilan oziqlanadi. Inson ham tabiatning bir qismi bo'lib, u tabiatga bog'liq. Bu o'zaro bog'liqlikni tushunish bolada tabiatni yaxlit tizim sifatida idrok etishni shakllantiradi.",
    "Tabiat doimo o'zgarib turadi. Yil fasllarining almashinuvi, kun va tunning navbatlashishi, ob-havoning o'zgarishi - bularning barchasi tabiatdagi o'zgarishlardir. Bola bu o'zgarishlarni kuzatib, tabiatning mavsumiy o'zgarishlari, sabab-natija aloqalari haqida tushuncha hosil qiladi. Tabiat haqidagi bu tushunchalar bolaning atrof-olam haqidagi bilimlarining asosini tashkil etadi.",
])


SECTIONS.append([
    "Bolalarni tabiat bilan tanishtirishning nazariy asoslari bir nechta fan va pedagogik nazariyalarga tayanadi. Birinchi nazariy asos - falsafiy asos. Falsafada tabiat va inson o'rtasidagi munosabat, insonning tabiatdagi o'rni va ularning o'zaro bog'liqligi masalalari o'rganiladi. Bola tabiatning bir qismi ekanligini va unga bog'liqligini tushunishi muhimdir.",
    "Ikkinchi nazariy asos - tabiiy-ilmiy asos. Bu asos biologiya, ekologiya, geografiya va boshqa tabiiy fanlardan olingan bilimlarga tayanadi. Tabiat haqidagi ilmiy bilimlar bolaga tabiatdagi narsa va hodisalarni to'g'ri tushuntirishga imkon beradi. Tarbiyachi bu bilimlarni bolaning yoshiga moslab, sodda va tushunarli tarzda yetkazadi.",
    "Uchinchi nazariy asos - psixologik asos. Bolalar psixologiyasi maktabgacha yoshdagi bolaning bilish jarayonlari, idroki, tafakkuri va qiziqishlarining xususiyatlarini o'rganadi. Bu yoshda bola ko'rgazmali-obrazli tafakkurga ega bo'lib, u tabiatni bevosita kuzatish, ushlab ko'rish va his qilish orqali o'rganadi. Bu xususiyatlar tanishtirish metodlarini belgilashda hisobga olinadi.",
    "To'rtinchi nazariy asos - pedagogik asos. Pedagogikada ta'lim va tarbiyaning umumiy qonuniyatlari, tamoyillari va usullari belgilanadi. Bolalarni tabiat bilan tanishtirishda ko'rgazmalilik, izchillik, ilmiylik, yoshga moslik kabi didaktik tamoyillarga rioya qilinadi. Buyuk pedagoglar - Ya.A. Komenskiy, K.D. Ushinskiy, Ye.I. Tixeyeva - tabiatning tarbiyaviy ahamiyatini ta'kidlaganlar.",
    "K.D. Ushinskiy tabiatni \"buyuk tarbiyachi\" deb atagan va uni bolaning aqliy va ma'naviy rivojlanishida muhim omil sifatida ko'rsatgan. Ye.I. Tixeyeva esa bolalarni tabiat bilan tanishtirishning izchil metodikasini ishlab chiqqan. Bu nazariy asoslar birgalikda bolalarni tabiat bilan tanishtirishning ilmiy poydevorini tashkil etadi va bu jarayonni samarali tashkil etish imkonini beradi.",
])


SECTIONS.append([
    "Bolalarni tabiat bilan tanishtirishning bosh maqsadi - bolada tabiat haqida dastlabki ilmiy tushunchalar tizimini shakllantirish, tabiatga ongli va g'amxo'r munosabatni tarbiyalash hamda ekologik madaniyat asoslarini yaratishdir. Bu maqsad bolaning atrof-olamni bilishi va tabiat bilan uyg'un yashashga o'rganishini ta'minlaydi.",
    "Birinchi vazifa - bolada tabiat haqida bilim va tushunchalarni shakllantirish. Bola o'simliklar, hayvonlar, tabiat hodisalari, yil fasllari va tabiatdagi o'zaro bog'liqliklar haqida bilim oladi. Bu bilimlar bolaning yoshiga mos, sodda va aniq bo'lishi kerak. Bola tabiatdagi narsa va hodisalarni nomlash, tasvirlash va farqlashni o'rganadi.",
    "Ikkinchi vazifa - bolada bilish qobiliyatlarini rivojlantirish. Tabiat bilan tanishuv jarayonida bola kuzatish, taqqoslash, tahlil qilish, guruhlash va xulosa chiqarish ko'nikmalarini egallaydi. Bola \"nima uchun?\", \"qanday qilib?\" degan savollarga javob izlaydi va tabiatdagi sabab-natija aloqalarini tushunadi.",
    "Uchinchi vazifa - bolada tabiatga ijobiy hissiy munosabatni shakllantirish. Bola tabiat go'zalligini his qilishni, undan zavqlanishni va tirik mavjudotlarga mehr bilan munosabatda bo'lishni o'rganadi. Tabiatga muhabbat bolaning ekologik tarbiyasining hissiy asosini tashkil etadi.",
    "To'rtinchi vazifa - bolada tabiatga g'amxo'rlik qilish ko'nikmalarini shakllantirish. Bola o'simliklarni parvarish qilish, hayvonlarga g'amxo'rlik qilish va tabiatni asrash ko'nikmalarini egallaydi. Beshinchi vazifa - bolada ekologik madaniyat va tabiatga nisbatan mas'uliyat hissini tarbiyalash. Bu vazifalar birgalikda bolaning tabiat bilan uyg'un munosabatini ta'minlaydi.",
])


SECTIONS.append([
    "Bolalarni tabiat bilan tanishtirishning mazmuni bolaning yoshiga qarab bosqichma-bosqich kengayib boradi. Mazmun bir nechta asosiy yo'nalishni o'z ichiga oladi. Birinchi yo'nalish - o'simliklar olami bilan tanishtirish. Bola daraxtlar, gullar, sabzavotlar, mevalar, xona o'simliklari bilan tanishadi, ularning tuzilishi, o'sishi va parvarishi haqida bilim oladi.",
    "Ikkinchi yo'nalish - hayvonot olami bilan tanishtirish. Bola uy va yovvoyi hayvonlar, qushlar, baliqlar, hasharotlar bilan tanishadi. U hayvonlarning tashqi ko'rinishi, yashash joyi, oziqlanishi, harakati va ularga g'amxo'rlik qilish haqida tushuncha hosil qiladi. Bola hayvonlarning insonga foydasini va ularni asrash zarurligini tushunadi.",
    "Uchinchi yo'nalish - jonsiz tabiat bilan tanishtirish. Bola suv, havo, tuproq, qum, tosh, quyosh kabi jonsiz tabiat ob'ektlari bilan tanishadi. U bu narsalarning xususiyatlari va tirik tabiat uchun ahamiyatini bilib oladi. Sodda tajribalar orqali bola suvning, havoning va boshqa moddalarning xossalarini o'rganadi.",
    "To'rtinchi yo'nalish - mavsumiy o'zgarishlar bilan tanishtirish. Bola yil fasllari - kuz, qish, bahor, yoz - va ularning o'ziga xos belgilari bilan tanishadi. U har bir faslda tabiatda, o'simlik va hayvonlar hayotida, insonlar mehnatida qanday o'zgarishlar ro'y berishini kuzatadi. Bu bolada vaqt va mavsumiylik tushunchasini shakllantiradi.",
    "Beshinchi yo'nalish - inson va tabiat o'rtasidagi munosabat bilan tanishtirish. Bola insonning tabiatga ta'siri, tabiatdan oqilona foydalanish va uni asrash zarurligi haqida tushuncha hosil qiladi. Bu yo'nalish ekologik tarbiyaning asosini tashkil etadi. Mazmunning barcha yo'nalishlari o'zaro bog'liq holda, bolaning yoshiga mos tarzda amalga oshiriladi.",
])


SECTIONS.append([
    "Bolalarni tabiat bilan tanishtirishda turli metodlardan foydalaniladi. Metodlar uch asosiy guruhga bo'linadi: ko'rgazmali, amaliy va og'zaki. Birinchi guruh - ko'rgazmali metodlar. Bularga kuzatish, rasmlar va illyustratsiyalarni ko'rib chiqish, video va filmlar namoyishi kiradi. Kuzatish - tabiat bilan tanishtirishning asosiy va eng samarali metodi hisoblanadi.",
    "Kuzatish metodi bolaning tabiat ob'ektlari va hodisalarini bevosita idrok etishiga asoslanadi. Bola o'simlik o'sishini, hayvonlar hayotini, ob-havo o'zgarishlarini kuzatadi. Kuzatish qisqa muddatli va uzoq muddatli bo'lishi mumkin. Masalan, urug'ning unib chiqishini kuzatish uzoq muddatli kuzatishdir. Kuzatish bolaning kuzatuvchanligini va bilish qiziqishini rivojlantiradi.",
    "Ikkinchi guruh - amaliy metodlar. Bularga tajribalar, mehnat faoliyati va didaktik o'yinlar kiradi. Sodda tajribalar orqali bola tabiat hodisalarini o'rganadi: suvning muzlashi, qorning erishi, o'simlikning suvga ehtiyoji. Mehnat faoliyati - o'simliklarni sug'orish, hayvonlarni boqish, tabiat burchagini parvarish qilish - bolada amaliy ko'nikmalarni shakllantiradi.",
    "Uchinchi guruh - og'zaki metodlar. Bularga tarbiyachining hikoyasi, suhbat, badiiy adabiyot o'qish kiradi. Tarbiyachi tabiat haqida qiziqarli hikoyalar aytadi, bolalar bilan suhbat o'tkazadi va tabiat haqidagi she'r, ertak, hikoyalarni o'qiydi. Bu metodlar bolaning tabiat haqidagi tushunchalarini boyitadi va mustahkamlaydi.",
    "Tabiat bilan tanishtirish vositalari sifatida quyidagilar qo'llaniladi: tabiat burchagi va undagi o'simlik va hayvonlar, bog'cha hududidagi gulzor va polizlar, ekskursiya va sayrlar, ko'rgazmali materiallar (rasmlar, gerbariy, kolleksiyalar), didaktik o'yinlar va kartochkalar, badiiy adabiyot va texnik vositalar. Bu vositalar bolaning tabiat bilan bevosita va bilvosita tanishuvini ta'minlaydi.",
])


SECTIONS.append([
    "Ekologik tarbiya - bolalarni tabiat bilan tanishtirishning eng muhim maqsadlaridan biri bo'lib, u bolada tabiatga ongli, g'amxo'r va mas'uliyatli munosabatni shakllantirishni nazarda tutadi. Zamonaviy dunyoda ekologik muammolar keskinlashayotgan bir paytda, bolalarda ekologik madaniyatni erta yoshdan shakllantirish katta ahamiyat kasb etadi.",
    "Ekologik tarbiyaning birinchi vazifasi - bolada tabiatga muhabbat va ehtiyotkorlik tuyg'usini shakllantirishdir. Bola tabiatni sevishi, uning go'zalligini his qilishi va tirik mavjudotlarga mehr bilan munosabatda bo'lishi kerak. Tabiatga muhabbat ekologik ongning hissiy asosini tashkil etadi va bolada tabiatni asrash istagini uyg'otadi.",
    "Ikkinchi vazifa - bolada tabiatdagi o'zaro bog'liqlikni tushunishni shakllantirish. Bola tabiatdagi barcha narsalar bir-biriga bog'liq ekanligini, insonning tabiatga ta'sirini va bu ta'sirning oqibatlarini tushunadi. Masalan, daraxtlar havoni tozalashini, suvni ifloslantirish baliqlarga zarar yetkazishini bola tushunadi.",
    "Uchinchi vazifa - bolada tabiatni asrash ko'nikmalarini shakllantirish. Bola suvni tejash, o'simliklarni ekish va parvarish qilish, qushlarga g'amxo'rlik qilish, chiqindilarni to'g'ri tashlash kabi amaliy ekologik ko'nikmalarni egallaydi. Bu ko'nikmalar bolaning kundalik hayotida ekologik xulq-atvorini shakllantiradi.",
    "Ekologik tarbiya bolada tabiatga nisbatan mas'uliyat hissini tarbiyalaydi. Bola o'zining har bir harakati tabiatga ta'sir qilishini va u tabiat oldida mas'ul ekanligini tushunadi. Bu tushuncha bolaning butun hayoti davomida tabiatga oqilona munosabatda bo'lishining asosini yaratadi. Shunday qilib, ekologik tarbiya kelajakda tabiatni asraydigan, ekologik ongli avlodni tarbiyalashga xizmat qiladi.",
])


SECTIONS.append([
    "Bolalarni tabiat bilan tanishtirishda tarbiyachining roli hal qiluvchi ahamiyatga ega. Tarbiyachi bolalarning tabiat bilan tanishuvini tashkil etadi, yo'naltiradi va bu jarayonni samarali boshqaradi. Uning bilimi, mahorati va tabiatga bo'lgan munosabati bolalarning tabiatga munosabatiga bevosita ta'sir ko'rsatadi.",
    "Tarbiyachining birinchi vazifasi - tabiat bilan tanishtirish jarayonini rejalashtirish va tashkil etish. U \"Ilk qadam\" davlat o'quv dasturi asosida mashg'ulotlarni rejalashtiradi, kuzatish va ekskursiyalarni tashkil etadi, tabiat burchagi va bog'cha hududini jihozlaydi. Tarbiyachi bolalarning yosh xususiyatlarini hisobga olib, mos mazmun va metodlarni tanlaydi.",
    "Tarbiyachining ikkinchi vazifasi - o'zi tabiat haqida chuqur bilimga ega bo'lish. Tarbiyachi o'simliklar, hayvonlar va tabiat hodisalari haqida yetarli ilmiy bilimga ega bo'lishi kerak. U bolalarning savollariga to'g'ri va aniq javob bera olishi, ularning bilish qiziqishini qondira olishi lozim.",
    "Tarbiyachining uchinchi vazifasi - bolada tabiatga ijobiy munosabatni shakllantirish. Tarbiyachining o'zi tabiatni sevishi va unga g'amxo'rlik qilishi bolalarga namuna bo'ladi. Tarbiyachi bolalarga tabiat go'zalligini ko'rsatadi, ularning kuzatuvchanligini rivojlantiradi va tabiatga mehr bilan munosabatda bo'lishni o'rgatadi.",
    "Tarbiyachining to'rtinchi vazifasi - bolalarning amaliy faoliyatini tashkil etish. U bolalarni o'simliklarni parvarish qilish, hayvonlarga g'amxo'rlik qilish va tabiatda mehnat qilishga jalb etadi. Beshinchi vazifasi - ota-onalar bilan hamkorlik qilish va o'z kasbiy mahoratini doimiy oshirib borish. Tarbiyachining mahorati bolalarning ekologik tarbiyasini ta'minlashda hal qiluvchi omil hisoblanadi.",
])


SECTIONS.append([
    "Mazkur mustaqil ishda maktabgacha ta'limda bolalarni tabiat bilan tanishtirishning nazariy asoslari va tabiat haqidagi tushuncha har tomonlama tahlil qilindi. Tahlillar shuni ko'rsatdiki, bolalarni tabiat bilan tanishtirish maktabgacha ta'limning muhim yo'nalishi bo'lib, u bolaning har tomonlama rivojlanishi va ekologik tarbiyasiga xizmat qiladi.",
    "Tabiat - tirik va jonsiz qismlardan iborat yaxlit tizim bo'lib, undagi barcha narsalar o'zaro bog'liqdir. Bolalarni tabiat bilan tanishtirish falsafiy, tabiiy-ilmiy, psixologik va pedagogik asoslarga tayanadi. Bu jarayonning maqsadi bolada tabiat haqida bilim, bilish qobiliyatlari, tabiatga ijobiy munosabat va ekologik madaniyatni shakllantirishdir.",
    "Tabiat bilan tanishtirish o'simliklar, hayvonlar, jonsiz tabiat, mavsumiy o'zgarishlar va inson-tabiat munosabati yo'nalishlarida amalga oshiriladi. Bu jarayonda ko'rgazmali (kuzatish), amaliy (tajriba, mehnat) va og'zaki (hikoya, suhbat) metodlar qo'llaniladi. Ekologik tarbiya esa bolada tabiatga ongli va mas'uliyatli munosabatni shakllantiradi.",
    "Xulosa qilib aytganda, bolalarni tabiat bilan tanishtirish - bu bolaning atrof-olamni bilishi, bilish qobiliyatlarining rivojlanishi va ekologik madaniyatining shakllanishini ta'minlaydigan muhim pedagogik jarayondir. To'g'ri tashkil etilgan bu jarayon kelajakda tabiatni sevadigan, uni asraydigan va u bilan uyg'un yashaydigan ongli avlodni tarbiyalashga xizmat qiladi.",
    "Foydalanilgan adabiyotlar:",
    "1. O'zbekiston Respublikasining \"Maktabgacha ta'lim va tarbiya to'g'risida\"gi Qonuni. - Toshkent, 2020.",
    "2. \"Ilk qadam\" maktabgacha ta'lim muassasalarining Davlat o'quv dasturi. - Toshkent, 2018.",
    "3. Sodiqova M. \"Bolalarni tabiat bilan tanishtirish metodikasi\". - Toshkent, 2020.",
    "4. Yusupova N. \"Maktabgacha yoshdagi bolalarning ekologik tarbiyasi\". - Toshkent, 2021.",
    "5. Nikolayeva S.N. \"Metodika ekologicheskogo vospitaniya doshkolnikov\". - Moskva, 2018.",
    "6. Solomennikova O.A. \"Oznakomleniye s prirodoy v detskom sadu\". - Moskva, 2017.",
])



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
body.append(make_para("Maktabgacha ta'limda bolalarni tabiat bilan tanishtirishning nazariy asoslari va tabiat haqida tushuncha", bold=True, size=28, align="center"))
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
core_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Mustaqil ish - Tabiat bilan tanishtirish</dc:title><dc:creator>Talaba</dc:creator></cp:coreProperties>'
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
