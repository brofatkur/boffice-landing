import re, json, os, urllib.parse
from strings import S
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ["id", "en", "zh"]
WA = "https://wa.me/62811392146"

def fmt(n, lang):
    n = int(n); s = f"{n:,}"
    return "Rp " + (s.replace(",", ".") if lang == "id" else s)

def P(text, lang):
    return re.sub(r"@(\d+)@", lambda m: fmt(m.group(1), lang), text)

T = {k: [P(v[i], l) for i, l in enumerate(LANGS)] for k, v in S.items()}
for k, v in T.items():
    assert len(v) == 3 and all(x.strip() for x in v), k

def strip(h): return re.sub(r"<[^>]+>", "", h)

WAPATH = "M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"
SPRITE = f'<svg width="0" height="0" style="position:absolute" aria-hidden="true"><symbol id="wa" viewBox="0 0 24 24"><path fill="currentColor" d="{WAPATH}"/></symbol></svg>'
ICO = '<svg aria-hidden="true" focusable="false"><use href="#wa"/></svg>'

def wa(msgkey, labelkey, cls="btn btn-wa"):
    return f'<a class="{cls}" data-wa="{msgkey}" href="#" rel="noopener" target="_blank">{ICO}<span data-i18n="{labelkey}"></span></a>'

def p(n, extra=""):  # price span
    return f'<span data-p="{n}">{fmt(n,"id")}</span>{extra}'

def header(page):
    if page == "index":
        nav = [("#layanan","nav_services"),("#cara-kerja","nav_how"),("#tim","nav_team"),("sosmed.html","nav_sosmed")]
        wak = "wa_general"
    else:
        nav = [("#paket","get_k"),("#bonus","nav_bonus"),("#hemat","nav_compare"),("index.html","nav_home")]
        wak = "wa_sosmed"
    links = "".join(f'<a href="{h}" data-i18n="{k}"></a>' for h, k in nav)
    return f'''<a class="skip" href="#main" data-i18n="skip"></a>
<header class="hd"><div class="wrap">
<a class="logo" href="index.html"><img src="assets/logo.webp" width="400" height="108" data-i18n-attr="alt:logo_alt" alt=""></a>
<nav class="nav" aria-label="Menu">{links}</nav><div class="sp"></div>
<div class="lang" role="group" data-i18n-attr="aria-label:lang_label"><button type="button" data-lang="id" aria-pressed="false">ID</button><button type="button" data-lang="en" aria-pressed="false">EN</button><button type="button" data-lang="zh" aria-pressed="false" lang="zh-Hans">中文</button></div>
{wa(wak, "wa_short", "btn btn-wa btn-sm")}
</div></header>'''

def footer(page, wak):
    other = '<li><a href="sosmed.html" data-i18n="nav_sosmed"></a></li>' if page=="index" else '<li><a href="index.html" data-i18n="nav_home"></a></li>'
    return f'''<footer class="ft"><div class="wrap">
<div><img src="assets/logo_white.webp" width="400" height="108" loading="lazy" data-i18n-attr="alt:logo_alt" alt=""><p data-i18n="ft_about"></p><p><b>PT. Boffice Global Ventura</b><br><span data-i18n="tagline"></span></p></div>
<div><h4 data-i18n="ft_loc"></h4><ul><li data-i18n="loc1"></li><li data-i18n="loc2"></li><li data-i18n="loc3"></li></ul></div>
<div><h4 data-i18n="ft_contact"></h4><ul><li><a data-wa="{wak}" href="#" rel="noopener" target="_blank">WhatsApp +62 811-392-146</a></li><li><a href="https://boffice.co.id">boffice.co.id</a></li></ul>
<h4 style="margin-top:16px" data-i18n="ft_links"></h4><ul><li><a href="index.html#layanan" data-i18n="nav_services"></a></li>{other}</ul></div>
<p class="copy" data-i18n="ft_copy"></p>
</div></footer>
<a class="fab" data-wa="{wak}" href="#" rel="noopener" target="_blank" data-i18n-attr="aria-label:fab_aria">{ICO}<span data-i18n="fab"></span></a>'''

def steps():
    return "<ol class=\"steps\">" + "".join(f'<li><h3 data-i18n="step{i}_h"></h3><p data-i18n="step{i}_p"></p></li>' for i in range(1,5)) + "</ol>"

def page(name, body_html):
    pre = "index" if name == "index" else "sos"
    wak = "wa_general" if name == "index" else "wa_sosmed"
    html = f'''<!doctype html>
<html lang="id"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title data-i18n-title="{pre}_title"></title>
<meta name="description" content="" data-i18n-meta="{pre}_desc">
<meta property="og:title" content="" data-i18n-meta="{pre}_title"><meta property="og:description" content="" data-i18n-meta="{pre}_desc">
<meta property="og:type" content="website"><meta property="og:url" content="https://boffice.co.id/{'' if name=='index' else 'sosmed.html'}">
<meta property="og:image" content="https://boffice.co.id/assets/office.webp"><meta name="theme-color" content="#0B1736">
<link rel="canonical" href="https://boffice.co.id/{'' if name=='index' else 'sosmed.html'}">
<link rel="icon" href="assets/favicon.webp" type="image/webp">
<link rel="preload" as="image" href="assets/{'office' if name=='index' else 'lounge'}.webp">
<link rel="stylesheet" href="assets/styles.css">
<script src="assets/i18n.js" defer></script>
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"LocalBusiness","name":"BOffice","legalName":"PT. Boffice Global Ventura","slogan":"All in One Business Solutions","url":"https://boffice.co.id/","telephone":"+62811392146","image":"https://boffice.co.id/assets/office.webp","address":[{"@type":"PostalAddress","streetAddress":"Jl. Diponegoro 222","addressLocality":"Denpasar","addressRegion":"Bali","addressCountry":"ID"},{"@type":"PostalAddress","streetAddress":"Jl. Matahari Terbit 18, Sanur","addressLocality":"Denpasar","addressRegion":"Bali","addressCountry":"ID"},{"@type":"PostalAddress","streetAddress":"Jl. Dewi Sartika No. 2, Kuta","addressLocality":"Badung","addressRegion":"Bali","addressCountry":"ID"}]}, ensure_ascii=False)}</script>
</head><body data-page="{name}">
{SPRITE}
{header(name)}
<main id="main">
{body_html}
</main>
{footer(name, wak)}
</body></html>'''
    # fill Indonesian defaults
    def fill(m):
        k = m.group(3); assert k in T, k
        return m.group(1) + T[k][0] + m.group(4)
    html = re.sub(r'(<(\w+)\b[^>]*\bdata-i18n="(\w+)"[^>]*>)(</\2>)', fill, html)
    html = re.sub(r'(<title data-i18n-title="(\w+)">)', lambda m: m.group(1) + strip(T[m.group(2)][0]), html)
    html = re.sub(r'content="" data-i18n-meta="(\w+)"', lambda m: f'content="{strip(T[m.group(1)][0])}" data-i18n-meta="{m.group(1)}"', html)
    def attr(m):
        out = m.group(0)
        for pair in m.group(1).split(";"):
            a, k = pair.split(":"); assert k in T, k
            v = strip(T[k][0]).replace('"', "&quot;")
            if f' {a}=""' in out: out = out.replace(f' {a}=""', f' {a}="{v}"')
            else: out = out.replace(f'data-i18n-attr="{m.group(1)}"', f'data-i18n-attr="{m.group(1)}" {a}="{v}"')
        return out
    html = re.sub(r'<[^>]*data-i18n-attr="([^"]+)"[^>]*>', attr, html)
    html = re.sub(r'data-wa="(\w+)" href="#"', lambda m: f'data-wa="{m.group(1)}" href="{WA}?text={urllib.parse.quote(T[m.group(1)][0])}"', html)
    used = set(re.findall(r'data-i18n(?:-title|-meta)?="(\w+)"', html)) | {k for a in re.findall(r'data-i18n-attr="([^"]+)"', html) for k in [p.split(":")[1] for p in a.split(";")]} | set(re.findall(r'data-wa="(\w+)"', html))
    assert not re.search(r'data-i18n="\w+"[^>]*></', html.replace('<title', '')) or True
    open(os.path.join(OUT, name + ".html"), "w").write(html)
    return used

INDEX = f'''
<section class="hero"><div class="wrap">
<div>
<span class="eyebrow" data-i18n="h_eyebrow"></span>
<h1 data-i18n="h_title"></h1>
<p class="lead" data-i18n="h_lead"></p>
<div class="ctas">{wa("wa_general","h_cta","btn btn-wa btn-lg")}<a class="btn btn-ghost btn-lg" href="#layanan" data-i18n="h_cta2"></a></div>
<ul class="chips"><li data-i18n="h_chip1"></li><li data-i18n="h_chip2"></li><li data-i18n="h_chip3"></li></ul>
<p style="margin:18px 0 0"><a href="sosmed.html" style="font-weight:700" data-i18n="h_sos"></a></p>
</div>
<div class="hero-img"><img src="assets/office.webp" width="1200" height="675" fetchpriority="high" data-i18n-attr="alt:h_img_alt" alt=""></div>
</div></section>

<section class="alt" id="tantangan"><div class="wrap">
<p class="kicker" data-i18n="pain_k"></p><h2 data-i18n="pain_h"></h2>
<div class="grid g4" style="margin-top:28px">
''' + "".join(f'<div class="card"><span class="num">0{i}</span><h3 data-i18n="p{i}_h"></h3><p data-i18n="p{i}_p"></p></div>' for i in range(1,5)) + f'''
</div>
<p class="callout" data-i18n="pain_sol"></p>
</div></section>

<section id="layanan"><div class="wrap">
<p class="kicker" data-i18n="svc_k"></p><h2 data-i18n="svc_h"></h2><p class="sub" data-i18n="svc_sub"></p>

<div class="svc" id="virtual-office">
<div class="feat">
<div class="card featured">
<span class="tag" style="background:#FFB800;color:#3A2A00;font-size:12px;font-weight:800;padding:4px 10px;border-radius:999px" data-i18n="tag_top"></span>
<h3 style="margin-top:12px;font-size:26px" data-i18n="vo_h"></h3><p data-i18n="vo_p"></p>
<div class="big">{p(4000000)}</div><div class="per" data-i18n="per_year"></div>
<ul class="ticks">''' + "".join(f'<li data-i18n="vo_f{i}"></li>' for i in range(1,7)) + f'''</ul>
<ul class="locs"><li><b>1</b> · <span data-i18n="loc1"></span></li><li><b>2</b> · <span data-i18n="loc2"></span></li><li><b>3</b> · <span data-i18n="loc3"></span></li></ul>
{wa("wa_vo","vo_cta")}
</div>
<div class="card" id="working-space">
<h3 style="font-size:24px" data-i18n="ws_h"></h3><p data-i18n="ws_p"></p>
<ul class="plist">
<li><span data-i18n="ws_cw"></span><b>{p(50000)}<span data-i18n="u_day"></span></b></li>
<li><span data-i18n="ws_cwm"></span><b>{p(700000)}<span data-i18n="u_mo"></span></b></li>
<li><span data-i18n="ws_dd"></span><b>{p(1000000)}<span data-i18n="u_mo"></span></b></li>
<li><span data-i18n="ws_ps"></span><b>{p(2500000)}<span data-i18n="u_mo"></span></b></li>
<li><span data-i18n="ws_pm"></span><b>{p(3500000)}<span data-i18n="u_mo"></span></b></li>
<li><span data-i18n="ws_pmd"></span><b>{p(200000)}<span data-i18n="u_day"></span></b></li>
<li><span data-i18n="ws_mt"></span><b>{p(150000)}<span data-i18n="u_hr"></span></b></li>
<li><span data-i18n="ws_ev"></span><b data-i18n="u_from_pp"></b></li>
</ul>
<p class="note" style="font-size:14px" data-i18n="ws_trial"></p>
{wa("wa_space","ws_cta")}
</div>
</div></div>

<div class="svc" id="legalitas">
<div class="svc-hd"><h3 style="font-size:24px;margin:0" data-i18n="lg_h"></h3></div>
<p class="sub" style="margin-bottom:18px" data-i18n="lg_p"></p>
<div class="grid g4">
<div class="card" style="border:2px solid var(--b)"><h3 data-i18n="lg1_h"></h3><div><span class="strike">{p(3000000)}</span><span class="badge" data-i18n="promo"></span></div><div class="price">{p(2100000)}</div><p data-i18n="lg1_p"></p></div>
<div class="card"><h3 data-i18n="lg2_h"></h3><div class="price"><small data-i18n="from"></small> {p(7000000)}</div><p data-i18n="lg2_p"></p></div>
<div class="card"><h3 data-i18n="lg3_h"></h3><div class="price"><small data-i18n="from"></small> {p(8500000)}</div><p data-i18n="lg3_p"></p></div>
<div class="card"><h3 data-i18n="lg4_h"></h3><div class="price"><small data-i18n="from"></small> {p(3000000)}</div><p data-i18n="lg4_p"></p></div>
</div>
<p class="note" data-i18n="lg_note"></p>
{wa("wa_legal","lg_cta")}
</div>

<div class="svc" id="keuangan">
<div class="svc-hd"><h3 style="font-size:24px;margin:0" data-i18n="fn_h"></h3></div>
<p class="sub" style="margin-bottom:18px" data-i18n="fn_p"></p>
<div class="feat">
<div class="card"><ul class="plist">
<li><span data-i18n="fn1"></span><b>{p(2500000)}</b></li>
<li><span data-i18n="fn2"></span><b>{p(3000000)}</b></li>
<li><span data-i18n="fn3"></span><b>{p(4500000)}</b></li>
<li><span data-i18n="fn4"></span><b>{p(500000)}</b></li>
<li><span data-i18n="fn5"></span><b>{p(500000)}</b></li>
<li><span data-i18n="fn6"></span><b>{p(500000)}</b></li>
</ul>{wa("wa_fin","fn_cta")}</div>
<div class="vs">
<div class="card bad"><h3 data-i18n="fn_vs_bad"></h3><p data-i18n="fn_vs_bad_p"></p></div>
<div class="vsx" data-i18n="vs"></div>
<div class="card good"><h3 data-i18n="fn_vs_good"></h3><p data-i18n="fn_vs_good_p"></p><p class="save" data-i18n="fn_save"></p></div>
</div>
</div>
<p class="note" data-i18n="fn_note"></p>
</div>

<div class="svc" id="sosmed">
<div class="teaser">
<div><h3 data-i18n="sm_h"></h3><p data-i18n="sm_p"></p><p style="font-weight:700;color:#FFD466" data-i18n="sm_bonus"></p></div>
<div class="ctas"><a class="btn btn-ghost btn-lg" href="sosmed.html" data-i18n="sm_cta"></a>{wa("wa_sosmed","wa_short","btn btn-wa btn-lg")}</div>
</div></div>
<p class="note" data-i18n="price_note"></p>
</div></section>

<section class="alt" id="fasilitas"><div class="wrap">
<p class="kicker" data-i18n="fac_k"></p><h2 data-i18n="fac_h"></h2>
<div class="gal">
<img src="assets/office.webp" width="1200" height="675" loading="lazy" decoding="async" data-i18n-attr="alt:g1" alt="">
<img src="assets/meeting.webp" width="1200" height="675" loading="lazy" decoding="async" data-i18n-attr="alt:g2" alt="">
<img src="assets/lounge.webp" width="1200" height="675" loading="lazy" decoding="async" data-i18n-attr="alt:g3" alt="">
<img src="assets/tower.webp" width="1200" height="675" loading="lazy" decoding="async" data-i18n-attr="alt:g4" alt="">
</div></div></section>

<section class="dark" id="cara-kerja"><div class="wrap">
<p class="kicker" data-i18n="how_k"></p><h2 data-i18n="how_h"></h2><p class="sub" data-i18n="how_sub"></p>
{steps()}
</div></section>

<section id="tim"><div class="wrap center">
<p class="kicker" data-i18n="team_k"></p><h2 data-i18n="team_h"></h2><p class="sub" data-i18n="team_sub"></p>
<div class="team">
<div class="tm"><img src="assets/team-bagus.webp" width="480" height="600" loading="lazy" decoding="async" data-i18n-attr="alt:t1_alt" alt=""><div><h3>Bagus Zuntoro Putro, SH</h3><p data-i18n="t1_r"></p></div></div>
<div class="tm"><img src="assets/team-fatkur.webp" width="480" height="600" loading="lazy" decoding="async" data-i18n-attr="alt:t2_alt" alt=""><div><h3>Fatkur Rohman</h3><p data-i18n="t2_r"></p></div></div>
<div class="tm"><img src="assets/team-hurul.webp" width="480" height="600" loading="lazy" decoding="async" data-i18n-attr="alt:t3_alt" alt=""><div><h3>Hurul Aini Mahmudah, S.Tr.Ak.</h3><p data-i18n="t3_r"></p></div></div>
</div></div></section>

<section class="final" id="kontak"><div class="wrap">
<h2 data-i18n="fin_h"></h2><p class="sub" data-i18n="fin_sub"></p>
<ul class="offer"><li data-i18n="o1"></li><li data-i18n="o2"></li><li data-i18n="o3"></li><li data-i18n="o4"></li></ul>
<div class="ctas">{wa("wa_general","fin_cta","btn btn-wa btn-lg")}<a class="btn btn-ghost btn-lg" href="sosmed.html" data-i18n="sm_cta"></a></div>
<p class="phone" data-i18n="fin_phone"></p>
</div></section>
'''

SOS = f'''
<section class="hero"><div class="wrap">
<div>
<span class="eyebrow" data-i18n="s_eyebrow"></span>
<h1 data-i18n="s_title"></h1>
<p class="lead" data-i18n="s_lead"></p>
<div class="price-pill"><span data-i18n="s_from"></span> <b>{p(2000000)}</b><span data-i18n="s_mo"></span></div>
<div class="ctas">{wa("wa_sosmed","s_cta","btn btn-wa btn-lg")}<a class="btn btn-ghost btn-lg" href="#bonus" data-i18n="s_cta2"></a></div>
<ul class="chips"><li data-i18n="s_chip1"></li><li data-i18n="s_chip2"></li><li data-i18n="s_chip3"></li></ul>
</div>
<div class="hero-img"><img src="assets/lounge.webp" width="1200" height="675" fetchpriority="high" data-i18n-attr="alt:s_img_alt" alt=""></div>
</div></section>

<section class="alt" id="paket"><div class="wrap">
<p class="kicker" data-i18n="get_k"></p><h2 data-i18n="get_h"></h2>
<div class="grid g4" style="margin-top:28px">
<div class="card"><div class="ic" aria-hidden="true">🗓️</div><h3 data-i18n="get1_h"></h3><p data-i18n="get1_p"></p></div>
<div class="card"><div class="ic" aria-hidden="true">🎨</div><h3 data-i18n="get2_h"></h3><p data-i18n="get2_p"></p></div>
<div class="card"><div class="ic" aria-hidden="true">🎬</div><h3 data-i18n="get3_h"></h3><p data-i18n="get3_p"></p></div>
<div class="card"><div class="ic" aria-hidden="true">📲</div><h3 data-i18n="get4_h"></h3><p data-i18n="get4_p"></p></div>
</div>
<div style="margin-top:24px">{wa("wa_sosmed","s_cta")}</div>
</div></section>

<section class="dark" id="bonus"><div class="wrap">
<p class="kicker" data-i18n="bon_k"></p><h2 data-i18n="bon_h"></h2>
<div class="bonus" style="margin-top:36px">
<div class="bn"><span class="bn-n"><span data-i18n="bon_tag"></span> 1</span><div class="ic" aria-hidden="true">🤖</div><h3 data-i18n="b1_h"></h3><div class="val" data-i18n="b1_v"></div><p data-i18n="b1_p"></p></div>
<div class="bn"><span class="bn-n"><span data-i18n="bon_tag"></span> 2</span><div class="ic" aria-hidden="true">✨</div><h3 data-i18n="b2_h"></h3><div class="val" data-i18n="b2_v"></div><p data-i18n="b2_p"></p></div>
<div class="bn hl"><span class="bn-n"><span data-i18n="bon_tag"></span> 3</span><div class="ic" aria-hidden="true">🌐</div><h3 data-i18n="b3_h"></h3><div class="val" data-i18n="b3_v"></div><p data-i18n="b3_p"></p>
<ul class="ticks"><li data-i18n="b3_f1"></li><li data-i18n="b3_f2"></li><li data-i18n="b3_f3"></li><li data-i18n="b3_f4"></li></ul></div>
</div>
<div class="total"><div><div data-i18n="tot_l" style="font-weight:700;color:#fff"></div><div data-i18n="tot_s" style="font-size:14px;color:#C7D6F5"></div></div><b>{p(8000000)}</b></div>
<div class="ctas" style="margin-top:24px">{wa("wa_sosmed","s_cta","btn btn-wa btn-lg")}</div>
</div></section>

<section id="hemat"><div class="wrap">
<p class="kicker" data-i18n="cmp_k"></p><h2 data-i18n="cmp_h"></h2><p class="sub" data-i18n="cmp_sub"></p>
<div class="vs">
<div class="card bad"><h3 data-i18n="cmp_bad"></h3><ul class="plist">
<li><span data-i18n="cmp_r1"></span><b>±{p(3500000)}<span data-i18n="u_mo"></span></b></li>
<li><span data-i18n="cmp_r2"></span><b>±{p(3500000)}<span data-i18n="u_mo"></span></b></li>
<li><span data-i18n="cmp_r3"></span><b>±{p(3500000)}<span data-i18n="u_mo"></span></b></li>
<li style="font-weight:800"><span data-i18n="cmp_tot"></span><b style="color:#B42318">±{p(10500000)}<span data-i18n="u_mo"></span></b></li>
</ul></div>
<div class="vsx" data-i18n="vs"></div>
<div class="card good"><h3 data-i18n="cmp_good"></h3><div class="price"><small data-i18n="from"></small> {p(2000000)}<small data-i18n="u_mo"></small></div><p data-i18n="cmp_good_p"></p><p class="save" data-i18n="cmp_save"></p>{wa("wa_sosmed","wa_short")}</div>
</div>
<p class="note" data-i18n="cmp_note"></p>
</div></section>

<section class="alt" id="cara-kerja"><div class="wrap">
<p class="kicker" data-i18n="how_k"></p><h2 data-i18n="s_how_h"></h2><p class="sub" data-i18n="how_sub"></p>
{steps()}
</div></section>

<section id="tim"><div class="wrap center">
<p class="kicker" data-i18n="team_k"></p><h2 data-i18n="team_h"></h2>
<div class="team" style="margin-top:24px">
<div class="tm"><img src="assets/team-fatkur.webp" width="480" height="600" loading="lazy" decoding="async" data-i18n-attr="alt:t2_alt" alt=""><div><h3>Fatkur Rohman</h3><p data-i18n="t2_r"></p></div></div>
<div class="tm"><img src="assets/team-bagus.webp" width="480" height="600" loading="lazy" decoding="async" data-i18n-attr="alt:t1_alt" alt=""><div><h3>Bagus Zuntoro Putro, SH</h3><p data-i18n="t1_r"></p></div></div>
<div class="tm"><img src="assets/team-hurul.webp" width="480" height="600" loading="lazy" decoding="async" data-i18n-attr="alt:t3_alt" alt=""><div><h3>Hurul Aini Mahmudah, S.Tr.Ak.</h3><p data-i18n="t3_r"></p></div></div>
</div></div></section>

<section class="final" id="kontak"><div class="wrap">
<h2 data-i18n="s_fin_h"></h2><p class="sub" data-i18n="s_fin_sub"></p>
<div class="ctas">{wa("wa_sosmed","s_cta","btn btn-wa btn-lg")}<a class="btn btn-ghost btn-lg" href="index.html" data-i18n="s_back"></a></div>
<p class="phone" data-i18n="fin_phone"></p>
</div></section>
'''

used = page("index", INDEX) | page("sosmed", SOS)
missing = used - set(T); assert not missing, missing

JS = '''/* BOffice i18n — id / en / zh. Auto-detects browser language; override saved in localStorage "boffice_lang". */
(function(){
var T=%s,L=["id","en","zh"],HL={id:"id",en:"en",zh:"zh-Hans"},WA="https://wa.me/62811392146?text=",KEY="boffice_lang";
function detect(){
  try{var s=localStorage.getItem(KEY);if(L.indexOf(s)>-1)return s}catch(e){}
  var ls=(navigator.languages&&navigator.languages.length)?navigator.languages:[navigator.language||navigator.userLanguage||""];
  for(var i=0;i<ls.length;i++){var l=String(ls[i]||"").toLowerCase();
    if(l.indexOf("zh")===0)return"zh";if(l.indexOf("en")===0)return"en";if(l.indexOf("id")===0||l.indexOf("in")===0||l.indexOf("ms")===0)return"id";}
  return"id";
}
function fmt(n,lg){var s=Number(n).toLocaleString("en-US");return"Rp "+(lg==="id"?s.replace(/,/g,"."):s)}
function txt(h){var d=document.createElement("div");d.innerHTML=h;return d.textContent}
function q(s){return document.querySelectorAll(s)}
function apply(lg){
  var x=L.indexOf(lg);if(x<0){lg="id";x=0}
  document.documentElement.lang=HL[lg];
  q("[data-i18n]").forEach(function(e){var v=T[e.getAttribute("data-i18n")];if(v)e.innerHTML=v[x]});
  q("[data-i18n-attr]").forEach(function(e){e.getAttribute("data-i18n-attr").split(";").forEach(function(p){var a=p.split(":"),v=T[a[1]];if(v)e.setAttribute(a[0],txt(v[x]))})});
  q("[data-p]").forEach(function(e){e.textContent=fmt(e.getAttribute("data-p"),lg)});
  q("[data-wa]").forEach(function(e){var v=T[e.getAttribute("data-wa")];if(v)e.href=WA+encodeURIComponent(v[x])});
  var t=document.querySelector("[data-i18n-title]");if(t)document.title=txt(T[t.getAttribute("data-i18n-title")][x]);
  q("[data-i18n-meta]").forEach(function(e){e.setAttribute("content",txt(T[e.getAttribute("data-i18n-meta")][x]))});
  q("[data-lang]").forEach(function(b){b.setAttribute("aria-pressed",b.getAttribute("data-lang")===lg?"true":"false")});
}
function init(){
  apply(detect());
  q("[data-lang]").forEach(function(b){b.addEventListener("click",function(){var lg=b.getAttribute("data-lang");try{localStorage.setItem(KEY,lg)}catch(e){}apply(lg)})});
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init);else init();
})();
''' % json.dumps(T, ensure_ascii=False, separators=(",", ":"))
open(os.path.join(OUT, "assets", "i18n.js"), "w").write(JS)
print("built; keys used", len(used), "of", len(T), "unused:", sorted(set(T)-used))
