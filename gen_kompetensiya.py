#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mustaqil ish: Maktabgacha yoshdagi bolalarga ta'lim berishda kompetensiyaviy yondashuv
"""
import os, zipfile
from xml.sax.saxutils import escape

OUT = "/projects/sandbox/mustaqil-ishlar/Kompetensiyaviy_yondashuv.docx"

PLAN = [
    "Kirish",
    "Kompetensiya va kompetensiyaviy yondashuv tushunchalari",
    "Kompetensiyaviy yondashuvning ilmiy-nazariy asoslari",
    "Maktabgacha ta'limda kompetensiyaviy yondashuvning maqsad va vazifalari",
    "Maktabgacha yoshdagi bolalarda shakllantirilishi lozim bo'lgan kompetensiyalar",
    "Kompetensiyaviy yondashuvni amalga oshirish usullari va vositalari",
    "Kompetensiyaviy yondashuvda tarbiyachining roli",
    "Kompetensiyaviy yondashuvning amaliy ahamiyati va istiqbollari",
    "Xulosa va foydalanilgan adabiyotlar",
]

SECTIONS = [
    [
        "Bugungi kunda ta'lim tizimida tubdan o'zgarishlar ro'y bermoqda. An'anaviy bilim berishga asoslangan yondashuv o'rniga shaxsning hayotiy ko'nikmalarini shakllantiruvchi zamonaviy yondashuvlar joriy etilmoqda. Ana shunday yondashuvlardan biri kompetensiyaviy yondashuv bo'lib, u ta'lim jarayonining pirovard natijasi sifatida bolaning muayyan faoliyatni mustaqil bajara olish qobiliyatini shakllantirishni ko'zda tutadi.",
        "Kompetensiyaviy yondashuv faqat umumta'lim maktablarida emas, balki maktabgacha ta'lim bosqichida ham muhim ahamiyat kasb etmoqda. Maktabgacha yosh — bolaning shaxsiy sifatlari, ko'nikmalari va qobiliyatlarining asoslari shaklanadigan eng muhim davr hisoblanadi. Aynan shu davrda bolada hayotda zarur bo'ladigan kompetensiyalarning dastlabki asoslari yaratiladi.",
        "Mazkur mustaqil ishda maktabgacha yoshdagi bolalarga ta'lim berishda kompetensiyaviy yondashuvning mohiyati, maqsadi, vazifalari, shakllantirilishi lozim bo'lgan kompetensiyalar, usullari va tarbiyachining roli batafsil yoritiladi. Mavzuning dolzarbligi shundaki, O'zbekiston Respublikasining maktabgacha ta'lim sohasidagi islohotlari kompetensiyaviy yondashuvga asoslangan va bu yondashuv \"Ilk qadam\" davlat o'quv dasturining ham asosiy tamoyillaridan biri hisoblanadi.",
    ],
    [
        "Kompetensiya tushunchasi lotincha \"competentia\" so'zidan olingan bo'lib, \"qodirlik\", \"layoqatlilik\" ma'nolarini anglatadi. Pedagogikada kompetensiya deganda shaxsning muayyan faoliyat sohasida bilim, ko'nikma, malaka va shaxsiy sifatlarni integratsiyalashgan holda qo'llay olish qobiliyati tushuniladi. Ya'ni kompetensiya — faqat bilim emas, balki bilimni amaliyotda qo'llay olish qobiliyatidir.",
        "Kompetensiyaviy yondashuv — bu ta'lim jarayonini shaxsning zarur kompetensiyalarini shakllantirish va rivojlantirishga yo'naltirilgan holda tashkil etishni nazarda tutuvchi pedagogik yondashuvdir. Bu yondashuvda ta'limning pirovard maqsadi shunchaki bilim berish emas, balki bolani hayotiy vaziyatlarda mustaqil harakat qila olishga tayyorlashdir.",
        "Kompetensiyaviy yondashuv an'anaviy bilim yo'naltirilgan yondashuvdan tubdan farq qiladi. An'anaviy yondashuvda asosiy e'tibor bolaga necha so'z bilishi, nechta she'r yodlashi yoki nechtagacha sana olishiga qaratiladi. Kompetensiyaviy yondashuvda esa bola olgan bilimlarini qanday qo'llashi, muammolarni qanday hal etishi va yangi vaziyatlarga qanday moslashishi baholanadi.",
        "Maktabgacha ta'lim kontekstida kompetensiyaviy yondashuv bolaning kundalik hayotida duch keladigan turli vaziyatlarda mustaqil, ongli va samarali harakat qila olish qobiliyatini shakllantirishga qaratilgan. Masalan, bola kiyimlarini mustaqil kiya olishi, tengdoshlari bilan muammoni so'z bilan hal eta olishi, xavfli vaziyatni sezib, to'g'ri harakat qila olishi — bularning barchasi kompetensiyaviy yondashuvning amaliy ifodasi hisoblanadi.",
    ],
    [
        "Kompetensiyaviy yondashuvning ilmiy-nazariy asoslari bir nechta muhim pedagogik va psixologik nazariyalarga tayanadi. Birinchi nazariy asos — faoliyat nazariyasi. L.S. Vigotskiy, A.N. Leontyev va S.L. Rubinshteyn tomonidan ishlab chiqilgan bu nazariyaga ko'ra, shaxs faoliyat jarayonida rivojlanadi. Kompetensiyalar ham faqat faol amaliy faoliyat jarayonida shakllanadi, shunchaki tushuntirish orqali emas.",
        "Ikkinchi nazariy asos — shaxsga yo'naltirilgan ta'lim nazariyasi. Bu nazariyaga ko'ra, ta'lim jarayonining markazida bola turadi. Uning individual xususiyatlari, qiziqishlari, ehtiyojlari va rivojlanish sur'ati hisobga olinadi. Kompetensiyaviy yondashuv ham har bir bolaning shaxsiy imkoniyatlaridan kelib chiqib, unga mos kompetensiyalarni shakllantirishni ko'zda tutadi.",
        "Uchinchi nazariy asos — konstruktivizm nazariyasi. J. Piaje va J. Dyui tomonidan asoslangan bu nazariyaga ko'ra, bola bilimni passiv ravishda qabul qilmaydi, balki uni mustaqil qurib chiqadi. Bola atrof-muhit bilan o'zaro ta'sir jarayonida tajriba to'playdi va shu tajriba asosida o'z bilim va ko'nikmalarini shakllantiradi. Bu kompetensiyaviy yondashuvning asosiy tamoyillaridan biriga mos keladi.",
        "To'rtinchi nazariy asos — \"yaqin rivojlanish zonasi\" konsepsiyasi. L.S. Vigotskiy tomonidan ilgari surilgan bu g'oyaga ko'ra, bola kattalar yordamida o'zi mustaqil bajara olmaydigan vazifalarni ham uddalay oladi. Tarbiyachi bolaga aynan shu zonada yordam berib, uning yangi kompetensiyalarini shakllantirishga ko'maklashadi.",
        "Beshinchi nazariy asos — hayot davomida o'rganish konsepsiyasi. Zamonaviy dunyoda shaxs butun hayoti davomida yangi bilim va ko'nikmalar egallashi zarur. Kompetensiyaviy yondashuv bolada aynan shu — mustaqil o'rganish, yangi vaziyatlarga moslashish va doimiy rivojlanish qobiliyatini shakllantirishga qaratilgan. Bu qobiliyatning asoslari maktabgacha davrda yaratiladi.",
    ],
    [
        "Maktabgacha ta'limda kompetensiyaviy yondashuvning bosh maqsadi — bolada hayotiy vaziyatlarda mustaqil, ongli va samarali harakat qila olish qobiliyatini shakllantirish, uni kelajakdagi ta'lim va hayotga tayyorlashdir. Bu maqsad an'anaviy bilim berishdan farqli ravishda, bolani faqat o'rganishga emas, balki o'rgangan narsalarini amalda qo'llashga o'rgatishni ko'zda tutadi.",
        "Kompetensiyaviy yondashuvning birinchi vazifasi — bolada mustaqillik va tashabbuskorlik kompetensiyasini shakllantirish. Bola o'z kuchi bilan kundalik ishlarni bajara olishi, o'z ehtiyojlarini qondira olishi va yangi faoliyatga o'zi tashabbas ko'rsata olishi kerak. Bu vazifa bolaning o'z-o'ziga ishonchini mustahkamlaydi.",
        "Ikkinchi vazifa — bolada muloqot va hamkorlik kompetensiyasini rivojlantirish. Bola kattalar va tengdoshlari bilan samarali muloqot qila olishi, o'z fikrini ifodalay olishi, boshqalarni tinglashi va jamoada hamkorlik qila olishi kerak. Uchinchi vazifa — bolada muammolarni hal etish kompetensiyasini shakllantirish. Bola kundalik hayotda yuzaga keladigan oddiy muammolarni mustaqil yechim topib hal eta olishi lozim.",
        "To'rtinchi vazifa — bolada bilishga oid kompetensiyalarni rivojlantirish. Bola kuzatish, taqqoslash, tahlil qilish, xulosa chiqarish va mustaqil izlanish ko'nikmalariga ega bo'lishi kerak. Beshinchi vazifa — bolada axloqiy va ijtimoiy kompetensiyalarni shakllantirish. Bola jamiyat qoidalariga rioya qilishi, boshqalarga hurmat bilan munosabatda bo'lishi va o'z xatti-harakatining natijalarini tushunishi kerak.",
        "Oltinchi vazifa — bolada sog'lom turmush tarzi va xavfsizlik kompetensiyasini tarbiyalash. Bola o'z sog'lig'ini asrash, gigiyena qoidalariga rioya qilish va xavfli vaziyatlardan saqlanish ko'nikmalariga ega bo'lishi lozim. Bu vazifalar birgalikda bolani hayotga har tomonlama tayyor shaxs sifatida shakllantirishga xizmat qiladi.",
    ],
    [
        "Maktabgacha yoshdagi bolalarda shakllantirilishi lozim bo'lgan kompetensiyalar bir nechta asosiy guruhlarga bo'linadi. Birinchi guruh — shaxsiy kompetensiyalar. Bularga bolaning o'zini anglashi, o'z kuchli va zaif tomonlarini bilishi, mustaqillik, o'z-o'ziga xizmat qilish, o'z his-tuyg'ularini boshqarish va o'ziga ishonch hissi kiradi. Bola o'zi kim ekanligini, nimani xohlashini va nimaga qodir ekanligini bilishi kerak.",
        "Ikkinchi guruh — ijtimoiy kompetensiyalar. Bularga boshqalar bilan muloqot qilish, hamkorlikda ishlash, nizolarni tinch yo'l bilan hal etish, boshqalarning his-tuyg'ularini tushunish, navbat kutish, iltimos va minnatdorchilik bildirish, kattalarning ko'rsatmalariga rioya qilish va jamoa qoidalariga bo'ysunish kiradi.",
        "Uchinchi guruh — bilish kompetensiyalari. Bularga kuzatish va taqqoslash, sabab-natija aloqalarini tushunish, mantiqiy fikrlash, muammoni aniqlash va yechim izlash, yangi bilimlarni mustaqil izlash, savollar berish va tajriba o'tkazish qobiliyatlari kiradi. Bu kompetensiyalar bolaning aqliy rivojlanishining asosini tashkil etadi.",
        "To'rtinchi guruh — kommunikativ kompetensiyalar. Bularga o'z fikrini og'zaki ifodalay olish, boshqalarni tinglash va tushunish, savollarga javob berish, hikoya tuzish va qayta hikoyalash, suhbatda faol ishtirok etish, verbal va noverbal muloqot vositalaridan foydalanish kiradi.",
        "Beshinchi guruh — amaliy kompetensiyalar. Bularga ishni rejalash va tartibli bajarish, vositalardan to'g'ri foydalanish, boshlagan ishni oxiriga yetkazish, natijani baholash va xatolarni tuzatish, yangi vaziyatlarga moslashish kiradi. Oltinchi guruh — sog'liqni saqlash kompetensiyalari: o'z tanasini bilish, gigiyena qoidalariga rioya qilish, to'g'ri ovqatlanish, harakatli turmush tarzi va xavfli narsalarni ajrata olish. Bu kompetensiyalar birgalikda bolani hayotga tayyor shaxs sifatida shakllantiradi.",
    ],
    [
        "Kompetensiyaviy yondashuvni maktabgacha ta'limda amalga oshirish uchun maxsus usullar va vositalardan foydalaniladi. Birinchi va eng samarali usul — o'yin usuli. Maktabgacha yoshda o'yin bolaning yetakchi faoliyati bo'lib, kompetensiyalar asosan o'yin jarayonida shakllanadi. Rolli o'yinlar ijtimoiy kompetensiyalarni, didaktik o'yinlar bilish kompetensiyalarini, harakatli o'yinlar esa jismoniy kompetensiyalarni rivojlantiradi.",
        "Ikkinchi usul — loyiha faoliyati. Bu usulda bolalar birgalikda muayyan mavzu bo'yicha loyiha ustida ishlaydi. Masalan, \"Bizning bog'chamiz\" loyihasida bolalar o'simliklar o'stiradi, kuzatadi, rasm chizadi va natijalarini taqdimot qiladi. Bu jarayonda bir vaqtda bir nechta kompetensiya — hamkorlik, muloqot, kuzatish, rejalash — shakllanadi.",
        "Uchinchi usul — muammoli vaziyatlar yaratish. Tarbiyachi bolalarga maxsus muammoli vaziyatlar taklif etadi va ulardan yechim izlashni so'raydi. Masalan: \"O'yinchoqlar yetishmayapti, nima qilamiz?\" yoki \"Qo'g'irchoq kasal bo'ldi, qanday yordam beramiz?\" Bu usul bolaning tanqidiy fikrlash va muammolarni hal etish kompetensiyalarini shakllantiradi.",
        "To'rtinchi usul — mustaqil faoliyatni tashkil etish. Rivojlanish markazlarida bola o'z xohishiga qarab faoliyat tanlaydi va mustaqil ishlaydi. Bu uning mustaqillik, tashabbuskorlik va o'z-o'zini boshqarish kompetensiyalarini rivojlantiradi. Beshinchi usul — kuzatish va tajriba o'tkazish. Tabiat burchagida va eksperiment markazida bola mustaqil kuzatishlar olib boradi, bu uning bilish kompetensiyalarini shakllantiradi.",
        "Oltinchi usul — birgalikdagi faoliyat. Bolalar kichik guruhlarda birgalikda ishlaydi — qurilish, rasm chizish, sahna ko'rinishi tayyorlash. Bu hamkorlik va muloqot kompetensiyalarini rivojlantiradi. Vositalar sifatida esa didaktik materiallar, rolli o'yinlar to'plamlari, konstruktorlar, eksperiment asboblari, kitoblar, rasm va kartochkalar, musiqa asboblari va multimedia vositalari qo'llaniladi.",
    ],
    [
        "Kompetensiyaviy yondashuvda tarbiyachining roli an'anaviy ta'limga nisbatan tubdan o'zgaradi. An'anaviy yondashuvda tarbiyachi asosan bilim beruvchi va ko'rsatma beruvchi bo'lsa, kompetensiyaviy yondashuvda u bolaning rivojlanishiga sharoit yaratuvchi, yo'naltiruvchi va qo'llab-quvvatlovchi sifatida faoliyat yuritadi. Tarbiyachi tayyor javob bermaydi, balki bolani mustaqil topishga undaydi.",
        "Tarbiyachining birinchi roli — muhit yaratuvchi. U guruhdagi ta'limiy muhitni shunday tashkil etadiki, bola mustaqil faoliyat yuritishi, tanlov qilishi va kompetensiyalarini amaliyotda sinab ko'rishi mumkin bo'ladi. Muhitdagi har bir element bolaning muayyan kompetensiyasini rivojlantirishga xizmat qilishi kerak.",
        "Ikkinchi roli — kuzatuvchi va tahlilchi. Tarbiyachi har bir bolaning kompetensiyalarini muntazam kuzatadi, uning kuchli va zaif tomonlarini aniqlaydi va shu asosda individual ish rejasini tuzadi. U maxsus kuzatuv kartochkalari va diagnostika vositalaridan foydalanadi. Bu ma'lumotlar asosida ta'lim jarayoni doimiy takomillashtirib boriladi.",
        "Uchinchi roli — scaffolding, ya'ni bolaga aynan kerak bo'lgan paytda zarur darajadagi yordam ko'rsatuvchi. Tarbiyachi bolaga na ko'p, na kam yordam beradi. U bolaning o'zi qila oladigan ishlariga aralashmaydi, lekin yordamga muhtoj bo'lganida o'z vaqtida qo'llab-quvvatlaydi. Bola yangi kompetensiyani egallab olgach, yordam asta-sekin kamaytiriladi.",
        "To'rtinchi roli — motivator va rag'batlantiruvchi. Tarbiyachi bolaning har bir muvaffaqiyatini qayd etadi, urinishlarini qadrlaydi va izlanishga undaydi. U ijobiy muhit yaratadi, bolada \"men qila olaman\" ishonchini mustahkamlaydi. Beshinchi roli — hamkor. Tarbiyachi bola bilan teng huquqli muloqot olib boradi, uning fikrlarini hurmat qiladi va qarorlar qabul qilishda ishtirok ettiradi.",
    ],
    [
        "Kompetensiyaviy yondashuvning maktabgacha ta'limdagi amaliy ahamiyati juda katta. Avvalo, bu yondashuv bolani hayotga haqiqiy tayyorlaydi. Bola nafaqat bilim oladi, balki shu bilimni kundalik hayotda qo'llay olishni o'rganadi. U muammolarga duch kelganda qo'rqmaydi, balki yechim izlaydi. Bu ko'nikma bolaning butun hayoti davomida zarur bo'ladi.",
        "Ikkinchidan, kompetensiyaviy yondashuv bolani maktab ta'limiga samarali tayyorlaydi. Maktabda boladan mustaqillik, mas'uliyat, e'tiborni jamlash, qoidalarga rioya qilish va tengdoshlari bilan hamkorlik qilish talab etiladi. Bu ko'nikmalarning barchasi kompetensiyaviy yondashuv orqali maktabgacha davrda shakllantiriladi.",
        "Uchinchidan, bu yondashuv har bir bolaning individual xususiyatlarini hisobga oladi. Har bir bola o'z tezligi va o'z yo'li bilan kompetensiyalarni egallaydi. Kimdir muloqotda kuchli, kimdir mantiqiy fikrlashda, kimdir jismoniy faoliyatda. Kompetensiyaviy yondashuv har bir bolaning kuchli tomonlarini rivojlantirishga va zaif tomonlarini qo'llab-quvvatlashga imkon beradi.",
        "To'rtinchidan, bu yondashuv tarbiyachining kasbiy mahoratini oshiradi. Tarbiyachi an'anaviy \"dars berish\" uslubidan chiqib, bolaning rivojlanishini ta'minlovchi muhit yaratish, individual yondashuvni amalga oshirish va zamonaviy usullarni qo'llash ko'nikmalarini egallaydi.",
        "Kompetensiyaviy yondashuvning istiqbollari ham porloqdir. Kelajakda bu yondashuv yanada chuqurroq ishlab chiqiladi, raqamli texnologiyalar bilan birlashtiriladi va har bir bola uchun individual ta'limiy marshrut tuzish imkonini beradi. Shuningdek, bu yondashuv inklyuziv ta'limda, iste'dodli bolalar bilan ishlashda va oilaviy ta'limda ham keng qo'llanilishi kutilmoqda. Kompetensiyaviy yondashuv — bu maktabgacha ta'limning kelajagi.",
    ],
    [
        "Mazkur mustaqil ishda maktabgacha yoshdagi bolalarga ta'lim berishda kompetensiyaviy yondashuv har tomonlama tahlil qilindi. Tahlillar shuni ko'rsatdiki, bu yondashuv zamonaviy maktabgacha ta'limning eng samarali yo'nalishlaridan biri bo'lib, u bolani faqat bilim bilan emas, balki hayotiy ko'nikmalar bilan qurollantirishga qaratilgan.",
        "Kompetensiyaviy yondashuvning mohiyati — bolaning bilimni amaliyotda qo'llay olish, mustaqil harakat qila olish va yangi vaziyatlarga moslasha olish qobiliyatini shakllantirishdir. Bu yondashuv faoliyat nazariyasi, konstruktivizm va shaxsga yo'naltirilgan ta'lim nazariyalariga tayanadi.",
        "Maktabgacha yoshdagi bolalarda shaxsiy, ijtimoiy, bilish, kommunikativ, amaliy va sog'liqni saqlash kompetensiyalari shakllantiriladi. Bu kompetensiyalar o'yin, loyiha faoliyati, muammoli vaziyatlar, mustaqil va birgalikdagi faoliyat orqali rivojlantiriladi. Tarbiyachi bu jarayonda muhit yaratuvchi, kuzatuvchi, yo'naltiruvchi va motivator sifatida ishtirok etadi.",
        "Xulosa qilib aytganda, kompetensiyaviy yondashuv — bu maktabgacha ta'limning zamonaviy va samarali yo'nalishi bo'lib, u bolalarni hayotga chinakam tayyorlash va ularning har tomonlama rivojlanishini ta'minlash imkonini beradi. Bu yondashuvni amaliyotga keng joriy etish O'zbekiston maktabgacha ta'limi sifatini yanada oshirishga xizmat qiladi.",
        "Foydalanilgan adabiyotlar:",
        "1. O'zbekiston Respublikasining \"Maktabgacha ta'lim va tarbiya to'g'risida\"gi Qonuni. — Toshkent, 2020.",
        "2. \"Ilk qadam\" maktabgacha ta'lim muassasalarining Davlat o'quv dasturi. — Toshkent, 2018.",
        "3. Xutorskoy A.V. \"Kompetentnostnyy podxod v obuchenii\". — Moskva, 2019.",
        "4. Sodiqova M. \"Maktabgacha ta'limda zamonaviy yondashuvlar\". — Toshkent, 2021.",
        "5. Zimnyaya I.A. \"Klyuchevye kompetentsii kak rezultativno-tselevaya osnova kompetentnostnogo podxoda\". — Moskva, 2018.",
        "6. Internet manbalari: uzedu.uz, mtt.uz.",
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
body.append(make_para("Maktabgacha yoshdagi bolalarga ta'lim berishda kompetensiyaviy yondashuv", bold=True, size=28, align="center"))
for _ in range(6):
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
core_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Mustaqil ish - Kompetensiyaviy yondashuv</dc:title><dc:creator>Talaba</dc:creator></cp:coreProperties>'
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
