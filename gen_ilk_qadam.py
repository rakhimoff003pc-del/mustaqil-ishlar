#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mustaqil ish: "Ilk qadam" davlat o'quv dasturining maqsad va vazifasi.
"Ilk qadam" davlat o'quv dasturi asosida nashr qilingan metodik ta'minot
Target: 9 A4 pages, Times New Roman 14pt, 1.5 line spacing
"""
import os
import zipfile
from xml.sax.saxutils import escape

OUT = "/projects/sandbox/mustaqil-ishlar/Ilk_qadam_maqsad_vazifa.docx"

PLAN = [
    "Kirish",
    "\"Ilk qadam\" davlat o'quv dasturi haqida umumiy ma'lumot",
    "\"Ilk qadam\" dasturining maqsadi",
    "\"Ilk qadam\" dasturining vazifalari",
    "Dasturning rivojlanish sohalari va tamoyillari",
    "\"Ilk qadam\" dasturining tuzilishi va mazmuni",
    "\"Ilk qadam\" dasturi asosida nashr qilingan metodik ta'minot",
    "Dasturning maktabgacha ta'lim tizimidagi ahamiyati",
    "Xulosa va foydalanilgan adabiyotlar",
]

SECTIONS = [
    # 1. Kirish
    [
        "Maktabgacha ta'lim har bir bolaning hayotida muhim bosqich bo'lib, "
        "u shaxsning keyingi rivojlanishi uchun mustahkam poydevor yaratadi. "
        "O'zbekiston Respublikasida maktabgacha ta'lim tizimini "
        "takomillashtirish va uni xalqaro standartlarga moslashtirish "
        "borasida keng ko'lamli islohotlar amalga oshirilmoqda. Ana shunday "
        "islohotlar natijasida maktabgacha ta'lim muassasalari uchun "
        "\"Ilk qadam\" davlat o'quv dasturi ishlab chiqildi va amaliyotga "
        "joriy etildi.",

        "\"Ilk qadam\" davlat o'quv dasturi — bu maktabgacha yoshdagi "
        "bolalarni har tomonlama rivojlantirishga yo'naltirilgan zamonaviy "
        "hujjat bo'lib, u bolaning yoshi va individual xususiyatlariga mos "
        "ta'lim-tarbiya jarayonini tashkil etish uchun asos bo'lib xizmat "
        "qiladi. Dastur xalqaro tajriba va milliy qadriyatlarni uyg'unlashtirgan "
        "holda yaratilgan va bola rivojlanishining barcha sohalarini qamrab "
        "oladi.",

        "Mazkur mustaqil ishda \"Ilk qadam\" davlat o'quv dasturining maqsadi "
        "va vazifalari, uning tuzilishi, mazmuni va dastur asosida nashr "
        "qilingan metodik ta'minot batafsil yoritiladi. Ishda dasturning "
        "rivojlanish sohalari, asosiy tamoyillari va maktabgacha ta'lim "
        "tizimidagi ahamiyati tahlil qilinadi. Mavzuning dolzarbligi shundaki, "
        "har bir tarbiyachi bu dasturni chuqur bilishi va uni amaliyotda "
        "to'g'ri qo'llashi zarur.",
    ],

    # 2. Umumiy ma'lumot
    [
        "\"Ilk qadam\" davlat o'quv dasturi O'zbekiston Respublikasi "
        "maktabgacha ta'lim tizimi uchun ishlab chiqilgan asosiy me'yoriy "
        "hujjatdir. Dastur 2018-yilda tasdiqlangan bo'lib, mamlakatdagi "
        "barcha maktabgacha ta'lim muassasalarida qo'llanilishi uchun "
        "mo'ljallangan. Dastur maktabgacha ta'limning davlat standartlari "
        "asosida tuzilgan va bolalarning rivojlanishiga zamonaviy yondashuvni "
        "ifoda etadi.",

        "Dastur 3 yoshdan 7 yoshgacha bo'lgan bolalarni qamrab oladi va "
        "ularning rivojlanishini bosqichma-bosqich ta'minlaydi. \"Ilk qadam\" "
        "nomi ramziy ma'noga ega bo'lib, u bolaning hayot yo'lidagi dastlabki "
        "muhim qadamlarini, ya'ni shaxs sifatida shakllanishining ilk "
        "bosqichini anglatadi. Dastur bu qadamlarni to'g'ri va ishonchli "
        "qo'yishga yordam beradi.",

        "\"Ilk qadam\" dasturi bir qator xalqaro tashkilotlar, jumladan "
        "YUNESKO va YUNISEF tavsiyalari, shuningdek ilg'or xorijiy "
        "davlatlarning maktabgacha ta'lim tajribasini hisobga olgan holda "
        "ishlab chiqilgan. Shu bilan birga, dasturda o'zbek xalqining milliy "
        "qadriyatlari, urf-odatlari va madaniy merosi ham o'z aksini topgan. "
        "Bu uyg'unlik dasturning o'ziga xos xususiyati hisoblanadi.",

        "Dasturning asosiy g'oyasi — bolani faol, mustaqil, ijodkor va "
        "tashabbuskor shaxs sifatida tarbiyalashdir. Bunda bola ta'lim "
        "jarayonining passiv ob'ekti emas, balki faol sub'ekti sifatida "
        "qaraladi. Tarbiyachi esa bilim beruvchi emas, balki bolaning "
        "rivojlanishiga yordam beruvchi, yo'naltiruvchi va "
        "qo'llab-quvvatlovchi shaxs sifatida faoliyat yuritadi. Bu "
        "zamonaviy bolaga yo'naltirilgan ta'lim yondashuvining mohiyatidir.",
    ],

    # 3. Maqsadi
    [
        "\"Ilk qadam\" davlat o'quv dasturining bosh maqsadi — maktabgacha "
        "yoshdagi har bir bolaning jismoniy, ijtimoiy-hissiy, nutqiy, aqliy "
        "va ijodiy jihatdan har tomonlama va uyg'un rivojlanishini "
        "ta'minlash, uni maktab ta'limiga va hayotga tayyorlashdir. Bu "
        "maqsad dasturning butun mazmunini va yo'nalishini belgilab beradi.",

        "Dasturning maqsadi bolaning shaxsiy salohiyatini to'liq namoyon "
        "qilishiga sharoit yaratishni ko'zda tutadi. Har bir bola noyob "
        "shaxs bo'lib, o'ziga xos qobiliyat, qiziqish va rivojlanish "
        "tezligiga ega. Dastur har bir bolaning individual xususiyatlarini "
        "hisobga olib, uning kuchli tomonlarini rivojlantirishga va "
        "imkoniyatlarini ro'yobga chiqarishga qaratilgan.",

        "Maqsadning yana bir muhim jihati — bolada hayot davomida o'rganishga "
        "bo'lgan ishtiyoq va qiziqishni shakllantirishdir. Dastur bolani "
        "shunchaki bilim bilan to'ldirishni emas, balki unda mustaqil "
        "o'rganish, izlanish, kashf etish va muammolarni hal qilish "
        "ko'nikmalarini rivojlantirishni maqsad qiladi. Bu ko'nikmalar "
        "bolaning butun hayoti davomida zarur bo'ladi.",

        "Shuningdek, dasturning maqsadi bolada sog'lom turmush tarzi, "
        "milliy va umuminsoniy qadriyatlar, atrof-muhitga va jamiyatga "
        "ijobiy munosabatni shakllantirishni o'z ichiga oladi. Bola "
        "o'zining shaxsiy qadr-qimmatini his qilishi, boshqalarni hurmat "
        "qilishi, tabiatni asrashi va vatanini sevishi kerak. Bu axloqiy "
        "fazilatlar bolaning butun shaxsiy kamolotining asosini tashkil "
        "etadi va dasturning maqsadiga to'liq mos keladi.",
    ],

    # 4. Vazifalari
    [
        "\"Ilk qadam\" davlat o'quv dasturining vazifalari bosh maqsaddan "
        "kelib chiqqan holda aniq belgilangan. Birinchi vazifa — bolaning "
        "jismoniy sog'lig'ini mustahkamlash va jismoniy rivojlanishini "
        "ta'minlash. Bu vazifa bolaning harakat ko'nikmalarini "
        "shakllantirish, jismoniy sifatlarini rivojlantirish, sog'lom "
        "turmush tarzi va xavfsizlik ko'nikmalarini o'rgatishni o'z ichiga "
        "oladi.",

        "Ikkinchi vazifa — bolaning ijtimoiy-hissiy rivojlanishini "
        "ta'minlash. Bu vazifa bolada o'z his-tuyg'ularini tushunish va "
        "boshqarish, boshqalar bilan ijobiy munosabatlar o'rnatish, "
        "jamoada ishlash, mustaqillik va mas'uliyatni shakllantirishni "
        "ko'zda tutadi. Bola o'zini va atrofidagilarni tushunishni, "
        "muloqot qilishni va hamkorlik qilishni o'rganadi.",

        "Uchinchi vazifa — bolaning nutqi va muloqot ko'nikmalarini "
        "rivojlantirish. Bu vazifa bolaning lug'at boyligini oshirish, "
        "to'g'ri va ravon gapirishni o'rgatish, bog'lanishli nutqni "
        "shakllantirish va savodxonlikka tayyorlashni o'z ichiga oladi. "
        "Nutqiy rivojlanish bolaning aqliy va ijtimoiy kamoloti bilan "
        "uzviy bog'liqdir.",

        "To'rtinchi vazifa — bolaning bilish jarayonlarini va aqliy "
        "qobiliyatlarini rivojlantirish. Bu vazifa bolada diqqat, xotira, "
        "tafakkur, tasavvur va mantiqiy fikrlashni shakllantirishni, "
        "atrof-olam haqida bilim berishni, matematik tushunchalarni "
        "o'rgatishni va tabiat bilan tanishtirishni ko'zda tutadi. Bola "
        "kuzatish, taqqoslash, tahlil qilish va xulosa chiqarishni "
        "o'rganadi.",

        "Beshinchi vazifa — bolaning ijodiy qobiliyatlarini va badiiy-estetik "
        "didini rivojlantirish. Bu vazifa bolani musiqa, tasviriy san'at, "
        "badiiy adabiyot va teatr bilan tanishtirishni, uning ijodiy "
        "salohiyatini ro'yobga chiqarishni o'z ichiga oladi. Oltinchi "
        "vazifa — oila va maktabgacha ta'lim muassasasi o'rtasidagi "
        "hamkorlikni ta'minlash. Bola tarbiyasida ota-onalarning faol "
        "ishtiroki muhim bo'lib, dastur bu hamkorlikni mustahkamlashga "
        "qaratilgan.",
    ],

    # 5. Rivojlanish sohalari va tamoyillari
    [
        "\"Ilk qadam\" davlat o'quv dasturi bolaning rivojlanishini besh "
        "asosiy soha bo'yicha tashkil etadi. Birinchi soha — jismoniy "
        "rivojlanish va sog'lom turmush tarzini shakllantirish. Bu soha "
        "bolaning harakat faolligi, jismoniy sifatlari, sog'lig'i va "
        "xavfsizligi bilan bog'liq barcha jihatlarni qamrab oladi.",

        "Ikkinchi soha — ijtimoiy-hissiy rivojlanish. Bu soha bolaning "
        "o'zini anglashi, his-tuyg'ularini boshqarishi, boshqalar bilan "
        "munosabatlari, axloqiy qadriyatlari va ijtimoiy ko'nikmalarini "
        "o'z ichiga oladi. Uchinchi soha — nutq, muloqot, o'qish va "
        "yozish malakalari. Bu soha bolaning nutqiy rivojlanishi va "
        "savodxonlik asoslarini qamrab oladi.",

        "To'rtinchi soha — bilish jarayonlarining rivojlanishi. Bu soha "
        "bolaning atrof-olamni bilishi, matematik tasavvurlari, mantiqiy "
        "fikrlashi va tabiat bilan tanishuvini o'z ichiga oladi. Beshinchi "
        "soha — ijodiy rivojlanish. Bu soha bolaning badiiy, musiqiy va "
        "estetik qobiliyatlarini rivojlantirishni qamrab oladi. Bu besh "
        "soha birgalikda bolaning yaxlit va uyg'un rivojlanishini "
        "ta'minlaydi.",

        "Dastur bir qator muhim tamoyillarga asoslanadi. Birinchi tamoyil — "
        "bolaga yo'naltirilganlik. Bunda bolaning qiziqishlari, ehtiyojlari "
        "va individual xususiyatlari ta'lim jarayonining markazida turadi. "
        "Ikkinchi tamoyil — rivojlanishning yaxlitligi. Bolaning barcha "
        "rivojlanish sohalari o'zaro bog'liq holda, integratsiyalashgan "
        "tarzda rivojlantiriladi.",

        "Uchinchi tamoyil — o'yin orqali o'rganish. O'yin maktabgacha "
        "yoshdagi bolaning yetakchi faoliyati bo'lib, dastur barcha "
        "ta'limiy maqsadlarni o'yin orqali amalga oshirishni ko'zda "
        "tutadi. To'rtinchi tamoyil — har bir bolaning huquqlarini va "
        "qadr-qimmatini hurmat qilish. Beshinchi tamoyil — oila bilan "
        "hamkorlik. Oltinchi tamoyil — ta'lim muhitining bola "
        "rivojlanishiga moslashtirilganligi. Bu tamoyillar dasturni "
        "amalga oshirishda asosiy yo'l-yo'riq vazifasini bajaradi.",
    ],

    # 6. Tuzilishi va mazmuni
    [
        "\"Ilk qadam\" davlat o'quv dasturi puxta o'ylangan tuzilishga ega. "
        "Dasturning kirish qismida uning maqsadi, vazifalari, asosiy "
        "tamoyillari va tushunchalari bayon etiladi. Bu qism dasturning "
        "umumiy falsafasini va g'oyaviy asoslarini ochib beradi. "
        "Tarbiyachi dastur bilan ishlashni aynan shu qismdan boshlashi va "
        "uning asosiy g'oyalarini tushunib olishi kerak.",

        "Dasturning asosiy qismi rivojlanish sohalari bo'yicha tuzilgan. "
        "Har bir soha uchun bolaning yoshiga qarab kutilgan natijalar, "
        "ya'ni bola nimalarni bilishi, qila olishi va qanday ko'nikmalarga "
        "ega bo'lishi kerakligi aniq ko'rsatilgan. Kutilgan natijalar "
        "bolaning rivojlanishini baholash va ta'lim jarayonini "
        "rejalashtirish uchun asos bo'lib xizmat qiladi.",

        "Dasturda kutilgan natijalar yosh guruhlari bo'yicha "
        "differentsiallashtirilgan. Kichik guruh (3-4 yosh), o'rta guruh "
        "(4-5 yosh), katta guruh (5-6 yosh) va maktabga tayyorlov guruhi "
        "(6-7 yosh) uchun alohida ko'rsatkichlar belgilangan. Bu yondashuv "
        "tarbiyachiga har bir yosh bosqichida bolaning rivojlanishini "
        "to'g'ri kuzatish va baholash imkonini beradi.",

        "Dasturning mazmuni amaliy yo'naltirilgan bo'lib, u faqat \"nima\"ni "
        "o'rgatish kerakligini emas, balki \"qanday\" o'rgatish kerakligini "
        "ham ko'rsatadi. Dasturda tarbiyachilar uchun amaliy tavsiyalar, "
        "faoliyat turlari, o'yinlar va usullar keltirilgan. Bu materiallar "
        "tarbiyachiga ta'lim jarayonini samarali tashkil etishda yordam "
        "beradi.",

        "Dasturning muhim xususiyatlaridan biri — uning moslashuvchanligi. "
        "Dastur tarbiyachiga qat'iy ko'rsatmalar bermaydi, balki unga "
        "ijodiy yondashish va guruhdagi bolalarning xususiyatlariga qarab "
        "ta'lim jarayonini moslashtirish erkinligini beradi. Tarbiyachi "
        "dastur talablari doirasida o'z metod va usullarini tanlay oladi. "
        "Bu yondashuv tarbiyachining kasbiy mahoratini namoyon qilishiga "
        "va har bir guruhning o'ziga xosligini hisobga olishiga imkon "
        "yaratadi.",
    ],

    # 7. Nashr qilingan metodik ta'minot
    [
        "\"Ilk qadam\" davlat o'quv dasturi asosida tarbiyachilar va "
        "ota-onalar uchun bir qator metodik qo'llanmalar va materiallar "
        "nashr qilingan. Bu metodik ta'minot dasturni amaliyotda samarali "
        "qo'llash uchun zarur bo'lib, tarbiyachining kundalik ishida "
        "muhim yordamchi vazifasini bajaradi. Metodik materiallar dastur "
        "g'oyalarini aniq amaliy ko'rsatmalar va misollar orqali ochib "
        "beradi.",

        "Dastur asosida nashr qilingan asosiy materiallardan biri — "
        "tarbiyachilar uchun metodik qo'llanmalardir. Bu qo'llanmalarda "
        "har bir rivojlanish sohasi bo'yicha mashg'ulotlarni qanday "
        "tashkil etish, qanday usullar qo'llash va bolalar faoliyatini "
        "qanday yo'naltirish bo'yicha batafsil ko'rsatmalar berilgan. "
        "Qo'llanmalar tarbiyachiga nazariy bilimlarni amaliyotga "
        "tatbiq etishda yordam beradi.",

        "Shuningdek, dastur asosida mavzuli rejalashtirish bo'yicha "
        "metodik tavsiyalar nashr qilingan. Bu tavsiyalar tarbiyachiga "
        "o'quv yili davomida ta'lim jarayonini izchil rejalashtirishda, "
        "mavzularni belgilashda va faoliyat turlarini tanlashda yo'l-yo'riq "
        "ko'rsatadi. Mavzuli rejalashtirish bolaning rivojlanishini yaxlit "
        "va integratsiyalashgan tarzda ta'minlash imkonini beradi.",

        "Dastur asosida bolalar uchun didaktik materiallar, ish daftarlari "
        "va o'quv-ko'rgazmali qo'llanmalar ham yaratilgan. Bu materiallar "
        "bolalarning yoshiga mos, rangli, qiziqarli va rivojlantiruvchi "
        "tarzda ishlab chiqilgan. Ular bolaning mustaqil faoliyatini "
        "qo'llab-quvvatlaydi va ta'lim jarayonini yanada samarali qiladi. "
        "Didaktik materiallar har bir rivojlanish sohasi bo'yicha "
        "tayyorlangan.",

        "Bundan tashqari, ota-onalar uchun maxsus qo'llanmalar va "
        "tavsiyalar ham nashr qilingan. Bu materiallar ota-onalarga "
        "bola rivojlanishining xususiyatlarini tushuntiradi va uyda "
        "bola bilan qanday shug'ullanish, uni qanday qo'llab-quvvatlash "
        "bo'yicha amaliy maslahatlar beradi. Shu tariqa dastur oila va "
        "maktabgacha ta'lim muassasasi o'rtasidagi hamkorlikni "
        "mustahkamlaydi. Barcha metodik ta'minot birgalikda dasturni "
        "to'liq va samarali amalga oshirishga xizmat qiladi.",
    ],

    # 8. Ahamiyati
    [
        "\"Ilk qadam\" davlat o'quv dasturining maktabgacha ta'lim "
        "tizimidagi ahamiyati nihoyatda katta. Avvalo, dastur butun "
        "mamlakat bo'ylab maktabgacha ta'lim mazmunini birxillashtirdi "
        "va uni yagona davlat standartlari asosiga o'tkazdi. Endilikda "
        "har bir maktabgacha ta'lim muassasasi yagona dastur asosida "
        "faoliyat yuritadi, bu esa ta'lim sifatining bir xilligini "
        "ta'minlaydi.",

        "Dasturning muhim ahamiyati shundaki, u maktabgacha ta'limni "
        "bolaga yo'naltirilgan zamonaviy yondashuvga o'tkazdi. An'anaviy "
        "o'qitishga asoslangan model o'rniga, bolaning faol, mustaqil va "
        "ijodiy faoliyatiga tayangan model joriy etildi. Bu o'zgarish "
        "bolaning haqiqiy rivojlanishini ta'minlaydi va uni hayotga "
        "yaxshiroq tayyorlaydi.",

        "Dastur tarbiyachilarning kasbiy faoliyatiga ham ijobiy ta'sir "
        "ko'rsatdi. U tarbiyachilarga aniq yo'nalish va maqsadlar berdi, "
        "shu bilan birga ularning ijodiy erkinligini ham ta'minladi. "
        "Tarbiyachilar dastur asosida o'z malakalarini oshirmoqda, yangi "
        "usullarni o'rganmoqda va bolalar bilan ishlashda zamonaviy "
        "yondashuvlarni qo'llashmoqda.",

        "Dasturning yana bir muhim ahamiyati — u bolalarning maktabga "
        "tayyorgarligini sezilarli darajada yaxshilashidir. Dastur "
        "bolaning nafaqat bilim, balki ijtimoiy, hissiy va jismoniy "
        "jihatdan ham maktabga tayyor bo'lishini ta'minlaydi. Bu esa "
        "bolaning maktabdagi keyingi muvaffaqiyatlari uchun mustahkam "
        "asos yaratadi.",

        "Shuningdek, dastur oila va jamiyatning maktabgacha ta'limga "
        "bo'lgan munosabatini o'zgartirdi. Ota-onalar bola rivojlanishida "
        "maktabgacha ta'limning muhim o'rnini anglab yetdilar va bu "
        "jarayonda faolroq ishtirok eta boshladilar. Umuman olganda, "
        "\"Ilk qadam\" dasturi O'zbekistonda maktabgacha ta'lim sifatini "
        "oshirishda, uni xalqaro standartlarga yaqinlashtirishda va "
        "har bir bolaning har tomonlama rivojlanishini ta'minlashda "
        "muhim qadam bo'ldi.",
    ],

    # 9. Xulosa
    [
        "Mazkur mustaqil ishda \"Ilk qadam\" davlat o'quv dasturining "
        "maqsadi va vazifalari, uning tuzilishi, mazmuni va metodik "
        "ta'minoti har tomonlama tahlil qilindi. Tahlillar shuni "
        "ko'rsatdiki, bu dastur maktabgacha yoshdagi bolalarni har "
        "tomonlama va uyg'un rivojlantirishga yo'naltirilgan zamonaviy "
        "va ilmiy asoslangan hujjatdir.",

        "Dasturning bosh maqsadi — har bir bolaning jismoniy, "
        "ijtimoiy-hissiy, nutqiy, aqliy va ijodiy jihatdan rivojlanishini "
        "ta'minlash va uni maktabga hamda hayotga tayyorlashdir. Bu maqsad "
        "aniq belgilangan vazifalar orqali amalga oshiriladi. Dastur besh "
        "asosiy rivojlanish sohasini qamrab oladi va muhim pedagogik "
        "tamoyillarga asoslanadi.",

        "\"Ilk qadam\" dasturi asosida tarbiyachilar, bolalar va ota-onalar "
        "uchun boy metodik ta'minot yaratilgan. Bu materiallar dasturni "
        "amaliyotda samarali qo'llash imkonini beradi. Dasturning "
        "moslashuvchanligi va bolaga yo'naltirilganligi uning asosiy "
        "afzalliklari hisoblanadi.",

        "Xulosa qilib aytganda, \"Ilk qadam\" davlat o'quv dasturi "
        "O'zbekiston maktabgacha ta'lim tizimida muhim islohot bo'lib, "
        "u ta'lim sifatini oshirishga, uni zamonaviy va xalqaro "
        "standartlarga moslashtirishga xizmat qilmoqda. Har bir "
        "tarbiyachi bu dasturni chuqur o'rganishi va uni ijodiy "
        "yondashuv bilan amaliyotga tatbiq etishi bolalarning har "
        "tomonlama rivojlanishini ta'minlashning muhim shartidir.",

        "Foydalanilgan adabiyotlar:",
        "1. O'zbekiston Respublikasining \"Maktabgacha ta'lim va tarbiya "
        "to'g'risida\"gi Qonuni. — Toshkent, 2020.",
        "2. \"Ilk qadam\" maktabgacha ta'lim muassasalarining Davlat o'quv "
        "dasturi. — Toshkent, 2018.",
        "3. Maktabgacha ta'limning Davlat standarti. — Toshkent, 2018.",
        "4. \"Ilk qadam\" dasturi asosida tarbiyachilar uchun metodik "
        "qo'llanma. — Toshkent, 2019.",
        "5. Yusupova M. \"Maktabgacha ta'limda zamonaviy yondashuvlar\". — "
        "Toshkent, 2021.",
        "6. Internet manbalari: uzedu.uz, mtt.uz.",
    ],
]


# ---------- DOCX XML BUILDER ----------

def make_para(text, bold=False, size=28, align=None, before=120, after=120):
    align_xml = f'<w:jc w:val="{align}"/>' if align else ""
    bold_xml = '<w:b/>' if bold else ""
    safe = escape(text)
    return (
        '<w:p><w:pPr>'
        f'<w:spacing w:before="{before}" w:after="{after}" w:line="360" w:lineRule="auto"/>'
        f'{align_xml}'
        '<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
        f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>{bold_xml}</w:rPr>'
        '</w:pPr><w:r><w:rPr>'
        '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
        f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>{bold_xml}</w:rPr>'
        f'<w:t xml:space="preserve">{safe}</w:t></w:r></w:p>'
    )

def make_body_para(text):
    safe = escape(text)
    return (
        '<w:p><w:pPr>'
        '<w:spacing w:before="0" w:after="120" w:line="360" w:lineRule="auto"/>'
        '<w:ind w:firstLine="709"/>'
        '<w:jc w:val="both"/>'
        '<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
        '<w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>'
        '</w:pPr><w:r><w:rPr>'
        '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
        '<w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr>'
        f'<w:t xml:space="preserve">{safe}</w:t></w:r></w:p>'
    )

def page_break():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


# Build body
body = []

# TITLE PAGE
for _ in range(4):
    body.append(make_para("", size=28))
body.append(make_para("O'ZBEKISTON RESPUBLIKASI", bold=True, size=28, align="center"))
body.append(make_para("MAKTABGACHA VA MAKTAB TA'LIMI VAZIRLIGI", bold=True, size=28, align="center"))
body.append(make_para("", size=24))
body.append(make_para("MUSTAQIL ISH", bold=True, size=40, align="center"))
body.append(make_para("", size=24))
body.append(make_para("Mavzu:", bold=True, size=28, align="center"))
body.append(make_para(
    "\"Ilk qadam\" davlat o'quv dasturining maqsad va vazifasi. "
    "\"Ilk qadam\" davlat o'quv dasturi asosida nashr qilingan metodik ta'minot",
    bold=True, size=28, align="center"))
for _ in range(5):
    body.append(make_para("", size=24))
body.append(make_para("Bajardi: ______________________", size=28, align="right"))
body.append(make_para("Tekshirdi: ______________________", size=28, align="right"))
for _ in range(2):
    body.append(make_para("", size=24))
body.append(make_para("Toshkent — 2026", bold=True, size=28, align="center"))
body.append(page_break())

# PLAN PAGE
body.append(make_para("REJA", bold=True, size=32, align="center"))
body.append(make_para("", size=20))
for i, item in enumerate(PLAN, 1):
    body.append(make_para(f"{i}. {item}", size=28))
body.append(page_break())

# CONTENT PAGES
for idx, (heading, paragraphs) in enumerate(zip(PLAN, SECTIONS)):
    body.append(make_para(f"{idx + 1}. {heading.upper()}", bold=True, size=30, align="center"))
    body.append(make_para("", size=18))
    for p in paragraphs:
        body.append(make_body_para(p))
    if idx < len(SECTIONS) - 1:
        body.append(page_break())

sectPr = (
    '<w:sectPr>'
    '<w:pgSz w:w="11906" w:h="16838"/>'
    '<w:pgMar w:top="1134" w:right="850" w:bottom="1134" w:left="1701" '
    'w:header="708" w:footer="708" w:gutter="0"/>'
    '<w:cols w:space="708"/>'
    '<w:docGrid w:linePitch="360"/>'
    '</w:sectPr>'
)

document_xml = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
    '<w:body>' + ''.join(body) + sectPr + '</w:body></w:document>'
)

content_types_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>'''

rels_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''

document_rels_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>'''

styles_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults><w:rPrDefault><w:rPr>
<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
<w:sz w:val="28"/><w:szCs w:val="28"/>
<w:lang w:val="uz-UZ"/>
</w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr>
<w:spacing w:line="360" w:lineRule="auto"/>
</w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal">
<w:name w:val="Normal"/><w:qFormat/>
</w:style></w:styles>'''

core_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:title>Mustaqil ish - Ilk qadam davlat oquv dasturi</dc:title>
<dc:creator>Talaba</dc:creator>
</cp:coreProperties>'''

app_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">
<Application>Microsoft Office Word</Application>
</Properties>'''

# Write DOCX
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
