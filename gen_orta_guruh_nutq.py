#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mustaqil ish: Maktabgacha ta'lim tashkilotlarida o'rta guruh bolalarining
nutqini o'stirish metodlari va vositalari
"""
import os, zipfile
from xml.sax.saxutils import escape

OUT = "/projects/sandbox/mustaqil-ishlar/Orta_guruh_nutq_metodlari.docx"

PLAN = [
    "Kirish",
    "O'rta guruh bolalarining nutqiy rivojlanish xususiyatlari",
    "O'rta guruhda nutqni o'stirishning maqsad va vazifalari",
    "Lug'at boyligini oshirish metodlari va vositalari",
    "Grammatik to'g'ri nutqni shakllantirish metodlari",
    "Bog'lanishli (dialogik va monologik) nutqni rivojlantirish",
    "Tovush madaniyatini tarbiyalash metodlari va vositalari",
    "Tarbiyachining o'rta guruh bolalari nutqini o'stirishdagi roli",
    "Xulosa va foydalanilgan adabiyotlar",
]

SECTIONS = [
    [
        "Nutq insonning eng muhim muloqot vositasi bo'lib, uning aqliy, ijtimoiy va shaxsiy rivojlanishi bilan uzviy bog'liqdir. Maktabgacha yoshdagi bolalarning nutqini o'stirish pedagogik faoliyatning eng muhim yo'nalishlaridan biri hisoblanadi. O'rta guruh (4-5 yosh) bolaning nutqiy rivojlanishida alohida ahamiyatga ega bo'lgan bosqich bo'lib, bu davrda bolaning nutqi sifat jihatidan keskin o'zgaradi va boyiydi.",
        "O'rta guruh bolalari kichik yoshdagilardan farqli ravishda allaqachon faol gapira oladi, savol bera boshlaydi, tengdoshlari bilan muloqot qiladi va o'z fikrini ifodalashga harakat qiladi. Bu yoshda bolaning lug'ati sezilarli darajada kengayadi, grammatik tuzilmalar murakkablashadi va bog'lanishli nutqning asoslari shakllana boshlaydi. Shu sababli o'rta guruhda nutqni o'stirish ishini to'g'ri tashkil etish katta ahamiyatga ega.",
        "Mazkur mustaqil ishda maktabgacha ta'lim tashkilotlarida o'rta guruh bolalarining nutqini o'stirish metodlari va vositalari batafsil yoritiladi. Ishda bu yosh bolalarining nutqiy rivojlanish xususiyatlari, nutqni o'stirishning maqsad va vazifalari, lug'at ishi, grammatik nutq, bog'lanishli nutq, tovush madaniyati metodlari hamda tarbiyachining roli tahlil qilinadi. Mavzuning dolzarbligi shundaki, o'rta guruhda nutqni samarali rivojlantirish bolani katta guruhga va keyinchalik maktabga tayyorlashning muhim shartidir.",
    ],
    [
        "O'rta guruh (4-5 yosh) bolalarining nutqiy rivojlanishi o'ziga xos xususiyatlarga ega. Bu yoshda bolaning faol lug'ati 2000-2500 so'zga yetadi. Bola nafaqat predmetlar nomini, balki ularning sifatlari, harakatlari, kattalik va vaqt tushunchalarini ham biladi. Lug'at jadal boyib boradi, bola yangi so'zlarning ma'nosiga qiziqadi va ularni faol nutqida qo'llaydi.",
        "Bu yoshda bolaning grammatik nutqi ancha rivojlangan bo'ladi. Bola sodda yoyiq gaplar, qo'shma gaplar tuza oladi. Biroq grammatik xatolar hali uchrab turadi: so'z qo'shimchalarini noto'g'ri qo'llash, qiyin so'z shakllarini xato aytish kabi. Bu yoshga xos bo'lgan o'ziga xos so'z ijodkorligi — bolaning yangi so'zlar to'qib chiqarishi ham kuzatiladi, bu nutqiy rivojlanishning faol jarayonidan dalolat beradi.",
        "O'rta guruh bolasining tovush talaffuzi sezilarli darajada yaxshilanadi. Ko'pchilik tovushlar to'g'ri talaffuz qilinadi, biroq ba'zi murakkab tovushlar — R, L, Sh, J, Ch — hali to'liq shakllanmagan bo'lishi mumkin. Bu yoshda fonematik eshitish, ya'ni tovushlarni farqlash qobiliyati faol rivojlanadi, bu esa keyinchalik savodxonlikka tayyorgarlikning asosi bo'ladi.",
        "Bu yoshda bolaning nutqiy faolligi keskin oshadi. O'rta guruh bolasi nihoyatda ko'p savol beradi — bu \"nima uchun?\" yoshi deb ham ataladi. Bola dunyoni so'z orqali o'rganishga intiladi, hamma narsaning sababini bilishni xohlaydi. Tarbiyachi bu qiziquvchanlikni qo'llab-quvvatlashi va har bir savolga sabr bilan javob berishi kerak.",
        "O'rta guruh bolasining nutqi asta-sekin situativ (vaziyatga bog'liq) nutqdan kontekstli (mustaqil) nutqqa o'ta boshlaydi. Bola endi o'zi ko'rmagan, eshitgan voqealar haqida ham gapira oladi, oddiy hikoya tuza boshlaydi va o'tmish hamda kelajak haqida fikr bildiradi. Shuningdek, bu yoshda dialogik nutq faol rivojlanadi — bola suhbatda faol qatnashadi, savol beradi va javob qaytaradi.",
    ],
    [
        "O'rta guruhda nutqni o'stirishning bosh maqsadi — bolaning nutqini sifat jihatidan takomillashtirish, uning lug'atini boyitish, grammatik to'g'ri nutqni shakllantirish, bog'lanishli nutqni rivojlantirish va tovush madaniyatini tarbiyalashdir. Bu maqsad bolani keyingi bosqich — katta guruhga tayyorlashga yo'naltirilgan.",
        "Birinchi vazifa — lug'at boyligini oshirish. O'rta guruhda bolaning lug'ati nafaqat miqdor jihatidan, balki sifat jihatidan ham boyitiladi. Bola umumlashtiruvchi so'zlar (mebel, idish, transport), antonimlar (katta-kichik, baland-past), sifat va harakat nomlarini o'zlashtiradi. Lug'at ishi bolaning bilim doirasi kengayishi bilan parallel olib boriladi.",
        "Ikkinchi vazifa — grammatik to'g'ri nutqni shakllantirish. Bola so'zlarni to'g'ri turlantirish, kelishik qo'shimchalarini to'g'ri qo'llash, sodda va qo'shma gaplar tuzishni o'rganadi. Uchinchi vazifa — bog'lanishli nutqni rivojlantirish. Bola savollarga to'liq javob berish, o'yinchoq yoki rasm bo'yicha hikoya tuzish, ertaklarni qayta hikoya qilish ko'nikmalarini egallaydi.",
        "To'rtinchi vazifa — nutqning tovush madaniyatini tarbiyalash. Bola barcha tovushlarni to'g'ri talaffuz qilishni, nutq nafasini boshqarishni, ovoz balandligi va tezligini muvofiqlashtirishni, intonatsiyadan to'g'ri foydalanishni o'rganadi. Beshinchi vazifa — badiiy adabiyot bilan tanishtirish. Bola she'rlarni yodlash, ertaklarni tinglash va tushunish, badiiy asar qahramonlariga baho berish ko'nikmalarini egallaydi.",
        "Oltinchi vazifa — nutqiy muloqot madaniyatini tarbiyalash. Bola suhbatdoshni tinglash, so'zini bo'lmaslik, savol berish, iltimos va minnatdorchilik bildirish, salomlashish kabi nutq odoblarini o'zlashtiradi. Bu vazifalar birgalikda bolaning nutqiy kamolotini har tomonlama ta'minlaydi va uni keyingi bosqichga tayyorlaydi.",
    ],
    [
        "Lug'at boyligini oshirish o'rta guruhda nutq o'stirishning eng muhim yo'nalishlaridan biridir. Bu yoshda bolaning lug'ati jadal boyib boradi va tarbiyachining vazifasi bu jarayonni maqsadli ravishda boshqarishdir. Lug'at ishi bolaning faol lug'atini (ishlatadigan so'zlari) va passiv lug'atini (tushunadigan, lekin ishlatmaydigan so'zlari) kengaytirishni o'z ichiga oladi.",
        "Lug'at boyitishning birinchi metodi — kuzatish va ekskursiya. Tarbiyachi bolalarni tabiat, atrofdagi narsalar va hodisalar bilan tanishtiradi va ularning nomlarini o'rgatadi. Masalan, kuzgi sayrda barglarning rangi (sariq, qizil, jigarrang), holati (quruq, ho'l) va harakati (uchadi, tushadi) haqida so'zlar o'rgatiladi. Bevosita kuzatish so'zlarni mustahkam o'zlashtirishga yordam beradi.",
        "Ikkinchi metod — predmetlar va rasmlarni ko'rib o'rganish. Tarbiyachi bolalarga predmetlarni yoki ularning rasmlarini ko'rsatib, ularning nomlari, qismlari, xususiyatlari va vazifalarini o'rgatadi. Didaktik o'yinlar — \"Nima o'zgardi?\", \"Ortiqchasini top\", \"Juftini top\", \"Bu nima?\" — lug'at boyitishning samarali vositasidir.",
        "Uchinchi metod — so'z o'yinlari. \"Aksincha ayt\" (antonimlar), \"Qanaqa?\" (sifatlar), \"Nima qiladi?\" (harakatlar), \"Bittadan ko'p\" (ko'plik) kabi o'yinlar bolaning lug'atini turli yo'nalishlarda boyitadi. Bu o'yinlar bolaga qiziqarli bo'lib, ular o'yin jarayonida yangi so'zlarni tabiiy tarzda o'zlashtiradi.",
        "Lug'at boyitish vositalari sifatida quyidagilar qo'llaniladi: predmetli va syujetli rasmlar, real predmetlar va o'yinchoqlar, didaktik o'yinlar va kartochkalar, badiiy adabiyot (she'r, ertak, hikoya), tabiat burchagi materiallari, mavzuli albomlar va ko'rgazmali plakatlar. Bularning barchasi bolaning lug'atini ko'rgazmali va qiziqarli tarzda boyitishga xizmat qiladi.",
    ],
    [
        "Grammatik to'g'ri nutqni shakllantirish o'rta guruhda muhim vazifalardan biridir. Bu yoshda bolaning nutqi grammatik jihatdan faol shakllanayotgan bo'lib, tarbiyachining vazifasi bolaga so'zlarni to'g'ri qo'llash, gaplarni to'g'ri tuzish ko'nikmalarini amaliy mashqlar orqali singdirishdir. Grammatik nutq maxsus qoidalarni yodlash orqali emas, balki amaliy faoliyat orqali shakllantiriladi.",
        "Grammatik nutqni shakllantirishning birinchi yo'nalishi — so'zlarni to'g'ri o'zgartirish (morfologiya). Bola otlarni kelishiklarda turlantirish, sonlarda o'zgartirish (birlik-ko'plik), fe'llarni zamonlarda qo'llash (o'tgan-hozirgi-kelasi zamon) ko'nikmalarini egallaydi. Bu didaktik o'yinlar orqali amalga oshiriladi: \"Nima yo'q?\", \"Kim bilan?\", \"Kecha, bugun, ertaga\" kabi.",
        "Ikkinchi yo'nalish — gap tuzish (sintaksis). Bola avval sodda gaplar, keyin yoyiq gaplar, so'ng qo'shma gaplar tuzishni o'rganadi. Tarbiyachi savollar orqali bolani to'liq gap tuzishga undaydi. Masalan, \"Mushuk nima qilyapti?\" degan savolga bola \"Uxlayapti\" emas, \"Mushuk gilamda uxlayapti\" deb to'liq javob berishga o'rgatiladi.",
        "Uchinchi yo'nalish — so'z yasash. Bola yangi so'zlar yasashni o'rganadi: kichraytirish shakllari (uy-uycha, kitob-kitobcha), kasb nomlari, sifatlardan so'z yasash. Bu yoshda bolaning o'ziga xos so'z ijodkorligi kuzatiladi va tarbiyachi buni to'g'ri yo'naltirishi kerak.",
        "Grammatik nutqni shakllantirish vositalari: maxsus didaktik o'yinlar va mashqlar, syujetli rasmlar, o'yinchoqlar bilan o'ynaladigan vaziyatli o'yinlar, tarbiyachining to'g'ri nutqi (namuna sifatida) va badiiy adabiyot. Tarbiyachi bolaning grammatik xatolarini to'g'ridan-to'g'ri tuzatmaydi, balki to'g'ri shaklni o'z nutqida takrorlash orqali bolaga namuna ko'rsatadi.",
    ],
    [
        "Bog'lanishli nutq — bolaning o'z fikrini izchil, mantiqiy va mazmunan to'liq ifodalay olish qobiliyatidir. O'rta guruhda bog'lanishli nutqning ikki turi — dialogik (suhbat) va monologik (hikoya) nutq rivojlantiriladi. Bu yosh bog'lanishli nutqning faol shakllanish davri bo'lib, tarbiyachining vazifasi bolaga to'liq va izchil gapirishni o'rgatishdir.",
        "Dialogik nutqni rivojlantirish suhbat metodi orqali amalga oshiriladi. Tarbiyachi bolalar bilan turli mavzularda suhbat o'tkazadi: bolaning oilasi, sevimli o'yinchoqlari, kun davomidagi voqealar haqida. Suhbatda tarbiyachi bolani nafaqat javob berishga, balki o'zi ham savol berishga undaydi. Dialogik nutq bolaning muloqot ko'nikmalarini va nutqiy faolligini oshiradi.",
        "Monologik nutqni rivojlantirishning birinchi usuli — o'yinchoq yoki predmet bo'yicha hikoya tuzish. Tarbiyachi bolaga o'yinchoqni ko'rsatib, uni tasvirlab berishni so'raydi: \"Bu nima? Qanaqa? Rangi qanaqa? U bilan nima qilish mumkin?\" Bola savollarga tayanib, predmet haqida kichik hikoya tuzadi.",
        "Ikkinchi usul — syujetli rasm bo'yicha hikoya tuzish. Tarbiyachi bolalarga syujetli rasmni ko'rsatib, undagi voqeani hikoya qilishni so'raydi. Avval savollar orqali rasm mazmuni ochiladi, keyin bola yaxlit hikoya tuzadi. Uchinchi usul — ertaklarni qayta hikoya qilish. Tarbiyachi qisqa, tanish ertakni aytib beradi va bola uni qayta hikoya qiladi. Bu bolaning xotirasi va izchil nutqini rivojlantiradi.",
        "Bog'lanishli nutqni rivojlantirish vositalari: syujetli rasmlar va rasmlar turkumi, o'yinchoqlar va predmetlar, qo'g'irchoq teatri va sahna ko'rinishlari, badiiy adabiyot (ertaklar, hikoyalar), mnemonik jadvallar (hikoya sxemalari) va bolalarning shaxsiy tajribasi. Bu vositalar bolaga hikoya tuzishda tayanch nuqta bo'lib xizmat qiladi va uning bog'lanishli nutqini bosqichma-bosqich rivojlantiradi.",
    ],
    [
        "Nutqning tovush madaniyatini tarbiyalash o'rta guruhda muhim ahamiyat kasb etadi. Tovush madaniyati deganda barcha nutq tovushlarini to'g'ri talaffuz qilish, nutq nafasini to'g'ri olish, ovoz va sur'atni boshqarish hamda intonatsion ifodalilik tushuniladi. Bu yoshda ko'pchilik tovushlar shakllangan bo'lsa-da, ba'zi murakkab tovushlar ustida maxsus ishlash talab etiladi.",
        "Tovush talaffuzini shakllantirishning asosiy usuli — artikulyatsion gimnastika. Bu til, lab va jag' mushaklarini mustahkamlovchi maxsus mashqlar majmui bo'lib, ular tovushlarni to'g'ri talaffuz qilish uchun artikulyatsion apparatni tayyorlaydi. \"Soatcha\", \"Otcha\", \"Murabbo\", \"Tilni tozalash\" kabi o'yin shaklidagi mashqlar bolalarga qiziqarli bo'ladi.",
        "Ikkinchi usul — nutq nafasini rivojlantirish. To'g'ri nutq nafasi ravon va aniq gapirishning asosidir. \"Shamol\", \"Kapalakni uchir\", \"Sham o'chir\", \"Pufakcha\" kabi nafas mashqlari bolaning nafas olishini kuchaytiradi va nutq nafasini boshqarishga o'rgatadi. Bu mashqlar har kuni qisqa vaqt davomida o'tkaziladi.",
        "Uchinchi usul — fonematik eshitishni rivojlantirish. Bola tovushlarni quloq bilan farqlashni o'rganadi. \"Qaysi tovushni eshitding?\", \"Bir xil tovushli so'zlar\", \"Tovushni top\" kabi o'yinlar fonematik eshitishni rivojlantiradi. Bu keyinchalik savodxonlikka tayyorgarlikning muhim asosi hisoblanadi.",
        "To'rtinchi usul — intonatsion ifodalilikni rivojlantirish. Bola she'rlarni ifodali aytish, ovoz balandligini o'zgartirish (sekin-baland), sur'atni boshqarish (tez-sekin) va hissiyotni ovoz orqali ifodalashni o'rganadi. Vositalar sifatida she'rlar, tez aytishlar, sanash o'yinlari, hayvon ovozlariga taqlid o'yinlari, oyna oldida mashqlar va audio-yozuvlar qo'llaniladi. Tovush madaniyatini tarbiyalash bolaning aniq va ifodali nutqining asosini yaratadi.",
    ],
    [
        "Maktabgacha ta'lim tashkilotlarida o'rta guruh bolalarining nutqini o'stirishda tarbiyachining roli hal qiluvchi ahamiyatga ega. Tarbiyachi nafaqat nutqiy mashg'ulotlarni tashkil etadi, balki kun davomida bolaning nutqiy rivojlanishi uchun qulay muhit yaratadi. Uning nutqi bola uchun asosiy namuna bo'lib xizmat qiladi.",
        "Tarbiyachining birinchi vazifasi — nutqiy mashg'ulotlarni rejalashtirish va o'tkazish. U \"Ilk qadam\" davlat o'quv dasturi asosida nutq o'stirish mashg'ulotlarini tizimli rejalashtiradi, har bir mashg'ulot uchun aniq maqsad qo'yadi, mos metod va vositalarni tanlaydi. Mashg'ulotlar o'rta guruh bolalari uchun 20 daqiqagacha davom etadi va o'yin elementi bilan boyitiladi.",
        "Ikkinchi vazifasi — boy nutqiy muhit yaratish. Tarbiyachi kun davomida bola bilan doimiy muloqotda bo'ladi, har bir rejim jarayonini nutqiy faoliyat bilan boyitadi va bolaning nutqiy faolligini rag'batlantiradi. U bolalarga savol berishni o'rgatadi va ularning qiziquvchanligini qo'llab-quvvatlaydi.",
        "Uchinchi vazifasi — individual yondashuvni amalga oshirish. Tarbiyachi har bir bolaning nutqiy rivojlanish darajasini kuzatadi, nutqiy qiyinchiliklarni aniqlaydi va individual ish olib boradi. Nutqi sust rivojlangan bolalar bilan qo'shimcha mashqlar, nutqi yaxshi rivojlangan bolalar bilan murakkabroq topshiriqlar bajariladi.",
        "To'rtinchi vazifasi — ota-onalar bilan hamkorlik. Tarbiyachi ota-onalarga bolaning nutqiy rivojlanishi haqida ma'lumot beradi, uyda qanday o'yin va mashqlar bajarish mumkinligini tushuntiradi. Beshinchi vazifasi — o'z kasbiy mahoratini doimiy oshirish, yangi metodlarni o'rganish va amaliyotga tatbiq etish. Tarbiyachining mahorati bevosita bolalar nutqining rivojlanishiga ta'sir ko'rsatadi.",
    ],
    [
        "Mazkur mustaqil ishda maktabgacha ta'lim tashkilotlarida o'rta guruh bolalarining nutqini o'stirish metodlari va vositalari har tomonlama tahlil qilindi. Tahlillar shuni ko'rsatdiki, o'rta guruh (4-5 yosh) bolaning nutqiy rivojlanishida muhim bosqich bo'lib, bu davrda nutqning barcha tomonlari faol shakllanadi va boyiydi.",
        "O'rta guruhda nutqni o'stirish to'rt asosiy yo'nalishda olib boriladi: lug'at boyligini oshirish, grammatik to'g'ri nutqni shakllantirish, bog'lanishli nutqni rivojlantirish va tovush madaniyatini tarbiyalash. Har bir yo'nalish o'ziga xos metod va vositalardan foydalanadi, lekin ular birgalikda bolaning nutqiy kamolotini yaxlit ta'minlaydi.",
        "Nutqni o'stirishda ko'rgazmali, og'zaki va amaliy metodlar uyg'unlashtirilgan holda qo'llaniladi. Vositalar sifatida rasmlar, o'yinchoqlar, didaktik o'yinlar, badiiy adabiyot va rivojlantiruvchi muhit ishlatiladi. Eng muhim vosita esa tarbiyachining boy, to'g'ri va ifodali nutqidir.",
        "Xulosa qilib aytganda, o'rta guruh bolalarining nutqini o'stirish — bu tizimli, izchil va ijodiy yondashuvni talab qiluvchi pedagogik jarayondir. Bu jarayonning muvaffaqiyati tarbiyachining mahoratiga, to'g'ri metod va vositalar tanlashiga hamda har bir bolaga individual yondashuviga bog'liq. To'g'ri tashkil etilgan nutqiy ish bolani katta guruhga va keyinchalik maktabga muvaffaqiyatli tayyorlaydi.",
        "Foydalanilgan adabiyotlar:",
        "1. O'zbekiston Respublikasining \"Maktabgacha ta'lim va tarbiya to'g'risida\"gi Qonuni. — Toshkent, 2020.",
        "2. \"Ilk qadam\" maktabgacha ta'lim muassasalarining Davlat o'quv dasturi. — Toshkent, 2018.",
        "3. Sodiqova M. \"Bolalar nutqini o'stirish metodikasi\". — Toshkent, 2019.",
        "4. Raximova D. \"Maktabgacha yoshdagi bolalar nutqini rivojlantirish\". — Toshkent, 2021.",
        "5. Ushakova O.S. \"Razvitiye rechi detey 4-5 let\". — Moskva, 2018.",
        "6. Gerbova V.V. \"Razvitiye rechi v detskom sadu. Srednyaya gruppa\". — Moskva, 2019.",
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
body.append(make_para("Maktabgacha ta'lim tashkilotlarida o'rta guruh bolalarining nutqini o'stirish metodlari va vositalari", bold=True, size=28, align="center"))
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
core_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Mustaqil ish - Orta guruh nutq metodlari</dc:title><dc:creator>Talaba</dc:creator></cp:coreProperties>'
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
