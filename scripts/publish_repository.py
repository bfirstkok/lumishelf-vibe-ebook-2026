"""Create this assignment repository using the configured Git credential manager.
Never print credentials or pass them in command-line arguments.
"""
import json, os, subprocess, urllib.request, urllib.error
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.chdir(ROOT)
credential=subprocess.run(['git','credential','fill'],input='protocol=https\nhost=github.com\nusername=bfirstkok\n\n',text=True,capture_output=True,check=True)
fields=dict(x.split('=',1) for x in credential.stdout.splitlines() if '=' in x)
token=fields.get('password')
if not token: raise RuntimeError('No GitHub credential is available')
def api(path,data=None):
    req=urllib.request.Request('https://api.github.com'+path,data=json.dumps(data).encode() if data else None,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'LumiShelf-Assignment'})
    with urllib.request.urlopen(req) as response:return json.load(response)
profile=api('/user')
if profile['login']!='bfirstkok':raise RuntimeError('Unexpected GitHub account')
name='lumishelf-vibe-ebook-2026'
try:
    repo=api('/repos/bfirstkok/'+name)
except urllib.error.HTTPError as e:
    if e.code!=404:raise
    repo=api('/user/repos',{'name':name,'description':'LumiShelf E-book Shop: Next.js, Supabase, mock payment and MIT App Inventor assignment','private':False,'auto_init':False})
print(repo['html_url'])
