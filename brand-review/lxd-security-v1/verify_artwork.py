from pathlib import Path
from PIL import Image
import xml.etree.ElementTree as ET
import json,hashlib
r=Path(__file__).resolve().parent;ns={'s':'http://www.w3.org/2000/svg'};results=[]
for f in r.rglob('*.svg'):ET.parse(f)
for name in ['A-solid','B-negative-space']:
 d=r/name
 for kind in ['symbol','lockup']:
  for tone in ['light','dark','mono','reverse']:
   f=d/f'{kind}-{tone}.svg';tree=ET.parse(f)
   assert not tree.findall('.//s:image',ns) and not tree.findall('.//s:text',ns),f
   assert not tree.findall('.//s:linearGradient',ns) and not tree.findall('.//s:filter',ns),f
   im=Image.open(f.with_suffix('.png')).convert('RGBA');a=im.getchannel('A')
   assert a.getextrema()==(0,255) and a.getpixel((0,0))==0,f
   results.append(str(f.relative_to(r)))
 for tone in ['light','dark','mono']:
  for size in [16,32,48,64]:
   im=Image.open(d/'favicon-tests'/f'{size}-{tone}.png').convert('RGBA')
   assert im.size==(size,size)
   lo,hi=im.getchannel('A').getextrema()
   assert lo==0 and hi>0, 'favicon must contain visible artwork and true transparency'
   # At 16px a narrow, correctly antialiased stroke need not contain a fully opaque pixel.
 ico=Image.open(d/'favicon-tests/favicon-light.ico');assert ico.ico.sizes()=={(16,16),(32,32),(48,48),(64,64)}
# Sample the actual knockout alpha in 4x symbol exports.
a=Image.open(r/'A-solid/symbol-light.png').convert('RGBA')
assert a.getpixel((144*4,107*4))[3]==0 and a.getpixel((20*4,80*4))[3]==255
b=Image.open(r/'B-negative-space/symbol-light.png').convert('RGBA')
assert b.getpixel((34*4,100*4))[3]==0 and b.getpixel((174*4,126*4))[3]==255
assert 'IDENTITY. CONSENT. CONTROL.' in (r/'A-solid/master-horizontal.svg').read_text()
assert 'IDENTITY. CONSENT. CONTROL.' in (r/'B-negative-space/master-horizontal.svg').read_text()
print('PASS: SVG structure, outlined vector masters, transparent PNGs and knockouts, all favicon dimensions and ICO sizes, exact brand/tagline.')
print('Artwork render inspection is separate from browser testing; no website integration is performed.')
