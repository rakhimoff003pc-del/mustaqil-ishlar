# -*- coding: utf-8 -*-
"""Maktabgacha ta'lim - 15 mavzulik mustaqil ish konspekti"""
import zipfile, datetime

TOPICS = []

def esc(t):
    return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")

def run(text, bold=False, size=28, font="Times New Roman"):
    rpr = '<w:rPr><w:rFonts w:ascii="%s" w:hAnsi="%s" w:cs="%s"/>' % (font, font, font)
    if bold: rpr += '<w:b/><w:bCs/>'
    rpr += '<w:sz w:val="%d"/><w:szCs w:val="%d"/></w:rPr>' % (size, size)
    return '<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (rpr, esc(text))

def para(text, bold=False, size=28, align="both", indent_first=709, space_after=120, line=360, keep_next=False):
    ppr = '<w:pPr>'
    if keep_next: ppr += '<w:keepNext/>'
    ppr += '<w:spacing w:after="%d" w:line="%d" w:lineRule="auto"/>' % (space_after, line)
    if indent_first: ppr += '<w:ind w:firstLine="%d"/>' % indent_first
    ppr += '<w:jc w:val="%s"/></w:pPr>' % align
    return '<w:p>%s%s</w:p>' % (ppr, run(text, bold=bold, size=size))

def page_break():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

def empty_para():
    return '<w:p><w:pPr><w:spacing w:after="0" w:line="360" w:lineRule="auto"/></w:pPr></w:p>'

def build_topic(t, is_first):
    parts = []
    if not is_first: parts.append(page_break())
    parts.append(para("%d-MAVZU. %s" % (t["num"], t["title"].upper()), bold=True, size=30, align="center", indent_first=0, space_after=180, keep_next=True))
    parts.append(para("Mustaqil ta'lim", bold=True, size=28, align="center", indent_first=0, space_after=180, keep_next=True))
    parts.append(para("Reja:", bold=True, size=28, align="left", indent_first=0, space_after=60, keep_next=True))
    for i, r in enumerate(t["reja"], 1):
        parts.append(para("%d. %s" % (i, r), size=28, align="left", indent_first=360, space_after=40))
    parts.append(empty_para())
    for idx, (head, paras) in enumerate(t["sections"], 1):
        parts.append(para("%d. %s" % (idx, head), bold=True, size=28, align="left", indent_first=0, space_after=80, keep_next=True))
        for p in paras:
            parts.append(para(p, size=28, align="both", indent_first=709, space_after=120))
    return "".join(parts)

def build_document():
    body = "".join(build_topic(t, i == 0) for i, t in enumerate(TOPICS))
    sect = '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1134" w:right="850" w:bottom="1134" w:left="1701" w:header="708" w:footer="708" w:gutter="0"/><w:pgNumType w:start="1"/></w:sectPr>'
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:body>' + body + sect + '</w:body></w:document>'

CT = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/><Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/><Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/></Types>'
RE = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/></Relationships>'
DR = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>'
ST = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="28"/><w:szCs w:val="28"/><w:lang w:val="uz-Latn-UZ"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:line="360" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults><w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr></w:style></w:styles>'

def cp():
    n = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>Maktabgacha ta\'lim - 15 mavzu</dc:title><dc:creator>Konspekt</dc:creator><dcterms:created xsi:type="dcterms:W3CDTF">%s</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">%s</dcterms:modified></cp:coreProperties>' % (n, n)

AP = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"><Application>Konspekt</Application></Properties>'

def write_docx(path):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CT)
        z.writestr("_rels/.rels", RE)
        z.writestr("word/document.xml", build_document())
        z.writestr("word/_rels/document.xml.rels", DR)
        z.writestr("word/styles.xml", ST)
        z.writestr("docProps/core.xml", cp())
        z.writestr("docProps/app.xml", AP)
    print("OK:", path, "|", len(TOPICS), "mavzu")


TOPICS.append({"num":1,"title":"\u201cIlk qadam\u201d davlat o\u2018quv dasturi asosida rivojlantiruvchi markazlarini tashkil etish","reja":[
"\u201cIlk qadam\u201d davlat o\u2018quv dasturi va uning tarbiyaviy g\u2018oyasi.","Rivojlantiruvchi markaz tushunchasi va uning ahamiyati.","Rivojlantiruvchi markazlarni tashkil etish tamoyillari.","Markazlarni jihozlash va faoliyatini tashkil etish."],"sections":[
("\u201cIlk qadam\u201d davlat o\u2018quv dasturi va uning tarbiyaviy g\u2018oyasi",[
"\u201cIlk qadam\u201d \u2014 O\u2018zbekiston Respublikasida amal qiladigan davlat o\u2018quv dasturi bo\u2018lib, u 3 yoshdan 7 yoshgacha bo\u2018lgan bolalarni har tomonlama rivojlantirishga qaratilgan. Dastur bola shaxsini, uning jismoniy, ijtimoiy-hissiy, nutqiy, bilish va ijodiy rivojlanishini ta\u2019minlashni asosiy maqsad qilib qo\u2018ygan.",
"Dasturning yetakchi g\u2018oyasi \u2014 bolaga tayyor bilim berish emas, balki uni mustaqil izlanishga, kashf etishga, faol harakat qilishga undaydigan muhit yaratishdir. Bola o\u2018yin va faoliyat orqali o\u2018rganadi, atrof-muhitni bilib oladi va o\u2018z imkoniyatlarini namoyon etadi.",
"\u201cIlk qadam\u201d dasturi bola rivojlanishining besh sohasini qamrab oladi: jismoniy rivojlanish va sog\u2018lom turmush tarzi; ijtimoiy-hissiy rivojlanish; nutq, muloqot, o\u2018qish va yozish malakalari; bilish jarayonining rivojlanishi; ijodiy rivojlanish. Bu sohalar uyg\u2018un tarzda rivojlantiriladi."]),
("Rivojlantiruvchi markaz tushunchasi va uning ahamiyati",[
"Rivojlantiruvchi markaz \u2014 maktabgacha ta\u2019lim tashkilotida guruh xonasining ma\u2019lum bir burchagi yoki maydoni bo\u2018lib, u muayyan rivojlanish sohasiga mo\u2018ljallangan jihoz, o\u2018yinchoq va materiallar bilan ta\u2019minlangan. Har bir markaz bolaning ma\u2019lum bir faoliyat turi bilan shug\u2018ullanishi uchun sharoit yaratadi.",
"Markazlarning ahamiyati shundaki, ular bolaga tanlash erkinligini beradi: bola o\u2018zi qiziqqan markazga borib, o\u2018zi xohlagan faoliyat bilan shug\u2018ullanadi. Bu mustaqillikni, tashabbuskorlikni va o\u2018z-o\u2018zini boshqarish ko\u2018nikmasini shakllantiradi.",
"Markazlar bolalarni kichik guruhlarga bo\u2018lib ishlash imkonini beradi. Bu tarbiyachiga har bir bolaga individual yondashish, uning ehtiyojlari va qiziqishlarini hisobga olish imkonini yaratadi. Markazlarda bola tengdoshlari bilan hamkorlik qilishni, muloqot qilishni o\u2018rganadi."]),
("Rivojlantiruvchi markazlarni tashkil etish tamoyillari",[
"Markazlarni tashkil etishda bir qancha tamoyillarga rioya qilinadi. Birinchidan, xavfsizlik tamoyili \u2014 barcha jihoz va materiallar bola sog\u2018lig\u2018i uchun xavfsiz, ekologik toza bo\u2018lishi shart. Ikkinchidan, yoshga moslik tamoyili \u2014 jihozlar bolalarning yoshi va rivojlanish darajasiga mos kelishi kerak.",
"Uchinchidan, ochiqlik va qulaylik tamoyili \u2014 materiallar bola ko\u2018zi va qo\u2018li yetadigan joyda, ochiq tokchalarda joylashtiriladi, shunda bola ularni mustaqil olishi va joyiga qo\u2018yishi mumkin. To\u2018rtinchidan, o\u2018zgaruvchanlik tamoyili \u2014 markazlar mavzuga va fasllarga qarab yangilanib turadi.",
"Beshinchidan, mazmunan boyitilganlik tamoyili \u2014 har bir markaz turli xil, bir-birini to\u2018ldiruvchi materiallar bilan ta\u2019minlanadi. Bu bolaning turli faoliyat bilan shug\u2018ullanishiga imkon beradi. Markazlar soni va mazmuni guruh xonasi maydoni va bolalar soniga qarab belgilanadi."]),
("Markazlarni jihozlash va faoliyatini tashkil etish",[
"Markazlarni jihozlashda tabiiy va sun\u2019iy materiallardan, sanoat ishlab chiqargan o\u2018yinchoqlardan hamda tarbiyachi va ota-onalar tomonidan tayyorlangan qo\u2018lbola materiallardan foydalaniladi. Har bir markaz aniq belgilangan, nomi yozilgan va rasmlar bilan ko\u2018rsatilgan bo\u2018ladi.",
"Tarbiyachi markazlar faoliyatini kun tartibiga muvofiq tashkil etadi. Erkin faoliyat vaqtida bolalar markazlarni o\u2018zlari tanlaydilar. Tarbiyachi kuzatuvchi va yo\u2018naltiruvchi rolini bajaradi, kerak bo\u2018lganda bolaga yordam beradi, savol beradi, fikrlashga undaydi.",
"Markazlarda faoliyat samarali bo\u2018lishi uchun tarbiyachi har kuni materiallarni yangilab turadi, mavzuga mos qo\u2018shimcha jihozlar qo\u2018shadi. Bolalar faoliyati kuzatiladi va baholanadi, natijalar rivojlanish kartasiga qayd etiladi. Bu bolaning rivojlanishini kuzatish imkonini beradi."])]})

TOPICS.append({"num":2,"title":"Maktabgacha ta'lim tashkilotida rivojlantiruvchi muhit","reja":[
"Rivojlantiruvchi muhit tushunchasi va mohiyati.","Rivojlantiruvchi muhitning tarkibiy qismlari.","Rivojlantiruvchi muhitga qo\u2018yiladigan talablar.","Muhitning bola rivojlanishidagi roli."],"sections":[
("Rivojlantiruvchi muhit tushunchasi va mohiyati",[
"Rivojlantiruvchi muhit \u2014 bolaning har tomonlama kamol topishiga xizmat qiladigan, maxsus tashkil etilgan moddiy va ijtimoiy sharoitlar majmuasidir. U guruh xonasi, jihozlar, materiallar, o\u2018yinchoqlar hamda bola bilan kattalar va tengdoshlar o\u2018rtasidagi munosabatlarni o\u2018z ichiga oladi.",
"Rivojlantiruvchi muhitning mohiyati shundaki, u bolani faol harakatga, izlanishga va ijodga undaydi. Yaxshi tashkil etilgan muhitda bola o\u2018zini erkin, xavfsiz va qulay his qiladi, o\u2018z qiziqishlarini namoyon etadi va mustaqil ravishda yangi bilim hamda ko\u2018nikmalarni egallaydi.",
"Maktabgacha yoshda muhit \u2014 \u201cuchinchi tarbiyachi\u201d deb ataladi (birinchi va ikkinchisi \u2014 ota-ona va tarbiyachi). Chunki to\u2018g\u2018ri tashkil etilgan muhit bolaga sezilmas tarzda ta\u2019sir ko\u2018rsatadi, uning faoliyatini yo\u2018naltiradi va rivojlanishini rag\u2018batlantiradi."]),
("Rivojlantiruvchi muhitning tarkibiy qismlari",[
"Rivojlantiruvchi muhit ikki asosiy qismdan iborat: moddiy (predmetli) muhit va ijtimoiy muhit. Moddiy muhit \u2014 bino, xona, mebel, jihozlar, o\u2018yinchoqlar, didaktik materiallar, kitoblar va boshqa narsalardir.",
"Ijtimoiy muhit \u2014 bola atrofidagi insonlar, ya\u2019ni tarbiyachilar, tengdoshlar, ota-onalar va ular o\u2018rtasidagi munosabatlardir. Iliq, mehribon, ishonchli ijtimoiy muhit bolaning hissiy farovonligini ta\u2019minlaydi va rivojlanishi uchun zamin yaratadi.",
"Moddiy muhit guruh ichida (xona) va guruhdan tashqarida (musiqa zali, sport zali, hovli, ekologik maydon) bo\u2018ladi. Ichki muhit rivojlantiruvchi markazlarga bo\u2018linadi. Tashqi muhit esa bolaning harakat faoliyati, tabiat bilan muloqoti uchun xizmat qiladi."]),
("Rivojlantiruvchi muhitga qo\u2018yiladigan talablar",[
"Rivojlantiruvchi muhit bir qator talablarga javob berishi kerak. Xavfsizlik \u2014 muhitdagi barcha narsalar bola hayoti va sog\u2018lig\u2018i uchun xavfsiz bo\u2018lishi shart. Sog\u2018lomlashtiruvchilik \u2014 yetarli yorug\u2018lik, toza havo, qulay harorat ta\u2019minlanishi kerak.",
"Moslashuvchanlik va o\u2018zgaruvchanlik \u2014 muhit bolalar yoshi, qiziqishlari va mavsumga qarab o\u2018zgarib turishi lozim. Mazmunan boylik \u2014 muhit bolaning barcha rivojlanish sohalarini qamrab oluvchi materiallar bilan to\u2018ldirilgan bo\u2018lishi kerak.",
"Qulaylik va estetiklik \u2014 muhit chiroyli, ozoda, uyg\u2018un rangda bezatilgan bo\u2018lishi, bolada ijobiy kayfiyat uyg\u2018otishi lozim. Erkinlik va mustaqillik \u2014 materiallar bola mustaqil foydalanishi mumkin bo\u2018lgan tarzda joylashtiriladi. Bu talablar muhit samaradorligini oshiradi."]),
("Muhitning bola rivojlanishidagi roli",[
"To\u2018g\u2018ri tashkil etilgan rivojlantiruvchi muhit bolaning jismoniy rivojlanishiga yordam beradi: harakat markazlari, sport jihozlari bola harakat faolligini, mayda va yirik motorikani rivojlantiradi. Muhit shuningdek bilish jarayonini faollashtiradi.",
"Rivojlantiruvchi muhit bolaning ijtimoiy-hissiy rivojlanishida ham muhim. Birgalikdagi o\u2018yinlar, rolli o\u2018yin markazlari bolani muloqotga, hamkorlikka, his-tuyg\u2018ularni boshqarishga o\u2018rgatadi. Bola jamoada o\u2018zini tutishni, qoidalarga rioya qilishni o\u2018rganadi.",
"Muhit bolaning nutqiy va ijodiy rivojlanishiga ham hissa qo\u2018shadi. Kitob burchagi, til markazlari nutqni boyitadi, san\u2019at va musiqa markazlari ijodiy qobiliyatlarni ochadi. Shunday qilib, rivojlantiruvchi muhit bola shaxsining barcha qirralarini uyg\u2018un rivojlantirishga xizmat qiladi."])]})

TOPICS.append({"num":3,"title":"Guruh yoshi nisbatida rivojlantiruvchi muhitning tashkil etilishi. Rivojlantiruvchi markazlari tasnifi","reja":[
"Yoshga mos rivojlantiruvchi muhitni tashkil etish zarurati.","Turli yosh guruhlarida muhitning xususiyatlari.","Rivojlantiruvchi markazlarning tasnifi.","Markazlarni yoshga moslab jihozlash."],"sections":[
("Yoshga mos rivojlantiruvchi muhitni tashkil etish zarurati",[
"Bolaning har bir yosh davri o\u2018ziga xos rivojlanish xususiyatlariga, ehtiyojlariga va imkoniyatlariga ega. Shu sababli rivojlantiruvchi muhit ham guruh bolalarining yoshiga moslab tashkil etilishi kerak. Yoshga mos kelmaydigan muhit bola rivojlanishiga to\u2018sqinlik qilishi mumkin.",
"Yoshga mos tashkil etish tamoyili shuni anglatadiki, jihozlar, o\u2018yinchoqlar va materiallarning murakkabligi, hajmi, miqdori va mazmuni bolalar yoshiga mutanosib bo\u2018lishi lozim. Masalan, kichik guruh bolalari uchun yirik, oddiy o\u2018yinchoqlar, katta guruh uchun esa murakkabroq materiallar tanlanadi.",
"Yoshga mos muhit \u201cyaqin rivojlanish zonasi\u201d tamoyiliga asoslanadi. Ya\u2019ni muhit bolaga hozirgi imkoniyatidan biroz yuqoriroq vazifalarni taklif etishi kerak, shunda bola rivojlanishga intiladi. Juda oson yoki juda qiyin muhit bolani qiziqtirmaydi."]),
("Turli yosh guruhlarida muhitning xususiyatlari",[
"Kichik yoshli (3-4 yosh) guruhda muhit harakat va sezgi rivojiga qaratiladi. Yirik, yorqin, xavfsiz o\u2018yinchoqlar, sensor materiallar, harakat uchun bo\u2018sh joy ta\u2019minlanadi. Bolalar narsalarni ushlash, taqqoslash orqali bilib oladi.",
"O\u2018rta yoshli (4-5 yosh) guruhda muhit rolli o\u2018yinlar, til va bilish faoliyatiga boyitiladi. Bolalar tasavvuri rivojlanayotgani uchun rolli o\u2018yin atributlari, qurilish materiallari, sodda didaktik o\u2018yinlar qo\u2018shiladi.",
"Katta yoshli (5-7 yosh) guruhda muhit maktabga tayyorlovga qaratiladi. Harf va raqamlar, yozuv-chizuv materiallari, murakkab boshqotirmalar, tajriba o\u2018tkazish uchun jihozlar joylashtiriladi. Bolalar mustaqil izlanish, tajriba va loyihalar bilan shug\u2018ullanadi."]),
("Rivojlantiruvchi markazlarning tasnifi",[
"Rivojlantiruvchi markazlar bola rivojlanishining sohalariga ko\u2018ra tasniflanadi. Asosiy markazlar quyidagilar: til va nutq (savodxonlik) markazi; qurish-yasash va matematika markazi; tabiat va ilmiy tajriba markazi; san\u2019at (tasviriy faoliyat) markazi.",
"Shuningdek rolli (syujetli) o\u2018yin markazi; musiqa va teatr markazi; kitob (mutolaa) burchagi; harakat (jismoniy tarbiya) markazi; qum va suv bilan o\u2018ynash markazi kabilar mavjud. Har bir markaz muayyan rivojlanish sohasiga xizmat qiladi.",
"Markazlar shuningdek joylashuviga ko\u2018ra (ichki va tashqi), faoliyat turiga ko\u2018ra (jim va shovqinli), foydalanish muddatiga ko\u2018ra (doimiy va vaqtinchalik) tasniflanadi. Jim markazlar (kitob, til) va shovqinli markazlar (qurilish, harakat) bir-biridan ajratib joylashtiriladi."]),
("Markazlarni yoshga moslab jihozlash",[
"Markazlarni jihozlashda bolalar yoshi hisobga olinadi. Kichik guruhda har bir markazda kam, lekin yirik va oddiy materiallar bo\u2018ladi. Bolalar diqqati tez tarqalgani uchun materiallar sodda va ko\u2018rgazmali bo\u2018lishi kerak.",
"Yosh ortgan sari markazlardagi materiallar soni va murakkabligi oshiriladi. Katta guruhda markazlar boy va xilma-xil materiallar bilan ta\u2019minlanadi, bola tanlash imkoni kengayadi. Materiallar bolaning mustaqil, ijodiy faoliyatini rag\u2018batlantirishi kerak.",
"Tarbiyachi markazlarni doimiy kuzatib boradi va bolalar rivojlanishiga qarab yangilab turadi. Bola materialdan to\u2018liq foydalanib bo\u2018lgach yoki unga qiziqishi yo\u2018qolgach, yangi, murakkabroq material taklif etiladi. Bu rivojlanishning uzluksizligini ta\u2019minlaydi."])]})

TOPICS.append({"num":4,"title":"Mavzuli rejalashtirish metodik qo\u2018llanmasidan foydalangan holda rivojlanish markazlarida ta'limiy faoliyatni tashkil etish","reja":[
"Mavzuli rejalashtirish tushunchasi va ahamiyati.","Mavzuli rejalashtirish metodik qo\u2018llanmasining tuzilishi.","Markazlarda ta\u2019limiy faoliyatni rejalashtirish.","Mavzuga mos faoliyat tashkil etish bosqichlari."],"sections":[
("Mavzuli rejalashtirish tushunchasi va ahamiyati",[
"Mavzuli rejalashtirish \u2014 ta\u2019lim-tarbiya jarayonini muayyan mavzular atrofida birlashtirib rejalashtirish usulidir. Har bir mavzu bir hafta yoki bir necha hafta davom etadi va shu davrda barcha faoliyat turlari shu mavzuga bo\u2018ysundiriladi.",
"Bu yondashuvning ahamiyati shundaki, bola bir mavzuni turli faoliyat orqali \u2014 o\u2018yin, kuzatish, suhbat, tasviriy san\u2019at, musiqa orqali har tomonlama o\u2018rganadi. Bu bilimning chuqur, mustahkam va o\u2018zaro bog\u2018liq holda o\u2018zlashtirilishini ta\u2019minlaydi.",
"Mavzuli rejalashtirish bolaning yaxlit dunyoqarashini shakllantiradi. Bola atrofidagi olamni alohida-alohida emas, balki o\u2018zaro bog\u2018liq tizim sifatida idrok etadi. Masalan, \u201cFasllar\u201d mavzusi orqali bola tabiat, kiyim, oziq-ovqat, bayramlar haqida birgalikda o\u2018rganadi."]),
("Mavzuli rejalashtirish metodik qo\u2018llanmasining tuzilishi",[
"Mavzuli rejalashtirish metodik qo\u2018llanmasi tarbiyachiga ish rejasini tuzishda yordam beradigan asosiy hujjatdir. Unda o\u2018quv yili davomida o\u2018rganiladigan mavzular ro\u2018yxati, har bir mavzuning maqsadi va vazifalari belgilab beriladi.",
"Qo\u2018llanmada har bir mavzu bo\u2018yicha taklif etiladigan faoliyat turlari, markazlarda o\u2018tkaziladigan ishlar, didaktik o\u2018yinlar, kuzatishlar, suhbatlar va kutilayotgan natijalar ko\u2018rsatiladi. Bu tarbiyachi ishini yengillashtiradi va tizimli qiladi.",
"Qo\u2018llanma bola rivojlanishining besh sohasini hisobga olgan holda tuzilgan. Har bir mavzu jismoniy, ijtimoiy-hissiy, nutqiy, bilish va ijodiy rivojlanishni qamrab oladi. Tarbiyachi qo\u2018llanmadan ijodiy foydalanib, o\u2018z guruhi xususiyatlariga moslaydi."]),
("Markazlarda ta\u2019limiy faoliyatni rejalashtirish",[
"Markazlarda ta\u2019limiy faoliyatni rejalashtirishda tarbiyachi avval haftalik mavzuni belgilaydi. So\u2018ngra har bir rivojlantiruvchi markazda shu mavzu bo\u2018yicha qanday faoliyat tashkil etilishini o\u2018ylab chiqadi va materiallar tayyorlaydi.",
"Masalan, mavzu \u201cMevalar\u201d bo\u2018lsa, til markazida mevalar nomi va she\u2019rlar, matematika markazida mevalarni sanash, san\u2019at markazida meva chizish, tabiat markazida mevalarni kuzatish faoliyatlari rejalashtiriladi. Shunday qilib mavzu barcha markazlarga singdiriladi.",
"Rejalashtirishda bolalarning qiziqishlari, oldingi bilimlari va rivojlanish darajasi hisobga olinadi. Tarbiyachi faoliyatlarni oson dan murakkabga, ma\u2019lumdan noma\u2019lumga tomon tartiblaydi. Har bir markaz uchun aniq maqsad va kutilayotgan natija belgilanadi."]),
("Mavzuga mos faoliyat tashkil etish bosqichlari",[
"Birinchi bosqich \u2014 mavzuga kirish. Tarbiyachi ertalabki davra suhbatida yangi mavzuni e\u2019lon qiladi, bolalarning mavzu haqidagi bilimlarini aniqlaydi, qiziqish uyg\u2018otadi. Bu bosqichda mavzuga oid materiallar markazlarga joylashtiriladi.",
"Ikkinchi bosqich \u2014 mavzuni o\u2018rganish. Bolalar erkin faoliyat vaqtida markazlarda mavzu bo\u2018yicha ishlaydi. Tarbiyachi kuzatadi, savol beradi, yo\u2018naltiradi. Tashkil etilgan mashg\u2018ulotlar ham shu mavzuga bag\u2018ishlanadi.",
"Uchinchi bosqich \u2014 mavzuni yakunlash va baholash. Hafta oxirida bolalar o\u2018rgangan bilimlari namoyish etiladi (ko\u2018rgazma, ertalik, loyiha taqdimoti). Tarbiyachi natijalarni baholaydi, bolalar rivojlanishini kuzatadi va keyingi mavzu uchun xulosa chiqaradi."])]})

TOPICS.append({"num":5,"title":"Maktabgacha ta'lim tashkilotlarida rivojlantiruvchi markazlari","reja":[
"Rivojlantiruvchi markazlar tizimi.","Asosiy markazlar va ularning vazifalari.","Markazlarni guruh xonasida joylashtirish.","Markazlar faoliyatini boshqarish."],"sections":[
("Rivojlantiruvchi markazlar tizimi",[
"Maktabgacha ta\u2019lim tashkilotlarida rivojlantiruvchi markazlar yaxlit tizimni tashkil etadi. Bu tizim bolaning barcha rivojlanish sohalarini qamrab oladi va uning har tomonlama kamol topishiga xizmat qiladi. Markazlar bir-birini to\u2018ldiradi va o\u2018zaro bog\u2018liq ishlaydi.",
"Markazlar tizimi \u201cIlk qadam\u201d davlat o\u2018quv dasturi talablariga muvofiq tuziladi. Har bir guruh xonasida bolalar yoshi va imkoniyatiga mos ravishda bir necha markaz tashkil etiladi. Markazlar soni xona maydoniga va bolalar soniga bog\u2018liq.",
"Markazlar tizimining asosiy g\u2018oyasi \u2014 bolaga tanlash erkinligini berish va uning mustaqil faoliyatini ta\u2019minlash. Bola o\u2018zi qiziqqan markazni tanlaydi, o\u2018z sur\u2019atida ishlaydi. Bu individual yondashuvni amalga oshirish imkonini beradi."]),
("Asosiy markazlar va ularning vazifalari",[
"Til va nutq (savodxonlik) markazi nutqni rivojlantiradi, lug\u2018atni boyitadi, o\u2018qish va yozishga tayyorlaydi. Qurish-yasash va matematika markazi mantiqiy tafakkur, fazoviy tasavvur va matematik tushunchalarni shakllantiradi.",
"Tabiat va ilmiy tajriba markazi bolada atrof-olamga qiziqish, kuzatuvchanlik va tadqiqotchilik ko\u2018nikmasini rivojlantiradi. San\u2019at markazi ijodiy qobiliyat, mayda motorika va estetik didni tarbiyalaydi. Rolli o\u2018yin markazi ijtimoiy ko\u2018nikma va tasavvurni rivojlantiradi.",
"Musiqa va teatr markazi badiiy-estetik tuyg\u2018u va ifoda qobiliyatini, kitob burchagi nutq va mutolaa madaniyatini, harakat markazi jismoniy faollik va sog\u2018liqni mustahkamlaydi. Har bir markaz o\u2018ziga xos vazifani bajaradi va birgalikda bolani har tomonlama rivojlantiradi."]),
("Markazlarni guruh xonasida joylashtirish",[
"Markazlarni joylashtirishda bir qancha qoidalarga rioya qilinadi. Jim markazlar (kitob, til, san\u2019at) yorug\u2018, tinch joyga, shovqinli markazlar (qurilish, rolli o\u2018yin, harakat) bir-biriga yaqin, lekin jim markazlardan uzoqroqqa joylashtiriladi.",
"Suv va tabiat markazlari suv manbai yaqiniga, san\u2019at markazi yuvinish joyiga yaqin joylashtirilsa qulay bo\u2018ladi. Markazlar o\u2018rtasida bolalar erkin harakatlanishi uchun yo\u2018laklar qoldiriladi. Har bir markaz aniq chegaralangan va belgilangan bo\u2018ladi.",
"Markazlar tabiiy yorug\u2018likdan unumli foydalanadigan tarzda derazaga nisbatan joylashtiriladi. Materiallar past, ochiq tokchalarda, bola qo\u2018li yetadigan balandlikda turadi. Har bir markaz nomi yozma va rasmli ko\u2018rsatkich bilan belgilanadi."]),
("Markazlar faoliyatini boshqarish",[
"Tarbiyachi markazlar faoliyatini kun tartibiga muvofiq boshqaradi. Ertalabki davra suhbatida bolalar bilan markazlardagi faoliyat rejasi muhokama qilinadi. Bolalar qaysi markazda ishlashni o\u2018zlari rejalashtiradi.",
"Erkin faoliyat vaqtida tarbiyachi kuzatuvchi va yordamchi rolida bo\u2018ladi. U bolalar faoliyatini kuzatadi, kerak bo\u2018lganda savol beradi, qiyinchilikda yordam beradi, lekin bola mustaqilligini cheklamaydi. Har bir markazda bolalar soni nazorat qilinadi.",
"Markazlar faoliyati yakunida bolalar o\u2018z ishlarini joyiga yig\u2018ishtiradi va davra suhbatida nima qilganini, nimani bilib olganini gapirib beradi. Tarbiyachi bolalar faoliyatini baholaydi va kuzatuv natijalarini rivojlanish kartasiga qayd etadi."])]})


TOPICS.append({"num":6,"title":"Mavzu asosida rivojlantirish markazlarini jihozlash, ulardan va AKTdan mashg\u2018ulot jarayonida foydalanish","reja":[
"Markazlarni mavzuga moslab jihozlash.","Jihozlash uchun materiallar va vositalar.","AKT (axborot-kommunikatsiya texnologiyalari) tushunchasi.","AKTdan mashg\u2018ulot jarayonida foydalanish."],"sections":[
("Markazlarni mavzuga moslab jihozlash",[
"Mavzuga moslab jihozlash \u2014 har bir hafta yoki davr mavzusiga muvofiq markazlardagi materiallarni yangilab borishni anglatadi. Tarbiyachi mavzuni e\u2019lon qilgach, har bir markazga shu mavzuga oid qo\u2018shimcha jihoz va materiallar joylashtiradi.",
"Masalan, \u201cTransport\u201d mavzusida til markaziga transport rasmlari va kitoblari, qurilish markaziga mashina va yo\u2018l maketlari, san\u2019at markaziga transport andozalari qo\u2018yiladi. Shunday qilib bola mavzuni har bir markazda turli faoliyat orqali o\u2018rganadi.",
"Mavzuga moslab jihozlashda tarbiyachi materiallarning xilma-xilligini, bolalar yoshiga mosligini va rivojlantiruvchi qiymatini hisobga oladi. Eskirgan yoki mavzuga aloqasi yo\u2018q materiallar olib qo\u2018yiladi, ularning o\u2018rniga yangi, qiziqarli materiallar taklif etiladi."]),
("Jihozlash uchun materiallar va vositalar",[
"Markazlarni jihozlashda turli xil materiallardan foydalaniladi. Tabiiy materiallar: tosh, qum, suv, barg, urug\u2018, yong\u2018oq, shox-shabba. Bu materiallar bolaning sensor rivojiga, tabiatni bilishiga yordam beradi va arzon hamda ekologik tozadir.",
"Sanoat materiallari: tayyor o\u2018yinchoqlar, konstruktorlar, didaktik o\u2018yinlar, kitoblar, qalam-bo\u2018yoqlar. Qo\u2018lbola (atrofdagi) materiallar: karton qutilar, plastik idishlar, mato bo\u2018laklari, tugma, ip \u2014 bularni tarbiyachi va ota-onalar tayyorlaydi.",
"Materiallarni tanlashda xavfsizlik birinchi o\u2018rinda turadi: ular o\u2018tkir, mayda (yutib yuborilishi mumkin), zaharli bo\u2018lmasligi kerak. Materiallar mustahkam, yuvilishi mumkin va estetik jihatdan chiroyli bo\u2018lishi lozim. Ular bolaning faolligini va ijodini rag\u2018batlantirishi kerak."]),
("AKT (axborot-kommunikatsiya texnologiyalari) tushunchasi",[
"AKT \u2014 axborot-kommunikatsiya texnologiyalari \u2014 axborotni yig\u2018ish, saqlash, qayta ishlash va uzatish uchun ishlatiladigan zamonaviy texnik vositalar va dasturlar majmuasidir. Bularga kompyuter, proyektor, interaktiv doska, planshet, audio va video qurilmalar kiradi.",
"Maktabgacha ta\u2019limda AKT ta\u2019lim jarayonini boyitish, ko\u2018rgazmali qilish va qiziqarli o\u2018tkazish vositasi sifatida foydalaniladi. Multimedia taqdimotlar, o\u2018quv multfilmlari, interaktiv o\u2018yinlar bola e\u2019tiborini jalb etadi va materialni yaxshi o\u2018zlashtirishga yordam beradi.",
"Shu bilan birga, maktabgacha yoshda AKTdan foydalanish me\u2019yorida bo\u2018lishi kerak. Bola ekran oldida ko\u2018p vaqt o\u2018tkazmasligi (kuniga 10-15 daqiqadan oshmasligi), AKT faqat jonli faoliyatni to\u2018ldiruvchi vosita sifatida ishlatilishi lozim. Salomatlik talablariga qat\u2019iy rioya qilinadi."]),
("AKTdan mashg\u2018ulot jarayonida foydalanish",[
"AKTdan mashg\u2018ulotda foydalanishning turli usullari bor. Multimedia taqdimotlar yordamida tarbiyachi mavzuni ko\u2018rgazmali tushuntiradi (masalan, hayvonlar, kosmos, fasllar haqida rasm va video). Bu bolaga real ko\u2018rsatib bo\u2018lmaydigan narsalarni ko\u2018rsatish imkonini beradi.",
"Interaktiv o\u2018yinlar va didaktik dasturlar orqali bola raqam, harf, rang, shaklni o\u2018rganadi. Audio yozuvlar (qo\u2018shiqlar, ertaklar, tabiat tovushlari) musiqa va nutq rivojiga xizmat qiladi. Interaktiv doska bilan bolalar guruh bo\u2018lib faol ishlaydi.",
"AKTdan foydalanishda tarbiyachi tayyorgarlik ko\u2018radi: jihozlarni tekshiradi, materialni oldindan tanlaydi va mashg\u2018ulot maqsadiga moslaydi. AKT mashg\u2018ulotning faqat bir qismida ishlatiladi, bola asosan amaliy, jonli faoliyat bilan shug\u2018ullanishi kerak. Bu uyg\u2018unlik samaradorlikni oshiradi."])]})

TOPICS.append({"num":7,"title":"\u201cIlk qadam\u201d davlat o\u2018quv dasturining mazmun, mohiyati","reja":[
"\u201cIlk qadam\u201d dasturining yaratilishi va maqsadi.","Dasturning mazmuni va tarkibi.","Dasturning asosiy tamoyillari.","Dasturning mohiyati va ahamiyati."],"sections":[
("\u201cIlk qadam\u201d dasturining yaratilishi va maqsadi",[
"\u201cIlk qadam\u201d \u2014 O\u2018zbekiston Respublikasi maktabgacha ta\u2019lim tizimi uchun ishlab chiqilgan davlat o\u2018quv dasturidir. U xalqaro tajriba va zamonaviy pedagogik yondashuvlar asosida, milliy qadriyatlarni hisobga olgan holda yaratilgan.",
"Dasturning asosiy maqsadi \u2014 3 yoshdan 7 yoshgacha bo\u2018lgan bolalarni maktab ta\u2019limiga va hayotga har tomonlama tayyorlash, ularning jismoniy, aqliy, ma\u2019naviy va ijtimoiy rivojlanishini ta\u2019minlashdir. Dastur har bir bolaning individual rivojlanishini qo\u2018llab-quvvatlaydi.",
"\u201cIlk qadam\u201d nomi ramziy ma\u2019noga ega \u2014 bu bolaning bilim olish, mustaqil hayotga qadam qo\u2018yishidagi birinchi qadamlari. Dastur shu birinchi qadamlarni ishonchli, mustahkam va to\u2018g\u2018ri qo\u2018yishga yordam beradi."]),
("Dasturning mazmuni va tarkibi",[
"\u201cIlk qadam\u201d dasturi bola rivojlanishining besh asosiy sohasini qamrab oladi. Birinchisi \u2014 jismoniy rivojlanish va sog\u2018lom turmush tarzi. Ikkinchisi \u2014 ijtimoiy-hissiy rivojlanish, ya\u2019ni his-tuyg\u2018ularni boshqarish, muloqot va o\u2018zaro munosabat.",
"Uchinchi soha \u2014 nutq, muloqot, o\u2018qish va yozish malakalari. To\u2018rtinchisi \u2014 bilish jarayonining rivojlanishi (matematika, atrof-olam, tabiat). Beshinchisi \u2014 badiiy-estetik va ijodiy rivojlanish (tasviriy san\u2019at, musiqa, ijod).",
"Har bir soha bo\u2018yicha dasturda yosh davrlariga mos rivojlanish ko\u2018rsatkichlari (standartlari) belgilangan. Bu ko\u2018rsatkichlar bola muayyan yoshda nimalarni bilishi va qila olishi kerakligini ko\u2018rsatadi. Ular tarbiyachiga mo\u2018ljal beradi va rivojlanishni baholash imkonini yaratadi."]),
("Dasturning asosiy tamoyillari",[
"Dastur bir qator pedagogik tamoyillarga asoslanadi. Bolaga yo\u2018naltirilganlik tamoyili \u2014 ta\u2019lim jarayoni markazida bola, uning ehtiyojlari va qiziqishlari turadi. Individuallashtirish tamoyili \u2014 har bir bola o\u2018ziga xosligini hisobga olib ishlash.",
"O\u2018yin orqali rivojlanish tamoyili \u2014 maktabgacha yoshda o\u2018yin yetakchi faoliyat bo\u2018lib, bola o\u2018yin orqali o\u2018rganadi. Faollik tamoyili \u2014 bola passiv tinglovchi emas, balki faol ishtirokchi, izlanuvchi va kashfiyotchi bo\u2018lishi kerak.",
"Yaxlitlik tamoyili \u2014 bola shaxsi yaxlit rivojlantiriladi, barcha sohalar uyg\u2018un bog\u2018lanadi. Hamkorlik tamoyili \u2014 ta\u2019lim-tarbiya bola, oila va ta\u2019lim tashkiloti hamkorligida amalga oshiriladi. Bu tamoyillar dasturning samaradorligini ta\u2019minlaydi."]),
("Dasturning mohiyati va ahamiyati",[
"Dasturning mohiyati shundaki, u bolani an\u2019anaviy, tarbiyachi markazli o\u2018qitishdan bola markazli, rivojlantiruvchi ta\u2019limga yo\u2018naltiradi. Bola tayyor bilimni emas, balki bilim olish, fikrlash, izlanish ko\u2018nikmalarini egallaydi.",
"Dastur bolaning mustaqilligini, tashabbuskorligini, ijodkorligini va tanqidiy fikrlashini rivojlantirishga qaratilgan. Bu sifatlar zamonaviy hayotda va kelajakdagi ta\u2019limda muhim ahamiyatga ega. Bola o\u2018rganishni sevishni va o\u2018rganishga qiziqishni o\u2018rganadi.",
"\u201cIlk qadam\u201d dasturining ahamiyati shundaki, u maktabgacha ta\u2019lim sifatini oshiradi, barcha bolalar uchun teng imkoniyatlar yaratadi va ularni maktabga yaxshi tayyorlaydi. Dastur maktabgacha ta\u2019limni zamonaviy talablar darajasiga ko\u2018taradi."])]})

TOPICS.append({"num":8,"title":"\u201cIlk qadam\u201d davlat o\u2018quv dasturining maqsad va vazifasi. \u201cIlk qadam\u201d davlat o\u2018quv dasturi asosida nashr qilingan","reja":[
"Dasturning maqsadi.","Dasturning asosiy vazifalari.","Dastur asosida nashr qilingan metodik materiallar.","Nashrlardan amaliyotda foydalanish."],"sections":[
("Dasturning maqsadi",[
"\u201cIlk qadam\u201d davlat o\u2018quv dasturining bosh maqsadi \u2014 maktabgacha yoshdagi har bir bolaning to\u2018liq va har tomonlama rivojlanishini ta\u2019minlash, uni maktab ta\u2019limiga va kelajakdagi mustaqil hayotga tayyorlashdir. Dastur bola salohiyatini ochishga qaratilgan.",
"Maqsad bolaning jismoniy salomatligini mustahkamlash, aqliy qobiliyatlarini rivojlantirish, ma\u2019naviy-axloqiy fazilatlarini shakllantirish va ijtimoiy ko\u2018nikmalarini tarbiyalashni o\u2018z ichiga oladi. Bola sog\u2018lom, bilimli, odobli va mehnatsevar bo\u2018lib voyaga yetishi ko\u2018zda tutiladi.",
"Dastur maqsadi har bir bolaning individualligini hisobga olishni nazarda tutadi. Maqsad barcha bolalarni bir qolipga solish emas, balki har birining o\u2018ziga xos qobiliyatlarini, qiziqishlarini va imkoniyatlarini ochib berishdir. Bu inson shaxsini ulug\u2018lash g\u2018oyasiga asoslanadi."]),
("Dasturning asosiy vazifalari",[
"Dasturning birinchi vazifasi \u2014 bola sog\u2018lig\u2018ini muhofaza qilish va jismoniy rivojlanishini ta\u2019minlash, sog\u2018lom turmush tarzi ko\u2018nikmalarini shakllantirish. Ikkinchi vazifa \u2014 bolaning bilish faolligini, qiziquvchanligini va tafakkurini rivojlantirish.",
"Uchinchi vazifa \u2014 bolaning nutqini boyitish, muloqot ko\u2018nikmalarini va savodxonlik asoslarini shakllantirish. To\u2018rtinchi vazifa \u2014 ijtimoiy-hissiy rivojlanishni ta\u2019minlash, ya\u2019ni bolani jamoada yashashga, hamkorlikka, his-tuyg\u2018ularni boshqarishga o\u2018rgatish.",
"Beshinchi vazifa \u2014 bolaning ijodiy va badiiy-estetik qobiliyatlarini rivojlantirish, go\u2018zallikni his etish va yaratish ko\u2018nikmasini tarbiyalash. Oltinchi vazifa \u2014 oila bilan hamkorlikni mustahkamlash. Bu vazifalar birgalikda bola shaxsini har tomonlama shakllantiradi."]),
("Dastur asosida nashr qilingan metodik materiallar",[
"\u201cIlk qadam\u201d dasturi asosida tarbiyachilar uchun bir qator metodik materiallar nashr etilgan. Bularning asosiysi \u2014 mavzuli rejalashtirish bo\u2018yicha metodik qo\u2018llanma bo\u2018lib, u o\u2018quv yili davomidagi mavzular va faoliyat rejasini taqdim etadi.",
"Shuningdek tarbiyachilar uchun metodik tavsiyalar, didaktik o\u2018yinlar to\u2018plamlari, bolalar rivojlanishini kuzatish va baholash bo\u2018yicha materiallar, har bir rivojlanish sohasi bo\u2018yicha qo\u2018llanmalar nashr qilingan. Bular tarbiyachi ishini tizimli va samarali qiladi.",
"Bolalar uchun ham maxsus didaktik materiallar, ish daftarlari, rasmli kitoblar tayyorlangan. Ota-onalar uchun esa bola tarbiyasi bo\u2018yicha tavsiyalar va qo\u2018llanmalar chop etilgan. Bu nashrlar dasturni amaliyotga to\u2018liq joriy etishga xizmat qiladi."]),
("Nashrlardan amaliyotda foydalanish",[
"Tarbiyachi nashr etilgan metodik materiallardan o\u2018z ish faoliyatida keng foydalanadi. Metodik qo\u2018llanma asosida u kunlik va haftalik ish rejasini tuzadi, mashg\u2018ulotlarni rejalashtiradi va markazlardagi faoliyatni tashkil etadi.",
"Didaktik o\u2018yin to\u2018plamlari va materiallaridan tarbiyachi bolalar bilan ishlashda foydalanadi. Kuzatish va baholash materiallari yordamida bolalar rivojlanishini muntazam kuzatib boradi va natijalarni qayd etadi. Bu individual ishni tashkil etishga yordam beradi.",
"Tarbiyachi nashrlardan ijodiy foydalanishi muhim. U tayyor materiallarni o\u2018z guruhining xususiyatlariga, bolalarning qiziqishlari va imkoniyatlariga moslab qo\u2018llaydi. Materiallarni mexanik takrorlash emas, balki ijodiy boyitish kutiladi. Ota-onalar bilan ishlashda ham nashrlar foydalidir."])]})

TOPICS.append({"num":9,"title":"Maktabgacha yoshdagi bolalarga ta'lim berishda kompetensiyaviy yondashuv","reja":[
"Kompetensiya va kompetensiyaviy yondashuv tushunchasi.","Maktabgacha ta\u2019limda kompetensiyaviy yondashuvning mohiyati.","Kompetensiyaviy yondashuvni amalga oshirish usullari.","Yondashuvning afzalliklari va natijalari."],"sections":[
("Kompetensiya va kompetensiyaviy yondashuv tushunchasi",[
"Kompetensiya \u2014 bilim, ko\u2018nikma va malakalarni amaliy vaziyatlarda qo\u2018llay olish qobiliyatidir. Bu nafaqat bilimga ega bo\u2018lish, balki shu bilimni hayotda, real holatlarda ishlata olishni anglatadi. Kompetensiya \u2014 \u201cbilaman\u201d emas, \u201cqila olaman\u201d demakdir.",
"Kompetensiyaviy yondashuv \u2014 ta\u2019limni bilim to\u2018plashga emas, balki amaliy qobiliyat va ko\u2018nikmalarni shakllantirishga yo\u2018naltirilgan zamonaviy pedagogik yondashuvdir. Bu yondashuvda muhimi \u2014 bola olgan bilimini hayotda qo\u2018llay olishidir.",
"Bu yondashuv an\u2019anaviy ta\u2019limdan farq qiladi. An\u2019anaviy ta\u2019limda bola tayyor bilimni yodlaydi, kompetensiyaviy yondashuvda esa bola faol izlanadi, muammoni hal qiladi, mustaqil xulosaga keladi. Bilim vosita, qobiliyat esa natija hisoblanadi."]),
("Maktabgacha ta\u2019limda kompetensiyaviy yondashuvning mohiyati",[
"Maktabgacha ta\u2019limda kompetensiyaviy yondashuvning mohiyati \u2014 bolada hayotiy ko\u2018nikmalarni shakllantirishdir. Bola nafaqat harf yoki raqamni bilishi, balki muloqot qila olishi, muammoni hal qila olishi, mustaqil qaror qabul qila olishi kerak.",
"\u201cIlk qadam\u201d dasturi kompetensiyaviy yondashuvga asoslangan. Dasturda bolaning rivojlanish sohalari bo\u2018yicha kompetensiyalar belgilangan. Tarbiyachi bolaga tayyor bilim bermaydi, balki uni mustaqil bilim olishga, izlanishga va kashf etishga undaydi.",
"Bu yondashuvda bola faol subyekt sifatida ko\u2018riladi. U o\u2018yin va amaliy faoliyat orqali tajriba orttiradi, xato qiladi va xatosidan o\u2018rganadi. Tarbiyachi esa yo\u2018naltiruvchi, qo\u2018llab-quvvatlovchi va sharoit yaratuvchi rolini bajaradi. Bola o\u2018rganishning markazida turadi."]),
("Kompetensiyaviy yondashuvni amalga oshirish usullari",[
"Kompetensiyaviy yondashuvni amalga oshirishda o\u2018yin asosiy usul hisoblanadi. O\u2018yin orqali bola tabiiy ravishda muloqot, hamkorlik, muammoni hal qilish ko\u2018nikmalarini egallaydi. Rolli o\u2018yinlar ijtimoiy kompetensiyani rivojlantiradi.",
"Loyiha usuli, muammoli vaziyatlar yaratish, tajriba va kuzatish o\u2018tkazish keng qo\u2018llaniladi. Bola savol beradi, gipoteza ilgari suradi, sinab ko\u2018radi va xulosa chiqaradi. Bu izlanish va tadqiqotchilik kompetensiyasini shakllantiradi.",
"Rivojlantiruvchi markazlardagi mustaqil faoliyat, kichik guruhlarda ishlash, atrof-muhit bilan faol muloqot ham muhim usullardir. Tarbiyachi ochiq savollar beradi, bolani fikrlashga undaydi, mustaqil qaror qabul qilishga imkon beradi. Bu kompetensiyalarni rivojlantiradi."]),
("Yondashuvning afzalliklari va natijalari",[
"Kompetensiyaviy yondashuvning asosiy afzalligi \u2014 bola olgan bilimini hayotda qo\u2018llay oladi. U faqat yodlamaydi, balki tushunadi, fikrlaydi va amalda foydalanadi. Bu bilimning mustahkam va amaliy bo\u2018lishini ta\u2019minlaydi.",
"Bu yondashuv bolaning mustaqilligini, tashabbuskorligini, ijodkorligini va o\u2018ziga ishonchini oshiradi. Bola muammolarni mustaqil hal qilishni, qaror qabul qilishni va mas\u2019uliyatni o\u2018rganadi. Bu sifatlar maktabda va keyingi hayotda juda zarur.",
"Natijada bola maktabga yaxshi tayyorlanadi \u2014 u nafaqat bilimga, balki o\u2018rganish ko\u2018nikmasiga ega bo\u2018ladi. Bola o\u2018rganishni sevadi, qiziquvchan va faol bo\u2018ladi. Kompetensiyaviy yondashuv bolani o\u2018zgaruvchan dunyoda yashashga va muvaffaqiyatli bo\u2018lishga tayyorlaydi."])]})

TOPICS.append({"num":10,"title":"Bolaning rivojlantiruvchi sohalari kompetensiyalari","reja":[
"Rivojlanish sohalari tushunchasi.","Besh asosiy rivojlanish sohasi.","Har bir soha bo\u2018yicha kompetensiyalar.","Sohalarning o\u2018zaro bog\u2018liqligi va uyg\u2018un rivojlanishi."],"sections":[
("Rivojlanish sohalari tushunchasi",[
"Bolaning rivojlanish sohalari \u2014 bola shaxsining turli qirralarini qamrab oluvchi, o\u2018zaro bog\u2018liq yo\u2018nalishlardir. \u201cIlk qadam\u201d dasturida bola rivojlanishi besh asosiy sohaga bo\u2018lib o\u2018rganiladi. Har bir soha bolaning ma\u2019lum bir tomonini rivojlantiradi.",
"Rivojlanish sohalarining belgilanishi tarbiyachiga ish jarayonini tizimli tashkil etish imkonini beradi. Tarbiyachi har bir soha bo\u2018yicha bola qanday rivojlanayotganini kuzatadi va kerakli yordamni ko\u2018rsatadi. Hech bir soha e\u2019tibordan chetda qolmaydi.",
"Har bir sohada bola yoshiga mos rivojlanish ko\u2018rsatkichlari (kompetensiyalari) belgilangan. Bu ko\u2018rsatkichlar bola muayyan yoshda nimalarni bilishi va qila olishi kerakligini ifodalaydi. Ular bola rivojlanishini baholash uchun mo\u2018ljal bo\u2018lib xizmat qiladi."]),
("Besh asosiy rivojlanish sohasi",[
"Birinchi soha \u2014 jismoniy rivojlanish va sog\u2018lom turmush tarzi. Bu soha bolaning yirik va mayda motorikasini, harakat malakalarini, sog\u2018liqni saqlash ko\u2018nikmalarini qamrab oladi. Bola o\u2018z tanasini boshqarishni va sog\u2018lom yashashni o\u2018rganadi.",
"Ikkinchi soha \u2014 ijtimoiy-hissiy rivojlanish. Bu soha bolaning his-tuyg\u2018ularini boshqarish, boshqalar bilan munosabat o\u2018rnatish, hamkorlik qilish, jamoada yashash ko\u2018nikmalarini o\u2018z ichiga oladi. Uchinchi soha \u2014 nutq, muloqot, o\u2018qish va yozish malakalari.",
"To\u2018rtinchi soha \u2014 bilish jarayonining rivojlanishi: matematik tushunchalar, atrof-olamni bilish, mantiqiy tafakkur, tabiat haqidagi bilimlar. Beshinchi soha \u2014 badiiy-estetik va ijodiy rivojlanish: tasviriy san\u2019at, musiqa, ijodiy ifoda. Bu besh soha bolani yaxlit qamrab oladi."]),
("Har bir soha bo\u2018yicha kompetensiyalar",[
"Jismoniy rivojlanish sohasida bola harakat koordinatsiyasi, muvozanat, mayda motorika (qalam ushlash, tugma qadash) kompetensiyalarini egallaydi. Shuningdek gigiyena va sog\u2018lom ovqatlanish ko\u2018nikmalari shakllanadi.",
"Ijtimoiy-hissiy sohada bola o\u2018z his-tuyg\u2018ularini tanish va boshqarish, boshqalar bilan til topish, qoidalarga rioya qilish kompetensiyalarini oladi. Nutqiy sohada lug\u2018at boyligi, to\u2018g\u2018ri talaffuz, fikrni ifoda etish va savodxonlik asoslari rivojlanadi.",
"Bilish sohasida bola sanash, taqqoslash, guruhlash, sabab-natijani aniqlash, atrof-olamni bilish kompetensiyalarini egallaydi. Badiiy-estetik sohada esa bola rasm chizish, modellashtirish, qo\u2018shiq aytish, raqsga tushish va ijod qilish qobiliyatlarini namoyon etadi."]),
("Sohalarning o\u2018zaro bog\u2018liqligi va uyg\u2018un rivojlanishi",[
"Rivojlanish sohalari bir-biridan ajralgan emas, balki o\u2018zaro chambarchas bog\u2018liq. Masalan, bola qurilish markazida o\u2018ynaganida bir vaqtning o\u2018zida mayda motorika (jismoniy), tafakkur (bilish), hamkorlik (ijtimoiy) va ijod (estetik) sohalari rivojlanadi.",
"Shu sababli ta\u2019lim-tarbiyada sohalarni yaxlit, uyg\u2018un rivojlantirishga e\u2019tibor qaratiladi. Tarbiyachi shunday faoliyat tashkil etadiki, unda bir necha soha bir vaqtda ishlaydi. Bu integratsiyalashgan (yaxlit) yondashuv deb ataladi.",
"Uyg\u2018un rivojlanish \u2014 barcha sohalarning muvozanatli rivojlanishini anglatadi. Hech bir soha boshqasidan ustun qo\u2018yilmaydi. Bola sog\u2018lom, aqlli, odobli, gapga chechan va ijodkor bo\u2018lib, har tomonlama barkamol shaxs sifatida shakllanadi. Bu dasturning asosiy maqsadidir."])]})


TOPICS.append({"num":11,"title":"Maktabgacha yoshdagi (6-7 yosh) bolaning tayanch kompetensiyalari: kommunikativ, ijtimoiy, shaxsiy, bilish","reja":[
"Tayanch kompetensiya tushunchasi.","Kommunikativ va ijtimoiy kompetensiyalar.","Shaxsiy (\u201cmen\u201d konsepsiyasi) kompetensiyasi.","Bilish kompetensiyasi va maktabga tayyorlik."],"sections":[
("Tayanch kompetensiya tushunchasi",[
"Tayanch kompetensiyalar \u2014 bolaning maktab ta\u2019limiga va keyingi hayotiga zarur bo\u2018lgan asosiy, eng muhim qobiliyat va ko\u2018nikmalardir. Ular 6-7 yoshli bolada shakllanishi kerak bo\u2018lgan rivojlanish natijalarini ifodalaydi. Bu maktabga tayyorlikning ko\u2018rsatkichidir.",
"6-7 yosh \u2014 bolaning maktabga o\u2018tish davri bo\u2018lib, bu yoshda u muayyan tayyorgarlik darajasiga erishishi lozim. Tayanch kompetensiyalar shu tayyorgarlikni baholash uchun asos bo\u2018ladi. Ular bolaning jismoniy, aqliy va ijtimoiy yetukligini aks ettiradi.",
"\u201cIlk qadam\u201d dasturida 6-7 yoshli bolaning to\u2018rt asosiy tayanch kompetensiyasi belgilangan: kommunikativ, ijtimoiy, shaxsiy (\u201cmen\u201d konsepsiyasi) va bilish kompetensiyalari. Bu kompetensiyalar bolani maktabga ham aqliy, ham ijtimoiy jihatdan tayyorlaydi."]),
("Kommunikativ va ijtimoiy kompetensiyalar",[
"Kommunikativ kompetensiya \u2014 bolaning boshqalar bilan samarali muloqot qila olish qobiliyatidir. 6-7 yoshli bola o\u2018z fikrini aniq ifoda etishi, boshqalarni tinglashi, savol berishi va javob qaytarishi, suhbatni davom ettirishi kerak. Bola so\u2018z boyligiga ega va to\u2018g\u2018ri gapiradi.",
"Ijtimoiy kompetensiya \u2014 bolaning jamiyatda, jamoada yashash va boshqalar bilan munosabat o\u2018rnatish qobiliyatidir. Bola hamkorlik qila oladi, qoidalarga rioya qiladi, navbatni kutadi, boshqalarning fikri va his-tuyg\u2018ularini hisobga oladi, nizolarni tinch hal qiladi.",
"Bu ikki kompetensiya o\u2018zaro bog\u2018liq, chunki muloqot ijtimoiy munosabatlarning asosidir. Bola tengdoshlari va kattalar bilan muloqotda o\u2018zini erkin tutadi, do\u2018stlasha oladi, jamoaviy o\u2018yin va faoliyatda faol ishtirok etadi. Bu maktabdagi muvaffaqiyat uchun zarur."]),
("Shaxsiy (\u201cmen\u201d konsepsiyasi) kompetensiyasi",[
"Shaxsiy kompetensiya \u2014 bolaning o\u2018zini anglashi, o\u2018ziga baho berishi va o\u2018zini boshqarishi bilan bog\u2018liq qobiliyatdir. Uning markazida \u201cmen\u201d konsepsiyasi, ya\u2019ni bolaning o\u2018zi haqidagi tasavvuri yotadi. Bola o\u2018zini, o\u2018z imkoniyatlarini va o\u2018rnini biladi.",
"\u201cMen\u201d konsepsiyasini qurish \u2014 bolaning \u201cMen kimman?\u201d, \u201cMen nimani bilaman?\u201d, \u201cMen nimaga qodirman?\u201d degan savollarga javob topishidir. Bola o\u2018z ismi, yoshi, oilasi, qiziqishlari, kuchli va kuchsiz tomonlarini anglaydi. Bu o\u2018ziga ishonchni shakllantiradi.",
"Shaxsiy kompetensiya bolaning mustaqilligini, o\u2018ziga ishonchini, mas\u2019uliyatini va o\u2018z-o\u2018zini boshqarishini o\u2018z ichiga oladi. Bola o\u2018z his-tuyg\u2018ularini boshqara oladi, qiyinchiliklarni yenga oladi, o\u2018z xatti-harakatlari uchun javobgarlikni his qiladi. Bu shaxsning yetukligini ko\u2018rsatadi."]),
("Bilish kompetensiyasi va maktabga tayyorlik",[
"Bilish kompetensiyasi \u2014 bolaning atrof-olamni bilish, fikrlash, tahlil qilish va yangi bilim olish qobiliyatidir. 6-7 yoshli bola taqqoslay oladi, guruhlay oladi, sabab-natijani aniqlay oladi, oddiy mantiqiy xulosalar chiqara oladi.",
"Bu yoshda bola matematik tushunchalarga (son, shakl, miqdor, fazo), savodxonlik asoslariga (harf, tovush, o\u2018qishning boshlang\u2018ich ko\u2018nikmalari) ega bo\u2018ladi. U atrof-olam, tabiat, jamiyat haqida ma\u2019lum bilimlarga ega va qiziquvchanlik namoyon etadi.",
"Bilish kompetensiyasi bolaning maktabga aqliy tayyorgarligini ko\u2018rsatadi. Bola diqqatini jamlay oladi, vazifani oxirigacha bajaradi, ko\u2018rsatmalarni tushunadi va bajaradi. Bularning barchasi maktabda muvaffaqiyatli o\u2018qish uchun zaruriy shartdir. To\u2018rt kompetensiya birgalikda bolani maktabga tayyorlaydi."])]})

TOPICS.append({"num":12,"title":"Maktabgacha ta'limda markazlar faoliyatida olib boriladigan ishlar","reja":[
"Markazlarda olib boriladigan ishlarning mazmuni.","Tarbiyachining markazlardagi roli.","Bolalarning markazlardagi faoliyati.","Markazlar ishini baholash va kuzatish."],"sections":[
("Markazlarda olib boriladigan ishlarning mazmuni",[
"Rivojlantiruvchi markazlarda olib boriladigan ishlar bola rivojlanishining barcha sohalarini qamrab oladi. Har bir markazda muayyan turdagi faoliyat tashkil etiladi: til markazida nutq va savodxonlik, matematika markazida sanash va mantiq, san\u2019at markazida ijod.",
"Markazlardagi ishlar asosan bolaning mustaqil va erkin faoliyatiga asoslanadi. Bola o\u2018zi qiziqqan markazni tanlaydi, o\u2018zi xohlagan materiallar bilan, o\u2018z sur\u2019atida ishlaydi. Bu mustaqillikni va tashabbuskorlikni rivojlantiradi.",
"Markazlardagi faoliyat haftalik mavzuga bog\u2018lanadi. Tarbiyachi har bir markazga mavzuga oid material va vazifalar joylashtiradi. Shunday qilib bola bir mavzuni turli markazlarda, turli faoliyat orqali har tomonlama o\u2018rganadi. Bu bilimni mustahkamlaydi."]),
("Tarbiyachining markazlardagi roli",[
"Markazlar faoliyatida tarbiyachi an\u2019anaviy \u201co\u2018qituvchi\u201d emas, balki yo\u2018naltiruvchi, qo\u2018llab-quvvatlovchi va sharoit yaratuvchi rolini bajaradi. U bolalar faoliyatini kuzatadi va kerak bo\u2018lganda yordam beradi, lekin bola mustaqilligini cheklamaydi.",
"Tarbiyachi bolalarga ochiq savollar beradi (\u201cBu qanday bo\u2018ldi?\u201d, \u201cNega shunday deb o\u2018ylaysan?\u201d, \u201cYana qanday qilsa bo\u2018ladi?\u201d), ularni fikrlashga, izlanishga undaydi. U bola xatosini darrov tuzatmaydi, balki bola o\u2018zi topishiga imkon beradi.",
"Tarbiyachi markazlarni jihozlaydi, materiallarni yangilab turadi, har bir bolaga individual e\u2019tibor beradi. U bola rivojlanishini kuzatadi, kuchsiz tomonlarini aniqlaydi va qo\u2018shimcha yordam ko\u2018rsatadi. Tarbiyachi bola va material o\u2018rtasidagi ko\u2018prik vazifasini bajaradi."]),
("Bolalarning markazlardagi faoliyati",[
"Bolalar markazlarda turli faoliyat bilan shug\u2018ullanadi. Til markazida ular kitob ko\u2018radi, hikoya tuzadi, harf va tovushlar bilan tanishadi. Matematika va qurilish markazida sanaydi, taqqoslaydi, qurilish quradi, boshqotirma yechadi.",
"San\u2019at markazida bolalar rasm chizadi, loy va plastilindan modellar yasaydi, applikatsiya qiladi. Tabiat markazida o\u2018simlik va hayvonlarni kuzatadi, oddiy tajribalar o\u2018tkazadi. Rolli o\u2018yin markazida turli rollarni o\u2018ynaydi (\u201cdo\u2018kon\u201d, \u201cshifoxona\u201d, \u201coila\u201d).",
"Bolalar markazlarda yakka, juftlik yoki kichik guruh bo\u2018lib ishlaydi. Birgalikdagi faoliyatda ular hamkorlik qilishni, kelishishni, navbatni kutishni o\u2018rganadi. Bola faoliyat davomida yangi bilim oladi, ko\u2018nikma hosil qiladi va o\u2018z imkoniyatlarini namoyon etadi."]),
("Markazlar ishini baholash va kuzatish",[
"Tarbiyachi markazlardagi bolalar faoliyatini muntazam kuzatib boradi. U har bir bolaning qaysi markazda, qanday ishlayotganini, nimani o\u2018zlashtirayotganini va qanday qiyinchiliklarga duch kelayotganini kuzatadi. Kuzatish baholashning asosiy usulidir.",
"Kuzatuv natijalari bolaning rivojlanish kartasiga qayd etiladi. Bunda bolaning yutuqlari, rivojlanish darajasi va qo\u2018llab-quvvatlash zarur bo\u2018lgan sohalari belgilanadi. Bu individual ishni rejalashtirish imkonini beradi.",
"Baholash bolani boshqalar bilan taqqoslash uchun emas, balki uning shaxsiy rivojlanishini kuzatish uchun o\u2018tkaziladi. Tarbiyachi bola \u201ckecha\u201d va \u201cbugun\u201d qanday bo\u2018lganini taqqoslaydi. Baholash natijalari asosida markazlar ishi takomillashtiriladi va bola rivojlanishi qo\u2018llab-quvvatlanadi."])]})

TOPICS.append({"num":13,"title":"Rivojlantiruvchi markazlaridagi ta'limiy faoliyatlar orqali yangi ma'lumotlarni bola ongiga to\u2018liq yetkazib berishda o\u2018yinlar va ulardan foydalanish","reja":[
"O\u2018yinning maktabgacha ta\u2019limdagi o\u2018rni.","O\u2018yinlarning turlari.","O\u2018yin orqali bilim berish usullari.","Markazlarda o\u2018yinlardan foydalanish."],"sections":[
("O\u2018yinning maktabgacha ta\u2019limdagi o\u2018rni",[
"O\u2018yin \u2014 maktabgacha yoshdagi bolaning yetakchi faoliyatidir. Bola o\u2018yin orqali atrof-olamni biladi, tajriba orttiradi, ko\u2018nikma hosil qiladi va rivojlanadi. Maktabgacha yoshda o\u2018yin bola hayotining asosiy mazmunini tashkil etadi.",
"O\u2018yinning ta\u2019limiy ahamiyati katta: o\u2018yin orqali berilgan bilim bolaga oson, qiziqarli va tabiiy tarzda yetib boradi. Bola o\u2018ynab turib, sezmagan holda o\u2018rganadi. Shuning uchun maktabgacha ta\u2019limda o\u2018yin asosiy o\u2018qitish usuli hisoblanadi.",
"O\u2018yin bolaning barcha rivojlanish sohalariga ijobiy ta\u2019sir ko\u2018rsatadi. U tafakkur, nutq, tasavvur, diqqat va xotirani rivojlantiradi; ijtimoiy ko\u2018nikma, his-tuyg\u2018u va irodani tarbiyalaydi; jismoniy faollikni oshiradi. O\u2018yin \u2014 bola uchun ham faoliyat, ham o\u2018rganish vositasidir."]),
("O\u2018yinlarning turlari",[
"O\u2018yinlar bir necha turga bo\u2018linadi. Ijodiy (mustaqil) o\u2018yinlar: rolli (syujetli) o\u2018yinlar, qurilish-konstruktiv o\u2018yinlar, teatrlashtirilgan o\u2018yinlar. Bularda bola o\u2018zi syujet o\u2018ylab topadi, rollarni taqsimlaydi va ijod qiladi.",
"Qoidali o\u2018yinlar: didaktik (ta\u2019limiy) o\u2018yinlar va harakatli o\u2018yinlar. Didaktik o\u2018yinlar maxsus ta\u2019limiy maqsadga qaratilgan bo\u2018lib, bola o\u2018ynab turib muayyan bilim va ko\u2018nikmani egallaydi. Harakatli o\u2018yinlar jismoniy rivojlanishga xizmat qiladi.",
"Shuningdek xalq o\u2018yinlari (milliy o\u2018yinlar) ham muhim o\u2018rin tutadi. Ular bolani milliy qadriyatlar bilan tanishtiradi. Har bir o\u2018yin turi o\u2018ziga xos rivojlantiruvchi qiymatga ega. Tarbiyachi maqsadga qarab mos o\u2018yin turini tanlaydi va ta\u2019lim jarayoniga singdiradi."]),
("O\u2018yin orqali bilim berish usullari",[
"O\u2018yin orqali bilim berishda didaktik o\u2018yinlar asosiy o\u2018rin tutadi. Ularda ta\u2019limiy vazifa o\u2018yin shaklida beriladi. Masalan, \u201cMo\u2018jizali xalta\u201d o\u2018yinida bola buyumni paypaslab topadi, shu orqali shakl va xususiyatlarni o\u2018rganadi.",
"O\u2018yinli vaziyatlar yaratish ham samarali usul. Tarbiyachi mashg\u2018ulotni o\u2018yin shaklida tashkil etadi: ertak qahramoni keladi, sayohatga chiqiladi, muammo hal qilinadi. Bu bola e\u2019tiborini jalb qiladi va bilimni qiziqarli yetkazadi.",
"O\u2018yinda yangi bilim bosqichma-bosqich beriladi: avval tanishtiriladi, keyin mustahkamlanadi, so\u2018ng amaliyotda qo\u2018llaniladi. O\u2018yin qoidalarini bola o\u2018zlashtiradi va ularga rioya qiladi. O\u2018yin takrorlanib turadi, bu bilimning mustahkam o\u2018rnashishini ta\u2019minlaydi."]),
("Markazlarda o\u2018yinlardan foydalanish",[
"Har bir rivojlantiruvchi markazda mos o\u2018yinlardan foydalaniladi. Til markazida nutqiy o\u2018yinlar (\u201cTovushni top\u201d, \u201cSo\u2018z o\u2018yini\u201d), matematika markazida didaktik o\u2018yinlar (\u201cSana va top\u201d, \u201cShakllarni jufrla\u201d) tashkil etiladi.",
"Qurilish markazida konstruktiv o\u2018yinlar, rolli o\u2018yin markazida syujetli o\u2018yinlar (\u201cShifokor\u201d, \u201cDo\u2018kon\u201d, \u201cOila\u201d), san\u2019at markazida ijodiy o\u2018yinlar o\u2018tkaziladi. Tabiat markazida tajriba va kuzatish o\u2018yinlari, harakat markazida harakatli o\u2018yinlar bo\u2018ladi.",
"Tarbiyachi markazlarga mavzuga va maqsadga mos o\u2018yinlar va o\u2018yin materiallarini joylashtiradi. Bola o\u2018yin orqali yangi ma\u2019lumotlarni qiyinchiliksiz, qiziqish bilan o\u2018zlashtiradi. O\u2018yin bilimni bola ongiga to\u2018liq va mustahkam yetkazishning eng samarali vositasidir."])]})

TOPICS.append({"num":14,"title":"Rivojlantiruvchi markazlar, ta'limiy faoliyat va ularga qo\u2018yilgan talablar","reja":[
"Rivojlantiruvchi markazlarga qo\u2018yilgan talablar.","Ta\u2019limiy faoliyatga qo\u2018yilgan talablar.","Markazlardagi materiallarga qo\u2018yilgan talablar.","Talablarga rioya qilishning ahamiyati."],"sections":[
("Rivojlantiruvchi markazlarga qo\u2018yilgan talablar",[
"Rivojlantiruvchi markazlarga bir qator talablar qo\u2018yiladi. Birinchidan, xavfsizlik \u2014 markaz va undagi barcha jihozlar bola hayoti va sog\u2018lig\u2018i uchun mutlaqo xavfsiz bo\u2018lishi shart. Ikkinchidan, yoshga moslik \u2014 markaz bolalar yoshi va rivojlanish darajasiga mos bo\u2018lishi kerak.",
"Uchinchidan, qulaylik va ochiqlik \u2014 markaz bola erkin foydalanadigan, materiallar uning qo\u2018li yetadigan joyda bo\u2018lishi lozim. To\u2018rtinchidan, estetiklik \u2014 markaz chiroyli, ozoda, uyg\u2018un bezatilgan bo\u2018lishi va bolada ijobiy kayfiyat uyg\u2018otishi kerak.",
"Beshinchidan, o\u2018zgaruvchanlik \u2014 markaz mavzuga, fasllarga va bolalar qiziqishiga qarab yangilanib turishi lozim. Oltinchidan, mazmunan boylik \u2014 markaz xilma-xil, bir-birini to\u2018ldiruvchi materiallar bilan ta\u2019minlangan bo\u2018lishi kerak. Bu talablar markaz samaradorligini ta\u2019minlaydi."]),
("Ta\u2019limiy faoliyatga qo\u2018yilgan talablar",[
"Ta\u2019limiy faoliyat \u2014 markazlarda bola rivojlanishiga qaratilgan maqsadli faoliyatdir. Unga ham bir qator talablar qo\u2018yiladi. Avvalo, faoliyat aniq maqsadga ega bo\u2018lishi va bola rivojlanish sohalarini qamrab olishi kerak.",
"Faoliyat bolaning yoshiga, qiziqishlariga va imkoniyatlariga mos bo\u2018lishi lozim. U bolaga qiziqarli, jalb etuvchi va mazmunli bo\u2018lishi kerak. Faoliyat oson dan murakkabga, ma\u2019lumdan noma\u2019lumga tomon tartiblanadi va bola mustaqilligini rag\u2018batlantiradi.",
"Ta\u2019limiy faoliyat asosan o\u2018yin shaklida tashkil etiladi, chunki o\u2018yin maktabgacha yoshda yetakchi faoliyatdir. Faoliyat bolani faol harakatga, izlanishga undashi, uning tafakkurini rivojlantirishi kerak. Bola passiv tinglovchi emas, faol ishtirokchi bo\u2018lishi lozim."]),
("Markazlardagi materiallarga qo\u2018yilgan talablar",[
"Markazlardagi materiallarga qo\u2018yilgan asosiy talab \u2014 xavfsizlik. Materiallar zaharsiz, o\u2018tkir qirralarsiz, yutib yuborib bo\u2018lmaydigan o\u2018lchamda bo\u2018lishi kerak. Ular ekologik toza va gigiyena talablariga javob berishi shart.",
"Materiallar mustahkam, chidamli va yuvilishi (tozalanishi) mumkin bo\u2018lishi lozim. Ular estetik jihatdan chiroyli, yorqin rangli va jozibador bo\u2018lishi kerak. Bu bolaning qiziqishini uyg\u2018otadi va faoliyatga jalb etadi.",
"Materiallar bolaning yoshiga mos va rivojlantiruvchi qiymatga ega bo\u2018lishi kerak. Ular bolaning faolligini, ijodini va mustaqil izlanishini rag\u2018batlantirishi lozim. Materiallar xilma-xil bo\u2018lib, bolaga tanlash imkonini berishi va turli faoliyat turlarini ta\u2019minlashi kerak."]),
("Talablarga rioya qilishning ahamiyati",[
"Belgilangan talablarga rioya qilish rivojlantiruvchi markazlar va ta\u2019limiy faoliyatning samaradorligini ta\u2019minlaydi. Xavfsizlik talablariga rioya qilish bola hayoti va sog\u2018lig\u2018ini muhofaza qiladi, baxtsiz hodisalarning oldini oladi.",
"Yoshga moslik va boshqa pedagogik talablarga rioya qilish bola rivojlanishini to\u2018g\u2018ri va samarali yo\u2018naltiradi. Talablarga javob beradigan muhit bolani rivojlanishga undaydi, uning qiziqishini saqlaydi va imkoniyatlarini to\u2018liq ochishga yordam beradi.",
"Talablar mexanik qoida emas, balki bola manfaatlariga xizmat qiluvchi ilmiy asoslangan tamoyillardir. Tarbiyachi ularni chuqur tushunib, amaliyotda ijodiy qo\u2018llashi kerak. Talablarga to\u2018liq rioya qilish maktabgacha ta\u2019lim sifatini va bola rivojlanishining muvaffaqiyatini kafolatlaydi."])]})

TOPICS.append({"num":15,"title":"Rivojlantiruvchi markazlari turlari. Til va nutq markazi. Qurish-yasash, konstruksiyalash va matematika markazi","reja":[
"Rivojlantiruvchi markazlar turlarining umumiy tavsifi.","Til va nutq markazi.","Qurish-yasash va konstruksiyalash markazi.","Matematika markazi."],"sections":[
("Rivojlantiruvchi markazlar turlarining umumiy tavsifi",[
"Rivojlantiruvchi markazlar bola rivojlanishining turli sohalariga muvofiq bir necha turga bo\u2018linadi. Asosiy markazlar: til va nutq markazi, qurish-yasash va matematika markazi, tabiat va tajriba markazi, san\u2019at markazi, rolli o\u2018yin markazi, musiqa markazi va kitob burchagi.",
"Har bir markaz o\u2018ziga xos vazifa bajaradi va bolaning ma\u2019lum bir rivojlanish sohasiga xizmat qiladi. Markazlar birgalikda yaxlit tizimni tashkil etib, bolani har tomonlama rivojlantiradi. Markazlar soni va turi guruh yoshiga va xona imkoniyatiga qarab belgilanadi.",
"Markazlar bir-birini to\u2018ldiradi va o\u2018zaro bog\u2018liq ishlaydi. Bola bir markazdan ikkinchisiga o\u2018tib, turli faoliyat bilan shug\u2018ullanadi va turli ko\u2018nikmalarni egallaydi. Quyida eng muhim markazlardan til-nutq hamda qurish-yasash va matematika markazlari batafsil ko\u2018rib chiqiladi."]),
("Til va nutq markazi",[
"Til va nutq (savodxonlik) markazi bolaning nutqini rivojlantirish, lug\u2018atini boyitish, o\u2018qish va yozishga tayyorlashga qaratilgan. Bu markazda kitoblar, rasmli albomlar, syujetli rasmlar, harf va tovush materiallari, nutqiy didaktik o\u2018yinlar joylashtiriladi.",
"Markazda bola kitob ko\u2018radi, hikoya va ertaklar tinglaydi, rasm asosida hikoya tuzadi, she\u2019r yodlaydi. Tovush va harflar bilan tanishadi, so\u2018zlarni bo\u2018g\u2018inlarga ajratadi, oddiy o\u2018qish va yozish ko\u2018nikmalariga ega bo\u2018ladi. Bu maktabga savod tayyorgarligini ta\u2019minlaydi.",
"Til markazi tinch, yorug\u2018 va qulay joyga joylashtiriladi. Unda yumshoq o\u2018rindiqlar, gilam bo\u2018lishi mumkin, bu bolaning kitob bilan qulay shug\u2018ullanishiga imkon beradi. Materiallar bolalar yoshiga mos va muntazam yangilanib turadigan bo\u2018lishi kerak. Markaz nutqning har tomonlama rivojiga xizmat qiladi."]),
("Qurish-yasash va konstruksiyalash markazi",[
"Qurish-yasash va konstruksiyalash markazi bolaning fazoviy tasavvurini, mantiqiy tafakkurini, mayda motorikasini va ijodkorligini rivojlantiradi. Markazda turli xil konstruktorlar, yog\u2018och va plastik g\u2018ishtchalar, kubiklar, bog\u2018lovchi detallar bo\u2018ladi.",
"Bola bu markazda turli inshootlar quradi: uy, ko\u2018prik, minora, qal\u2019a. U detallarni bir-biriga ulaydi, muvozanat va mustahkamlikni sinab ko\u2018radi, o\u2018z g\u2018oyasini amalga oshiradi. Bu jarayonda bola rejalashtirishni, muammoni hal qilishni va xatosini tuzatishni o\u2018rganadi.",
"Konstruksiyalash faoliyati ko\u2018pincha jamoaviy o\u2018tadi \u2014 bolalar birgalikda katta inshootlar quradi. Bu hamkorlik, kelishish va muloqot ko\u2018nikmalarini rivojlantiradi. Markaz shovqinli bo\u2018lgani uchun tinch markazlardan uzoqroq, lekin bolalar erkin harakatlanadigan keng joyga joylashtiriladi."]),
("Matematika markazi",[
"Matematika markazi bolada matematik tushunchalarni \u2014 son, miqdor, shakl, o\u2018lcham, fazo va vaqt haqidagi bilimlarni shakllantiradi. Markazda sanash materiallari, raqamlar, geometrik shakllar, o\u2018lchov vositalari, didaktik o\u2018yinlar va boshqotirmalar joylashtiriladi.",
"Bola bu markazda sanashni, taqqoslashni (katta-kichik, ko\u2018p-oz), guruhlashni, ketma-ketlikni aniqlashni o\u2018rganadi. U shakllarni tanib oladi, narsalarni o\u2018lchaydi, oddiy matematik amallarni bajaradi. Bu mantiqiy tafakkurni va maktab matematikasiga tayyorgarlikni ta\u2019minlaydi.",
"Matematika markazi ko\u2018pincha qurish-yasash markazi bilan birga yoki yaqin joylashtiriladi, chunki bu ikki faoliyat o\u2018zaro bog\u2018liq \u2014 ikkalasida ham mantiq, fazoviy tasavvur va o\u2018lcham tushunchalari ishlaydi. Markazdagi materiallar bolaning matematikaga qiziqishini uyg\u2018otadi va uni amaliy o\u2018rganishga undaydi."])]})

if __name__ == "__main__":
    write_docx("/projects/sandbox/mustaqil-ishlar/Maktabgacha_talim_Konspekt_15_mavzu.docx")
