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
