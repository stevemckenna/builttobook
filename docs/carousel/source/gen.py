import json
INK="#151A18";BLUE="#2E6171";GREEN="#C7F36B";CON="#F4F3ED";HAIR="#212A26";DIM="#7A8580"
S='stroke="currentColor" stroke-width="4" fill="none" stroke-linecap="square" stroke-linejoin="miter"'
I={
"net1":f'<rect x="8" y="12" width="32" height="24" {S}/><path d="M16 42h16" {S}/>',
"net2":f'<rect x="4" y="8" width="22" height="18" {S}/><rect x="22" y="22" width="22" height="18" {S}/>',
"copy":f'<path d="M8 12h32M8 22h32M8 32h20" {S}/><path d="M34 30l6 6-8 6h-6v-6z" {S}/>',
"season":f'<rect x="6" y="10" width="36" height="32" {S}/><path d="M6 20h36M16 6v8M32 6v8" {S}/><rect x="14" y="27" width="8" height="7" fill="currentColor"/>',
"track":f'<path d="M8 40h32" {S}/><rect x="10" y="26" width="6" height="10" fill="currentColor"/><rect x="21" y="18" width="6" height="18" fill="currentColor"/><rect x="32" y="10" width="6" height="26" fill="currentColor"/>',
"report":f'<rect x="10" y="6" width="28" height="36" {S}/><path d="M16 16h16M16 24h16M16 32h10" {S}/>',
"retarget":f'<path d="M38 24a14 14 0 1 1-4-10" {S}/><path d="M36 6v10H26" {S}/><rect x="20" y="20" width="8" height="8" fill="currentColor"/>',
"alert":f'<rect x="14" y="4" width="20" height="40" {S}/><path d="M20 38h8" {S}/><rect x="32" y="2" width="12" height="12" fill="currentColor"/>',
"follow":f'<rect x="6" y="12" width="36" height="26" {S}/><path d="M6 12l18 14 18-14" {S}/>',
"creative":f'<rect x="6" y="8" width="36" height="32" {S}/><path d="M6 34l12-12 10 10 6-6 8 8" {S}/><rect x="30" y="14" width="6" height="6" fill="currentColor"/>',
"video":f'<rect x="4" y="10" width="40" height="28" {S}/><path d="M20 17v14l11-7z" fill="currentColor"/>',
"crm":f'<rect x="4" y="8" width="12" height="32" {S}/><rect x="18" y="8" width="12" height="22" {S}/><rect x="32" y="8" width="12" height="14" {S}/>',
"cats":f'<rect x="6" y="6" width="16" height="16" {S}/><rect x="26" y="6" width="16" height="16" {S}/><rect x="6" y="26" width="16" height="16" {S}/><rect x="26" y="26" width="16" height="16" fill="currentColor"/>',
"year":f'<rect x="4" y="6" width="40" height="36" {S}/><path d="M4 18h40M17 18v24M31 18v24M4 30h40" {S}/>',
"review":f'<circle cx="24" cy="24" r="18" {S}/><path d="M24 12v12l8 6" {S}/>',
"priority":f'<path d="M8 28v-6a16 16 0 0 1 32 0v6" {S}/><rect x="6" y="28" width="8" height="12" fill="currentColor"/><rect x="34" y="28" width="8" height="12" fill="currentColor"/>',
}
CHECK=f'<svg viewBox="0 0 24 24" width="22" height="22"><path d="M5 12l5 5 9-10" stroke="{INK}" stroke-width="3.5" fill="none" stroke-linecap="square"/></svg>'
TILES=[("net1","One ad network",1),("copy","Ad copy",1),("season","Seasonal campaigns",1),("track","Call + lead tracking",1),
("report","Monthly report",1),("net2","Second network",2),("retarget","Retargeting",2),("alert","Instant lead alerts",2),
("follow","Automated follow-up",2),("creative","Custom creative",2),("video","Video ad editing",3),("crm","Full CRM + booking",3),
("cats","Every service category",3),("year","Yearly season calendar",3),("review","Bi-weekly reviews",3),("priority","Priority support",3)]
def ic(k,c,sz=52): return f'<svg viewBox="0 0 48 48" width="{sz}" height="{sz}" style="color:{c}">{I[k]}</svg>'
def meter(n): return ''.join(f'<span style="display:inline-block;width:34px;height:14px;margin-left:6px;{"background:"+CON if i<n else "border:2px solid #5a6560;box-sizing:border-box"}"></span>' for i in range(3))
def band(eyebrow,l1,l2,right,lvl=None):
    m=f'<div>{meter(lvl)}</div>' if lvl else ''
    return f'''<div class="band"><div class="bar"></div>
<div class="eyerow"><span class="eye">{eyebrow}</span>{m}</div>
<div class="hrow"><div class="h"><div>{l1}</div><div style="color:{GREEN}">{l2}</div></div>{right}</div>
<div class="rule"></div></div>'''
def foot(t): return f'<div class="foot">{t}</div>'
def tier(lvl,l1,l2,cap,tag=""):
    n=sum(1 for t in TILES if t[2]<=lvl)
    cells=""
    for k,lab,tl in TILES:
        if tl<=lvl:
            new = tl==lvl and lvl>1
            badge=f'<div class="badge">{CHECK}</div>' if new else ''
            cells+=f'<div class="tile on">{badge}{ic(k,INK)}<div class="lab">{lab}</div></div>'
        else:
            cells+=f'<div class="tile off">{ic(k,DIM)}<div class="lab">{lab}</div></div>'
    right=f'<div class="count"><b>{n}</b><span>/16</span></div>'
    legend=f'<div class="legend"><span class="lg">{CHECK}</span> New at this level</div>' if lvl>1 else f'<div class="legend">{tag}</div>'
    return band(f"LEVEL {lvl} OF 3"+(f' &nbsp;·&nbsp; <span style="color:{GREEN}">MOST POPULAR</span>' if lvl==2 else ''),l1,l2,right,lvl)+f'<div class="grid">{cells}</div>{legend}'+foot(cap)
def cover():
    cols=""
    for n,price,name in [(5,"$1,200","STARTER"),(10,"$2,500","BOOKED GROWTH"),(16,"$4,500","MARKET DOMINATOR")]:
        blocks=''.join(f'<div class="blk" style="background:{CON}"></div>' for i in range(n))
        cols+=f'<div class="col"><div class="stack">{blocks}</div><div class="price">{price}</div><div class="nm">{name}</div><div class="nm2">{n} of 16 tools</div></div>'
    return band("ADS MANAGEMENT, PRICED IN THE OPEN","WHAT $1,200 VS $4,500","ACTUALLY GETS YOU.","")+f'<div class="cols">{cols}</div>'+foot("16 tools. Three levels. Swipe to see what each one gets.")
def cta():
    return band("YOUR NEXT STEP","WHICH LEVEL","FITS YOUR SHOP?","")+f'''<div class="ctab">
<p>Book a 15-minute fit call.</p>
<p>We look at your area, budget and busy season. Then I'll tell you which level makes sense, even if it's the smallest one.</p>
<div class="btn">BOOK A FIT CALL</div><div class="lib">Link in bio &nbsp;·&nbsp; @built.tobook</div></div>'''+foot("Prices monthly, CAD in Canada, USD in the US. Ad spend is separate and paid directly to Meta and Google.")
SL=[("01-cover",cover()),
("02-starter",tier(1,"STARTER: $1,200/MO.","ONE NETWORK. DONE RIGHT.","Meta or Google, your pick. Core copy, standard seasonal campaigns, basic tracking, monthly email report.","Ad spend separate. Paid to Meta or Google.")),
("03-booked-growth",tier(2,"BOOKED GROWTH: $2,500/MO.","EVERY LEAD CHASED.","Both networks, retargeting, instant SMS and email lead alerts, automated follow-up, custom creative, monthly reporting call.")),
("04-market-dominator",tier(3,"MARKET DOMINATOR: $4,500/MO.","ALL 16. EVERY SEASON.","Every service category, full retargeting, ongoing video editing, full CRM and booking, yearly calendar, bi-weekly reviews.")),
("05-cta",cta())]
CSS=f'''@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=block');
*{{margin:0;padding:0;box-sizing:border-box}} body{{background:#000}}
.wrap{{width:1080px;background:{INK};position:relative;overflow:hidden}}
.wrap.reel{{height:1920px;padding-top:285px}} .wrap.post{{height:1350px}}
.reeltop{{position:absolute;top:110px;left:0;right:0;text-align:center;font:400 34px 'Arial Black','Archivo Black';color:{CON};letter-spacing:1px}}
.slide{{width:1080px;height:1350px;position:relative;background:{INK};background-image:linear-gradient({HAIR} 1px,transparent 1px),linear-gradient(90deg,{HAIR} 1px,transparent 1px);background-size:40px 40px;font-family:Arial,'Liberation Sans',sans-serif;color:{CON}}}
.band{{position:relative;padding:56px 56px 0 72px;height:360px}} .bar{{position:absolute;left:0;top:56px;width:14px;height:250px;background:{GREEN}}}
.eyerow{{display:flex;justify-content:space-between;align-items:center;font:700 24px Arial,'Liberation Sans';letter-spacing:1px;color:#B8BEB9}}
.hrow{{display:flex;justify-content:space-between;align-items:flex-end;margin-top:26px}}
.h{{font:400 54px/1.06 'Arial Black','Archivo Black';text-transform:uppercase}}
.count{{font-family:'Arial Black','Archivo Black';text-align:right;line-height:1}} .count b{{font-size:110px;font-weight:400}} .count span{{font-size:40px;color:#B8BEB9}}
.rule{{width:120px;height:6px;background:{BLUE};margin-top:26px}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;padding:12px 56px 0;}}
.tile{{height:168px;padding:20px;position:relative;display:flex;flex-direction:column;justify-content:space-between;border-radius:4px}}
.tile.on{{background:{CON};color:{INK}}} .tile.off{{border:2px dashed #3A4541;color:{DIM}}}
.lab{{font:700 23px/1.15 Arial,'Liberation Sans';text-transform:uppercase}}
.badge{{position:absolute;top:0;right:0;width:40px;height:40px;background:{GREEN};display:flex;align-items:center;justify-content:center}}
.legend{{padding:18px 56px 0;font:700 22px Arial,'Liberation Sans';color:#B8BEB9;display:flex;align-items:center;gap:12px;text-transform:uppercase;letter-spacing:.5px}}
.lg{{width:32px;height:32px;background:{GREEN};display:inline-flex;align-items:center;justify-content:center}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:160px;background:{GREEN};color:{INK};padding:30px 56px;font:700 31px/1.3 Arial,'Liberation Sans';display:flex;align-items:center}}
.cols{{display:flex;justify-content:space-around;align-items:flex-end;height:770px;padding:0 56px 60px}}
.col{{text-align:center;width:320px}} .nm{{white-space:nowrap}} .stack{{display:flex;flex-direction:column-reverse;align-items:center;gap:8px}}
.blk{{width:180px;height:30px;border-radius:2px}} .price{{font:400 64px 'Arial Black','Archivo Black';margin-top:26px}}
.nm{{font:700 22px Arial,'Liberation Sans';letter-spacing:1px;margin-top:6px}} .nm2{{font:700 22px Arial,'Liberation Sans';color:#B8BEB9;margin-top:4px;text-transform:uppercase}}
.ctab{{padding:70px 72px 0}} .ctab p{{font:400 40px/1.35 Arial,'Liberation Sans';margin-bottom:30px;max-width:900px}} .ctab p:first-child{{font-weight:700;font-size:48px}}
.btn{{display:inline-block;background:{GREEN};color:{INK};font:400 44px 'Arial Black','Archivo Black';padding:34px 56px;border-radius:8px;margin-top:20px}}
.lib{{font:700 30px Arial,'Liberation Sans';color:#B8BEB9;margin-top:30px;text-transform:uppercase;letter-spacing:1px}}'''
for name,body in SL:
    for mode in ("post","reel"):
        top='<div class="reeltop">BUILT TO BOOK</div>' if mode=="reel" else ''
        open(f"{name}-{mode}.html","w").write(f'<!doctype html><meta charset="utf-8"><style>{CSS}</style><div class="wrap {mode}">{top}<div class="slide">{body}</div></div>')
json.dump([n for n,_ in SL],open("list.json","w"))
