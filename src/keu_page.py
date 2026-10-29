# Body for keuangan.html (Finance & Tax landing)
SVC_ICONS = ["📒","📊","🧾","📅","🏷️","🏪","👥","💬","🛡️","💻"]
PROB_ICONS = ["⏰","🗂️","🧩","📈","✉️","💸"]
WHY_ICONS = ["🏢","🎓","💰","🔄"]

def build_keu(wa, p):
    def lis(keys): return "".join(f'<li data-i18n="{k}"></li>' for k in keys)
    probs = "".join(f'<div class="card"><div class="ic" aria-hidden="true">{PROB_ICONS[i-1]}</div><h3 data-i18n="kp{i}_h"></h3><p data-i18n="kp{i}_p"></p></div>' for i in range(1,7))
    svcs = "".join(f'<div class="card ksv"><div class="kic" aria-hidden="true">{SVC_ICONS[i-1]}</div><div><h3 data-i18n="ks{i}_h"></h3><p data-i18n="ks{i}_p"></p></div></div>' for i in range(1,11))
    steps = "<ol class=\"steps\">" + "".join(f'<li><h3 data-i18n="kh{i}_h"></h3><p data-i18n="kh{i}_p"></p></li>' for i in range(1,5)) + "</ol>"
    why = "".join(f'<div class="card"><div class="ic" aria-hidden="true">{WHY_ICONS[i-1]}</div><h3 data-i18n="kw{i}_h"></h3><p data-i18n="kw{i}_p"></p></div>' for i in range(1,5))
    faq = "".join(f'<details class="qa"{" open" if i==1 else ""}><summary data-i18n="kf{i}_q"></summary><p data-i18n="kf{i}_a"></p></details>' for i in range(1,9))
    def pkg(n, feats, wak, hl=False):
        tag = '<span class="pk-tag" data-i18n="kk_pop"></span>' if hl else ""
        return f'''<div class="card pk{' pk-hl' if hl else ''}">{tag}
<h3 class="pk-n" data-i18n="kk{n}_n"></h3>
<p class="pk-fit"><b data-i18n="kk_fit"></b> <span data-i18n="kk{n}_fit"></span></p>
<div class="price" data-i18n="kk_contact"></div>
<ul class="ticks">{lis(feats)}</ul>
{wa(wak, "kk_pick", "btn btn-wa pk-btn")}
</div>'''
    return f'''
<section class="hero"><div class="wrap">
<div>
<span class="eyebrow" data-i18n="k_eyebrow"></span>
<h1 data-i18n="k_title"></h1>
<p class="lead" data-i18n="k_lead"></p>
<div class="ctas">{wa("wa_keu","k_cta","btn btn-wa btn-lg")}<a class="btn btn-ghost btn-lg" href="#paket" data-i18n="k_cta2"></a></div>
<ul class="chips"><li data-i18n="k_chip1"></li><li data-i18n="k_chip2"></li><li data-i18n="k_chip3"></li></ul>
</div>
<div class="khero">
<div class="hero-img"><img src="assets/meeting.webp" width="1200" height="675" fetchpriority="high" data-i18n-attr="alt:k_img_alt" alt=""></div>
<div class="kexp"><img src="assets/team-hurul.webp" width="480" height="600" data-i18n-attr="alt:t3_alt" alt=""><div><small data-i18n="k_exp_lbl"></small><b>Hurul Aini Mahmudah, S.Tr.Ak.</b><span data-i18n="t3_r"></span></div></div>
</div>
</div></section>

<section class="alt" id="masalah"><div class="wrap">
<p class="kicker" data-i18n="kp_k"></p><h2 data-i18n="kp_h"></h2>
<div class="grid g3" style="margin-top:28px">{probs}</div>
<p class="callout" data-i18n="kp_sol"></p>
</div></section>

<section id="layanan-keuangan"><div class="wrap">
<p class="kicker" data-i18n="ks_k"></p><h2 data-i18n="ks_h"></h2><p class="sub" data-i18n="ks_sub"></p>
<div class="ksvc">{svcs}</div>
<div class="ctas" style="margin-top:28px">{wa("wa_keu","k_cta","btn btn-wa btn-lg")}{wa("wa_k_sp2dk","kfin_cta2","btn btn-ghost btn-lg")}</div>
</div></section>

<section class="alt" id="spesialis"><div class="wrap kx">
<div class="kx-img"><img src="assets/team-hurul.webp" width="480" height="600" loading="lazy" decoding="async" data-i18n-attr="alt:t3_alt" alt=""><div class="kx-cap"><b>Hurul Aini Mahmudah, S.Tr.Ak.</b><span data-i18n="t3_r"></span></div></div>
<div>
<p class="kicker" data-i18n="kx_k"></p><h2 data-i18n="kx_h"></h2>
<p class="sub" style="margin-bottom:8px" data-i18n="kx_p"></p>
<ul class="ticks">{lis(["kx_f1","kx_f2","kx_f3","kx_f4"])}</ul>
<div class="kmini">
<div><img src="assets/team-bagus.webp" width="480" height="600" loading="lazy" decoding="async" data-i18n-attr="alt:t1_alt" alt=""><p><b>Bagus Zuntoro Putro, SH</b><span data-i18n="t1_r"></span></p></div>
<div><img src="assets/team-fatkur.webp" width="480" height="600" loading="lazy" decoding="async" data-i18n-attr="alt:t2_alt" alt=""><p><b>Fatkur Rohman</b><span data-i18n="t2_r"></span></p></div>
</div>
</div>
</div></section>

<section class="dark" id="cara-kerja"><div class="wrap">
<p class="kicker" data-i18n="how_k"></p><h2 data-i18n="kh_h"></h2><p class="sub" data-i18n="kh_sub"></p>
{steps}
</div></section>

<section class="alt" id="paket"><div class="wrap">
<p class="kicker" data-i18n="kk_k"></p><h2 data-i18n="kk_h"></h2><p class="sub" data-i18n="kk_sub"></p>
<div class="pks">
{pkg(1, ["kk1_f1","kk1_f2","kk1_f3","kk1_f4"], "wa_k_starter")}
{pkg(2, ["kk2_f1","kk2_f2","kk2_f3","kk2_f4","kk2_f5"], "wa_k_growth", True)}
{pkg(3, ["kk3_f1","kk3_f2","kk3_f3","kk3_f4","kk3_f5"], "wa_k_pro")}
</div>
<div class="feat" style="margin-top:28px">
<div class="card"><h3 data-i18n="kk_list_h"></h3><p data-i18n="kk_list_p"></p><ul class="plist">
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
<p class="note" data-i18n="kk_note"></p>
</div></section>

<section id="kenapa"><div class="wrap">
<p class="kicker" data-i18n="kw_k"></p><h2 data-i18n="kw_h"></h2>
<div class="grid g4" style="margin-top:28px">{why}</div>
<h3 style="margin:40px 0 14px;font-size:22px" data-i18n="kc_h"></h3>
<div class="grid g2">
<a class="kcross" href="index.html#virtual-office"><div><b data-i18n="kc_vo_h"></b><span data-i18n="kc_vo_p"></span></div><em data-i18n="kc_vo_cta"></em></a>
<a class="kcross kcross-d" href="sosmed.html"><div><b data-i18n="kc_sm_h"></b><span data-i18n="kc_sm_p"></span></div><em data-i18n="kc_sm_cta"></em></a>
</div>
</div></section>

<section class="alt" id="faq"><div class="wrap kfaq">
<div><p class="kicker" data-i18n="kf_k"></p><h2 data-i18n="kf_h"></h2><div style="margin-top:18px">{wa("wa_keu","wa_short")}</div></div>
<div>{faq}</div>
</div></section>

<section class="final" id="kontak"><div class="wrap">
<h2 data-i18n="kfin_h"></h2><p class="sub" data-i18n="kfin_sub"></p>
<div class="ctas">{wa("wa_keu","k_cta","btn btn-wa btn-lg")}<a class="btn btn-ghost btn-lg" href="index.html" data-i18n="s_back"></a></div>
<p class="phone" data-i18n="fin_phone"></p>
</div></section>
'''
