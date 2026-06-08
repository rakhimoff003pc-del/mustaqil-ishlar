# -*- coding: utf-8 -*-
"""Nutqini o'stirish metodikasi - 13 mavzu mustaqil ishlar to'plami.

Har bir mavzu A4 qog'ozda Times New Roman 14pt, 1.5 qator oraliq bilan
taxminan 11-12 sahifani egallaydi. Sahifa o'lchamlari va chekkalari
oldingi gen_jismoniy_v2.py skripti bilan moslashtirilgan.
"""
import zipfile
import datetime

TOPICS = []


def esc(t):
    return (
        t.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def run(text, bold=False, size=28, font="Times New Roman"):
    rpr = '<w:rPr><w:rFonts w:ascii="%s" w:hAnsi="%s" w:cs="%s"/>' % (font, font, font)
    if bold:
        rpr += "<w:b/><w:bCs/>"
    rpr += '<w:sz w:val="%d"/><w:szCs w:val="%d"/></w:rPr>' % (size, size)
    return '<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (rpr, esc(text))


def para(
    text,
    bold=False,
    size=28,
    align="both",
    indent_first=709,
    space_after=120,
    line=456,
    keep_next=False,
):
    ppr = "<w:pPr>"
    if keep_next:
        ppr += "<w:keepNext/>"
    ppr += '<w:spacing w:after="%d" w:line="%d" w:lineRule="auto"/>' % (
        space_after,
        line,
    )
    if indent_first:
        ppr += '<w:ind w:firstLine="%d"/>' % indent_first
    ppr += '<w:jc w:val="%s"/></w:pPr>' % align
    return "<w:p>%s%s</w:p>" % (ppr, run(text, bold=bold, size=size))


def page_break():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def empty_para():
    return '<w:p><w:pPr><w:spacing w:after="0" w:line="456" w:lineRule="auto"/></w:pPr></w:p>'


def build_topic(t, is_first):
    parts = []
    if not is_first:
        parts.append(page_break())
    parts.append(
        para(
            "%d-MAVZU. %s" % (t["num"], t["title"].upper()),
            bold=True,
            size=30,
            align="center",
            indent_first=0,
            space_after=200,
            keep_next=True,
        )
    )
    parts.append(
        para(
            "Reja:",
            bold=True,
            size=28,
            align="left",
            indent_first=0,
            space_after=80,
            keep_next=True,
        )
    )
    for i, r in enumerate(t["reja"], 1):
        parts.append(
            para(
                "%d. %s" % (i, r),
                size=28,
                align="left",
                indent_first=360,
                space_after=60,
            )
        )
    parts.append(empty_para())
    for idx, (head, paras) in enumerate(t["sections"], 1):
        parts.append(
            para(
                "%d. %s" % (idx, head),
                bold=True,
                size=28,
                align="left",
                indent_first=0,
                space_after=120,
                keep_next=True,
            )
        )
        section_paras = list(paras)
        extra = EXTRA.get((t["num"], idx - 1))
        if extra:
            section_paras.append(extra)
        for p in section_paras:
            parts.append(
                para(p, size=28, align="both", indent_first=709, space_after=220)
            )
    parts.append(empty_para())
    parts.append(
        para(
            "Foydalanilgan adabiyotlar:",
            bold=True,
            size=28,
            align="left",
            indent_first=0,
            space_after=80,
            keep_next=True,
        )
    )
    for i, ref in enumerate(t.get("refs", []), 1):
        parts.append(
            para(
                "%d. %s" % (i, ref),
                size=28,
                align="both",
                indent_first=360,
                space_after=60,
            )
        )
    return "".join(parts)


def build_document():
    body = "".join(build_topic(t, i == 0) for i, t in enumerate(TOPICS))
    sect = (
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1134" w:right="850" w:bottom="1134" w:left="1701" '
        'w:header="708" w:footer="708" w:gutter="0"/>'
        '<w:pgNumType w:start="1"/></w:sectPr>'
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        "<w:body>" + body + sect + "</w:body></w:document>"
    )


CT = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
    '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
    '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>'
    "</Types>"
)
RE = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
    '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
    '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>'
    "</Relationships>"
)
DR = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
    "</Relationships>"
)
ST = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
    "<w:docDefaults><w:rPrDefault><w:rPr>"
    '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
    '<w:sz w:val="28"/><w:szCs w:val="28"/><w:lang w:val="uz-Latn-UZ"/>'
    "</w:rPr></w:rPrDefault><w:pPrDefault><w:pPr>"
    '<w:spacing w:line="456" w:lineRule="auto"/>'
    "</w:pPr></w:pPrDefault></w:docDefaults>"
    '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
    '<w:name w:val="Normal"/><w:rPr>'
    '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
    '<w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr></w:style></w:styles>'
)


def cp():
    n = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        "<dc:title>Nutqini o'stirish metodikasi - mustaqil ishlar</dc:title>"
        "<dc:creator>Mustaqil ish</dc:creator>"
        '<dcterms:created xsi:type="dcterms:W3CDTF">%s</dcterms:created>'
        '<dcterms:modified xsi:type="dcterms:W3CDTF">%s</dcterms:modified>'
        "</cp:coreProperties>" % (n, n)
    )


AP = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">'
    "<Application>Mustaqil ish</Application></Properties>"
)


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


# ============================================================================
# MAVZULAR
# ============================================================================
# Topiclar fayllar nutq_topic_NN.py kabi alohida modullarda saqlanadi.
# Bu yerda ularni import qilamiz.
from topics import all_topics
from topics._extra import EXTRA

TOPICS.extend(all_topics)

if __name__ == "__main__":
    write_docx("Nutq_ostirish_metodikasi_13_mustaqil_ish.docx")
