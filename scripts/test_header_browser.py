"""Real computed-layout regression. Requires normal Python Playwright/browser install.
Run: python3 scripts/test_header_browser.py
LXDIN_CHROMIUM may select a normal installed browser. Chromium sandbox stays enabled.
"""
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
import os,json,shutil
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1];public=root/'public'
out=Path(os.environ.get('LXDIN_QA_ARTIFACTS','/tmp/lxdin-header-browser'));out.mkdir(parents=True,exist_ok=True)
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*a,**kw):super().__init__(*a,directory=str(public),**kw)
 def log_message(self,*a):pass
server=ThreadingHTTPServer(('127.0.0.1',0),Handler);Thread(target=server.serve_forever,daemon=True).start();results=[]
try:
 with sync_playwright() as p:
  options={'chromium_sandbox':True}
  executable=os.environ.get('LXDIN_CHROMIUM') or shutil.which('chromium')
  if executable:options['executable_path']=executable
  browser=p.chromium.launch(**options)
  for label,w,h in [('ipad-landscape',1024,768),('ipad-large-landscape',1180,820),('desktop',1440,1000),('ipad-portrait',768,1024),('phone',390,844)]:
   for mode in (['current','stale-brand-css'] if w in [1024,1180] else ['current']):
    context=browser.new_context(viewport={'width':w,'height':h},device_scale_factor=2,has_touch=label!='desktop')
    page=context.new_page();errors=[];bad=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.on('response',lambda r:bad.append([r.url,r.status]) if r.status>=400 else None)
    if mode=='stale-brand-css':
     # Deliberately omit the entire logo-specific CSS, reproducing an older cached sheet.
     page.route('**/styles.css*',lambda route:route.fulfill(content_type='text/css',body=(public/'styles.css').read_text().split('/* Approved logo integration:')[0]))
    page.goto(f'http://127.0.0.1:{server.server_port}/',wait_until='networkidle');page.evaluate('document.fonts.ready')
    values=page.evaluate('''()=>{const image=document.querySelector('header.nav > .brand > img'),parent=image.parentElement,header=document.querySelector('header.nav'),nav=header.querySelector('nav');const rect=e=>{const r=e.getBoundingClientRect();return {width:r.width,height:r.height,left:r.left,right:r.right,top:r.top,bottom:r.bottom}};return {image:rect(image),parent:rect(parent),header:rect(header),nav:rect(nav),links:[...nav.querySelectorAll('a')].map(rect),computedImageWidth:getComputedStyle(image).width,computedParentWidth:getComputedStyle(parent).width,navDisplay:getComputedStyle(nav).display,headerScrollWidth:header.scrollWidth,headerClientWidth:header.clientWidth,loaded:image.complete&&image.naturalWidth>0,pageOverflow:document.documentElement.scrollWidth>innerWidth+1}}''')
    expected=112 if w<=600 else 144
    assert values['loaded'],(label,mode,'logo failed to load')
    assert abs(values['image']['width']-expected)<.5,(label,mode,values)
    assert abs(values['parent']['width']-expected)<.5,(label,mode,'parent',values)
    assert abs(values['image']['height']-expected*558/864)<.5,(label,mode,'distortion',values)
    assert values['headerScrollWidth']<=values['headerClientWidth']+1,(label,mode,'header overflow',values)
    if w>900:
     assert values['navDisplay']=='flex'
     assert max(r['top'] for r in values['links'])-min(r['top'] for r in values['links'])<1,'navigation wrapped'
     assert values['image']['right']<values['nav']['left'],'navigation overlaps logo'
     assert values['nav']['right']<=values['header']['right']+1,'navigation outside header'
     assert max(r['height'] for r in values['links'])<30,'individual navigation text wrapped'
    else:
     assert values['navDisplay']=='none'
     page.locator('#navmenu').click();assert page.locator('#navmenu').get_attribute('aria-expanded')=='true'
     assert page.locator('header nav').is_visible();page.locator('#navmenu').click()
    assert not errors and not bad,(label,mode,errors,bad)
    page.screenshot(path=str(out/f'{label}-{mode}.png'),full_page=False)
    values.update({'device':label,'viewport':[w,h],'mode':mode,'pageErrors':errors,'badResponses':bad});results.append(values);context.close()
  browser.close()
finally:server.shutdown();server.server_close()
(out/'computed-layout.json').write_text(json.dumps(results,indent=2)+'\n')
for r in results:print('PASS',r['viewport'],r['mode'],r['computedImageWidth'],'height',r['image']['height'],'parent',r['computedParentWidth'],'header',r['header']['height'],'no header overflow; pageOverflow=',r['pageOverflow'])
print('PASS: 7 sandboxed Chromium cases, current/stale CSS, actual loaded image/computed dimensions, parent bounds, single-row landscape navigation, mobile menu, console and network checks.')
