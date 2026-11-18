"""Dependency-free source and deployment integrity checks; not browser QA."""
from pathlib import Path
from html.parser import HTMLParser
import base64,hashlib,json,re,subprocess,shutil,tempfile
root=Path(__file__).resolve().parents[1]; public=root/'public'
source=json.loads((root/'SOURCE.json').read_text())
for name,expected in source['sha256'].items():
 assert hashlib.sha256((public/name).read_bytes()).hexdigest()==expected,name+' differs from approved source'
landing=(public/'index.html').read_text(); demo=(public/'demo/index.html').read_text()
assert landing.count('Explore Interactive Demo')==1
assert 'href="demo/"' in landing and 'href="../"' in demo
assert 'LXDiN — A technology venture from LA02UK.' in landing
for url in ['https://soccercenter.org','https://arenapathway.com','https://la02uk.com']:assert 'href="'+url+'"' in landing
assert 'function resetDemo(){state=initial();detail.close();render();' in demo
for token in ['NSID','Box','DocuSign','resetDemo()','Fictional','simulated']:assert token.lower() in demo.lower(),token
class Links(HTMLParser):
 def __init__(self,base):super().__init__();self.base=base
 def handle_starttag(self,tag,attrs):
  for key,value in attrs:
   if key in ('src','href') and value:
    if value.startswith('data:'):
     if ';base64,' in value:base64.b64decode(value.split(',',1)[1],validate=True)
    elif not value.startswith(('http:','https:','#')):assert (self.base/value).exists(),value
for name in ['index.html','demo/index.html']:Links((public/name).parent).feed((public/name).read_text())
scripts=re.findall(r'<script\b[^>]*>(.*?)</script>',demo,re.S)
assert not re.search(r'\b(fetch\s*\(|XMLHttpRequest|WebSocket|localStorage|sessionStorage)\b',''.join(scripts))
for p in public.rglob('*'):
 if p.is_file():
  text=p.read_text()
  assert not re.search(r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY|gh[pousr]_[A-Za-z0-9]{30,}|AKIA[A-Z0-9]{16}|sk_live_[A-Za-z0-9]+',text),str(p)
if shutil.which('node'):
 for script in scripts:
  with tempfile.NamedTemporaryFile(suffix='.js',mode='w') as f:
   f.write(script);f.flush();subprocess.run(['node','--check',f.name],check=True)
 print('PASS: demo JavaScript syntax')
else:print('NOT RUN: JavaScript syntax (Node not installed on verification machine; not a hosting dependency)')
print('PASS: exact source hashes, local routes/assets, inline image encoding, single CTA, footer, ecosystem links, reset/navigation implementation, no network/storage API dependencies, credential-pattern scan')
print('INCOMPLETE: browser interaction, accessibility, rendering and console QA')
