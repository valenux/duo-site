import sys
HEAD='''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Duo</title>
<meta name="description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='18' fill='%23111114'/%3E%3Ccircle cx='26' cy='32' r='11' fill='%23CFC8FF'/%3E%3Ccircle cx='38' cy='32' r='11' fill='%23fff'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{{--fond:#F4F4F6;--texte:#111114;--texte-2:#3A3A42;--attenue:#6B6B73;--ligne:#EDEDF1;--accent:#5B4FD6;--barre:#CFC8FF}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:'Inter',system-ui,-apple-system,sans-serif;color:var(--texte);background:var(--fond);-webkit-font-smoothing:antialiased;line-height:1.6}}
a{{color:var(--accent)}}
header{{background:#fff;border-bottom:1px solid var(--ligne)}}
.wrap{{max-width:760px;margin:0 auto;padding:0 24px}}
header .wrap{{display:flex;align-items:center;justify-content:space-between;height:68px}}
.logo{{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--texte);font-weight:600;font-size:19px;letter-spacing:-.02em}}
.mark{{width:32px;height:32px;border-radius:10px;background:var(--texte);display:flex;align-items:center;justify-content:center}}
.mark i{{width:10px;height:10px;border-radius:50%;background:var(--barre)}}.mark i+i{{background:#fff;margin-left:-3px}}
header nav a{{color:var(--texte-2);text-decoration:none;font-size:15px;font-weight:500;margin-left:22px}}
main{{padding:56px 0 72px}}
h1{{font-size:clamp(32px,5vw,44px);letter-spacing:-.03em;line-height:1.1;margin:0 0 10px;font-weight:600}}
.lead{{color:var(--attenue);font-size:17px;margin:0 0 36px}}
.card{{background:#fff;border-radius:24px;padding:28px 28px 12px;margin-bottom:16px}}
h2{{font-size:20px;letter-spacing:-.01em;margin:0 0 10px;font-weight:600}}
p,li{{font-size:16px;color:var(--texte-2)}}
ul{{padding-left:20px}} li{{margin-bottom:6px}}
.btn{{display:inline-flex;align-items:center;height:50px;padding:0 22px;border-radius:999px;background:var(--texte);color:#fff;text-decoration:none;font-weight:600;margin:4px 0 16px}}
details{{border-top:1px solid var(--ligne);padding:14px 0}} details:first-of-type{{border-top:0}}
summary{{cursor:pointer;font-weight:600;font-size:16px;color:var(--texte)}}
details p{{margin:8px 0 0}}
footer{{border-top:1px solid var(--ligne);padding:28px 0;font-size:14px;color:var(--attenue);background:#fff}}
footer .wrap{{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}} footer a{{color:var(--attenue);text-decoration:none;margin-left:18px}}
</style>
</head>
<body>
<header><div class="wrap"><a class="logo" href="./"><span class="mark" aria-hidden="true"><i></i><i></i></span>Duo</a>
<nav><a href="aide.html">Aide</a><a href="confidentialite.html">Confidentialité</a></nav></div></header>
<main><div class="wrap">
'''
FOOT='''</div></main>
<footer><div class="wrap"><span>© 2026 Duo · Valentin Guilbert, Montréal</span><nav><a href="./">Accueil</a><a href="aide.html">Aide</a><a href="confidentialite.html">Confidentialité</a></nav></div></footer>
</body></html>
'''
def page(fn,title,desc,body):
    open(fn,'w').write(HEAD.format(title=title,desc=desc)+body+FOOT)
