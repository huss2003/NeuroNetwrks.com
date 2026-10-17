import sys, numpy as np
from PIL import Image, ImageDraw, ImageFilter
src, outdir = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB'); W,H = im.size
a = np.asarray(im).astype(np.int16)

# 1. foreground = everything that is not background white (flood-fill from the border)
nonwhite = (a.min(axis=2) < 235)
fg = Image.fromarray((nonwhite*255).astype(np.uint8))
bgfill = fg.copy(); ImageDraw.floodfill(bgfill, (2,2), 128)   # background becomes 128
fgmask = np.asarray(bgfill) != 128                             # includes white shirt interior

# 2. man polygon (traced on the source grid), tight on the side that overlaps the car
man_poly = [(1050,300),(1048,290),(1035,250),(1028,200),(1030,140),(1050,105),(1090,92),(1140,95),
            (1180,115),(1210,150),(1235,200),(1248,250),(1245,300),(1250,320),(1275,345),(1288,380),
            (1295,420),(1300,470),(1302,520),(1292,560),(1278,600),(1268,650),(1262,700),(1262,732),
            (1300,750),(1306,775),(1292,792),(1250,794),(1200,794),(1175,787),(1166,765),(1160,730),
            (1150,700),(1135,660),(1115,620),(1097,606),(1082,550),(1058,500),(1045,450),(1040,400),
            (1043,350)]
pm = Image.new('L',(W,H),0); ImageDraw.Draw(pm).polygon(man_poly, fill=255)
man = (np.asarray(pm)>0) & fgmask

# 3. wheels = circles (tyre outline included); keep the man's pixels inside them too,
#    so nothing shows a seam under his edge
yy,xx = np.mgrid[0:H,0:W]
def disc(cx,cy,r): return (xx-cx)**2+(yy-cy)**2 <= r*r
dL, dR = disc(715,687,108), disc(1345,688,104)
wheels = (dL | dR) & fgmask

# 4. shadow = everything on the ground band (tyre bottoms and shoes included) - static
shadow = fgmask & (yy > 688)

# 5. body = the car, minus the lower half of each wheel (so its dip never peeks out
#    below the static tyres). It keeps a copy of the man only where he overlaps the car,
#    so his lean exposes car-coloured pixels, never white.
car_poly = [(540,560),(560,480),(640,330),(720,285),(900,262),(1050,268),(1180,300),(1280,380),
            (1330,420),(1400,440),(1460,520),(1470,620),(1430,690),(560,690)]
pc = Image.new('L',(W,H),0); ImageDraw.Draw(pc).polygon(car_poly, fill=255)
car_region = np.asarray(pc) > 0
lower_wheels = (dL & (yy > 687)) | (dR & (yy > 688))
grey = (np.abs(a[:,:,0]-a[:,:,1])<12) & (np.abs(a[:,:,1]-a[:,:,2])<12) & (a[:,:,0]>140)
ground = grey & (yy > 696) & ~(dL | dR)
body = fgmask & ~lower_wheels & ~ground & ~(man & ~car_region) & ~(man & (yy > 700))

def save(mask, name, feather=1):
    m = Image.fromarray((mask*255).astype(np.uint8))
    if feather: m = m.filter(ImageFilter.GaussianBlur(feather))
    rgb = np.asarray(im).copy(); am = np.asarray(m)
    rgb[am==0] = 0                       # drop hidden pixels so the PNG stays small
    out = Image.fromarray(rgb).convert('RGBA'); out.putalpha(m)
    bbox = m.getbbox(); print(name, 'bbox', bbox)
    out.save(f'{outdir}/{name}.png', optimize=True)
for mask,name in [(shadow,'shadow'),(body,'body'),(wheels,'wheels'),(man,'man')]:
    save(mask,name)

# debug overlay
dbg = np.asarray(im).copy()
for mask,col in [(shadow,(0,200,0)),(body,(0,120,255)),(wheels,(255,200,0)),(man,(255,0,120))]:
    dbg[mask] = (dbg[mask]*0.55 + np.array(col)*0.45).astype(np.uint8)
Image.fromarray(dbg).crop((500,80,1500,820)).save(f'{outdir}/../../../{"debug-layers.png"}' if False else sys.argv[3])
print('done')
