"""Original LXDiN vector artwork. Run from repo root with fontTools, CairoSVG, Pillow.
No website files are modified. All masters are outlined SVGs with true knockout paths.
"""
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from xml.sax.saxutils import escape
import json, shutil
import cairosvg
from PIL import Image
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[1]
NAVY='#102A43'; BLUE='#087FC1'; CYAN='#38C7F0'; SILVER='#DCE5EF'; GRAPHITE='#263745'; WHITE='#FFFFFF'; MUTED='#637789'
fonts={k:TTFont(REPO/'public/fonts'/f) for k,f in [('bold','manrope-bold.ttf'),('regular','dm-sans-regular.ttf')]}
def lettering(value,x,y,size,color=NAVY,weight='regular',tracking=0):
 f=fonts[weight];gs=f.getGlyphSet();cmap=f.getBestCmap();up=f['head'].unitsPerEm;pos=0;parts=[]
 for c in value:
  name=cmap.get(ord(c),'space');pen=SVGPathPen(gs);gs[name].draw(pen);d=pen.getCommands()
  if d:parts.append(f'<path transform="translate({pos:g} 0)" d="{d}"/>')
  pos+=f['hmtx'][name][0]+tracking*up/size
 return f'<g aria-label="{escape(value)}" fill="{color}" transform="translate({x} {y}) scale({size/up:g} {-size/up:g})">'+''.join(parts)+'</g>'

def artwork(concept,tone='light'):
 ink= SILVER if tone=='dark' else NAVY
 accent=CYAN if tone=='dark' else BLUE
 if tone=='mono':ink=accent=NAVY
 if tone=='reverse':ink=accent=WHITE
 if concept=='A':
  L='M16 72H38V126H84V146H16Z'
  D='M208 72H245C276 72 292 85 292 109C292 133 276 146 245 146H208Z M230 92V126H244C261 126 270 120 270 109C270 98 261 92 244 92Z'
  X='M104 72H130L144 94L158 72H184L158 108L186 146H160L144 124L128 146H102L130 108Z'
  key='M144 102C141 102 139 104 139 107C139 109 140 111 142 112L141 119H147L146 112C148 111 149 109 149 107C149 104 147 102 144 102Z'
  return f'<g><path fill="{ink}" d="{L}"/><path fill="{accent}" fill-rule="evenodd" d="{X} {key}"/><path d="M126 76V50A18 18 0 0 1 162 50V76" fill="none" stroke="{accent}" stroke-width="14"/><path fill="{ink}" fill-rule="evenodd" d="{D}"/></g>'
 outer='M16 76H208L216 84V164L208 172H24L16 164Z'
 L='M30 92H43V147H68V160H30Z'
 X='M80 92H96L112 116L128 92H144L122 126L144 160H128L112 136L96 160H80L102 126Z'
 D='M156 92H175C194 92 202 105 202 126C202 147 194 160 175 160H156Z M169 105V147H174C184 147 189 140 189 126C189 112 184 105 174 105Z'
 return f'<g><path d="M90 80V46A22 22 0 0 1 134 46V80" fill="none" stroke="{accent}" stroke-width="16"/><path fill="{ink}" fill-rule="evenodd" d="{outer} {L} {X} {D}"/></g>'

def svg(body,w,h,title,desc=''):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{escape(title)}</title><desc>{escape(desc)}</desc>{body}</svg>'
def symbol(c,tone='light',square=False):
 w=320 if c=='A' else 232
 if square:return f'<svg x="0" y="0" width="256" height="256" viewBox="0 0 {w} 190" preserveAspectRatio="xMidYMid meet">{artwork(c,tone)}</svg>'
 return artwork(c,tone)
def place_symbol(c,tone,x,y,w,h):
 vw=320 if c=='A' else 232
 return f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {vw} 190" preserveAspectRatio="xMidYMid meet">{artwork(c,tone)}</svg>'
def lockup(c,tone='light'):
 color=SILVER if tone=='dark' else NAVY
 if tone=='reverse':color=WHITE
 return place_symbol(c,tone,14,14,190,126)+lettering('LXDiN',234,100,72,color,'bold',-1.8)+lettering('IDENTITY. CONSENT. CONTROL.',237,133,12,color,tracking=1.3)
def place_lockup(c,tone,x,y,w,h):
 return f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 580 168">{lockup(c,tone)}</svg>'
def write_image(path,body,w,h,title,png_width=None,desc=''):
 content=svg(body,w,h,title,desc);path.write_text(content)
 cairosvg.svg2png(bytestring=content.encode(),write_to=str(path.with_suffix('.png')),output_width=png_width or w)
 return content

for c,name in [('A','A-solid'),('B','B-negative-space')]:
 d=ROOT/name;d.mkdir(exist_ok=True)
 for tone in ['light','dark','mono','reverse']:
  w=320 if c=='A' else 232
  write_image(d/f'symbol-{tone}.svg',artwork(c,tone),w,190,f'LXDiN concept {c}: {name}, {tone} symbol',png_width=w*4,desc='Original LXD monogram. The padlock shackle is centered above the X. Transparent background; no stock icon or security certification implied.')
  write_image(d/f'lockup-{tone}.svg',lockup(c,tone),580,168,f'LXDiN — IDENTITY. CONSENT. CONTROL. — concept {c}, {tone}',png_width=1740)
 shutil.copy2(d/'symbol-light.svg',d/'master-symbol.svg');shutil.copy2(d/'lockup-light.svg',d/'master-horizontal.svg')
 icons=d/'favicon-tests';icons.mkdir(exist_ok=True)
 for tone in ['light','dark','mono']:
  content=svg(symbol(c,tone,True),256,256,f'LXDiN {c} favicon {tone}')
  (icons/f'favicon-master-{tone}.svg').write_text(content)
  for size in [16,32,48,64]:cairosvg.svg2png(bytestring=content.encode(),write_to=str(icons/f'{size}-{tone}.png'),output_width=size,output_height=size)
 if c=='B':
  # Pixel-hinted 16px derivative: larger counters and whole-pixel outer bounds.
  for tone in ['light','dark','mono']:
   ink=SILVER if tone=='dark' else NAVY;accent=CYAN if tone=='dark' else BLUE
   if tone=='mono':accent=ink
   micro=f'<path d="M5.5 7V3.5A2 2 0 0 1 9.5 3.5V7" fill="none" stroke="{accent}" stroke-width="1.5"/><path fill="{ink}" fill-rule="evenodd" d="M0 6H15L16 7V14L15 15H1L0 14Z M1 8H2V12H4V13H1Z M5 8h1v1h-1Z M9 8h1v1h-1Z M6 9h1v1h-1Z M8 9h1v1h-1Z M7 10h1v1h-1Z M6 11h1v1h-1Z M8 11h1v1h-1Z M5 12h1v1h-1Z M9 12h1v1h-1Z M11 8H13V9H14V12H13V13H11Z M12 9V12H13V9Z"/>'
   content=svg(micro,16,16,'LXDiN B optically hinted 16px favicon '+tone)
   (icons/f'favicon-micro-16-{tone}.svg').write_text(content)
   cairosvg.svg2png(bytestring=content.encode(),write_to=str(icons/f'16-{tone}.png'),output_width=16,output_height=16)
 im=Image.open(icons/'64-light.png');im.save(icons/'favicon-light.ico',sizes=[(16,16),(32,32),(48,48),(64,64)],append_images=[Image.open(icons/'16-light.png'),Image.open(icons/'32-light.png'),Image.open(icons/'48-light.png')])
 # Website header placement illustration, deliberately outside public/.
 body=f'<rect width="1440" height="760" fill="#071522"/><rect width="1440" height="38" fill="#16334C"/>'+lettering('PROPOSED HEADER PLACEMENT / FOUNDER REVIEW ONLY',50,25,11,'#C5DBE8',tracking=1.8)
 body+=place_symbol(c,'dark',44,56,130,78)+lettering('LXDiN',188,108,45,SILVER,'bold',-1.1)
 for txt,x in [('Solution',780),('How it works',900),('About & Mission',1060),('Contact',1260)]:body+=lettering(txt,x,102,14,SILVER)
 body+='<path d="M50 151H1390" stroke="#284254"/>'
 body+=lettering('IDENTITY. CONSENT. CONTROL.',72,222,14,CYAN,tracking=2)
 body+=lettering('Verification stays expert.',72,318,52,WHITE,'bold',-1.5)+lettering('The experience becomes effortless.',72,389,49,CYAN,'bold',-1.5)
 body+=lettering('Connect specialist verification, consent and authorized handoffs',74,455,21,'#B6CAD7')+lettering('around the organizational systems you already use.',74,490,21,'#B6CAD7')
 body+='<rect x="74" y="538" width="270" height="54" rx="5" fill="#38C7F0"/>'+lettering('Explore Interactive Demo',95,572,16,NAVY,'bold')
 body+=lettering('Fictional demonstration · Integrations are simulated',74,627,13,'#9CB6C8')
 body+=lettering('LXDiN — A technology venture from LA02UK.',74,720,13,'#9CB6C8')
 write_image(d/'website-header-mockup.svg',body,1440,760,f'LXDiN concept {c}: proposed website header, not integrated')
 # Presentation cover, flat vector master rather than artificial photographic mockup.
 b='<rect width="1440" height="900" fill="#0B1E30"/><rect x="0" y="0" width="14" height="900" fill="#38C7F0"/>'+place_lockup(c,'dark',70,55,460,134)
 b+=lettering('Trust, coordinated.',86,391,78,WHITE,'bold',-2)+lettering('Connecting specialist providers',91,477,30,'#B5C9D7')+lettering('to established organizational workflows.',91,526,30,'#B5C9D7')
 b+='<path d="M90 660H1350" stroke="#365167"/>'+lettering('IDENTITY. CONSENT. CONTROL.',91,711,16,CYAN,tracking=3)+lettering('LXDiN · LA02UK',91,820,15,SILVER)+lettering('CONCEPT '+c+' / PRESENTATION COVER',1030,820,12,'#90A6BA',tracking=1)
 content=write_image(d/'presentation-mockup.svg',b,1440,900,f'LXDiN concept {c}: business presentation cover')
 cairosvg.svg2pdf(bytestring=content.encode(),write_to=str(d/'presentation-mockup.pdf'))
 # Document / proposal cover.
 b='<rect width="840" height="1088" fill="white"/>'+place_lockup(c,'light',48,45,380,110)+'<path d="M60 191H780" stroke="#CAD5DF"/>'
 b+=lettering('WORKFLOW BRIEF',65,278,13,BLUE,tracking=2.6)+lettering('Secure handoffs.',60,361,49,NAVY,'bold',-1)+lettering('Clear authorization.',60,426,49,NAVY,'bold',-1)
 b+=lettering('Identity verification, consent and document handling',64,507,19,GRAPHITE)+lettering('orchestrated with established specialist providers.',64,543,19,GRAPHITE)
 b+='<rect x="64" y="609" width="712" height="179" fill="#F0F5F8"/><rect x="64" y="609" width="5" height="179" fill="#087FC1"/>'
 for txt,y in [('Purpose-specific consent',657),('Appropriate information sharing',706),('Respect for existing systems',755)]:b+=lettering(txt,91,y,19,NAVY,'bold')
 b+=lettering('IDENTITY. CONSENT. CONTROL.',64,924,13,BLUE,tracking=2)+lettering('LXDiN — A technology venture from LA02UK.',64,1005,13,MUTED)+lettering('PROPOSED DOCUMENT TREATMENT / REVIEW ONLY',64,1044,10,MUTED,tracking=1)
 content=write_image(d/'document-mockup.svg',b,840,1088,f'LXDiN concept {c}: business document cover')
 cairosvg.svg2pdf(bytestring=content.encode(),write_to=str(d/'document-mockup.pdf'))

# Comparative board.
b='<rect width="2400" height="1800" fill="#EAF0F4"/>'+lettering('LXDiN / LXD SECURITY IDENTITY',88,93,36,NAVY,'bold',1)+lettering('TWO ORIGINAL VECTOR TREATMENTS · FOUNDER SELECTION REVIEW',90,135,14,MUTED,tracking=2)
for c,x,title,sub in [('A',70,'A / SOLID LXD','OPEN LETTERFORMS · INTEGRATED LOCK'),('B',1230,'B / NEGATIVE-SPACE LXD','COMPACT HOUSING · KNOCKOUT LETTERFORMS')]:
 b+=f'<rect x="{x}" y="184" width="1100" height="1490" rx="12" fill="white"/>'+lettering(title,x+40,242,27,NAVY,'bold')+lettering(sub,x+41,276,12,MUTED,tracking=1.8)
 b+=place_symbol(c,'light',x+250,321,600,310)
 b+=lettering('LIGHT / TRANSPARENT MASTER',x+40,678,12,MUTED,tracking=1.5)+place_lockup(c,'light',x+105,705,880,247)
 b+=f'<rect x="{x+25}" y="974" width="1050" height="330" rx="8" fill="#0B1E30"/>'+place_lockup(c,'dark',x+105,1000,880,247)
 b+=lettering('DARK / TRANSPARENT MASTER',x+53,1277,12,'#A4BBCB',tracking=1.5)
 b+=lettering('ONE COLOR / NO SPECIAL EFFECTS',x+40,1360,12,MUTED,tracking=1.5)+place_symbol(c,'mono',x+55,1400,260,160)+place_symbol(c,'reverse',x+360,1400,260,160)
 b+=f'<rect x="{x+345}" y="1390" width="290" height="180" rx="5" fill="#233645"/>'+place_symbol(c,'reverse',x+360,1400,260,160)
 if c=='A':notes=['Most legible L, X and D at normal identity sizes.','The X is the lock body; a true keyhole knockout.']
 else:notes=['Stronger compact silhouette and solid housing.','LXD is cut through the body; no background matte.']
 for i,t in enumerate(notes):b+=lettering(t,x+40,1610+i*25,15,GRAPHITE)
b+=lettering('RECOMMENDATION: A as the primary identity. B is a credible compact alternate. Founder selection is still required.',85,1740,19,NAVY,'bold')
write_image(ROOT/'comparison-board.svg',b,2400,1800,'LXDiN LXD solid versus negative-space: founder comparison board')

# Pixel scale comparison. Embedded raster previews are only on this presentation board.
import base64
b='<rect width="1600" height="1050" fill="#EAF0F4"/>'+lettering('FAVICON OPTICAL TEST / ACTUAL PIXELS',55,64,25,NAVY,'bold')+lettering('Native 16 / 32 / 48 / 64 px tests plus an enlarged nearest-neighbor view. No claim of browser acceptance.',55,105,14,MUTED)
for row,(c,name) in enumerate([('A','A-solid'),('B','B-negative-space')]):
 y=160+row*420;b+=lettering(c+' / '+('SOLID LXD' if c=='A' else 'NEGATIVE SPACE'),55,y+28,22,NAVY,'bold')
 for tone,yy,bg in [('light',y+62,'#FFFFFF'),('dark',y+205,'#0B1E30')]:
  b+=f'<rect x="55" y="{yy}" width="1490" height="130" rx="5" fill="{bg}"/>'
  for i,size in enumerate([16,32,48,64]):
   xx=95+i*180;data=base64.b64encode((ROOT/name/'favicon-tests'/f'{size}-{tone}.png').read_bytes()).decode()
   b+=f'<image x="{xx}" y="{yy+22}" width="{size}" height="{size}" href="data:image/png;base64,{data}"/>'
   b+=lettering(str(size)+' px',xx,yy+108,12,MUTED if tone=='light' else '#B6C9D7')
  # nearest-neighbor enlargement of the native 16px raster; no vector smoothing.
  im=Image.open(ROOT/name/'favicon-tests'/f'16-{tone}.png').resize((96,96),Image.Resampling.NEAREST)
  import io
  tmp=io.BytesIO();im.save(tmp,format='PNG');data=base64.b64encode(tmp.getvalue()).decode()
  b+=f'<image x="1110" y="{yy+14}" width="96" height="96" href="data:image/png;base64,{data}"/>'+lettering('16 px × 6',1240,yy+65,14,MUTED if tone=='light' else '#B6C9D7')
b+=lettering('At 16 px, lock silhouette survives more reliably than all three letters. Prefer 32 px+ when LXD recognition is required.',55,1020,15,NAVY,'bold')
write_image(ROOT/'favicon-comparison.svg',b,1600,1050,'LXDiN native-size favicon tests and magnified pixels')

# Composite placement sheet.
b='<rect width="2400" height="1780" fill="#EAF0F4"/>'+lettering('LXDiN / IN CONTEXT',65,75,34,NAVY,'bold')+lettering('Illustrative placement mockups only. Neither candidate has been integrated into the website.',65,115,16,MUTED)
for c,x,n in [('A',60,'A-solid'),('B',1240,'B-negative-space')]:
 b+=lettering('CONCEPT '+c,x,168,22,NAVY,'bold')
 for file,y,h in [('website-header-mockup.svg',200,580),('presentation-mockup.svg',850,660)]:
  original=(ROOT/n/file).read_text();inner=original[original.index('>')+1:original.rfind('</svg>')]
  vw,vh=(1440,760) if file.startswith('website') else (1440,900)
  b+=f'<svg x="{x}" y="{y}" width="1100" height="{h}" viewBox="0 0 {vw} {vh}">{inner}</svg>'
 b+=lettering('HEADER PLACEMENT + PRESENTATION COVER',x,1630,14,MUTED,tracking=1.4)
write_image(ROOT/'application-comparison.svg',b,2400,1780,'LXDiN concept A and B header and presentation mockups')
# Licensing attribution for outlined lettering.
lic=ROOT/'licenses';lic.mkdir(exist_ok=True)
for f in ['manrope-OFL.txt','dmsans-OFL.txt']:(lic/f).write_text('\n'.join(line.rstrip() for line in (REPO/'public/fonts'/f).read_text().splitlines())+'\n')
print('Created two original outlined vector systems, transparent exports, favicon tests and review mockups.')
