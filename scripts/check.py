from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
root=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
 def __init__(self): super().__init__(); self.refs=[]; self.ids=set()
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  for key in ('href','src'):
   if key in a:self.refs.append(a[key])
pages={}
for path in root.glob('*.html'):
 parser=Page();parser.feed(path.read_text());pages[path.name]=parser
for name,page in pages.items():
 for ref in page.refs:
  u=urlsplit(ref)
  if u.scheme:continue
  target=u.path.lstrip('/') or ('index.html' if u.path=='/' else name)
  assert (root/target).is_file(),(name,ref)
  if u.fragment:assert u.fragment in pages[target].ids,(name,ref)
home=(root/'index.html').read_text()
assert 'href="https://exubis.com"' in home
assert 'href="https://taskdizzle.online"' in home
assert 'FREE' in home and 'App Store link coming soon' in home
assert 'jemlabs@myyahoo.com' in home
assert '<script' not in home
print(f'Validated {len(pages)} pages: internal links, anchors, assets, product CTA destinations, required labels.')
