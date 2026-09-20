#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Replay in temporary copies, ordinary/optimized modes, and semantic controls."""
import hashlib,json,subprocess,sys,tempfile
from pathlib import Path
root=Path(__file__).resolve().parent

def require(ok,message):
    if not ok: raise RuntimeError(message)

def run(source,mode):
    with tempfile.TemporaryDirectory() as tmp:
        p=Path(tmp)/'check.py';p.write_text(source)
        r=subprocess.run([sys.executable,'-I',*(['-O'] if mode else []),str(p)],text=True,capture_output=True)
        cert=Path(tmp)/'certificate.json'
        return r,cert.read_bytes() if cert.exists() else None

receipts=[]
for name in ['check_certificate.py','review_independent_checker.py']:
    source=(root/'research'/name).read_text()
    modes=[]
    for mode in [False,True]:
        r,cert=run(source,mode);require(r.returncode==0,r.stderr)
        if cert:require(cert==(root/'research/certificate.json').read_bytes(),'certificate differs')
        modes.append((r.stdout,cert));receipts.append({'checker':name,'optimized':mode,'passed':True})
    require(modes[0]==modes[1],'mode divergence')
# These controls change mathematical inputs, rather than just corrupting hashes.
source=(root/'research/check_certificate.py').read_text()
controls=[('wrong total',source.replace("'11661/10250'","'11662/10250'")),('wrong effective constant',source.replace("'20827163033/10847244000'","'20827163034/10847244000'")),('wrong component claim',source.replace('sides[0] > 0 and sides[1] < 0','sides[0] < 0 and sides[1] < 0'))]
for name,mutant in controls:
    require(mutant!=source,'ineffective mutation '+name)
    for mode in [False,True]:
        r,_=run(mutant,mode);require(r.returncode!=0 and 'Exact check failed:' in r.stderr,'negative control accepted '+name)
    receipts.append({'semanticNegativeControl':name,'rejectedBothModes':True})
manifest=root/'MANIFEST.sha256'
if manifest.exists():
    listed=set()
    for line in manifest.read_text().splitlines():
        expected,name=line.split('  ',1);p=root/name
        require(p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==expected,'hash mismatch '+name);listed.add(name)
    actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts and p.name!='MANIFEST.sha256'}
    require(actual==listed,'manifest inventory mismatch')
print(json.dumps({'status':'PASS','scope':'Producer replay and semantic negative controls; not a formal topological proof.','checks':receipts},indent=2))
