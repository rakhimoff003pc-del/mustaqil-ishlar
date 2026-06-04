#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mustaqil ish: Bolalar jismoniy tarbiya fanining predmeti va asosiy tushunchalari
"""
import os, zipfile
from xml.sax.saxutils import escape

OUT = "/projects/sandbox/mustaqil-ishlar/Jismoniy_tarbiya_predmeti.docx"

PLAN = [
    "Kirish",
    "Bolalar jismoniy tarbiya fanining predmeti",
    "Jismoniy tarbiya fanining maqsad va vazifalari",
    "\"Jismoniy tarbiya\" va \"jismoniy rivojlanish\" tushunchalari",
    "\"Jismoniy tayyorgarlik\" va \"jismoniy kamolot\" tushunchalari",
    "\"Jismoniy mashq\" va \"harakat faolligi\" tushunchalari",
    "Jismoniy tarbiya fanining boshqa fanlar bilan aloqasi",
    "Jismoniy tarbiya fanining maktabgacha ta'limdagi ahamiyati",
    "Xulosa va foydalanilgan adabiyotlar",
]

SECTIONS = [
    [
        "Jismoniy tarbiya shaxsning har tomonlama kamol topishining ajralmas qismi bo'lib, u bolaning sog'lig'ini mustahkamlash, harakat ko'nikmalarini shakllantirish va jismoniy sifatlarini rivojlantirishga yo'naltirilgan pedagogik jarayondir. Maktabgacha yoshdagi bolalarning jismoniy tarbiyasi ularning butun hayoti davomidagi sog'lig'i va farovonligi uchun mustahkam poydevor yaratadi.",
        "Bolalar jismoniy tarbiya fani mustaqil pedagogik fan sifatida o'zining aniq predmeti, maqsad va vazifalari hamda asosiy tushunchalar tizimiga ega. Har qanday fanni o'rganish uning predmeti va asosiy tushunchalarini aniqlashdan boshlanadi. Bu tushunchalar fanning ilmiy poydevorini tashkil etadi va uni boshqa fanlardan ajratib turadi.",
        "Mazkur mustaqil ishda bolalar jismoniy tarbiya fanining predmeti va asosiy tushunchalari batafsil yoritiladi. Ishda fanning predmeti, maqsad va vazifalari, asosiy tushunchalar - jismoniy tarbiya, jismoniy rivojlanish, jismoniy tayyorgarlik, jismoniy kamolot, jismoniy mashq, harakat faolligi - hamda fanning boshqa fanlar bilan aloqasi tahlil qilinadi. Mavzuning dolzarbligi shundaki, fanning asosiy tushunchalarini to'g'ri tushunish har bir tarbiyachi uchun kasbiy zaruratdir.",
    ],
    [
        "Bolalar jismoniy tarbiya fani - bu maktabgacha yoshdagi bolalarning jismoniy tarbiyasi qonuniyatlarini, mazmunini, usullarini va tashkiliy shakllarini o'rganuvchi pedagogik fan sohasidir. Fanning predmeti - maktabgacha yoshdagi bolalarning jismoniy tarbiyasi pedagogik jarayoni bo'lib, u bolaning harakat ko'nikmalarini shakllantirish, jismoniy sifatlarini rivojlantirish va sog'lig'ini mustahkamlashni o'z ichiga oladi.",
        "Fanning predmeti bir nechta muhim jihatlarni qamrab oladi. Birinchi jihat - bolaning jismoniy rivojlanishi qonuniyatlarini o'rganish. Har bir yosh davrida bolaning organizmi o'ziga xos xususiyatlarga ega bo'lib, jismoniy tarbiya bu xususiyatlarni hisobga olgan holda tashkil etiladi. Ikkinchi jihat - harakat ko'nikmalarini shakllantirish usullarini ishlab chiqish.",
        "Uchinchi jihat - jismoniy sifatlarni (tezkorlik, kuch, chidamlilik, egiluvchanlik, chaqqonlik) rivojlantirish yo'llarini belgilash. To'rtinchi jihat - jismoniy tarbiya mashg'ulotlarining tashkiliy shakllarini takomillashtirish. Beshinchi jihat - bolaning jismoniy rivojlanishini baholash mezonlarini ishlab chiqish. Bu jihatlar birgalikda fanning predmetini to'liq ochib beradi.",
        "Fan o'rganadigan ob'ekt - bu maktabgacha yoshdagi bola va uning jismoniy rivojlanishi. Fanning predmeti esa shu ob'ektni boshqarish, ya'ni bolaning jismoniy tarbiyasini maqsadli ravishda tashkil etishning pedagogik shart-sharoitlari, mazmuni, usullari va shakllaridir. Predmet aniq belgilanishi fanning mustaqilligini va ilmiy asosini ta'minlaydi.",
    ],
    [
        "Bolalar jismoniy tarbiya fanining bosh maqsadi - maktabgacha yoshdagi bolalarning sog'lig'ini mustahkamlash, jismoniy rivojlanishini ta'minlash, hayot uchun zarur harakat ko'nikmalarini shakllantirish va sog'lom turmush tarzi asoslarini tarbiyalashdir. Bu maqsad fanning butun mazmunini va yo'nalishini belgilab beradi.",
        "Fanning vazifalari uch guruhga bo'linadi. Birinchi guruh - sog'lomlashtirish vazifalari. Bularga bolaning sog'lig'ini saqlash va mustahkamlash, organizmni chiniqtirish, to'g'ri gavda holatini shakllantirish, organlar va tizimlar funksiyalarini yaxshilash hamda kasalliklarning oldini olish kiradi. Bu vazifalar bolaning biologik rivojlanishini ta'minlaydi.",
        "Ikkinchi guruh - ta'limiy vazifalar. Bularga asosiy harakat turlarini (yurish, yugurish, sakrash, otish, irmalab chiqish) o'rgatish, harakat ko'nikmalarini takomillashtirish va jismoniy mashqlar texnikasini o'zlashtirish kiradi. Bola hayotda zarur bo'lgan barcha asosiy harakatlarni to'g'ri va ishonchli bajara olishi kerak.",
        "Uchinchi guruh - tarbiyaviy vazifalar. Bularga bolada jismoniy mashqlarga qiziqish va ehtiyoj tuyg'usini shakllantirish, irodaviy sifatlarni (jasorat, qat'iyat, chidamlilik) tarbiyalash, jamoaviylik, o'rtoqlik va intizomlilik kabi axloqiy sifatlarni shakllantirish kiradi.",
        "Bu uch guruh vazifalar bir-biri bilan uzviy bog'liq bo'lib, ular birgalikda amalga oshiriladi. Masalan, bola harakatli o'yin o'ynaganda bir vaqtning o'zida sog'lig'i mustahkamlanadi (sog'lomlashtirish), yangi harakatni o'rganadi (ta'limiy) va jamoada o'ynashni o'rganadi (tarbiyaviy). Vazifalarning bunday yaxlitligi jismoniy tarbiyaning samaradorligini ta'minlaydi.",
    ],
    [
        "Bolalar jismoniy tarbiya fanining asosiy tushunchalaridan biri \"jismoniy tarbiya\" tushunchasidir. Jismoniy tarbiya - bu shaxsning jismoniy kamolotiga yo'naltirilgan, harakat ko'nikmalarini shakllantirish va maxsus bilimlarni o'zlashtirishni o'z ichiga olgan pedagogik jarayondir. Jismoniy tarbiya tarbiyaning umumiy tizimining ajralmas qismi bo'lib, u aqliy, axloqiy, estetik va mehnat tarbiyasi bilan uzviy bog'liqdir.",
        "Jismoniy tarbiya ikki muhim tomonni o'z ichiga oladi: jismoniy ta'lim va jismoniy rivojlantirish. Jismoniy ta'lim - bu harakat ko'nikmalari va maxsus bilimlarni o'rgatish jarayoni. Jismoniy rivojlantirish esa - bu jismoniy sifatlarni (kuch, tezkorlik, chidamlilik) maqsadli rivojlantirish jarayoni. Bu ikki tomon birgalikda jismoniy tarbiyaning mohiyatini tashkil etadi.",
        "\"Jismoniy rivojlanish\" tushunchasi jismoniy tarbiyadan farq qiladi. Jismoniy rivojlanish - bu organizmning hayoti davomida ro'y beradigan morfologik va funksional o'zgarishlar jarayoni va natijasidir. U inson tanasining shakllanishi, o'sishi va o'zgarishini anglatadi. Jismoniy rivojlanish bo'y uzunligi, tana vazni, ko'krak qafasi aylanasi kabi antropometrik ko'rsatkichlar bilan o'lchanadi.",
        "Jismoniy rivojlanish uch omil ta'sirida kechadi: irsiyat (genetik omillar), atrof-muhit (ijtimoiy va tabiiy sharoitlar) va jismoniy tarbiya (maqsadli pedagogik ta'sir). Bulardan jismoniy tarbiya eng faol va boshqariladigan omil bo'lib, u jismoniy rivojlanishni to'g'ri yo'naltirish imkonini beradi.",
        "Shunday qilib, jismoniy tarbiya va jismoniy rivojlanish o'zaro bog'liq, lekin turli tushunchalardir. Jismoniy tarbiya - bu maqsadli pedagogik jarayon, jismoniy rivojlanish esa - bu organizmdagi tabiiy o'zgarishlar natijasi. To'g'ri tashkil etilgan jismoniy tarbiya bolaning jismoniy rivojlanishini ijobiy yo'nalishda boshqaradi va uning uyg'un kamol topishini ta'minlaydi.",
    ],
    [
        "\"Jismoniy tayyorgarlik\" - bolalar jismoniy tarbiya fanining yana bir muhim tushunchasidir. Jismoniy tayyorgarlik - bu jismoniy tarbiya jarayonida erishilgan natija bo'lib, u shaxsning harakat ko'nikmalari darajasi va jismoniy sifatlarining rivojlanganlik holatini ifodalaydi. Boshqacha aytganda, jismoniy tayyorgarlik - bu bolaning muayyan harakat faoliyatini bajara olish qobiliyatidir.",
        "Jismoniy tayyorgarlik ikki turga bo'linadi: umumiy va maxsus. Umumiy jismoniy tayyorgarlik - bu shaxsning har tomonlama jismoniy rivojlanishini ta'minlovchi, barcha asosiy jismoniy sifatlar va harakat ko'nikmalarini o'z ichiga olgan tayyorgarlik. Maxsus jismoniy tayyorgarlik esa - bu muayyan sport turi yoki faoliyatga yo'naltirilgan tayyorgarlik. Maktabgacha yoshda asosan umumiy jismoniy tayyorgarlik shakllantiriladi.",
        "\"Jismoniy kamolot\" tushunchasi shaxsning jismoniy rivojlanishining yuqori darajasini ifodalaydi. Jismoniy kamolot - bu inson sog'lig'i, jismoniy sifatlari va harakat imkoniyatlarining uyg'un va to'liq rivojlanganlik holatidir. Jismoniy kamolotga erishgan inson sog'lom, baquvvat, chidamli va harakatchan bo'ladi.",
        "Jismoniy kamolot tarixiy tushuncha bo'lib, uning mezonlari jamiyat taraqqiyoti bilan o'zgarib boradi. Har bir tarixiy davrda jismoniy kamolotning o'ziga xos talablari mavjud bo'lgan. Zamonaviy tushunchada jismoniy kamolot nafaqat kuchli tana, balki sog'lom turmush tarzi, harakat madaniyati va o'z sog'lig'iga ongli munosabatni ham o'z ichiga oladi.",
        "Jismoniy tayyorgarlik va jismoniy kamolot o'zaro bog'liq tushunchalardir. Jismoniy tayyorgarlik - bu muayyan vaqtdagi holatni ifodalovchi natija bo'lsa, jismoniy kamolot - bu jismoniy rivojlanishning umumiy yuqori darajasini bildiruvchi keng tushunchadir. Bolaning jismoniy tayyorgarligini muntazam oshirib borish uni jismoniy kamolotga olib boradi.",
    ],
    [
        "\"Jismoniy mashq\" - bolalar jismoniy tarbiya fanining markaziy tushunchalaridan biridir. Jismoniy mashq - bu jismoniy tarbiya qonuniyatlariga muvofiq tanlangan va maxsus maqsad bilan bajariladigan harakat faoliyatidir. Jismoniy mashq jismoniy tarbiyaning asosiy vositasi bo'lib, u orqali bolaning harakat ko'nikmalari shakllantiriladi va jismoniy sifatlari rivojlantiriladi.",
        "Jismoniy mashqlar bir nechta turlarga bo'linadi. Gimnastika mashqlari - umumrivojlantiruvchi mashqlar, asosiy harakatlar, qurilish mashqlari. O'yinlar - harakatli va sport o'yinlari. Sport mashqlari - changida yurish, velosipedda yurish, suzish elementlari. Turistik mashqlar - piyoda sayohatlar. Har bir tur o'ziga xos ta'sir ko'rsatadi va bolaning yoshi va imkoniyatlariga qarab tanlanadi.",
        "Jismoniy mashqning samaradorligi bir qator omillarga bog'liq: mashq texnikasining to'g'riligi, yuklamaning dozasi (takrorlash soni, intensivlik, davomiylik), mashqlar orasidagi dam olish va bolaning individual xususiyatlari. Tarbiyachi bu omillarni hisobga olgan holda mashqlarni tanlaydi va dozalaydi.",
        "\"Harakat faolligi\" tushunchasi bolaning kun davomidagi barcha harakatlari yig'indisini ifodalaydi. Harakat faolligi - bu inson hayot faoliyatining tabiiy biologik ehtiyojidir. Maktabgacha yoshdagi bola uchun yetarli harakat faolligi uning normal o'sishi, rivojlanishi va sog'lig'i uchun zarurdir. Harakat faolligining yetishmasligi (gipodinamiya) bolaning sog'lig'iga salbiy ta'sir ko'rsatadi.",
        "Harakat faolligi tashkil etilgan (mashg'ulotlar, gimnastika, o'yinlar) va mustaqil (bolaning erkin harakatlari) turlarga bo'linadi. Tarbiyachining vazifasi bolaning kun davomidagi harakat faolligini optimal darajada ta'minlashdir. Bu jismoniy mashqlar, harakatli o'yinlar va erkin faoliyat orqali amalga oshiriladi. Jismoniy mashq va harakat faolligi tushunchalari bolaning jismoniy tarbiyasining amaliy asosini tashkil etadi.",
    ],
    [
        "Bolalar jismoniy tarbiya fani mustaqil fan sifatida boshqa ko'plab fanlar bilan chambarchas bog'liqdir. Bu aloqadorlik fanning interdistsiplinar xarakterini belgilaydi va uning ilmiy asosini boyitadi. Avvalo, jismoniy tarbiya fani anatomiya va fiziologiya fanlari bilan bog'liq. Bu fanlar bolaning tana tuzilishi, organlar va tizimlarning ishlash mexanizmlari hamda yosh xususiyatlari haqida bilim beradi.",
        "Anatomiya va fiziologiya bilimlari jismoniy mashqlarni to'g'ri tanlash va dozalashda zarurdir. Tarbiyachi bolaning suyak-mushak tizimi, yurak-qon tomir va nafas tizimlarining yosh xususiyatlarini bilmasdan turib, to'g'ri jismoniy yuklamani belgilay olmaydi. Gigiyena fani esa sog'lom muhit, to'g'ri kun tartibi va chiniqtirish qoidalarini belgilaydi.",
        "Jismoniy tarbiya fani psixologiya bilan ham uzviy bog'liq. Psixologiya bolaning harakat faoliyatiga bo'lgan motivatsiyasini, qiziqishlarini, emotsional holatini va harakat ko'nikmalarini o'zlashtirish jarayonlarini tushunishga yordam beradi. Bolaning yosh psixologik xususiyatlarini bilish mashg'ulotlarni qiziqarli va samarali tashkil etish imkonini beradi.",
        "Pedagogika fani jismoniy tarbiyaning umumiy nazariy asosini tashkil etadi. Didaktika tamoyillari, ta'lim va tarbiya usullari, pedagogik jarayonni tashkil etish qonuniyatlari jismoniy tarbiyada ham qo'llaniladi. Jismoniy tarbiya umumiy pedagogikaning bir qismi sifatida uning barcha qonuniyatlariga bo'ysunadi.",
        "Shuningdek, jismoniy tarbiya fani biomexanika (harakatlarning mexanik qonuniyatlari), tibbiyot (sog'liqni saqlash), valeologiya (sog'lom turmush tarzi) va sport nazariyasi bilan ham bog'liqdir. Bu fanlar bilan aloqadorlik jismoniy tarbiya fanining ilmiy asosini mustahkamlaydi va uni amaliy jihatdan boyitadi. Tarbiyachi bu fanlarning asosiy bilimlaridan xabardor bo'lishi kerak.",
    ],
    [
        "Bolalar jismoniy tarbiya fanining maktabgacha ta'limdagi ahamiyati nihoyatda katta. Avvalo, jismoniy tarbiya bolaning sog'lig'ini mustahkamlash va kasalliklarning oldini olishda muhim rol o'ynaydi. Muntazam jismoniy mashqlar bolaning immunitetini kuchaytiradi, organizmni chiniqtiradi va uni turli kasalliklardan himoya qiladi. Sog'lom bola esa faol o'rganadi va har tomonlama rivojlanadi.",
        "Jismoniy tarbiya bolaning to'g'ri jismoniy rivojlanishini ta'minlaydi. Maktabgacha yoshda bolaning suyak-mushak tizimi faol shakllanadi. To'g'ri tanlangan jismoniy mashqlar to'g'ri gavda holatini shakllantiradi, mushaklarni mustahkamlaydi va organizmning uyg'un rivojlanishini ta'minlaydi. Bu kelajakda bolaning sog'lig'i uchun mustahkam asos yaratadi.",
        "Jismoniy tarbiyaning yana bir muhim ahamiyati - u bolaning aqliy rivojlanishiga ijobiy ta'sir ko'rsatadi. Ilmiy tadqiqotlar harakat faolligi va miya faoliyati orasidagi mustahkam aloqani isbotlagan. Harakatli bola yaxshiroq fikrlaydi, e'tiborini jamlaydi va yangi bilimlarni tezroq o'zlashtiradi. Ayniqsa, mayda motorikani rivojlantiruvchi mashqlar nutq va tafakkur rivojlanishiga bog'liqdir.",
        "Jismoniy tarbiya bolaning ijtimoiy va axloqiy rivojlanishiga ham hissa qo'shadi. Jamoaviy o'yinlar va mashg'ulotlar jarayonida bola hamkorlik qilishni, qoidalarga rioya qilishni, o'z navbatini kutishni va g'alaba hamda mag'lubiyatni qabul qilishni o'rganadi. Irodaviy sifatlar - qat'iyat, chidamlilik, jasorat - ham jismoniy tarbiya jarayonida shakllanadi.",
        "Nihoyat, jismoniy tarbiya bolada sog'lom turmush tarziga ongli munosabatni shakllantiradi. Bola harakatning, toza havoning, gigiyena qoidalarining ahamiyatini tushunadi va o'z sog'lig'iga g'amxo'rlik qilishni o'rganadi. Bu ko'nikmalar bolaning butun hayoti davomida zarur bo'ladi. Shu sababli jismoniy tarbiya maktabgacha ta'limning ajralmas va muhim qismi hisoblanadi.",
    ],
    [
        "Mazkur mustaqil ishda bolalar jismoniy tarbiya fanining predmeti va asosiy tushunchalari har tomonlama tahlil qilindi. Tahlillar shuni ko'rsatdiki, bu fan mustaqil pedagogik fan bo'lib, uning aniq predmeti, maqsad va vazifalari hamda asosiy tushunchalar tizimi mavjud.",
        "Fanning predmeti - maktabgacha yoshdagi bolalarning jismoniy tarbiyasi pedagogik jarayoni bo'lib, u harakat ko'nikmalarini shakllantirish, jismoniy sifatlarni rivojlantirish va sog'lig'ini mustahkamlashni o'z ichiga oladi. Fanning vazifalari sog'lomlashtirish, ta'limiy va tarbiyaviy guruhlarga bo'linadi.",
        "Fanning asosiy tushunchalari - jismoniy tarbiya, jismoniy rivojlanish, jismoniy tayyorgarlik, jismoniy kamolot, jismoniy mashq va harakat faolligi - o'zaro bog'liq bo'lib, ular fanning ilmiy poydevorini tashkil etadi. Bu tushunchalarni to'g'ri tushunish jismoniy tarbiya jarayonini ilmiy asosda tashkil etish imkonini beradi.",
        "Xulosa qilib aytganda, bolalar jismoniy tarbiya fanining predmeti va asosiy tushunchalarini chuqur o'rganish har bir tarbiyachi uchun kasbiy zaruratdir. Bu bilimlar tarbiyachiga jismoniy tarbiya jarayonini ilmiy asosda, samarali va bolaning yosh xususiyatlariga mos tarzda tashkil etish imkonini beradi. Fan boshqa fanlar bilan uzviy bog'liq bo'lib, uning maktabgacha ta'limdagi ahamiyati beqiyosdir.",
        "Foydalanilgan adabiyotlar:",
        "1. O'zbekiston Respublikasining \"Jismoniy tarbiya va sport to'g'risida\"gi Qonuni. - Toshkent, 2015.",
        "2. \"Ilk qadam\" maktabgacha ta'lim muassasalarining Davlat o'quv dasturi. - Toshkent, 2018.",
        "3. Xolmatov A. \"Bolalar jismoniy tarbiyasi nazariyasi va metodikasi\". - Toshkent, 2020.",
        "4. Abdullayev B. \"Maktabgacha yoshdagi bolalarning jismoniy tarbiyasi\". - Toshkent, 2021.",
        "5. Stepanenkova E.Ya. \"Teoriya i metodika fizicheskogo vospitaniya i razvitiya rebyonka\". - Moskva, 2018.",
        "6. Xolodov J.K., Kuznetsov V.S. \"Teoriya i metodika fizicheskoy kultury i sporta\". - Moskva, 2017.",
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
body.append(make_para("Bolalar jismoniy tarbiya fanining predmeti va asosiy tushunchalari", bold=True, size=28, align="center"))
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
core_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Mustaqil ish - Jismoniy tarbiya predmeti</dc:title><dc:creator>Talaba</dc:creator></cp:coreProperties>'
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
