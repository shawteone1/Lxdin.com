"""Dependency-free logo/provenance preservation checks; not browser visual acceptance."""
from pathlib import Path
import hashlib,json,re,struct
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'brand/approved-lxdin/manifest.json').read_text())
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha((root/manifest['master']).read_bytes())=='d6b1b9646edcb396787cc895e718d174169e1533258aff83135480eea1b174cb'
for path,record in manifest['exports'].items():assert sha((root/path).read_bytes())==record['sha256'],path
html=(root/'public/index.html').read_text()
normalized=re.sub(r'(<a class="brand"[^>]*>).*?(</a>)',r'\1BRAND\2',html,flags=re.S)
normalized=re.sub(r'<link\b[^>]+href="brand/lxdin/[^>]+>','',normalized)
normalized=re.sub(r'href="styles\.css\?v=[a-f0-9]{12}"','href="styles.css"',normalized)
assert sha(normalized.encode())==(root/'review/approved-logo-integration/non-brand-baseline.sha256').read_text().strip(),'non-brand HTML changed'
css=(root/'public/styles.css').read_text();base=css.split('\n/* Approved logo integration:')[0]
assert sha(base.encode())==(root/'review/approved-logo-integration/base-styles.sha256').read_text().strip(),'original CSS changed'
assert html.count('class="approved-logo"')==2
assert 'sizes="(max-width:600px) 112px, 144px" width="144" height="93"' in html
assert 'width="864" height="558"' in html # unchanged footer
assert 'styles.css?v='+sha((root/'public/styles.css').read_bytes())[:12] in html
for size in [16,32,48,64,180,192,512]:
 data=(root/f'public/brand/lxdin/icon-{size}.png').read_bytes()
 assert data[:8]==b'\x89PNG\r\n\x1a\n' and struct.unpack('>II',data[16:24])==(size,size)
source=json.loads((root/'SOURCE.json').read_text())
assert sha((root/'public/demo/index.html').read_bytes())==source['pre_logo_sha256']['demo/index.html']=='3944142fe75379a8005f1bb9243dfb48c0ad0749cf0263dc4376b2755b82d3b7'
print('PASS: exact approved master/export hashes, 2 proportional logo images, icon dimensions, unchanged non-brand HTML/scripts, original CSS prefix and byte-identical fictional demo.')
