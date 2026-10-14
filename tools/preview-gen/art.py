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
    return f'<svg viewBox="0 0 488 280" role="presentation" aria-hidden="true" focusable="false" class="shotsvg" preserveAspectRatio="xMidYMid slice"><rect width="488" height="280" fill="#EEF5FF"/>{body}</svg>'


def stage_pv(i):
    """Interface previews for the five learning stages (decorative inline SVG)."""
    B, N, L, P, M = "#006DEE", "#0B1B33", "#49B716", "#D9E8FF", "#B3D0FF"
    def r(x, y, w, h, f="#fff", s=None, rx=0):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{f}"' + (f' stroke="{s}"' if s else "") + "/>"
    def b(x, y, w, c=P, h=8): return r(x, y, w, h, c, None, 3)
    chrome = r(0, 0, 520, 34, "#EAF2FF", M) + "".join(f'<circle cx="{18+k*16}" cy="17" r="4.5" fill="{M}"/>' for k in range(3))
    if i == 0:
        body = (r(20, 52, 140, 228, "#F2F7FF", P) + b(34, 70, 70, B) + "".join(b(34, 96 + k * 24, 96 - (k % 3) * 14) for k in range(7))
                + b(184, 62, 200, N, 12) + b(184, 90, 300) + b(184, 108, 270) + b(184, 126, 150)
                + r(184, 156, 316, 100, "#fff", L) + b(200, 172, 70, L, 6) + b(200, 192, 270, N) + b(200, 210, 230) + b(200, 228, 180))
    elif i == 1:
        body = (r(20, 52, 190, 228, "#fff", P) + "".join(f'<circle cx="40" cy="{80+k*40}" r="9" fill="{L if k<2 else "#fff"}" stroke="{L if k<2 else B}" stroke-width="2"/>' + b(60, 76 + k * 40, 120 - k * 14, N if k < 2 else P) for k in range(5))
                + r(228, 52, 272, 228, N) + "".join(b(246, 74 + k * 24, w, c, 7) for k, (w, c) in enumerate([(90, L), (180, M), (150, M), (200, "#7FB1F7"), (110, M), (160, M), (60, L)])))
    elif i == 2:
        body = (r(20, 52, 120, 228, "#F2F7FF", P) + "".join(b(34 + (k % 2) * 12, 72 + k * 26, 70 - (k % 2) * 8, B if k == 2 else P) for k in range(7))
                + r(158, 52, 342, 228, "#fff", P) + r(176, 70, 306, 30, "#EAF2FF") + r(176, 112, 96, 74, B) + r(284, 112, 198, 34, "#fff", M) + r(284, 152, 198, 34, "#fff", M)
                + r(176, 198, 306, 62, "#EAF2FF") + b(190, 214, 150, B) + b(190, 232, 220))
    elif i == 3:
        body = (r(20, 52, 190, 228, "#fff", P) + f'<circle cx="115" cy="140" r="56" fill="none" stroke="{P}" stroke-width="12"/><path d="M115 84 A56 56 0 1 1 61 154" fill="none" stroke="{B}" stroke-width="12" stroke-linecap="round"/>' + b(80, 222, 70, N, 10)
                + r(228, 52, 272, 228, "#fff", P) + "".join(r(244, 70 + k * 52, 240, 38, "#fff", M if k != 1 else B) + b(256, 84 + k * 52, 150, N) + f'<circle cx="466" cy="{89+k*52}" r="7" fill="{B if k==1 else "#fff"}" stroke="{B}" stroke-width="2"/>' for k in range(4)))
    else:
        body = (r(20, 52, 230, 228, "#fff", P) + b(36, 70, 90, N, 10) + "".join(r(36, 100 + k * 36, 198, 12, "#EAF2FF") + r(36, 100 + k * 36, w, 12, L if k == 0 else B) for k, w in enumerate([198, 158, 120]))
                + r(36, 214, 90, 44, B) + b(48, 232, 66, "#fff")
                + r(268, 52, 232, 110, "#F2F7FF", L) + b(284, 70, 60, L, 6) + b(284, 90, 190, N) + b(284, 108, 150) + b(284, 126, 110)
                + r(268, 176, 232, 104, "#fff", P) + f'<path d="M286 250 L330 224 L372 238 L420 206 L482 190" fill="none" stroke="{B}" stroke-width="3"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="4.5" fill="{L}"/>' for x, y in [(330, 224), (420, 206), (482, 190)]))
    return f'<svg viewBox="0 0 520 300" aria-hidden="true" focusable="false" class="pvs"><rect width="520" height="300" fill="#fff"/>{chrome}{body}</svg>'


def programs_motif():
    """Small geometric motif for the programs listing: one short bar then five tall bars."""
    bars = "".join(f'<rect x="{20+k*58}" y="{150-h}" width="46" height="{h}" fill="{"#49B716" if k==0 else "#006DEE"}" fill-opacity="{1 if k==0 else .22+.1*k}"/>' for k, h in enumerate([34, 70, 96, 122, 98, 134]))
    return f'<svg viewBox="0 0 380 170" role="img" aria-label="Illustration: one short bar for the beginner course and five taller bars for the three-year programs" style="width:100%;height:auto">{bars}<path d="M0 154 H380" stroke="#0B1B33" stroke-width="2"/></svg>'
