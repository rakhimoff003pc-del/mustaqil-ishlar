#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mustaqil ish: Maktabgacha ta'lim tashkilotlarida musiqaviy tarbiyaning
maqsad va vazifalari
"""
import os, zipfile
from xml.sax.saxutils import escape

OUT = "/projects/sandbox/mustaqil-ishlar/Musiqaviy_tarbiya_maqsad_vazifa.docx"

PLAN = [
    "Kirish",
    "Musiqaviy tarbiya tushunchasi va uning mohiyati",
    "Maktabgacha ta'limda musiqaviy tarbiyaning maqsadi",
    "Musiqaviy tarbiyaning asosiy vazifalari",
    "Musiqaviy tarbiyaning bola rivojlanishidagi ahamiyati",
    "Musiqaviy faoliyat turlari",
    "Musiqaviy tarbiyani tashkil etish shakllari va vositalari",
    "Musiqa rahbari va tarbiyachining roli",
    "Xulosa va foydalanilgan adabiyotlar",
]

SECTIONS = [
    [
        "Musiqa - inson hayotining ajralmas qismi bo'lib, u kishining his-tuyg'ulariga ta'sir ko'rsatadigan, uni ma'naviy boyitadigan va estetik jihatdan tarbiyalaydigan qudratli vositadir. Maktabgacha yoshdagi bolalarning musiqaviy tarbiyasi ularning har tomonlama va uyg'un rivojlanishida muhim o'rin tutadi. Aynan bolalik davrida musiqaga muhabbat, badiiy did va estetik tuyg'ular shakllana boshlaydi.",
        "Musiqaviy tarbiya maktabgacha ta'limning muhim tarkibiy qismlaridan biri bo'lib, u bolaning hissiy, aqliy, axloqiy va jismoniy rivojlanishiga ijobiy ta'sir ko'rsatadi. Musiqa orqali bola go'zallikni his qilishni, o'z hissiyotlarini ifodalashni va atrofdagi olamni nozik idrok etishni o'rganadi. Shu sababli musiqaviy tarbiyaning maqsad va vazifalarini to'g'ri belgilash katta ahamiyatga ega.",
        "Mazkur mustaqil ishda maktabgacha ta'lim tashkilotlarida musiqaviy tarbiyaning maqsad va vazifalari batafsil yoritiladi. Ishda musiqaviy tarbiyaning mohiyati, maqsadi, asosiy vazifalari, bola rivojlanishidagi ahamiyati, musiqaviy faoliyat turlari, tashkil etish shakllari hamda musiqa rahbari va tarbiyachining roli tahlil qilinadi. Mavzuning dolzarbligi shundaki, to'g'ri tashkil etilgan musiqaviy tarbiya bolaning estetik kamoloti uchun mustahkam asos yaratadi.",
    ],
    [
        "Musiqaviy tarbiya - bu bolaning musiqaviy qobiliyatlarini rivojlantirish, unda musiqaga muhabbat va qiziqish uyg'otish hamda musiqa vositasida uni estetik jihatdan tarbiyalashga yo'naltirilgan pedagogik jarayondir. Musiqaviy tarbiya umumiy estetik tarbiyaning ajralmas qismi bo'lib, u bolaning badiiy didini va go'zallikni his qilish tuyg'usini shakllantiradi.",
        "Musiqaviy tarbiyaning mohiyati shundan iboratki, u bolani nafaqat musiqa tinglashga va kuylashga o'rgatadi, balki uning shaxsini har tomonlama boyitadi. Musiqa bolaning hissiy olamiga ta'sir ko'rsatib, unda nozik tuyg'ular, kechinmalar va emotsional sezgirlikni shakllantiradi. Bola musiqa orqali quvonch, qayg'u, tantanavorlik kabi turli hissiyotlarni his qilishni o'rganadi.",
        "Musiqaviy tarbiya bolaning musiqaviy qobiliyatlarini rivojlantiradi. Bu qobiliyatlarga musiqaviy eshitish (ladovoy his), ritm hissi va musiqaviy xotira kiradi. Musiqaviy eshitish - bu tovushlarning balandligini farqlash qobiliyati. Ritm hissi - musiqaning ritmik tuzilishini his qilish va unga harakat bilan javob berish. Musiqaviy xotira - kuy va qo'shiqlarni eslab qolish qobiliyatidir.",
        "Musiqaviy tarbiya tarixiy va ijtimoiy hodisa bo'lib, har bir xalqning o'ziga xos musiqaviy madaniyati va an'analari mavjud. O'zbek xalqining boy musiqaviy merosi - allalar, bolalar qo'shiqlari, xalq kuylari va cholg'u asboblari - bolaning milliy musiqaviy tarbiyasida muhim manba bo'lib xizmat qiladi. Shu bilan birga, bola jahon musiqa madaniyati namunalari bilan ham tanishtiriladi.",
    ],
    [
        "Maktabgacha ta'lim tashkilotlarida musiqaviy tarbiyaning bosh maqsadi - bolada musiqaga muhabbat va qiziqish uyg'otish, uning musiqaviy qobiliyatlarini rivojlantirish, musiqaviy madaniyat asoslarini shakllantirish va musiqa vositasida uni estetik jihatdan tarbiyalashdir. Bu maqsad bolaning butun maktabgacha davridagi musiqaviy tarbiyasining umumiy yo'nalishini belgilaydi.",
        "Maqsadning birinchi jihati - bolada musiqaga emotsional munosabat va muhabbat shakllantirishdir. Bola musiqani tinglashdan zavqlanishi, unga qiziqishi va musiqaviy faoliyatda ishtirok etishni xohlashi kerak. Musiqaga muhabbat bolaning butun hayoti davomida uni hamroh bo'ladigan ma'naviy boylik hisoblanadi.",
        "Maqsadning ikkinchi jihati - bolaning musiqaviy qobiliyatlarini ro'yobga chiqarish va rivojlantirishdir. Har bir bola muayyan darajada musiqaviy qobiliyatga ega bo'ladi va to'g'ri tashkil etilgan musiqaviy tarbiya bu qobiliyatlarni rivojlantirishga imkon beradi. Iste'dodli bolalar esa maxsus e'tibor va qo'llab-quvvatlashga muhtoj bo'ladi.",
        "Maqsadning uchinchi jihati - bolada musiqaviy madaniyat asoslarini shakllantirishdir. Bu bolaning musiqa asarlarini idrok etish, ularni tushunish va baholash, turli janr va xarakterdagi musiqani farqlash qobiliyatini o'z ichiga oladi. Bola xalq musiqasi, klassik musiqa va zamonaviy bolalar musiqasi bilan tanishadi.",
        "Maqsadning to'rtinchi jihati - musiqa vositasida bolaning shaxsini har tomonlama tarbiyalashdir. Musiqa bolaning estetik, axloqiy, aqliy va jismoniy rivojlanishiga ijobiy ta'sir ko'rsatadi. Shunday qilib, musiqaviy tarbiyaning maqsadi keng qamrovli bo'lib, u bolani musiqa olamiga olib kirish va uning shaxsini boyitishga qaratilgan.",
    ],
    [
        "Maktabgacha ta'limda musiqaviy tarbiyaning vazifalari bosh maqsaddan kelib chiqqan holda aniq belgilangan. Birinchi vazifa - bolada musiqaga qiziqish va muhabbatni tarbiyalash. Bu vazifa bolaning musiqa tinglashga, kuylashga va musiqaviy faoliyatda ishtirok etishga bo'lgan ishtiyoqini shakllantirishni o'z ichiga oladi. Musiqaga qiziqish barcha musiqaviy faoliyatning asosi hisoblanadi.",
        "Ikkinchi vazifa - bolaning musiqaviy qobiliyatlarini rivojlantirish. Bu vazifa musiqaviy eshitishni, ritm hissini va musiqaviy xotirani maxsus mashqlar va faoliyat orqali rivojlantirishni nazarda tutadi. Bola tovushlarni balandligi, davomiyligi va tembri bo'yicha farqlashni o'rganadi.",
        "Uchinchi vazifa - bolada musiqaviy bilim va ko'nikmalarni shakllantirish. Bola musiqa haqida dastlabki tushunchalarga ega bo'ladi: kuy, ritm, temp, dinamika, musiqa xarakteri. Shuningdek, u to'g'ri kuylash, ritmga mos harakatlanish va oddiy cholg'u asboblarida chalish ko'nikmalarini egallaydi.",
        "To'rtinchi vazifa - bolaning ijodiy qobiliyatlarini rivojlantirish. Musiqaviy tarbiya bolada ijodiy tashabbusni rag'batlantiradi: o'z kuyini to'qish, harakatlar o'ylab topish, musiqaga mos improvizatsiya qilish. Bu bolaning ijodiy salohiyatini ro'yobga chiqaradi.",
        "Beshinchi vazifa - musiqa orqali bolani estetik va axloqiy jihatdan tarbiyalash. Bola musiqa orqali go'zallikni his qilishni, ezgu tuyg'ularni o'zida shakllantirishni o'rganadi. Oltinchi vazifa - milliy musiqaviy meros bilan tanishtirish. Bola o'zbek xalq qo'shiqlari, allalar va cholg'u asboblari bilan tanishib, milliy musiqaviy madaniyatga muhabbat hissini shakllantiradi.",
    ],
    [
        "Musiqaviy tarbiya bolaning rivojlanishida ko'p qirrali ahamiyatga ega. Avvalo, musiqa bolaning hissiy-emotsional rivojlanishiga kuchli ta'sir ko'rsatadi. Musiqa orqali bola o'z his-tuyg'ularini ifodalashni va boshqalarning hissiyotlarini tushunishni o'rganadi. Musiqa bolaning emotsional olamini boyitadi, unda nozik tuyg'ular va kechinmalarni shakllantiradi.",
        "Musiqaviy tarbiya bolaning aqliy rivojlanishiga ham ijobiy ta'sir ko'rsatadi. Musiqa tinglash va idrok etish jarayonida bolaning diqqati, xotirasi va tafakkuri rivojlanadi. Bola musiqani tahlil qilishni, taqqoslashni va xulosa chiqarishni o'rganadi. Ilmiy tadqiqotlar musiqa mashg'ulotlari bolaning matematik va til qobiliyatlariga ham ijobiy ta'sir ko'rsatishini isbotlagan.",
        "Musiqaviy tarbiya bolaning nutqiy rivojlanishi bilan uzviy bog'liqdir. Qo'shiq kuylash bolaning talaffuzini, nutq nafasini va lug'at boyligini rivojlantiradi. Qo'shiq matnlari orqali bola yangi so'zlar o'rganadi, to'g'ri talaffuz qilishni mashq qiladi. Ritmik mashqlar esa fonematik eshitishni rivojlantirib, savodxonlikka tayyorgarlikka yordam beradi.",
        "Musiqaviy tarbiya bolaning jismoniy rivojlanishiga ham hissa qo'shadi. Musiqaga mos harakatlar, raqs va ritmik gimnastika bolaning harakat koordinatsiyasini, chaqqonligini va plastikligini rivojlantiradi. Musiqa jo'natmasida bajarilgan jismoniy mashqlar bolaga qiziqarli bo'lib, uning harakat faolligini oshiradi.",
        "Bundan tashqari, musiqaviy tarbiya bolaning ijtimoiy va axloqiy rivojlanishiga ta'sir ko'rsatadi. Jamoaviy kuylash, raqs va musiqaviy o'yinlar bolada hamkorlik, jamoaviylik va o'zaro hurmat tuyg'ularini shakllantiradi. Bola o'z navbatini kutishni, boshqalar bilan uyg'un harakat qilishni va birgalikda go'zal natijaga erishishni o'rganadi. Shunday qilib, musiqaviy tarbiya bolaning barcha rivojlanish sohalariga ijobiy ta'sir ko'rsatadi.",
    ],
    [
        "Maktabgacha ta'lim tashkilotlarida musiqaviy tarbiya turli faoliyat turlari orqali amalga oshiriladi. Birinchi va asosiy faoliyat turi - musiqa tinglash. Bu faoliyatda bola turli xarakterdagi musiqa asarlarini tinglaydi, ularni idrok etadi va his qiladi. Musiqa tinglash bolaning musiqaviy didini shakllantiradi va musiqani tushunishga o'rgatadi. Tarbiyachi bolalarga musiqaning xarakteri va mazmuni haqida tushuntiradi.",
        "Ikkinchi faoliyat turi - qo'shiq kuylash (vokal faoliyat). Qo'shiq kuylash bolalarning eng sevimli musiqaviy faoliyati hisoblanadi. Kuylash jarayonida bolaning ovozi, musiqaviy eshitishi va nafasi rivojlanadi. Bola yakka va jamoa bo'lib kuylashni o'rganadi. Qo'shiqlar bolaning yoshiga mos, oddiy kuyli va tushunarli matnli bo'lishi kerak.",
        "Uchinchi faoliyat turi - musiqaviy-ritmik harakatlar. Bu faoliyatga raqslar, musiqaviy o'yinlar va ritmik mashqlar kiradi. Bola musiqaga mos harakat qilishni, uning ritmini, tempini va xarakterini harakat orqali ifodalashni o'rganadi. Musiqaviy-ritmik harakatlar bolaning plastikligini va harakat koordinatsiyasini rivojlantiradi.",
        "To'rtinchi faoliyat turi - bolalar cholg'u asboblarida chalish. Bolalar metallofon, baraban, qo'ng'iroqcha, marakas kabi oddiy cholg'u asboblarida chalishni o'rganadi. Bu faoliyat bolaning ritm hissini, mayda motorikasini va musiqaviy xotirasini rivojlantiradi. Bolalar cholg'u orkestri tashkil etilib, jamoaviy ijro mashq qilinadi.",
        "Beshinchi faoliyat turi - musiqaviy ijodkorlik. Bu faoliyatda bola o'z kuyini to'qiydi, harakatlar o'ylab topadi va improvizatsiya qiladi. Musiqaviy ijodkorlik bolaning ijodiy salohiyatini ro'yobga chiqaradi. Bu besh faoliyat turi birgalikda bolaning har tomonlama musiqaviy rivojlanishini ta'minlaydi va musiqaviy tarbiyaning maqsadiga erishishga xizmat qiladi.",
    ],
    [
        "Maktabgacha ta'lim tashkilotlarida musiqaviy tarbiya turli tashkiliy shakllar orqali amalga oshiriladi. Birinchi va asosiy shakl - musiqa mashg'uloti. Bu musiqa rahbari tomonidan haftada ikki marta o'tkaziladigan maxsus mashg'ulot bo'lib, unda barcha musiqaviy faoliyat turlari - tinglash, kuylash, ritmik harakatlar va cholg'uda chalish - uyg'unlashtirilgan holda olib boriladi.",
        "Ikkinchi shakl - bayramlar va o'yin-kulgilar. Maktabgacha ta'lim muassasalarida turli bayramlar - Yangi yil, Navro'z, 8-mart, Mustaqillik kuni - musiqaviy dasturlar bilan o'tkaziladi. Bayramlarda bolalar kuylaydi, raqsga tushadi va musiqaviy sahna ko'rinishlarini namoyish etadi. Bayramlar bolaning musiqaviy tajribasini boyitadi va unga quvonch bag'ishlaydi.",
        "Uchinchi shakl - kundalik hayotda musiqadan foydalanish. Musiqa bolaning kundalik faoliyatiga - ertalabki gimnastika, sayr, o'yin va dam olish vaqtlariga - kiritiladi. Tinch musiqa bolani tinchlantiradi, quvnoq musiqa esa uning kayfiyatini ko'taradi. Bu musiqaning bola hayotidagi tabiiy o'rnini ta'minlaydi.",
        "Musiqaviy tarbiya vositalari ham xilma-xildir. Birinchi vosita - musiqa asarlari: xalq qo'shiqlari, bolalar qo'shiqlari, klassik musiqa namunalari, instrumental asarlar. Ikkinchi vosita - musiqa asboblari: pianino, bolalar cholg'u asboblari, milliy cholg'ular. Uchinchi vosita - texnik vositalar: audio va video yozuvlar, musiqa markazi, multimedia jihozlari.",
        "To'rtinchi vosita - ko'rgazmali materiallar: rasmlar, qo'g'irchoqlar, niqoblar, raqs uchun atributlar. Beshinchi vosita - musiqa zali va uning jihozlari. Maktabgacha ta'lim muassasasida maxsus musiqa zali bo'lib, u barcha zarur jihozlar bilan ta'minlangan bo'lishi kerak. Bu vositalarning to'g'ri tanlanishi va qo'llanilishi musiqaviy tarbiyaning samaradorligini oshiradi.",
    ],
    [
        "Maktabgacha ta'lim tashkilotlarida musiqaviy tarbiyani amalga oshirishda musiqa rahbari va tarbiyachining roli hal qiluvchi ahamiyatga ega. Musiqa rahbari - bu maxsus musiqaviy ma'lumotga ega bo'lgan mutaxassis bo'lib, u musiqaviy tarbiyaning asosiy tashkilotchisi hisoblanadi. U musiqa mashg'ulotlarini rejalashtiradi va o'tkazadi, bayramlarni tayyorlaydi va bolalarning musiqaviy rivojlanishini ta'minlaydi.",
        "Musiqa rahbarining birinchi vazifasi - musiqa mashg'ulotlarini ilmiy asosda rejalashtirish va o'tkazish. U bolalarning yosh xususiyatlarini hisobga olgan holda repertuar tanlaydi, mashg'ulot mazmunini belgilaydi va mos usullarni qo'llaydi. Musiqa rahbari o'z sohasini mukammal bilishi, cholg'u asbobida chala olishi va yaxshi ovozga ega bo'lishi kerak.",
        "Musiqa rahbarining ikkinchi vazifasi - har bir bolaning musiqaviy qobiliyatlarini aniqlash va rivojlantirish. U iste'dodli bolalarni aniqlaydi va ularga alohida e'tibor beradi. Shuningdek, musiqaviy rivojlanishida qiyinchilik chekayotgan bolalar bilan ham individual ishlaydi.",
        "Tarbiyachining roli ham musiqaviy tarbiyada muhimdir. Tarbiyachi musiqa rahbari bilan hamkorlik qiladi, musiqa mashg'ulotlarida faol ishtirok etadi va o'rganilgan qo'shiq hamda raqslarni guruhda mustahkamlaydi. Tarbiyachi kundalik hayotda musiqadan foydalanadi va bolalarning musiqaviy tajribasini boyitadi.",
        "Tarbiyachi shuningdek bolalarning musiqaga qiziqishini qo'llab-quvvatlaydi, ularni musiqaviy o'yinlarga undaydi va ota-onalar bilan musiqaviy tarbiya bo'yicha hamkorlik qiladi. Musiqa rahbari va tarbiyachining uyg'un hamkorligi musiqaviy tarbiyaning samaradorligini ta'minlaydi. Ikkala mutaxassis ham o'z kasbiy mahoratini doimiy oshirib borishi va yangi metodlarni o'rganishi kerak.",
    ],
    [
        "Mazkur mustaqil ishda maktabgacha ta'lim tashkilotlarida musiqaviy tarbiyaning maqsad va vazifalari har tomonlama tahlil qilindi. Tahlillar shuni ko'rsatdiki, musiqaviy tarbiya maktabgacha ta'limning muhim tarkibiy qismi bo'lib, u bolaning har tomonlama va uyg'un rivojlanishida katta o'rin tutadi.",
        "Musiqaviy tarbiyaning bosh maqsadi - bolada musiqaga muhabbat uyg'otish, uning musiqaviy qobiliyatlarini rivojlantirish, musiqaviy madaniyat asoslarini shakllantirish va musiqa vositasida uni estetik jihatdan tarbiyalashdir. Bu maqsad aniq belgilangan vazifalar - qiziqish tarbiyalash, qobiliyatlarni rivojlantirish, bilim va ko'nikmalar shakllantirish, ijodkorlikni rag'batlantirish - orqali amalga oshiriladi.",
        "Musiqaviy tarbiya bolaning hissiy, aqliy, nutqiy, jismoniy va ijtimoiy rivojlanishiga ijobiy ta'sir ko'rsatadi. U musiqa tinglash, qo'shiq kuylash, musiqaviy-ritmik harakatlar, cholg'uda chalish va musiqaviy ijodkorlik kabi faoliyat turlari orqali amalga oshiriladi. Musiqa rahbari va tarbiyachining uyg'un hamkorligi bu jarayonning samaradorligini ta'minlaydi.",
        "Xulosa qilib aytganda, musiqaviy tarbiya - bu bolaning ma'naviy olamini boyitadigan, uning estetik didini shakllantiradigan va shaxsini har tomonlama rivojlantiradigan muhim pedagogik jarayondir. To'g'ri tashkil etilgan musiqaviy tarbiya bolaning butun hayoti davomida unga hamroh bo'ladigan go'zallik va musiqaga muhabbat tuyg'usini shakllantiradi.",
        "Foydalanilgan adabiyotlar:",
        "1. O'zbekiston Respublikasining \"Maktabgacha ta'lim va tarbiya to'g'risida\"gi Qonuni. - Toshkent, 2020.",
        "2. \"Ilk qadam\" maktabgacha ta'lim muassasalarining Davlat o'quv dasturi. - Toshkent, 2018.",
        "3. Nazarova M. \"Maktabgacha ta'limda musiqaviy tarbiya metodikasi\". - Toshkent, 2020.",
        "4. Qodirova R. \"Bolalar musiqaviy tarbiyasi\". - Toshkent, 2019.",
        "5. Vetlugina N.A. \"Muzykalnoye vospitaniye v detskom sadu\". - Moskva, 2018.",
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
body.append(make_para("Maktabgacha ta'lim tashkilotlarida musiqaviy tarbiyaning maqsad va vazifalari", bold=True, size=28, align="center"))
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
core_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Mustaqil ish - Musiqaviy tarbiya maqsad vazifalari</dc:title><dc:creator>Talaba</dc:creator></cp:coreProperties>'
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
