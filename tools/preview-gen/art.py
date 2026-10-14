"""Program-specific illustrations as inline SVG (brand colours only). Illustrative, not student work."""
B,B9,B2,B1,B5,G,I="#006DEE","#0A2A66","#B3D0FF","#D9E8FF","#EEF5FF","#49B716","#0B1B33"
def _svg(label,body,vb="0 0 520 360"):
    return f'<svg viewBox="{vb}" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto" font-family="Manrope,sans-serif">{body}</svg>'
def t(x,y,s,size=13,fill=I,weight=600,anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'
def found():
    pts=[(70,300,"AI basics"),(160,250,"Python"),(250,200,"Data"),(340,150,"Machine learning"),(430,100,"Small AI apps")]
    b='<rect x="0" y="0" width="520" height="360" fill="#fff"/>'
    for i,(x,y,l) in enumerate(pts):
        b+=f'<rect x="{x-45}" y="{y}" width="90" height="{340-y}" fill="{B5 if i<4 else B1}" stroke="{B2}"/>'
        b+=f'<rect x="{x-45}" y="{y-6}" width="90" height="10" fill="{B if i<4 else G}"/>'
        b+=t(x,y-18,l,12.5,I,700,"middle")
        b+=f'<circle cx="{x}" cy="{y-48}" r="7" fill="{G if i==4 else B}"/>' if False else ""
    b+=f'<path d="M70 280 L160 230 L250 180 L340 130 L430 80" stroke="{G}" stroke-width="2.5" fill="none" stroke-dasharray="5 6"/>'
    for (x,y,l) in pts: b+=f'<circle cx="{x}" cy="{y-70+ (0)}" r="0" />'
    return _svg("Illustration: five steps rising from AI basics to small AI applications",b)
def aiml():
    st=[("Year 1","Foundations and classical ML"),("Year 2","Deep learning and MLOps"),("Year 3","Generative AI and production")]
    b='<rect width="520" height="360" fill="#fff"/>'
    for i,(y,l) in enumerate(st):
        x=30+i*165
        b+=f'<rect x="{x}" y="{200-i*45}" width="150" height="{130+i*45}" fill="{B5}" stroke="{B2}"/><rect x="{x}" y="{200-i*45}" width="150" height="8" fill="{B if i<2 else G}"/>'
        b+=t(x+14,{0:232,1:187,2:142}[i],y.upper(),11,B9,600)+t(x+14,{0:254,1:209,2:164}[i],l.split(" and ")[0],14,I,700)+t(x+14,{0:274,1:229,2:184}[i],("and "+l.split(" and ")[1]) if " and " in l else "",12.5,B9,500)
        for k in range(3): b+=f'<rect x="{x+14+k*40}" y="{{0:300,1:{300}, 2:300}}" width="0" height="0"/>'.replace("{{0:300,1:300, 2:300}}","300") if False else ""
        for k in range(3): b+=f'<rect x="{x+14+k*42}" y="{312}" width="30" height="6" fill="{B2}"/>'
    b+=f'<path d="M105 195 L270 150 L435 105" stroke="{B}" stroke-width="2" fill="none" stroke-dasharray="4 6"/><circle cx="435" cy="105" r="9" fill="{G}"/>'
    b+=t(30,50,"Roadmap: 36 monthly modules",15,I,700)
    return _svg("Illustration: a three-year roadmap from foundations through deep learning to generative AI",b)
def sw():
    b='<rect width="520" height="360" fill="#fff"/>'
    for i,l in enumerate(["Programming logic","Frontend","Backend","Cloud"]):
        x=24+i*124
        b+=f'<rect x="{x}" y="40" width="104" height="64" fill="{B5}" stroke="{B2}"/>'+t(x+52,78,l,12.5,I,700,"middle")
        if i<3: b+=f'<path d="M{x+104} 72 H{x+124}" stroke="{B}" stroke-width="2"/><path d="M{x+118} 66 l6 6 -6 6" stroke="{B}" stroke-width="2" fill="none"/>'
    b+=f'<rect x="24" y="130" width="472" height="206" fill="#fff" stroke="{B2}"/><rect x="24" y="130" width="472" height="26" fill="{B1}"/>'
    for k,c in enumerate([B2,B2,G]): b+=f'<circle cx="{42+k*14}" cy="143" r="4" fill="{c}"/>'
    b+=f'<rect x="44" y="176" width="110" height="140" fill="{B5}"/><rect x="170" y="176" width="306" height="22" fill="{B1}"/><rect x="170" y="212" width="240" height="10" fill="{B2}"/><rect x="170" y="232" width="280" height="10" fill="{B2}"/><rect x="170" y="252" width="200" height="10" fill="{B2}"/><rect x="170" y="284" width="96" height="32" fill="{B}"/>'
    return _svg("Illustration: a development workflow from programming logic through frontend and backend to cloud deployment, with an interface preview",b)
def ds():
    b='<rect width="520" height="360" fill="#fff"/>'
    b+=f'<rect x="24" y="24" width="472" height="312" fill="{B5}" stroke="{B2}"/>'
    for k,h in enumerate([60,100,80,130,110,150]): b+=f'<rect x="{48+k*34}" y="{190-h+60}" width="22" height="{h}" fill="{B if k%2==0 else B2}"/>'
    b+=f'<path d="M260 240 L300 200 L340 215 L380 160 L420 175 L470 120" stroke="{G}" stroke-width="3" fill="none"/>'
    b+=f'<circle cx="150" cy="95" r="34" fill="none" stroke="{B2}" stroke-width="14"/><circle cx="150" cy="95" r="34" fill="none" stroke="{B}" stroke-width="14" stroke-dasharray="120 214" transform="rotate(-90 150 95)"/>'
    b+=t(200,88,"Python and SQL",13,I,700)+t(200,108,"Analytics, ML, data engineering",12,B9,500)
    b+=f'<rect x="260" y="60" width="210" height="14" fill="{B1}"/><rect x="260" y="82" width="150" height="14" fill="{B1}"/>'
    return _svg("Illustration: an analytics dashboard with bar, line and ring charts",b)
def ux():
    b='<rect width="520" height="360" fill="#fff"/>'
    b+=f'<rect x="24" y="30" width="300" height="220" fill="#fff" stroke="{B2}"/><rect x="24" y="30" width="300" height="24" fill="{B1}"/><rect x="44" y="76" width="120" height="14" fill="{B2}"/><rect x="44" y="104" width="260" height="60" fill="{B5}"/><rect x="44" y="184" width="90" height="34" fill="{B}"/><rect x="146" y="184" width="90" height="34" fill="#fff" stroke="{B}"/>'
    b+=f'<rect x="352" y="30" width="144" height="290" rx="14" fill="#fff" stroke="{B2}" stroke-width="2"/><rect x="368" y="62" width="112" height="70" fill="{B5}"/><rect x="368" y="146" width="80" height="10" fill="{B2}"/><rect x="368" y="166" width="112" height="10" fill="{B1}"/><rect x="368" y="270" width="112" height="32" fill="{B}"/>'
    for k,c in enumerate([B,B9,B2,G,B1]): b+=f'<circle cx="{44+k*36}" cy="290" r="14" fill="{c}" stroke="{B2}"/>'
    b+=t(24,338,"Fundamentals, product thinking, prototyping",12,B9,600)
    return _svg("Illustration: wireframes for a desktop and a mobile interface with a colour palette",b)
def cy():
    b='<rect width="520" height="360" fill="#fff"/>'
    nodes=[(90,90),(220,60),(360,100),(110,230),(250,200),(400,250),(300,310)]
    for a,c in [(0,1),(1,2),(0,3),(1,4),(2,5),(3,4),(4,5),(4,6),(3,6)]: b+=f'<path d="M{nodes[a][0]} {nodes[a][1]} L{nodes[c][0]} {nodes[c][1]}" stroke="{B2}" stroke-width="2"/>'
    for i,(x,y) in enumerate(nodes): b+=f'<circle cx="{x}" cy="{y}" r="{11 if i!=4 else 16}" fill="{B if i!=4 else G}" stroke="#fff" stroke-width="3"/>'
    b+=f'<path d="M250 168 l22 8 v16 c0 14 -10 24 -22 28 c-12 -4 -22 -14 -22 -28 v-16 z" fill="#fff" stroke="{I}" stroke-width="2.5" transform="translate(0 -4) scale(1)"/>'
    b+=f'<rect x="372" y="28" width="124" height="70" fill="{B5}" stroke="{B2}"/>'+''.join(f'<rect x="{384+k*20}" y="{84-h}" width="12" height="{h}" fill="{B}"/>' for k,h in enumerate([20,34,26,44,30]))
    b+=t(24,344,"Networking basics, security operations, authorised labs",12,B9,600)
    return _svg("Illustration: a monitored network of connected systems protected by a shield",b)
ART={"ai-foundation":found,"ai-ml-engineering":aiml,"software-development":sw,"data-science-ai":ds,"product-ux-ai-design":ux,"cybersecurity":cy}


def shot(i):
    """Interface mockups used as project visuals (inline SVG, decorative)."""
    B, N, L = "#006DEE", "#0B1B33", "#49B716"
    def bar(x, y, w, c="#D9E8FF", h=8): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="{c}"/>'
    if i % 3 == 0:
        body = (f'<rect x="24" y="24" width="150" height="232" fill="#F2F7FF" stroke="#D9E8FF"/>' + bar(38, 44, 90, B) + bar(38, 68, 110) + bar(38, 86, 96) + bar(38, 104, 104) + bar(38, 122, 80)
                + f'<rect x="192" y="40" width="190" height="34" fill="{B}"/>' + bar(204, 53, 120, "#fff")
                + f'<rect x="258" y="94" width="206" height="70" fill="#fff" stroke="#B3D0FF"/>' + bar(270, 110, 170, N) + bar(270, 128, 150) + bar(270, 144, 110)
                + f'<rect x="258" y="176" width="64" height="22" fill="#fff" stroke="{L}"/><rect x="330" y="176" width="64" height="22" fill="#fff" stroke="{L}"/>' + bar(268, 184, 44, L, 6) + bar(340, 184, 44, L, 6)
                + f'<rect x="192" y="220" width="272" height="36" fill="#fff" stroke="#B3D0FF"/>' + bar(204, 235, 130) + f'<rect x="424" y="228" width="30" height="20" fill="{B}"/>')
    elif i % 3 == 1:
        body = (f'<rect x="24" y="24" width="210" height="232" fill="#EAF2FF" stroke="#B3D0FF"/><path d="M24 220 L90 140 L140 190 L170 150 L234 220Z" fill="#B3D0FF"/><circle cx="188" cy="74" r="20" fill="#fff"/><rect x="70" y="100" width="110" height="90" fill="none" stroke="{L}" stroke-width="3"/>'
                + f'<rect x="254" y="24" width="210" height="232" fill="#fff" stroke="#D9E8FF"/>' + bar(270, 44, 100, N)
                + f'<rect x="270" y="74" width="172" height="12" fill="#EAF2FF"/><rect x="270" y="74" width="148" height="12" fill="{B}"/>'
                + f'<rect x="270" y="104" width="172" height="12" fill="#EAF2FF"/><rect x="270" y="104" width="60" height="12" fill="#7FB1F7"/>'
                + f'<rect x="270" y="134" width="172" height="12" fill="#EAF2FF"/><rect x="270" y="134" width="26" height="12" fill="#B3D0FF"/>'
                + bar(270, 176, 140) + bar(270, 194, 110) + f'<rect x="270" y="222" width="86" height="22" fill="{B}"/>')
    else:
        body = (f'<rect x="24" y="24" width="440" height="232" fill="#F2F7FF" stroke="#D9E8FF"/>'
                + "".join(f'<rect x="{40+k*140}" y="{60+(k%2)*60}" width="116" height="52" fill="#fff" stroke="{B}"/>' + bar(52 + k * 140, 78 + (k % 2) * 60, 70, N) + bar(52 + k * 140, 94 + (k % 2) * 60, 90) for k in range(3))
                + f'<path d="M156 86 H180 V146 H196 M296 146 H320 V86 H336" fill="none" stroke="{B}" stroke-width="2"/>'
                + f'<rect x="40" y="196" width="408" height="44" fill="#fff" stroke="#D9E8FF"/>' + bar(54, 212, 190, B) + bar(54, 226, 140) + f'<circle cx="420" cy="218" r="9" fill="{L}"/>')
    return f'<svg viewBox="0 0 488 280" role="presentation" aria-hidden="true" focusable="false" style="display:block;width:100%;height:auto"><rect width="488" height="280" fill="#EEF5FF"/>{body}</svg>'


def tile_art(slug):
    """Animated glass-style illustration for a program tile. Decorative; animation is CSS and paused until the tile is in view."""
    B, L = "#006DEE", "#49B716"
    g = f'<defs><linearGradient id="g-{slug}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset="1" stop-color="#7FB1F7" stop-opacity=".55"/></linearGradient><linearGradient id="d-{slug}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3D8CF5"/><stop offset="1" stop-color="#0A55C8"/></linearGradient></defs>'
    G, D = f"url(#g-{slug})", f"url(#d-{slug})"
    if slug == "ai-foundation":
        steps = "".join(f'<g class="ta-step" style="--i:{i}"><path d="M{14+i*26} {112-i*16} h30 l10 -7 h-30z" fill="#fff" fill-opacity=".9"/><path d="M{14+i*26} {112-i*16} h30 v10 h-30z" fill="{D}" fill-opacity=".85"/><path d="M{44+i*26} {112-i*16} l10 -7 v10 l-10 7z" fill="#0A55C8" fill-opacity=".7"/></g>' for i in range(5))
        body = steps + f'<circle class="ta-ball" cx="0" cy="0" r="7" fill="{L}"/>'
    elif slug == "ai-ml-engineering":
        layers = [(30, [40, 70, 100]), (80, [30, 55, 85, 110]), (130, [55, 85])]
        edges = "".join(f'<line class="ta-edge" style="--i:{k}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>' for k, (x1, y1, x2, y2) in enumerate([(a, ya, b, yb) for (a, ys), (b, ys2) in zip(layers, layers[1:]) for ya in ys for yb in ys2]))
        nodes = "".join(f'<circle class="ta-node" style="--i:{li*3+ni}" cx="{x}" cy="{y}" r="7" fill="{G}" stroke="{B}" stroke-width="2"/>' for li, (x, ys) in enumerate(layers) for ni, y in enumerate(ys))
        body = f'<g stroke="{B}" stroke-opacity=".35" stroke-width="1.5">{edges}</g>{nodes}<circle class="ta-spark" r="5" fill="{L}"/>'
    elif slug == "software-development":
        lay = "".join(f'<g class="ta-layer" style="--i:{i}"><path d="M80 {96-i*28} l46 -20 l46 20 l-46 20z" fill="{G if i else D}" stroke="#fff" stroke-opacity=".8" stroke-width="1.5"/><path d="M34 {96-i*28} l46 20 v10 l-46 -20z" fill="#0A55C8" fill-opacity=".55"/><path d="M80 {116-i*28} l46 -20 v10 l-46 20z" fill="#0A55C8" fill-opacity=".35"/></g>' for i in range(3))
        body = f'<g transform="translate(-14,10)">{lay}</g><circle class="ta-dot" cx="112" cy="40" r="6" fill="{L}"/>'
    elif slug == "data-science-ai":
        bars = "".join(f'<rect class="ta-bar" style="--i:{i}" x="{22+i*26}" y="{120-h}" width="18" height="{h}" rx="3" fill="{D if i%2==0 else G}" stroke="{B}" stroke-opacity=".4"/>' for i, h in enumerate([36, 58, 46, 80, 98]))
        body = bars + f'<polyline class="ta-line" points="31,78 57,58 83,66 109,38 135,22" fill="none" stroke="{L}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" pathLength="1"/><circle class="ta-pt" r="5" fill="{L}"/>'
    elif slug == "product-ux-ai-design":
        body = (f'<g class="ta-spin"><rect x="38" y="22" width="84" height="84" rx="26" fill="none" stroke="{B}" stroke-width="3" stroke-opacity=".5"/><rect x="48" y="32" width="64" height="64" rx="20" fill="{G}" stroke="{B}" stroke-width="2"/></g>'
                f'<g class="ta-spin2"><circle cx="80" cy="64" r="22" fill="{D}" fill-opacity=".9"/><circle cx="80" cy="64" r="9" fill="#fff"/></g><circle class="ta-orb" cx="80" cy="64" r="7" fill="{L}"/>')
    else:
        body = (f'<circle class="ta-ring" cx="80" cy="66" r="34" fill="none" stroke="{B}" stroke-width="2"/><circle class="ta-ring r2" cx="80" cy="66" r="34" fill="none" stroke="{B}" stroke-width="2"/>'
                f'<clipPath id="c-{slug}"><path id="sh-{slug}" d="M80 18 L120 32 V68 C120 94 102 110 80 120 C58 110 40 94 40 68 V32Z"/></clipPath>'
                f'<path d="M80 18 L120 32 V68 C120 94 102 110 80 120 C58 110 40 94 40 68 V32Z" fill="{G}" stroke="{B}" stroke-width="3" stroke-linejoin="round"/>'
                f'<g clip-path="url(#c-{slug})"><rect class="ta-scan" x="36" y="14" width="88" height="14" fill="{L}" fill-opacity=".55"/></g>'
                f'<rect x="66" y="62" width="28" height="22" rx="4" fill="{D}"/><path d="M71 62 v-7 a9 9 0 0 1 18 0 v7" fill="none" stroke="{D}" stroke-width="4"/><circle cx="80" cy="72" r="3" fill="#fff"/>')
    return f'<svg class="ta" viewBox="0 0 160 140" aria-hidden="true" focusable="false">{g}{body}</svg>'
