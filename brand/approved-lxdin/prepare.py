"""Deterministic crops/resizing of the exact founder-approved raster. No redraw/recolor."""
from pathlib import Path
from PIL import Image
import hashlib,json
root=Path(__file__).resolve().parents[2];folder=root/'public/brand/lxdin';folder.mkdir(parents=True,exist_ok=True)
master=root/'brand/approved-lxdin/master.jpg';im=Image.open(master).convert('RGB');assert im.size==(1280,640)
header_box=(208,20,1072,578);symbol_box=(304,24,960,392)
header=im.crop(header_box);header.save(folder/'header-original-crop.png')
for width in [432,864]:
 header.resize((width,round(width*header.height/header.width)),Image.Resampling.LANCZOS).save(folder/f'header-{width}.webp',lossless=True,method=6)
symbol=im.crop(symbol_box);bg=im.getpixel((16,16));square=Image.new('RGB',(656,656),bg);square.paste(symbol,(0,144))
for size in [16,32,48,64,180,192,512]:square.resize((size,size),Image.Resampling.LANCZOS).save(folder/f'icon-{size}.png',optimize=True)
square.save(folder/'favicon.ico',sizes=[(16,16),(32,32),(48,48),(64,64)])
manifest={'master':'brand/approved-lxdin/master.jpg','master_sha256':hashlib.sha256(master.read_bytes()).hexdigest(),'dimensions':[1280,640],'header_crop':header_box,'icon_monogram_crop':symbol_box,'icon_canvas':{'size':[656,656],'paste':[0,144],'background_rgb':bg},'processing':'Original background preserved. Crops, proportional Lanczos resize and sampled navy icon padding only. No transparency, tracing, regeneration or recoloring.','exports':{str(p.relative_to(root)):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'size':Image.open(p).size} for p in sorted(folder.iterdir()) if p.is_file()}}
(root/'brand/approved-lxdin/manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Master SHA256:',manifest['master_sha256'])
