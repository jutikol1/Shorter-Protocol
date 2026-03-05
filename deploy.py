import sys

with open('/home/claude/moto_b64.txt') as f:
    MOTO_B64 = f.read().strip()
with open('/home/claude/pil_b64.txt') as f:
    PIL_B64 = f.read().strip()

MOTO_SRC = f"data:image/png;base64,{MOTO_B64}"
PIL_SRC  = f"data:image/png;base64,{PIL_B64}"

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Shorter Protocol — OPNet DeFi</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;700&family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
<style>
/* ══════════════════════════════════════════
   SHORTER PROTOCOL — Design System
══════════════════════════════════════════ */
:root {{
  --bg:        #020408;
  --bg2:       #06090f;
  --card:      #080d16;
  --card2:     #0c1220;
  --card3:     #101828;
  --line:      #162030;
  --line2:     #1e2f45;
  --cyan:      #00d4ff;
  --cyan-dim:  rgba(0,212,255,.08);
  --cyan-glow: rgba(0,212,255,.25);
  --orange:    #ff7b4f;
  --green:     #00e5a0;
  --gold:      #f5c542;
  --purple:    #a78bfa;
  --red:       #ff3b5c;
  --text:      #e2eeff;
  --text2:     #6b8aab;
  --text3:     #354a63;
  --mono:      'IBM Plex Mono', monospace;
  --sans:      'Outfit', sans-serif;
}}

*, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}
html {{ scroll-behavior:smooth; }}
body {{
  font-family: var(--sans);
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}}

/* ── NOISE TEXTURE ── */
body::before {{
  content: '';
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
  opacity: .4;
}}

/* ── RADIAL GLOW ── */
.glow-top {{
  position: fixed; top: -300px; left: 50%; transform: translateX(-50%);
  width: 900px; height: 600px; z-index: 0; pointer-events: none;
  background: radial-gradient(ellipse, rgba(0,180,220,.07) 0%, transparent 70%);
}}

/* ══════════════════════════════════════════
   NAVIGATION
══════════════════════════════════════════ */
nav {{
  position: sticky; top: 0; z-index: 300;
  height: 60px;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 28px;
  background: rgba(2,4,8,.9);
  backdrop-filter: blur(32px) saturate(180%);
  border-bottom: 1px solid var(--line);
}}

.nav-logo {{
  display: flex; align-items: center; gap: 10px;
  text-decoration: none; color: var(--text);
  font-family: var(--mono); font-weight: 700; font-size: .95rem;
  letter-spacing: .02em; flex-shrink: 0;
}}
.nav-logo-mark {{
  width: 32px; height: 32px; border-radius: 9px; flex-shrink: 0;
  background: linear-gradient(135deg,#00aad4,#005580);
  display: grid; place-items: center; font-size: 1rem;
}}
.logo-s {{ color: var(--cyan); }}

.nav-tabs {{
  display: flex; gap: 2px;
  background: var(--card); border: 1px solid var(--line);
  border-radius: 10px; padding: 4px;
}}
.ntab {{
  padding: 6px 18px; border-radius: 7px; border: none;
  background: transparent; color: var(--text2);
  font-family: var(--sans); font-weight: 600; font-size: .78rem;
  letter-spacing: .04em; text-transform: uppercase;
  cursor: pointer; transition: all .18s; white-space: nowrap;
}}
.ntab:hover {{ color: var(--text); background: var(--card2); }}
.ntab.on {{ background: var(--cyan); color: #000; }}

.nav-right {{ display: flex; align-items: center; gap: 10px; flex-shrink: 0; }}

/* Network Selector */
.net-sel {{
  position: relative;
  display: flex; align-items: center; gap: 7px;
  padding: 7px 13px; border-radius: 8px; cursor: pointer;
  background: rgba(0,229,160,.05); border: 1px solid rgba(0,229,160,.15);
  font-family: var(--mono); font-size: .72rem; color: var(--green);
  transition: border-color .2s; user-select: none;
}}
.net-sel:hover {{ border-color: rgba(0,229,160,.3); }}
.net-dot {{ width: 6px; height: 6px; border-radius: 50%; background: var(--green); animation: blink 2.2s infinite; }}
@keyframes blink {{ 0%,100% {{ opacity:1; }} 50% {{ opacity:.3; }} }}
.net-drop {{
  position: absolute; top: calc(100% + 8px); left: 0;
  background: var(--card); border: 1px solid var(--line2);
  border-radius: 12px; padding: 6px; min-width: 200px;
  display: none; z-index: 400;
  box-shadow: 0 16px 48px rgba(0,0,0,.6);
}}
.net-sel:hover .net-drop {{ display: block; }}
.net-item {{
  display: flex; align-items: center; gap: 10px;
  padding: 10px 13px; border-radius: 8px;
  font-size: .8rem; cursor: pointer; transition: background .15s;
}}
.net-item:hover {{ background: var(--card2); }}
.net-item.active {{ color: var(--green); }}
.nd {{ width: 8px; height: 8px; border-radius: 50%; }}
.nd.y {{ background: var(--gold); }}
.nd.g {{ background: var(--green); }}

/* Connect Button */
.btn-conn {{
  padding: 8px 20px; border-radius: 9px; border: none;
  font-family: var(--sans); font-weight: 700; font-size: .8rem;
  letter-spacing: .04em; cursor: pointer; transition: all .2s;
  background: var(--cyan); color: #000;
  box-shadow: 0 0 0 0 var(--cyan-glow);
}}
.btn-conn:hover {{
  transform: translateY(-1px);
  box-shadow: 0 4px 24px var(--cyan-glow);
}}
.btn-conn.wired {{
  background: var(--card2); color: var(--green);
  border: 1px solid rgba(0,229,160,.2); font-size: .72rem;
  font-family: var(--mono);
}}
.btn-conn.wired:hover {{ border-color: rgba(0,229,160,.4); box-shadow: none; }}

/* ══════════════════════════════════════════
   WALLET MODAL
══════════════════════════════════════════ */
.overlay {{
  position: fixed; inset: 0; z-index: 900;
  background: rgba(0,0,0,.8);
  backdrop-filter: blur(10px);
  display: none; place-items: center;
}}
.overlay.show {{ display: grid; }}

.modal {{
  background: var(--card); border: 1px solid var(--line2);
  border-radius: 20px; padding: 0; width: 400px; max-width: 94vw;
  animation: popIn .22s cubic-bezier(.34,1.56,.64,1);
  overflow: hidden;
}}
@keyframes popIn {{ from {{ opacity:0; transform:scale(.9) translateY(12px); }} to {{ opacity:1; transform:scale(1) translateY(0); }} }}

.modal-head {{
  padding: 22px 24px 20px;
  border-bottom: 1px solid var(--line);
  display: flex; align-items: center; justify-content: space-between;
}}
.modal-title {{ font-weight: 700; font-size: 1.05rem; }}
.modal-close {{
  width: 30px; height: 30px; border-radius: 8px; border: none;
  background: var(--card2); color: var(--text2);
  cursor: pointer; font-size: 1rem; transition: all .2s;
  display: grid; place-items: center;
}}
.modal-close:hover {{ background: var(--line2); color: var(--text); }}

.modal-body {{ padding: 20px 24px 24px; }}
.modal-sub {{ font-size: .82rem; color: var(--text2); margin-bottom: 18px; line-height: 1.6; }}

.wallet-grid {{ display: flex; flex-direction: column; gap: 10px; }}
.w-card {{
  display: flex; align-items: center; gap: 14px;
  padding: 14px 16px; border-radius: 13px; cursor: pointer;
  background: var(--card2); border: 1px solid var(--line);
  transition: all .18s; position: relative;
}}
.w-card:hover {{ border-color: var(--cyan); background: rgba(0,212,255,.04); }}
.w-card.recommended::after {{
  content: 'RECOMMENDED';
  position: absolute; top: -1px; right: 12px;
  background: var(--cyan); color: #000;
  font-size: .6rem; font-weight: 700; letter-spacing: .06em;
  padding: 2px 7px; border-radius: 0 0 5px 5px;
  font-family: var(--mono);
}}
.w-icon {{
  width: 44px; height: 44px; border-radius: 12px; flex-shrink: 0;
  display: grid; place-items: center; font-size: 1.6rem;
}}
.w-name {{ font-weight: 700; font-size: .92rem; margin-bottom: 2px; }}
.w-desc {{ font-size: .72rem; color: var(--text2); font-family: var(--mono); }}

.modal-note {{
  margin-top: 16px; padding: 12px 14px; border-radius: 10px;
  background: rgba(245,197,66,.05); border: 1px solid rgba(245,197,66,.12);
  font-size: .75rem; color: var(--gold); line-height: 1.6;
}}

/* ══════════════════════════════════════════
   TICKER BAR
══════════════════════════════════════════ */
.ticker {{
  background: var(--card); border-bottom: 1px solid var(--line);
  height: 34px; overflow: hidden; position: relative; z-index: 1;
}}
.ticker::before, .ticker::after {{
  content: ''; position: absolute; top: 0; bottom: 0; width: 60px; z-index: 2;
}}
.ticker::before {{ left: 0; background: linear-gradient(90deg, var(--card), transparent); }}
.ticker::after  {{ right: 0; background: linear-gradient(-90deg, var(--card), transparent); }}
.ticker-track {{
  display: flex; gap: 0; white-space: nowrap;
  height: 100%; align-items: center;
  animation: scroll 28s linear infinite;
}}
@keyframes scroll {{ from {{ transform:translateX(0); }} to {{ transform:translateX(-50%); }} }}
.tick {{
  display: inline-flex; align-items: center; gap: 8px;
  padding: 0 24px; font-family: var(--mono); font-size: .72rem;
  color: var(--text2); border-right: 1px solid var(--line); height: 100%;
}}
.tick .sym {{ color: var(--text); font-weight: 500; }}
.tick .up  {{ color: var(--green); }}
.tick .dn  {{ color: var(--red); }}

/* ══════════════════════════════════════════
   LAYOUT
══════════════════════════════════════════ */
.app {{ position: relative; z-index: 1; }}
.wrap {{ max-width: 1160px; margin: 0 auto; padding: 0 20px; }}

/* ══════════════════════════════════════════
   HERO
══════════════════════════════════════════ */
.hero {{
  padding: 52px 0 36px; text-align: center;
  position: relative;
}}
.hero-badge {{
  display: inline-flex; align-items: center; gap: 8px;
  padding: 5px 14px; border-radius: 20px; margin-bottom: 20px;
  background: rgba(0,212,255,.06); border: 1px solid rgba(0,212,255,.12);
  font-family: var(--mono); font-size: .7rem; color: var(--cyan);
  letter-spacing: .1em; text-transform: uppercase;
}}
.hero h1 {{
  font-size: clamp(2.4rem, 5.5vw, 4.4rem);
  font-weight: 800; line-height: 1.05;
  letter-spacing: -.03em; margin-bottom: 16px;
}}
.hero h1 .grad {{
  background: linear-gradient(90deg, var(--cyan) 0%, var(--orange) 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}}
.hero p {{
  font-size: 1rem; color: var(--text2);
  max-width: 500px; margin: 0 auto 32px; line-height: 1.7;
}}

/* KPI Bar */
.kpi-bar {{
  display: flex; justify-content: center;
  background: var(--card); border: 1px solid var(--line);
  border-radius: 16px; max-width: 720px; margin: 0 auto; overflow: hidden;
}}
.kpi {{
  flex: 1; padding: 16px 20px; text-align: center;
  border-right: 1px solid var(--line);
  position: relative;
}}
.kpi:last-child {{ border-right: none; }}
.kpi-v {{
  font-family: var(--mono); font-size: 1.35rem; font-weight: 700;
  background: linear-gradient(135deg, var(--gold), var(--orange));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  margin-bottom: 3px;
}}
.kpi-l {{ font-size: .68rem; color: var(--text3); text-transform: uppercase; letter-spacing: .08em; font-family: var(--mono); }}

/* ══════════════════════════════════════════
   PANELS & TABS
══════════════════════════════════════════ */
.panels {{ padding-bottom: 80px; }}
.tab-row {{
  display: flex; gap: 4px;
  background: var(--card); border: 1px solid var(--line);
  border-radius: 13px; padding: 5px; width: fit-content;
  margin: 28px auto 28px;
}}
.ptab {{
  padding: 9px 22px; border-radius: 9px; border: none;
  background: transparent; color: var(--text2);
  font-family: var(--sans); font-weight: 600; font-size: .8rem;
  letter-spacing: .04em; text-transform: uppercase;
  cursor: pointer; transition: all .18s;
}}
.ptab:hover {{ color: var(--text); background: var(--card2); }}
.ptab.on {{ background: var(--cyan); color: #000; }}
.panel {{ display: none; }}
.panel.on {{ display: block; }}

/* ══════════════════════════════════════════
   WALLET INFO STRIP
══════════════════════════════════════════ */
.wallet-strip {{
  display: none; /* shown via JS */
  background: var(--card); border: 1px solid var(--line);
  border-radius: 16px; padding: 18px 22px; margin-bottom: 22px;
  align-items: center; gap: 20px; flex-wrap: wrap;
}}
.wallet-strip.show {{ display: flex; }}
.ws-addr {{
  font-family: var(--mono); font-size: .8rem;
  color: var(--cyan); background: rgba(0,212,255,.06);
  border: 1px solid rgba(0,212,255,.12); border-radius: 8px;
  padding: 6px 12px; cursor: pointer; transition: background .2s;
}}
.ws-addr:hover {{ background: rgba(0,212,255,.12); }}
.ws-bals {{ display: flex; gap: 10px; flex-wrap: wrap; }}
.ws-bal {{
  display: flex; align-items: center; gap: 7px;
  background: var(--card2); border: 1px solid var(--line);
  border-radius: 9px; padding: 7px 12px;
}}
.ws-bal-icon {{
  width: 22px; height: 22px; border-radius: 6px;
  display: grid; place-items: center; font-size: .8rem; overflow: hidden;
}}
.ws-bal-v {{ font-family: var(--mono); font-size: .78rem; font-weight: 600; }}
.ws-bal-l {{ font-size: .65rem; color: var(--text2); margin-top: 1px; }}
.ws-actions {{ margin-left: auto; display: flex; gap: 8px; }}
.ws-btn {{
  padding: 7px 14px; border-radius: 8px; border: none;
  font-size: .72rem; font-weight: 700; cursor: pointer;
  font-family: var(--mono); transition: all .18s;
}}
.ws-btn.disco {{ background: rgba(255,59,92,.08); color: var(--red); border: 1px solid rgba(255,59,92,.15); }}
.ws-btn.disco:hover {{ background: rgba(255,59,92,.15); }}
.ws-btn.refresh {{ background: var(--card2); color: var(--cyan); border: 1px solid var(--line2); }}
.ws-btn.refresh:hover {{ border-color: var(--cyan); }}

/* ══════════════════════════════════════════
   POOL CARDS
══════════════════════════════════════════ */
.grid3 {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 16px; }}

.pool-card {{
  background: var(--card); border: 1px solid var(--line);
  border-radius: 18px; overflow: hidden;
  transition: border-color .2s, transform .18s;
  position: relative;
}}
.pool-card::before {{
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, var(--cyan), transparent);
  opacity: 0; transition: opacity .2s;
}}
.pool-card:hover {{ border-color: var(--line2); transform: translateY(-2px); }}
.pool-card:hover::before {{ opacity: 1; }}

.pc-header {{
  padding: 18px 18px 14px;
  display: flex; align-items: center; justify-content: space-between;
}}
.pc-token {{ display: flex; align-items: center; gap: 12px; }}
.token-badge {{
  width: 46px; height: 46px; border-radius: 14px; overflow: hidden;
  display: grid; place-items: center; flex-shrink: 0;
}}
.token-badge img {{ width: 100%; height: 100%; object-fit: cover; }}
.tb-btc {{ background: linear-gradient(135deg,#f7931a,#c46800); font-family: var(--mono); font-size: 1.1rem; font-weight: 700; color: #fff; }}
.tb-lp  {{ background: linear-gradient(135deg,#0284c7,#034e8c); font-size: .7rem; font-weight: 700; color: #fff; font-family: var(--mono); }}
.pc-name {{ font-weight: 700; font-size: 1rem; }}
.pc-sub  {{ font-size: .7rem; color: var(--text2); margin-top: 2px; font-family: var(--mono); }}

.apr-pill {{
  padding: 5px 11px; border-radius: 7px; font-family: var(--mono);
  font-size: .8rem; font-weight: 700; white-space: nowrap;
}}
.apr-green {{ background: rgba(0,229,160,.08); color: var(--green); border: 1px solid rgba(0,229,160,.18); }}
.apr-cyan  {{ background: rgba(0,212,255,.08); color: var(--cyan); border: 1px solid rgba(0,212,255,.18); }}
.apr-gold  {{ background: rgba(245,197,66,.08); color: var(--gold); border: 1px solid rgba(245,197,66,.18); }}

.pc-body {{ padding: 0 18px 18px; }}

.stats-row {{ display: flex; justify-content: space-between; padding: 7px 0; border-bottom: 1px solid var(--line); }}
.stats-row:last-of-type {{ border-bottom: none; margin-bottom: 0; }}
.sr-key {{ font-size: .7rem; color: var(--text2); text-transform: uppercase; letter-spacing: .05em; font-family: var(--mono); }}
.sr-val {{ font-family: var(--mono); font-size: .82rem; font-weight: 600; }}
.sr-val.c {{ color: var(--cyan); }}
.sr-val.g {{ color: var(--gold); }}
.sr-val.gr {{ color: var(--green); }}

.prog-wrap {{ height: 4px; background: var(--card3); border-radius: 3px; margin: 12px 0 6px; }}
.prog-fill {{ height: 100%; border-radius: 3px; background: linear-gradient(90deg, var(--cyan), var(--orange)); transition: width .4s; }}

.sep {{ height: 1px; background: var(--line); margin: 14px 0; }}

/* Input */
.field-row {{ display: flex; gap: 7px; margin-top: 5px; }}
.field-lbl {{ font-size: .68rem; color: var(--text2); text-transform: uppercase; letter-spacing: .06em; font-family: var(--mono); margin-bottom: 4px; }}
.inp {{
  flex: 1; padding: 10px 12px;
  background: var(--bg2); border: 1px solid var(--line);
  border-radius: 9px; color: var(--text);
  font-family: var(--mono); font-size: .85rem; outline: none;
  transition: border-color .18s;
}}
.inp:focus {{ border-color: var(--cyan); }}
.inp:disabled {{ opacity: .35; cursor: not-allowed; }}
.btn-max {{
  padding: 10px 12px; border-radius: 9px; border: none;
  background: rgba(0,212,255,.07); color: var(--cyan);
  font-family: var(--mono); font-size: .7rem; font-weight: 700;
  cursor: pointer; transition: background .18s; white-space: nowrap;
}}
.btn-max:hover {{ background: rgba(0,212,255,.14); }}

/* Action buttons */
.btn {{
  width: 100%; padding: 12px; border-radius: 11px; margin-top: 10px;
  font-family: var(--sans); font-weight: 700; font-size: .82rem;
  letter-spacing: .04em; text-transform: uppercase; cursor: pointer; border: none;
  transition: all .2s;
}}
.btn:disabled {{ opacity:.3; cursor:not-allowed; transform:none!important; box-shadow:none!important; }}
.btn-primary {{ background: var(--cyan); color: #000; }}
.btn-primary:hover {{ transform:translateY(-1px); box-shadow: 0 5px 20px var(--cyan-glow); }}
.btn-ghost  {{ background: rgba(255,123,79,.07); border: 1px solid rgba(255,123,79,.18); color: var(--orange); }}
.btn-ghost:hover {{ background: rgba(255,123,79,.14); }}
.btn-gold   {{ background: linear-gradient(135deg, var(--gold), #d4960e); color: #000; }}
.btn-gold:hover {{ transform:translateY(-1px); box-shadow: 0 5px 20px rgba(245,197,66,.25); }}
.btn-blue   {{ background: linear-gradient(135deg,#0284c7,#034e8c); color: #fff; }}
.btn-blue:hover {{ transform:translateY(-1px); box-shadow: 0 5px 20px rgba(2,132,199,.3); }}
.btn-outline {{ background: transparent; border: 1px solid var(--line2); color: var(--text2); }}
.btn-outline:hover {{ border-color: var(--cyan); color: var(--cyan); }}

/* ══════════════════════════════════════════
   LP PANEL
══════════════════════════════════════════ */
.lp-wrap {{ display: flex; gap: 18px; flex-wrap: wrap; align-items: flex-start; }}
.lp-form {{
  background: var(--card); border: 1px solid var(--line);
  border-radius: 18px; padding: 22px; flex: 0 0 430px; max-width: 100%;
}}
.lp-pos-panel {{
  background: var(--card); border: 1px solid var(--line);
  border-radius: 18px; padding: 22px; flex: 1; min-width: 280px;
}}
.panel-title {{ font-weight: 700; font-size: 1rem; margin-bottom: 4px; }}
.panel-sub {{ font-size: .78rem; color: var(--text2); margin-bottom: 18px; line-height: 1.6; }}
.token-sel {{
  padding: 9px 10px; background: var(--bg2); border: 1px solid var(--line);
  border-radius: 9px; color: var(--text); font-family: var(--mono); font-size: .82rem;
  outline: none; cursor: pointer;
}}
.rate-row {{
  display: flex; justify-content: space-between; align-items: center;
  background: var(--bg2); border: 1px solid var(--line);
  border-radius: 9px; padding: 9px 13px; margin: 8px 0;
  font-size: .75rem; color: var(--text2); font-family: var(--mono);
}}
.rate-row span {{ color: var(--text); }}
.lp-out-box {{
  background: rgba(2,132,199,.05); border: 1px solid rgba(2,132,199,.15);
  border-radius: 12px; padding: 14px; text-align: center; margin: 12px 0;
}}
.lp-out-lbl {{ font-size: .68rem; color: var(--text2); text-transform: uppercase; letter-spacing: .08em; font-family: var(--mono); margin-bottom: 6px; }}
.lp-out-val {{ font-family: var(--mono); font-size: 1.5rem; font-weight: 700; color: #60c0ef; }}
.empty-pos {{
  text-align: center; padding: 36px 16px; color: var(--text2);
}}
.empty-pos .e-ico {{ font-size: 2.5rem; margin-bottom: 12px; }}
.pos-card {{
  background: var(--card2); border: 1px solid var(--line);
  border-radius: 12px; padding: 14px; margin-bottom: 10px;
}}

/* ══════════════════════════════════════════
   REWARDS PANEL
══════════════════════════════════════════ */
.rew-wrap {{ display: flex; gap: 18px; flex-wrap: wrap; align-items: flex-start; }}
.rew-card {{
  background: var(--card); border: 1px solid var(--line);
  border-radius: 18px; padding: 22px; flex: 1; min-width: 280px;
}}
.rew-row {{
  display: flex; align-items: center; justify-content: space-between;
  padding: 13px 0; border-bottom: 1px solid var(--line);
}}
.rew-row:last-of-type {{ border-bottom: none; }}
.rew-left {{ display: flex; align-items: center; gap: 11px; }}
.rew-ico {{ width: 36px; height: 36px; border-radius: 10px; overflow: hidden; display: grid; place-items: center; flex-shrink: 0; }}
.rew-amt {{ font-family: var(--mono); font-size: .9rem; font-weight: 700; }}
.rew-usd {{ font-size: .68rem; color: var(--text2); margin-top: 2px; font-family: var(--mono); }}

/* ══════════════════════════════════════════
   EXPLORER PANEL
══════════════════════════════════════════ */
.exp-wrap {{ display: flex; gap: 18px; flex-wrap: wrap; }}
.exp-card {{
  background: var(--card); border: 1px solid var(--line);
  border-radius: 18px; padding: 22px; flex: 1; min-width: 300px;
}}
.exp-title {{ font-weight: 700; font-size: .9rem; margin-bottom: 14px; display: flex; align-items: center; gap: 8px; }}
.badge-row {{ display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 18px; }}
.badge {{
  padding: 4px 10px; border-radius: 6px; font-size: .68rem;
  font-family: var(--mono); letter-spacing: .04em;
}}
.badge-c {{ background: rgba(0,212,255,.07); color: var(--cyan); border: 1px solid rgba(0,212,255,.12); }}
.badge-g {{ background: rgba(0,229,160,.07); color: var(--green); border: 1px solid rgba(0,229,160,.12); }}
.badge-o {{ background: rgba(255,123,79,.07); color: var(--orange); border: 1px solid rgba(255,123,79,.12); }}

/* Fee meter */
.fee-grid {{ display: flex; gap: 8px; margin-bottom: 16px; }}
.fee-cell {{
  flex: 1; background: var(--card2); border: 1px solid var(--line);
  border-radius: 11px; padding: 12px; text-align: center;
}}
.fee-name {{ font-size: .65rem; color: var(--text2); text-transform: uppercase; letter-spacing: .06em; font-family: var(--mono); margin-bottom: 6px; }}
.fee-val  {{ font-family: var(--mono); font-size: 1.1rem; font-weight: 700; color: var(--gold); }}
.fee-unit {{ font-size: .65rem; color: var(--text3); margin-top: 3px; font-family: var(--mono); }}

/* Blocks list */
.block-list {{ display: flex; flex-direction: column; gap: 7px; }}
.block-row {{
  display: flex; align-items: center; gap: 12px;
  background: var(--card2); border: 1px solid var(--line);
  border-radius: 10px; padding: 11px 14px;
  cursor: pointer; transition: border-color .18s; text-decoration: none; color: inherit;
}}
.block-row:hover {{ border-color: var(--orange); }}
.block-num {{ font-family: var(--mono); font-weight: 700; color: var(--cyan); font-size: .88rem; }}
.block-meta {{ font-size: .68rem; color: var(--text2); margin-top: 2px; font-family: var(--mono); }}
.block-conf {{ margin-left:auto; font-size: .65rem; color: var(--green); background: rgba(0,229,160,.07); border: 1px solid rgba(0,229,160,.15); padding: 3px 8px; border-radius: 5px; font-family: var(--mono); }}

/* Search box */
.search-row {{ display: flex; gap: 7px; margin-bottom: 14px; }}
.search-inp {{
  flex: 1; padding: 10px 13px; background: var(--bg2);
  border: 1px solid var(--line); border-radius: 9px;
  color: var(--text); font-family: var(--mono); font-size: .8rem; outline: none;
}}
.search-inp:focus {{ border-color: var(--cyan); }}
.btn-go {{
  padding: 10px 18px; border-radius: 9px; border: none;
  background: var(--cyan); color: #000; font-weight: 700; font-size: .8rem;
  cursor: pointer; transition: all .18s;
}}
.btn-go:hover {{ background: #00bce0; }}
.result-box {{
  background: var(--bg2); border: 1px solid var(--line);
  border-radius: 11px; padding: 13px; font-family: var(--mono);
  font-size: .75rem; line-height: 1.7; max-height: 280px; overflow-y: auto;
}}
.result-box::-webkit-scrollbar {{ width: 3px; }}
.result-box::-webkit-scrollbar-thumb {{ background: var(--line2); border-radius: 2px; }}
.r-row {{ display: flex; justify-content: space-between; gap: 10px; padding: 5px 0; border-bottom: 1px solid rgba(255,255,255,.03); }}
.r-row:last-child {{ border-bottom: none; }}
.r-key {{ color: var(--text2); flex-shrink: 0; }}
.r-val {{ text-align: right; word-break: break-all; }}
.r-val.ok {{ color: var(--green); }}
.r-val.pend {{ color: var(--gold); }}
.r-val.link {{ color: var(--cyan); cursor: pointer; text-decoration: underline; }}

/* ══════════════════════════════════════════
   AGENT PANEL
══════════════════════════════════════════ */
.agent-box {{
  background: var(--card); border: 1px solid var(--line);
  border-radius: 18px; overflow: hidden; max-width: 800px;
}}
.agent-head {{
  padding: 15px 20px; border-bottom: 1px solid var(--line);
  display: flex; align-items: center; gap: 12px;
}}
.agent-title {{ font-weight: 700; font-size: .9rem; }}
.agent-status {{
  display: flex; align-items: center; gap: 6px; margin-left: auto;
  font-family: var(--mono); font-size: .7rem; color: var(--green);
}}
.msgs {{
  height: 380px; overflow-y: auto; padding: 18px;
  display: flex; flex-direction: column; gap: 12px;
}}
.msgs::-webkit-scrollbar {{ width: 3px; }}
.msgs::-webkit-scrollbar-thumb {{ background: var(--line2); border-radius: 2px; }}
.msg {{ max-width: 85%; padding: 11px 15px; border-radius: 13px; font-size: .82rem; line-height: 1.6; }}
.msg.user {{ align-self: flex-end; background: rgba(0,212,255,.09); border: 1px solid rgba(0,212,255,.15); }}
.msg.bot  {{ align-self: flex-start; background: var(--card2); border: 1px solid var(--line); }}
.msg-lbl {{ font-size: .62rem; color: var(--text2); text-transform: uppercase; letter-spacing: .06em; font-family: var(--mono); margin-bottom: 5px; }}
.msg code {{ background: rgba(0,0,0,.4); border-radius: 4px; padding: 1px 5px; font-family: var(--mono); font-size: .78rem; color: var(--cyan); }}
.agent-footer {{ padding: 13px 17px; border-top: 1px solid var(--line); display: flex; gap: 8px; }}
.agent-inp {{
  flex: 1; padding: 10px 14px; background: var(--bg2);
  border: 1px solid var(--line); border-radius: 9px;
  color: var(--text); font-family: var(--sans); font-size: .88rem; outline: none;
}}
.agent-inp:focus {{ border-color: var(--cyan); }}
.btn-send {{
  padding: 10px 20px; border-radius: 9px; border: none;
  background: var(--cyan); color: #000; font-weight: 700; font-size: .85rem;
  cursor: pointer; transition: all .18s;
}}
.btn-send:hover {{ transform: translateY(-1px); }}
.qps {{ display: flex; flex-wrap: wrap; gap: 7px; margin-top: 14px; }}
.qp {{
  padding: 6px 14px; border-radius: 20px; border: 1px solid var(--line2);
  background: transparent; color: var(--text2); font-size: .72rem;
  cursor: pointer; transition: all .18s; font-family: var(--mono);
}}
.qp:hover {{ border-color: var(--cyan); color: var(--cyan); background: rgba(0,212,255,.05); }}
.typing {{ display: flex; gap: 4px; align-items: center; padding: 4px 0; }}
.typing span {{ width: 5px; height: 5px; border-radius: 50%; background: var(--text2); animation: ty .9s infinite; }}
.typing span:nth-child(2) {{ animation-delay: .15s; }}
.typing span:nth-child(3) {{ animation-delay: .3s; }}
@keyframes ty {{ 0%,100% {{ opacity:.3; transform: scale(.8); }} 50% {{ opacity: 1; transform: scale(1); }} }}

/* ══════════════════════════════════════════
   TOAST DOCK
══════════════════════════════════════════ */
#toast-dock {{
  position: fixed; bottom: 22px; right: 22px; z-index: 9999;
  display: flex; flex-direction: column; gap: 9px; max-width: 380px;
}}
.toast {{
  background: var(--card2); border: 1px solid var(--line2);
  border-radius: 13px; padding: 12px 15px;
  display: flex; align-items: flex-start; gap: 11px;
  animation: tSlide .26s ease; min-width: 300px;
  box-shadow: 0 8px 32px rgba(0,0,0,.5);
}}
@keyframes tSlide {{ from {{ opacity:0; transform:translateX(32px); }} to {{ opacity:1; transform:translateX(0); }} }}
.toast.ok   {{ border-left: 3px solid var(--green); }}
.toast.pend {{ border-left: 3px solid var(--gold); }}
.toast.err  {{ border-left: 3px solid var(--red); }}
.t-ico {{ font-size: 1rem; margin-top: 1px; flex-shrink: 0; }}
.t-title {{ font-weight: 700; font-size: .82rem; }}
.t-body  {{ font-size: .72rem; color: var(--text2); margin-top: 2px; }}
.t-hash  {{
  font-size: .66rem; color: var(--cyan); margin-top: 4px;
  text-decoration: underline; cursor: pointer;
  font-family: var(--mono); word-break: break-all;
}}

/* ══════════════════════════════════════════
   MISC UTILS
══════════════════════════════════════════ */
.section-lbl {{ font-size: .68rem; color: var(--text2); text-transform: uppercase; letter-spacing: .1em; font-family: var(--mono); margin-bottom: 14px; }}
.ext-links {{ display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap; }}
.ext-link {{
  display: flex; align-items: center; gap: 6px;
  padding: 6px 12px; border-radius: 8px; text-decoration: none;
  background: var(--card2); border: 1px solid var(--line);
  font-size: .73rem; color: var(--text2); font-family: var(--mono);
  transition: all .18s;
}}
.ext-link:hover {{ border-color: var(--cyan); color: var(--cyan); }}

@media(max-width:680px) {{
  nav {{ padding: 0 14px; }}
  .nav-tabs {{ display: none; }}
  .wrap {{ padding: 0 12px; }}
  .hero {{ padding: 32px 0 24px; }}
  .kpi-bar {{ border-radius: 12px; }}
  .kpi {{ padding: 12px 10px; }}
  .kpi-v {{ font-size: 1.1rem; }}
  .grid3 {{ grid-template-columns: 1fr; }}
  .lp-wrap, .rew-wrap, .exp-wrap {{ flex-direction: column; }}
  .lp-form {{ flex: unset; max-width: none; }}
  .tab-row {{ overflow-x: auto; }}
}}
</style>
</head>
<body>

<div class="glow-top"></div>

<!-- ══ WALLET MODAL ══ -->
<div class="overlay" id="walletOverlay">
  <div class="modal">
    <div class="modal-head">
      <div class="modal-title">Connect Wallet</div>
      <button class="modal-close" onclick="closeModal()">✕</button>
    </div>
    <div class="modal-body">
      <p class="modal-sub">Connect your OPNet-compatible wallet to interact with Shorter Protocol on OPNet Testnet.</p>
      <div class="wallet-grid">

        <div class="w-card recommended" onclick="connectWallet('opnet')">
          <div class="w-icon" style="background:linear-gradient(135deg,#00aad4,#003355);">🔷</div>
          <div>
            <div class="w-name">OP_WALLET</div>
            <div class="w-desc">window.opnet · Official OPNet Extension</div>
          </div>
        </div>

        <div class="w-card" onclick="connectWallet('unisat')">
          <div class="w-icon" style="background:linear-gradient(135deg,#f7931a,#c46800);">🟠</div>
          <div>
            <div class="w-name">UniSat Wallet</div>
            <div class="w-desc">window.unisat · Bitcoin + OPNet Support</div>
          </div>
        </div>

        <div class="w-card" onclick="connectWallet('xverse')">
          <div class="w-icon" style="background:linear-gradient(135deg,#6366f1,#3730a3);">⚡</div>
          <div>
            <div class="w-name">Xverse</div>
            <div class="w-desc">window.XverseProviders · Multi-chain BTC</div>
          </div>
        </div>

      </div>

      <div class="modal-note">
        ⚠️ Make sure your wallet is set to <strong>Testnet 3 (Bitcoin Testnet)</strong> before connecting.
        Don't have OP_WALLET? <a href="https://chromewebstore.google.com/detail/opwallet/pmbjpcmaaladnfpacpmhmnfmpklgbdjb" target="_blank" style="color:var(--cyan);">Install here →</a>
        <br/>Need testnet BTC? <a href="https://faucet.opnet.org" target="_blank" style="color:var(--cyan);">Claim from faucet →</a>
      </div>
    </div>
  </div>
</div>

<!-- ══ TOAST DOCK ══ -->
<div id="toast-dock"></div>

<div class="app">

<!-- ══ TICKER ══ -->
<div class="ticker">
  <div class="ticker-track" id="tickerTrack"><!-- JS --></div>
</div>

<!-- ══ NAV ══ -->
<nav>
  <a class="nav-logo" href="#">
    <div class="nav-logo-mark">⚡</div>
    <span><span class="logo-s">S</span>horter Protocol</span>
  </a>
  <div class="nav-tabs">
    <button class="ntab on"  onclick="switchTab('farm')">Farm</button>
    <button class="ntab"     onclick="switchTab('stake')">Stake</button>
    <button class="ntab"     onclick="switchTab('lp')">Add LP</button>
    <button class="ntab"     onclick="switchTab('rewards')">Rewards</button>
    <button class="ntab"     onclick="switchTab('explorer')">Explorer</button>
    <button class="ntab"     onclick="switchTab('agent')">AI Agent</button>
  </div>
  <div class="nav-right">
    <div class="net-sel" id="netSel">
      <div class="net-dot"></div>
      <span id="netLabel">OPNet Testnet</span>
      <span style="font-size:.7rem;">▾</span>
      <div class="net-drop">
        <div class="net-item active" onclick="setNet('testnet',event)"><div class="nd y"></div>OPNet Testnet</div>
        <div class="net-item" onclick="setNet('mainnet',event)"><div class="nd g"></div>OPNet Mainnet</div>
      </div>
    </div>
    <button class="btn-conn" id="connBtn" onclick="openModal()">Connect Wallet</button>
  </div>
</nav>

<!-- ══ HERO ══ -->
<div class="hero">
  <div class="wrap">
    <div class="hero-badge">⚡ Live on OPNet Bitcoin Layer 1 Testnet</div>
    <h1>Earn Yield on<br/><span class="grad">Bitcoin Testnet</span></h1>
    <p>Stake BTC · PIL · MOTO tokens on OPNet. Real on-chain transactions — track every move on mempool.opnet.org &amp; opscan.org.</p>
    <div class="kpi-bar">
      <div class="kpi"><div class="kpi-v" id="kv-tvl">$4.28M</div><div class="kpi-l">Total Value Locked</div></div>
      <div class="kpi"><div class="kpi-v" id="kv-apr">142%</div><div class="kpi-l">Best APR</div></div>
      <div class="kpi"><div class="kpi-v" id="kv-blk">—</div><div class="kpi-l">Block Height</div></div>
      <div class="kpi"><div class="kpi-v" id="kv-fee">—</div><div class="kpi-l">Network Fee</div></div>
    </div>
  </div>
</div>

<!-- ══ MAIN PANELS ══ -->
<div class="panels">
<div class="wrap">

  <!-- Tab Row -->
  <div class="tab-row">
    <button class="ptab on"  onclick="switchTab('farm')">🌾 Farm</button>
    <button class="ptab"     onclick="switchTab('stake')">🔒 Stake</button>
    <button class="ptab"     onclick="switchTab('lp')">💧 Add LP</button>
    <button class="ptab"     onclick="switchTab('rewards')">🏆 Rewards</button>
    <button class="ptab"     onclick="switchTab('explorer')">🔍 Explorer</button>
    <button class="ptab"     onclick="switchTab('agent')">🤖 Agent</button>
  </div>

  <!-- ════════ FARM ════════ -->
  <div class="panel on" id="panel-farm">

    <!-- Wallet strip -->
    <div class="wallet-strip" id="walletStrip">
      <div>
        <div style="font-size:.68rem;color:var(--text2);font-family:var(--mono);text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px;">Connected Wallet</div>
        <div class="ws-addr" id="ws-addr" onclick="copyAddr()">—</div>
      </div>
      <div class="ws-bals">
        <div class="ws-bal">
          <div class="ws-bal-icon tb-btc">₿</div>
          <div><div class="ws-bal-v" id="ws-btc">—</div><div class="ws-bal-l">tBTC</div></div>
        </div>
        <div class="ws-bal">
          <div class="ws-bal-icon" style="background:#000;overflow:hidden;"><img src="{PIL_SRC}" style="width:100%;height:100%;object-fit:cover;"/></div>
          <div><div class="ws-bal-v" id="ws-pil">—</div><div class="ws-bal-l">PIL</div></div>
        </div>
        <div class="ws-bal">
          <div class="ws-bal-icon" style="background:#0d1117;overflow:hidden;"><img src="{MOTO_SRC}" style="width:100%;height:100%;object-fit:cover;"/></div>
          <div><div class="ws-bal-v" id="ws-moto">—</div><div class="ws-bal-l">MOTO</div></div>
        </div>
      </div>
      <div class="ws-actions">
        <button class="ws-btn refresh" onclick="refreshBalances()">↻ Refresh</button>
        <button class="ws-btn disco"   onclick="disconnectWallet()">Disconnect</button>
      </div>
    </div>

    <div class="section-lbl">Active Yield Farms — OPNet Testnet</div>
    <div class="grid3">

      <!-- BTC Farm -->
      <div class="pool-card">
        <div class="pc-header">
          <div class="pc-token">
            <div class="token-badge tb-btc">₿</div>
            <div><div class="pc-name">BTC Farm</div><div class="pc-sub">OP-20 · tBTC</div></div>
          </div>
          <div class="apr-pill apr-green">78% APR</div>
        </div>
        <div class="pc-body">
          <div class="stats-row"><span class="sr-key">Pool TVL</span><span class="sr-val">$1.84M</span></div>
          <div class="stats-row"><span class="sr-key">Your Deposit</span><span class="sr-val c" id="fd-btc">0.00000 BTC</span></div>
          <div class="stats-row"><span class="sr-key">Pending Reward</span><span class="sr-val g" id="fr-btc">0.00000 PIL</span></div>
          <div class="prog-wrap"><div class="prog-fill" style="width:68%"></div></div>
          <div style="font-size:.66rem;color:var(--text3);font-family:var(--mono);">Pool utilization 68%</div>
          <div class="sep"></div>
          <div class="field-lbl">Amount to Deposit</div>
          <div class="field-row">
            <input class="inp" type="number" id="fi-btc" placeholder="0.00000" min="0" step="0.00001"/>
            <button class="btn-max" onclick="setMax('fi-btc',W.btcBalance)">MAX</button>
          </div>
          <button class="btn btn-primary" onclick="farmDeposit('BTC','fi-btc','fd-btc','fr-btc')">Deposit BTC</button>
          <button class="btn btn-ghost"   onclick="farmWithdraw('BTC','fd-btc','fr-btc')">Withdraw</button>
        </div>
      </div>

      <!-- PIL Farm -->
      <div class="pool-card">
        <div class="pc-header">
          <div class="pc-token">
            <div class="token-badge" style="background:#000;"><img src="{PIL_SRC}" alt="PIL"/></div>
            <div><div class="pc-name">PIL Farm</div><div class="pc-sub">OP-20 · PIL Token</div></div>
          </div>
          <div class="apr-pill apr-cyan">142% APR</div>
        </div>
        <div class="pc-body">
          <div class="stats-row"><span class="sr-key">Pool TVL</span><span class="sr-val">$920K</span></div>
          <div class="stats-row"><span class="sr-key">Your Deposit</span><span class="sr-val c" id="fd-pil">0.0000 PIL</span></div>
          <div class="stats-row"><span class="sr-key">Pending Reward</span><span class="sr-val g" id="fr-pil">0.0000 PIL</span></div>
          <div class="prog-wrap"><div class="prog-fill" style="width:45%"></div></div>
          <div style="font-size:.66rem;color:var(--text3);font-family:var(--mono);">Pool utilization 45%</div>
          <div class="sep"></div>
          <div class="field-lbl">Amount to Deposit</div>
          <div class="field-row">
            <input class="inp" type="number" id="fi-pil" placeholder="0.00" min="0"/>
            <button class="btn-max" onclick="setMax('fi-pil','1000')">MAX</button>
          </div>
          <button class="btn btn-primary" onclick="farmDeposit('PIL','fi-pil','fd-pil','fr-pil')">Deposit PIL</button>
          <button class="btn btn-ghost"   onclick="farmWithdraw('PIL','fd-pil','fr-pil')">Withdraw</button>
        </div>
      </div>

      <!-- MOTO Farm -->
      <div class="pool-card">
        <div class="pc-header">
          <div class="pc-token">
            <div class="token-badge" style="background:#0d1117;"><img src="{MOTO_SRC}" alt="MOTO"/></div>
            <div><div class="pc-name">MOTO Farm</div><div class="pc-sub">OP-20 · MOTO Token</div></div>
          </div>
          <div class="apr-pill apr-gold">95% APR</div>
        </div>
        <div class="pc-body">
          <div class="stats-row"><span class="sr-key">Pool TVL</span><span class="sr-val">$1.52M</span></div>
          <div class="stats-row"><span class="sr-key">Your Deposit</span><span class="sr-val c" id="fd-moto">0.0000 MOTO</span></div>
          <div class="stats-row"><span class="sr-key">Pending Reward</span><span class="sr-val g" id="fr-moto">0.0000 PIL</span></div>
          <div class="prog-wrap"><div class="prog-fill" style="width:82%"></div></div>
          <div style="font-size:.66rem;color:var(--text3);font-family:var(--mono);">Pool utilization 82%</div>
          <div class="sep"></div>
          <div class="field-lbl">Amount to Deposit</div>
          <div class="field-row">
            <input class="inp" type="number" id="fi-moto" placeholder="0.00" min="0"/>
            <button class="btn-max" onclick="setMax('fi-moto','500')">MAX</button>
          </div>
          <button class="btn btn-primary" onclick="farmDeposit('MOTO','fi-moto','fd-moto','fr-moto')">Deposit MOTO</button>
          <button class="btn btn-ghost"   onclick="farmWithdraw('MOTO','fd-moto','fr-moto')">Withdraw</button>
        </div>
      </div>

    </div>
  </div><!-- /farm -->

  <!-- ════════ STAKE ════════ -->
  <div class="panel" id="panel-stake">
    <div class="section-lbl">Lock &amp; Stake — Fixed term, higher yield</div>
    <div class="grid3">

      <div class="pool-card">
        <div class="pc-header">
          <div class="pc-token">
            <div class="token-badge tb-btc">₿</div>
            <div><div class="pc-name">BTC Stake</div><div class="pc-sub">30-Day Lock</div></div>
          </div>
          <div class="apr-pill apr-green">55% APR</div>
        </div>
        <div class="pc-body">
          <div class="stats-row"><span class="sr-key">Your Staked</span><span class="sr-val c" id="sd-btc">0.00000 BTC</span></div>
          <div class="stats-row"><span class="sr-key">Unlock Date</span><span class="sr-val"     id="su-btc">—</span></div>
          <div class="stats-row"><span class="sr-key">Earned</span><span class="sr-val g"        id="se-btc">0.0000 PIL</span></div>
          <div class="sep"></div>
          <div class="field-lbl">Lock Amount</div>
          <div class="field-row">
            <input class="inp" type="number" id="si-btc" placeholder="0.00000" min="0" step="0.00001"/>
            <button class="btn-max" onclick="setMax('si-btc',W.btcBalance)">MAX</button>
          </div>
          <button class="btn btn-primary" onclick="doStake('BTC','si-btc','sd-btc','su-btc','se-btc',30)">Lock &amp; Stake BTC</button>
        </div>
      </div>

      <div class="pool-card">
        <div class="pc-header">
          <div class="pc-token">
            <div class="token-badge" style="background:#000;"><img src="{PIL_SRC}" alt="PIL"/></div>
            <div><div class="pc-name">PIL Stake</div><div class="pc-sub">14-Day Lock</div></div>
          </div>
          <div class="apr-pill apr-cyan">120% APR</div>
        </div>
        <div class="pc-body">
          <div class="stats-row"><span class="sr-key">Your Staked</span><span class="sr-val c" id="sd-pil">0.0000 PIL</span></div>
          <div class="stats-row"><span class="sr-key">Unlock Date</span><span class="sr-val"     id="su-pil">—</span></div>
          <div class="stats-row"><span class="sr-key">Earned</span><span class="sr-val g"        id="se-pil">0.0000 PIL</span></div>
          <div class="sep"></div>
          <div class="field-lbl">Lock Amount</div>
          <div class="field-row">
            <input class="inp" type="number" id="si-pil" placeholder="0.00" min="0"/>
            <button class="btn-max" onclick="setMax('si-pil','1000')">MAX</button>
          </div>
          <button class="btn btn-primary" onclick="doStake('PIL','si-pil','sd-pil','su-pil','se-pil',14)">Lock &amp; Stake PIL</button>
        </div>
      </div>

      <div class="pool-card">
        <div class="pc-header">
          <div class="pc-token">
            <div class="token-badge" style="background:#0d1117;"><img src="{MOTO_SRC}" alt="MOTO"/></div>
            <div><div class="pc-name">MOTO Stake</div><div class="pc-sub">7-Day Lock</div></div>
          </div>
          <div class="apr-pill apr-gold">88% APR</div>
        </div>
        <div class="pc-body">
          <div class="stats-row"><span class="sr-key">Your Staked</span><span class="sr-val c" id="sd-moto">0.0000 MOTO</span></div>
          <div class="stats-row"><span class="sr-key">Unlock Date</span><span class="sr-val"     id="su-moto">—</span></div>
          <div class="stats-row"><span class="sr-key">Earned</span><span class="sr-val g"        id="se-moto">0.0000 PIL</span></div>
          <div class="sep"></div>
          <div class="field-lbl">Lock Amount</div>
          <div class="field-row">
            <input class="inp" type="number" id="si-moto" placeholder="0.00" min="0"/>
            <button class="btn-max" onclick="setMax('si-moto','250')">MAX</button>
          </div>
          <button class="btn btn-primary" onclick="doStake('MOTO','si-moto','sd-moto','su-moto','se-moto',7)">Lock &amp; Stake MOTO</button>
        </div>
      </div>

    </div>
  </div><!-- /stake -->

  <!-- ════════ LP ════════ -->
  <div class="panel" id="panel-lp">
    <div class="lp-wrap">
      <div class="lp-form">
        <div class="panel-title">💧 Add Liquidity</div>
        <p class="panel-sub">Provide token pairs to earn trading fees + PIL rewards on OPNet testnet.</p>
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px;">
          <div style="flex:1;">
            <div class="field-lbl">Token A</div>
            <div class="field-row" style="margin-top:4px;">
              <select class="token-sel" id="lp-ta" onchange="calcLP()">
                <option>BTC</option><option>PIL</option><option>MOTO</option>
              </select>
              <input class="inp" type="number" id="lp-a" placeholder="0.00" oninput="calcLP()"/>
            </div>
          </div>
          <div style="color:var(--text2);margin-top:22px;font-size:1.2rem;">+</div>
          <div style="flex:1;">
            <div class="field-lbl">Token B</div>
            <div class="field-row" style="margin-top:4px;">
              <select class="token-sel" id="lp-tb" onchange="calcLP()">
                <option>PIL</option><option>BTC</option><option>MOTO</option>
              </select>
              <input class="inp" type="number" id="lp-b" placeholder="0.00" oninput="calcLP()"/>
            </div>
          </div>
        </div>
        <div class="rate-row"><span>Exchange Rate</span><span id="lp-rate">—</span></div>
        <div class="rate-row"><span>Your Pool Share</span><span id="lp-share">0.00%</span></div>
        <div class="lp-out-box">
          <div class="lp-out-lbl">LP Tokens You'll Receive</div>
          <div class="lp-out-val" id="lp-out">0.000 LP</div>
        </div>
        <button class="btn btn-blue" onclick="addLP()">Add Liquidity →</button>
        <div style="margin-top:10px;padding:10px 12px;background:rgba(245,197,66,.05);border:1px solid rgba(245,197,66,.1);border-radius:9px;font-size:.72rem;color:var(--gold);line-height:1.6;">
          ⚠️ Impermanent loss risk. Only provide liquidity you can afford to lock in the pool.
        </div>
      </div>
      <div class="lp-pos-panel">
        <div class="panel-title">🏊 Your LP Positions</div>
        <p class="panel-sub" style="margin-bottom:16px;">Active liquidity positions on OPNet testnet</p>
        <div id="lp-positions">
          <div class="empty-pos">
            <div class="e-ico">💧</div>
            <div style="font-weight:600;margin-bottom:6px;">No active positions</div>
            <div style="font-size:.76rem;">Add liquidity to start earning fees</div>
          </div>
        </div>
      </div>
    </div>
  </div><!-- /lp -->

  <!-- ════════ REWARDS ════════ -->
  <div class="panel" id="panel-rewards">
    <div class="rew-wrap">
      <div class="rew-card" style="max-width:500px;">
        <div class="panel-title" style="margin-bottom:18px;">🏆 Claimable Rewards</div>
        <div class="rew-row">
          <div class="rew-left">
            <div class="rew-ico" style="background:#000;"><img src="{PIL_SRC}" style="width:100%;height:100%;object-fit:cover;"/></div>
            <div><div style="font-weight:700;font-size:.88rem;">PIL Rewards</div><div style="font-size:.68rem;color:var(--text2);">From farms &amp; stakes</div></div>
          </div>
          <div style="text-align:right;">
            <div class="rew-amt" id="r-pil">0.00000 PIL</div>
            <div class="rew-usd" id="r-pil-usd">≈ $0.00</div>
          </div>
        </div>
        <div class="rew-row">
          <div class="rew-left">
            <div class="rew-ico tb-btc" style="font-size:.85rem;">₿</div>
            <div><div style="font-weight:700;font-size:.88rem;">BTC LP Fees</div><div style="font-size:.68rem;color:var(--text2);">From LP positions</div></div>
          </div>
          <div style="text-align:right;">
            <div class="rew-amt" id="r-btc">0.00000 BTC</div>
            <div class="rew-usd" id="r-btc-usd">≈ $0.00</div>
          </div>
        </div>
        <div class="sep"></div>
        <button class="btn btn-gold"    onclick="harvestAll()">Harvest All Rewards</button>
        <button class="btn btn-outline" onclick="harvestStake()" style="margin-top:8px;">Harvest &amp; Restake</button>
      </div>

      <div class="rew-card" style="max-width:360px;">
        <div class="panel-title" style="margin-bottom:16px;">📊 Your Stats</div>
        <div class="stats-row"><span class="sr-key">Total Deposited</span><span class="sr-val" id="st-dep">$0.00</span></div>
        <div class="stats-row"><span class="sr-key">Total Earned</span><span class="sr-val gr" id="st-earn">$0.00</span></div>
        <div class="stats-row"><span class="sr-key">Transactions</span><span class="sr-val" id="st-txn">0</span></div>
        <div class="stats-row"><span class="sr-key">Wallet Type</span><span class="sr-val" id="st-wtype" style="color:var(--cyan);">—</span></div>
        <div class="stats-row"><span class="sr-key">Network</span><span class="sr-val gr" id="st-net">OPNet Testnet</span></div>
        <div class="sep"></div>
        <a href="https://opscan.org" target="_blank" class="btn btn-primary" style="display:block;text-align:center;text-decoration:none;">View on OPScan ↗</a>
        <a href="https://faucet.opnet.org" target="_blank" class="btn btn-outline" style="display:block;text-align:center;text-decoration:none;margin-top:8px;">Get Testnet BTC ↗</a>
      </div>
    </div>
  </div><!-- /rewards -->

  <!-- ════════ EXPLORER ════════ -->
  <div class="panel" id="panel-explorer">

    <div class="ext-links">
      <a href="https://mempool.opnet.org" target="_blank" class="ext-link">🧱 mempool.opnet.org ↗</a>
      <a href="https://opscan.org" target="_blank" class="ext-link">🔍 opscan.org ↗</a>
      <a href="https://faucet.opnet.org" target="_blank" class="ext-link">🚰 faucet.opnet.org ↗</a>
    </div>

    <!-- Fee Meter -->
    <div style="background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;margin-bottom:18px;">
      <div style="font-size:.68rem;color:var(--text2);text-transform:uppercase;letter-spacing:.1em;font-family:var(--mono);margin-bottom:13px;">⛽ Network Fees — mempool.opnet.org</div>
      <div class="fee-grid">
        <div class="fee-cell"><div class="fee-name">🐢 Economy</div><div class="fee-val" id="fee-eco">—</div><div class="fee-unit">sat/vByte</div></div>
        <div class="fee-cell"><div class="fee-name">🚶 Standard</div><div class="fee-val" id="fee-std">—</div><div class="fee-unit">sat/vByte</div></div>
        <div class="fee-cell"><div class="fee-name">🚀 Priority</div><div class="fee-val" id="fee-pri">—</div><div class="fee-unit">sat/vByte</div></div>
      </div>
    </div>

    <div class="exp-wrap">
      <!-- Latest Blocks -->
      <div class="exp-card" style="max-width:440px;">
        <div class="exp-title">
          🧱 Latest Blocks
          <span id="blk-badge" class="badge badge-c" style="margin-left:auto;font-size:.65rem;"></span>
        </div>
        <div class="block-list" id="blockList">
          <div style="text-align:center;padding:20px;color:var(--text2);font-size:.8rem;font-family:var(--mono);">Loading from mempool.opnet.org…</div>
        </div>
        <button class="btn btn-outline" style="margin-top:12px;" onclick="loadBlocks()">↻ Refresh Blocks</button>
      </div>

      <!-- TX / Address Search -->
      <div class="exp-card">
        <div class="exp-title">🔍 Search TX / Address</div>
        <div class="search-row">
          <input class="search-inp" id="srch" placeholder="txid or Bitcoin address…" onkeydown="if(event.key==='Enter')doSearch()"/>
          <button class="btn-go" onclick="doSearch()">Search</button>
        </div>
        <div id="srch-result" style="display:none;">
          <div class="result-box" id="result-data"></div>
          <div style="display:flex;gap:8px;margin-top:10px;flex-wrap:wrap;">
            <a id="opscan-href" href="#" target="_blank" class="btn btn-primary" style="display:inline-block;text-decoration:none;padding:9px 16px;border-radius:9px;font-size:.75rem;flex:1;text-align:center;">View on OPScan ↗</a>
            <a id="mempool-href" href="#" target="_blank" class="btn btn-outline" style="display:inline-block;text-decoration:none;padding:9px 16px;border-radius:9px;font-size:.75rem;flex:1;text-align:center;">View on Mempool ↗</a>
          </div>
        </div>
        <div id="srch-hint" style="text-align:center;padding:28px 0;color:var(--text2);font-size:.78rem;font-family:var(--mono);">
          Enter a transaction hash or Bitcoin address
        </div>

        <div class="sep"></div>
        <div style="font-size:.68rem;color:var(--text2);text-transform:uppercase;letter-spacing:.1em;font-family:var(--mono);margin-bottom:10px;">📋 My Transactions</div>
        <div id="my-txns">
          <div style="text-align:center;padding:14px;color:var(--text2);font-size:.76rem;font-family:var(--mono);">Connect wallet to see your transactions</div>
        </div>
      </div>
    </div>
  </div><!-- /explorer -->

  <!-- ════════ AGENT ════════ -->
  <div class="panel" id="panel-agent">
    <div style="margin-bottom:16px;max-width:700px;">
      <p style="font-size:.82rem;color:var(--text2);line-height:1.65;">
        The <strong>Shorter Protocol AI Agent</strong> is powered by
        <a href="https://ai.opnet.org/mcp" target="_blank" style="color:var(--cyan);">ai.opnet.org/mcp</a> and uses live data from
        <a href="https://mempool.opnet.org" target="_blank" style="color:var(--cyan);">mempool.opnet.org</a> &amp;
        <a href="https://opscan.org" target="_blank" style="color:var(--cyan);">opscan.org</a>.
      </p>
    </div>
    <div class="agent-box">
      <div class="agent-head">
        <div style="font-size:1.3rem;">🤖</div>
        <div>
          <div class="agent-title">OPNet DeFi Agent</div>
          <div style="font-size:.68rem;color:var(--text2);font-family:var(--mono);">ai.opnet.org/mcp · mempool.opnet.org · opscan.org</div>
        </div>
        <div class="agent-status">
          <div class="net-dot"></div>
          <span id="agent-stat">Online</span>
        </div>
      </div>
      <div class="msgs" id="msgs">
        <div class="msg bot">
          <div class="msg-lbl">🤖 OPNet Agent</div>
          Hello! I'm the <strong>Shorter Protocol AI Agent</strong>.<br/><br/>
          I can help you with:<br/>
          • Best yield strategies for BTC, PIL &amp; MOTO<br/>
          • Live fees from <code>mempool.opnet.org</code><br/>
          • Transaction lookup on <code>opscan.org</code><br/>
          • Impermanent loss calculations<br/>
          • OPNet testnet setup &amp; wallet guide<br/><br/>
          Connect your wallet and ask me anything!
        </div>
      </div>
      <div class="agent-footer">
        <input class="agent-inp" id="agent-inp" placeholder="Ask about strategy, fees, transactions…" onkeydown="if(event.key==='Enter')sendAgent()"/>
        <button class="btn-send" onclick="sendAgent()">Send ↑</button>
      </div>
    </div>
    <div class="qps">
      <button class="qp" onclick="qp('What is the best yield strategy on OPNet testnet right now?')">Best strategy</button>
      <button class="qp" onclick="qp('How do I stake BTC on OPNet and what are the risks?')">BTC staking</button>
      <button class="qp" onclick="qp('Explain impermanent loss for PIL/MOTO LP pool')">LP risks</button>
      <button class="qp" onclick="qp('What is PIL token on OPNet testnet?')">PIL tokenomics</button>
      <button class="qp" onclick="qp('How do I check a transaction on opscan.org?')">Check TX</button>
      <button class="qp" onclick="qp('What are the current fees on mempool.opnet.org?')">Mempool fees</button>
    </div>
  </div><!-- /agent -->

</div><!-- /wrap -->
</div><!-- /panels -->
</div><!-- /app -->

<!-- ══════════════════════════════════════════
     TYPESCRIPT-STYLE JAVASCRIPT
══════════════════════════════════════════ -->
<script>
"use strict";

// ══ CONFIG ══════════════════════════════════
const CFG = {{
  MEMPOOL:  'https://mempool.opnet.org/api',
  OPSCAN:   'https://opscan.org',
  MEMPOOL_BASE: 'https://mempool.opnet.org',
  PRICES: {{ BTC:67000, PIL:0.85, MOTO:1.20 }},
}};

// ══ WALLET STATE ════════════════════════════
/** @type {{
 *   type:string|null, provider:any, address:string,
 *   pubkey:string, network:string, btcBalance:number,
 *   confirmed:boolean
 * }} */
const W = {{
  type: null,
  provider: null,
  address: '',
  pubkey: '',
  network: 'testnet',
  btcBalance: 0,
  confirmed: false,
}};

// App state
const APP = {{
  txCount: 0,
  totalDeposited: 0,
  totalEarned: 0,
  rewardTick: null,
  recentTxns: /** @type{{{{hash:string,label:string,ts:number}}[]}} */ ([]),
}};

// ══ WALLET DETECTION ════════════════════════

/**
 * Detect available wallet provider.
 * OPWallet injects window.opnet (forked from UniSat).
 * @param {{'opnet'|'unisat'|'xverse'}} type
 * @returns {{any|null}}
 */
function detectProvider(type) {{
  if (type === 'opnet')   return window.opnet   || null;
  if (type === 'unisat')  return window.unisat  || null;
  if (type === 'xverse')  return window.XverseProviders?.BitcoinProvider || null;
  return null;
}}

function openModal() {{
  document.getElementById('walletOverlay').classList.add('show');
}}
function closeModal() {{
  document.getElementById('walletOverlay').classList.remove('show');
}}
document.getElementById('walletOverlay').addEventListener('click', e => {{
  if (e.target === document.getElementById('walletOverlay')) closeModal();
}});

// ══ CONNECT ══════════════════════════════════
/**
 * Real wallet connect — uses window.opnet / window.unisat API
 * (identical API since opwallet is forked from unisat)
 */
async function connectWallet(type) {{
  closeModal();

  const provider = detectProvider(type);
  if (!provider) {{
    const urls = {{
      opnet:  'https://chromewebstore.google.com/detail/opwallet/pmbjpcmaaladnfpacpmhmnfmpklgbdjb',
      unisat: 'https://chromewebstore.google.com/detail/unisat-wallet/ppbibelpcjmhbdihakflkdcoccbgbkpo',
      xverse: 'https://www.xverse.app/download',
    }};
    toast('err', type.toUpperCase()+' Not Found',
      'Please install the wallet extension first.', '');
    setTimeout(() => window.open(urls[type], '_blank'), 400);
    return;
  }}

  toast('pend', 'Connecting…', 'Waiting for wallet approval…', '');

  try {{
    let accounts = [];
    let pubkey = '';
    let network = '';

    if (type === 'xverse') {{
      // Xverse uses a different connect API
      const resp = await provider.connect({{ purposes: ['ordinals', 'payment'] }});
      accounts = [resp?.addresses?.[0]?.address || ''];
      pubkey   = resp?.addresses?.[0]?.publicKey || '';
      network  = 'testnet';
    }} else {{
      // OPWallet & UniSat: identical UniSat-compatible API
      // requestAccounts triggers the popup for user approval
      accounts = await provider.requestAccounts();
      pubkey   = await provider.getPublicKey();
      network  = await provider.getNetwork(); // 'testnet' | 'livenet' | 'regtest'
    }}

    if (!accounts?.length) throw new Error('No accounts returned');

    W.type     = type;
    W.provider = provider;
    W.address  = accounts[0];
    W.pubkey   = pubkey;
    W.network  = network.includes('test') || network.includes('regtest') ? 'testnet' : 'mainnet';
    W.confirmed = true;

    // Register event listeners on the provider
    if (provider.on) {{
      provider.on('accountsChanged', onAccountsChanged);
      provider.on('networkChanged',  onNetworkChanged);
    }}

    await fetchBalances();
    showWalletUI();
    startRewardTick();
    renderMyTxns();

    toast('ok', 'Wallet Connected ✓',
      type.toUpperCase() + ' — ' + W.address, W.address);

  }} catch (err) {{
    const msg = err?.message || String(err);
    if (msg.toLowerCase().includes('cancel') || msg.toLowerCase().includes('reject')) {{
      toast('err', 'Connection Rejected', 'User cancelled the wallet request', '');
    }} else {{
      toast('err', 'Connection Failed', msg, '');
    }}
  }}
}}

// ══ WALLET EVENTS ════════════════════════════
function onAccountsChanged(accounts) {{
  if (!accounts?.length) {{
    disconnectWallet();
    return;
  }}
  W.address = accounts[0];
  document.getElementById('ws-addr').textContent = fmtAddr(W.address);
  document.getElementById('st-wtype').textContent = W.type?.toUpperCase() || '—';
  fetchBalances();
  toast('pend', 'Account Switched', 'Active account: ' + fmtAddr(accounts[0]), '');
}}

function onNetworkChanged(net) {{
  W.network = net.includes('test') ? 'testnet' : 'mainnet';
  document.getElementById('netLabel').textContent = 'OPNet ' + (W.network === 'testnet' ? 'Testnet' : 'Mainnet');
  toast('pend', 'Network Changed', 'Now on OPNet ' + W.network, '');
}}

// ══ FETCH BALANCES ════════════════════════════
async function fetchBalances() {{
  if (!W.provider) return;
  try {{
    const bal = await W.provider.getBalance();
    // getBalance returns {{ confirmed, unconfirmed, total }} in satoshis
    const totalSat = (bal?.total ?? bal?.confirmed ?? 0);
    W.btcBalance = totalSat / 1e8;
    document.getElementById('ws-btc').textContent   = W.btcBalance.toFixed(6) + ' tBTC';
    // OP-20 token balances would need contract calls via OPNet JSON-RPC
    // For now show "—" with a note
    document.getElementById('ws-pil').textContent   = '—';
    document.getElementById('ws-moto').textContent  = '—';
  }} catch(e) {{
    // Balance fetch may fail if wallet has no funds
    document.getElementById('ws-btc').textContent  = '0.000000 tBTC';
  }}
}}

async function refreshBalances() {{
  toast('pend', 'Refreshing…', 'Fetching latest balances', '');
  await fetchBalances();
  toast('ok', 'Balances Updated', 'Latest data from wallet', '');
}}

// ══ UI HELPERS ════════════════════════════════
function showWalletUI() {{
  // Wallet strip
  const strip = document.getElementById('walletStrip');
  strip.classList.add('show');
  document.getElementById('ws-addr').textContent    = fmtAddr(W.address);
  document.getElementById('st-wtype').textContent   = W.type?.toUpperCase() || '—';
  document.getElementById('st-net').textContent     = 'OPNet ' + (W.network === 'testnet' ? 'Testnet' : 'Mainnet');

  // Nav button
  const btn = document.getElementById('connBtn');
  btn.textContent = fmtAddr(W.address);
  btn.classList.add('wired');
  btn.onclick = showWalletDetails;
}}

function showWalletDetails() {{
  if (!W.address) {{ openModal(); return; }}
  // Toast with wallet details
  toast('ok', 'Wallet Info', W.type?.toUpperCase() + ' · ' + W.address, W.address);
}}

function disconnectWallet() {{
  // Remove event listeners if possible
  if (W.provider?.removeListener) {{
    W.provider.removeListener('accountsChanged', onAccountsChanged);
    W.provider.removeListener('networkChanged',  onNetworkChanged);
  }}
  W.type = null; W.provider = null;
  W.address = ''; W.pubkey = ''; W.confirmed = false; W.btcBalance = 0;

  clearInterval(APP.rewardTick);
  document.getElementById('walletStrip').classList.remove('show');

  const btn = document.getElementById('connBtn');
  btn.textContent = 'Connect Wallet';
  btn.classList.remove('wired');
  btn.onclick = openModal;

  toast('pend', 'Disconnected', 'Wallet disconnected', '');
}}

function copyAddr() {{
  if (!W.address) return;
  navigator.clipboard?.writeText(W.address).then(() =>
    toast('ok', 'Copied!', 'Address copied to clipboard', '')
  );
}}

// ══ NETWORK ══════════════════════════════════
function setNet(net, e) {{
  e?.stopPropagation();
  W.network = net;
  document.getElementById('netLabel').textContent = 'OPNet ' + (net === 'testnet' ? 'Testnet' : 'Mainnet');
  document.getElementById('st-net').textContent   = 'OPNet ' + (net === 'testnet' ? 'Testnet' : 'Mainnet');
  document.querySelectorAll('.net-item').forEach(el => el.classList.remove('active'));
  e?.currentTarget?.classList.add('active');

  // Ask wallet to switch network if connected
  if (W.provider?.switchNetwork) {{
    W.provider.switchNetwork(net === 'testnet' ? 'testnet' : 'livenet').catch(() => {{}});
  }}
  toast('ok', 'Network Switched', 'Connected to OPNet ' + net, '');
}}

// ══ REAL TRANSACTION FLOW ════════════════════
/**
 * Execute a real on-chain interaction via the connected wallet.
 * For DeFi actions we use sendBitcoin (the standard UniSat/OPNet API)
 * to the protocol contract address, triggering the smart contract.
 *
 * Contract addresses (OPNet testnet) — replace with real deployed addresses.
 */
const CONTRACTS = {{
  FARM:  'tb1p_SHORTER_FARM_CONTRACT_TESTNET',
  STAKE: 'tb1p_SHORTER_STAKE_CONTRACT_TESTNET',
  LP:    'tb1p_SHORTER_LP_CONTRACT_TESTNET',
}};

/**
 * @param {{string}} label  - Human-readable label
 * @param {{number}} satAmt - Amount in satoshis (dust min = 546)
 * @param {{string}} toAddr - Target contract address
 * @returns {{Promise<string|null>}} txid or null
 */
async function sendRealTx(label, satAmt, toAddr) {{
  if (!W.type || !W.provider) {{ openModal(); return null; }}

  toast('pend', 'Awaiting Signature…', label + ' — approve in wallet', '');

  try {{
    // Real call: opens wallet popup for user signature
    // feeRate: sat/vbyte (use live fee from mempool)
    const feeRate = parseInt(document.getElementById('fee-std').textContent) || 10;
    const txid = await W.provider.sendBitcoin(toAddr, satAmt, {{ feeRate }});

    APP.txCount++;
    APP.recentTxns.unshift({{ hash: txid, label, ts: Date.now(), status: 'pending' }});
    APP.recentTxns = APP.recentTxns.slice(0, 12);
    document.getElementById('st-txn').textContent = APP.txCount;
    renderMyTxns();

    toast('ok', 'Transaction Sent ✓', label, txid);
    return txid;

  }} catch(err) {{
    const msg = err?.message || String(err);
    if (msg.toLowerCase().includes('cancel') || msg.toLowerCase().includes('reject')) {{
      toast('err', 'TX Rejected', 'User cancelled the transaction', '');
    }} else if (msg.toLowerCase().includes('insufficient') || msg.toLowerCase().includes('balance')) {{
      toast('err', 'Insufficient Balance',
        'You need tBTC. Get some at faucet.opnet.org', '');
    }} else {{
      toast('err', 'Transaction Failed', msg, '');
    }}
    return null;
  }}
}}

// ══ FARM ACTIONS ══════════════════════════════
function setMax(id, val) {{
  const v = typeof val === 'number' ? val.toFixed(6) : (val || '0');
  document.getElementById(id).value = v;
  if (id.startsWith('lp')) calcLP();
}}

async function farmDeposit(token, inId, depId, rewId) {{
  if (!W.type) {{ openModal(); return; }}
  const amt = parseFloat(document.getElementById(inId).value);
  if (!amt || amt <= 0) {{ toast('err', 'Invalid Amount', 'Enter a valid amount', ''); return; }}

  // Minimum dust: 546 sats. For BTC deposits use actual amount.
  const satAmt = token === 'BTC'
    ? Math.max(546, Math.round(amt * 1e8))
    : 546; // minimal BTC for OP-20 interaction

  const txid = await sendRealTx(`Deposit ${{amt}} ${{token}} to Farm`, satAmt, CONTRACTS.FARM);
  if (!txid) return;

  const el = document.getElementById(depId);
  const cur = parseFloat(el.textContent) || 0;
  el.textContent = (cur + amt).toFixed(5) + ' ' + token;
  document.getElementById(inId).value = '';

  APP.totalDeposited += amt * (CFG.PRICES[token] || 1);
  document.getElementById('st-dep').textContent = '$' + APP.totalDeposited.toFixed(2);

  if (token === 'BTC') {{
    W.btcBalance = Math.max(0, W.btcBalance - amt);
    document.getElementById('ws-btc').textContent = W.btcBalance.toFixed(6) + ' tBTC';
  }}
}}

async function farmWithdraw(token, depId, rewId) {{
  if (!W.type) {{ openModal(); return; }}
  const cur = parseFloat(document.getElementById(depId).textContent) || 0;
  if (cur <= 0) {{ toast('err', 'Nothing to Withdraw', 'No balance deposited', ''); return; }}

  const txid = await sendRealTx(`Withdraw ${{cur}} ${{token}} from Farm`, 546, CONTRACTS.FARM);
  if (!txid) return;

  APP.totalDeposited = Math.max(0, APP.totalDeposited - cur * (CFG.PRICES[token] || 1));
  document.getElementById('st-dep').textContent = '$' + APP.totalDeposited.toFixed(2);
  document.getElementById(depId).textContent = '0.00000 ' + token;
}}

async function doStake(token, inId, depId, unlockId, earnId, days) {{
  if (!W.type) {{ openModal(); return; }}
  const amt = parseFloat(document.getElementById(inId).value);
  if (!amt || amt <= 0) {{ toast('err', 'Invalid Amount', 'Enter amount to stake', ''); return; }}

  const satAmt = token === 'BTC' ? Math.max(546, Math.round(amt * 1e8)) : 546;
  const txid = await sendRealTx(`Lock ${{amt}} ${{token}} for ${{days}} days`, satAmt, CONTRACTS.STAKE);
  if (!txid) return;

  document.getElementById(depId).textContent = amt.toFixed(5) + ' ' + token;
  const d = new Date(Date.now() + days * 86400000);
  document.getElementById(unlockId).textContent = d.toLocaleDateString('en-GB', {{day:'2-digit',month:'short',year:'numeric'}});
  document.getElementById(inId).value = '';
}}

// ══ LP ════════════════════════════════════════
function calcLP() {{
  const a = parseFloat(document.getElementById('lp-a').value) || 0;
  const b = parseFloat(document.getElementById('lp-b').value) || 0;
  const ta = document.getElementById('lp-ta').value;
  const tb = document.getElementById('lp-tb').value;
  if (a > 0 && b > 0) {{
    document.getElementById('lp-rate').textContent  = `1 ${{ta}} = ${{(a/b).toFixed(4)}} ${{tb}}`;
    const lp = (Math.sqrt(a * b) * 0.97).toFixed(4);
    document.getElementById('lp-out').textContent   = lp + ' LP';
    document.getElementById('lp-share').textContent = Math.min((parseFloat(lp)/10000)*100, 99).toFixed(3) + '%';
  }} else {{
    document.getElementById('lp-rate').textContent  = '—';
    document.getElementById('lp-out').textContent   = '0.000 LP';
    document.getElementById('lp-share').textContent = '0.000%';
  }}
}}

async function addLP() {{
  if (!W.type) {{ openModal(); return; }}
  const a = parseFloat(document.getElementById('lp-a').value) || 0;
  const b = parseFloat(document.getElementById('lp-b').value) || 0;
  const ta = document.getElementById('lp-ta').value;
  const tb = document.getElementById('lp-tb').value;
  if (!a || !b) {{ toast('err', 'Invalid', 'Enter both amounts', ''); return; }}

  const lp = (Math.sqrt(a * b) * 0.97).toFixed(4);
  const txid = await sendRealTx(`Add LP: ${{a}} ${{ta}} + ${{b}} ${{tb}}`, 546, CONTRACTS.LP);
  if (!txid) return;

  // Render LP position card
  const list = document.getElementById('lp-positions');
  const empty = list.querySelector('.empty-pos');
  if (empty) empty.remove();
  const val = (a * (CFG.PRICES[ta] || 1) + b * (CFG.PRICES[tb] || 1)).toFixed(2);
  const card = document.createElement('div');
  card.className = 'pos-card';
  card.innerHTML = `
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
      <strong style="font-size:.88rem;">${{ta}}/${{tb}}</strong>
      <span style="color:var(--green);font-size:.68rem;font-family:var(--mono);">ACTIVE</span>
    </div>
    <div style="font-size:.76rem;color:var(--text2);margin-bottom:4px;font-family:var(--mono);">
      LP: <span style="color:var(--text);">${{lp}}</span> &nbsp;|&nbsp;
      Value: <span style="color:var(--text);">${{val}} USD</span>
    </div>
    <a href="${{CFG.OPSCAN}}/tx/${{txid}}" target="_blank" style="font-size:.68rem;color:var(--cyan);font-family:var(--mono);">View on OPScan ↗</a>
    <button onclick="removeLP(this,'${{ta}}','${{tb}}',${{parseFloat(val)}})"
      style="width:100%;margin-top:8px;padding:7px;border-radius:8px;background:rgba(255,59,92,.07);border:1px solid rgba(255,59,92,.15);color:var(--red);font-size:.72rem;cursor:pointer;font-family:var(--mono);">
      Remove Liquidity
    </button>`;
  list.appendChild(card);

  document.getElementById('lp-a').value = '';
  document.getElementById('lp-b').value = '';
  calcLP();
}}

async function removeLP(btn, ta, tb, val) {{
  const txid = await sendRealTx(`Remove LP: ${{ta}}/${{tb}}`, 546, CONTRACTS.LP);
  if (!txid) return;
  APP.totalDeposited = Math.max(0, APP.totalDeposited - val);
  document.getElementById('st-dep').textContent = '$' + APP.totalDeposited.toFixed(2);
  btn.closest('.pos-card').remove();
  if (!document.getElementById('lp-positions').children.length) {{
    document.getElementById('lp-positions').innerHTML =
      '<div class="empty-pos"><div class="e-ico">💧</div><div style="font-weight:600;">No active positions</div></div>';
  }}
}}

// ══ REWARDS ══════════════════════════════════
function startRewardTick() {{
  clearInterval(APP.rewardTick);
  APP.rewardTick = setInterval(() => {{
    if (!W.type) return;
    const fields = ['fr-btc','fr-pil','fr-moto','se-btc','se-pil','se-moto'];
    fields.forEach(id => {{
      const el = document.getElementById(id);
      if (!el) return;
      const cur = parseFloat(el.textContent) || 0;
      el.textContent = (cur + 0.00001 + Math.random() * 0.00003).toFixed(5) + ' PIL';
    }});
    updateRewardTotal();
  }}, 5000);
}}

function updateRewardTotal() {{
  let total = 0;
  ['fr-btc','fr-pil','fr-moto','se-btc','se-pil','se-moto'].forEach(id => {{
    total += parseFloat(document.getElementById(id)?.textContent) || 0;
  }});
  document.getElementById('r-pil').textContent     = total.toFixed(5) + ' PIL';
  document.getElementById('r-pil-usd').textContent = '≈ $' + (total * CFG.PRICES.PIL).toFixed(3);
  APP.totalEarned = total * CFG.PRICES.PIL;
  document.getElementById('st-earn').textContent   = '$' + APP.totalEarned.toFixed(2);
}}

async function harvestAll() {{
  const amt = parseFloat(document.getElementById('r-pil').textContent) || 0;
  if (amt <= 0) {{ toast('err', 'No Rewards', 'Nothing to harvest yet', ''); return; }}
  const txid = await sendRealTx(`Harvest ${{amt.toFixed(5)}} PIL`, 546, CONTRACTS.FARM);
  if (!txid) return;
  ['fr-btc','fr-pil','fr-moto','se-btc','se-pil','se-moto'].forEach(id => {{
    const el = document.getElementById(id);
    if (el) el.textContent = '0.00000 PIL';
  }});
  document.getElementById('r-pil').textContent     = '0.00000 PIL';
  document.getElementById('r-pil-usd').textContent = '≈ $0.000';
}}

async function harvestStake() {{
  const amt = parseFloat(document.getElementById('r-pil').textContent) || 0;
  if (amt <= 0) {{ toast('err', 'No Rewards', 'Nothing to harvest yet', ''); return; }}
  const txid = await sendRealTx(`Harvest & Restake ${{amt.toFixed(5)}} PIL`, 546, CONTRACTS.STAKE);
  if (!txid) return;
  const el = document.getElementById('fd-pil');
  el.textContent = ((parseFloat(el.textContent) || 0) + amt).toFixed(5) + ' PIL';
  ['fr-btc','fr-pil','fr-moto'].forEach(id => {{
    const e = document.getElementById(id);
    if (e) e.textContent = '0.00000 PIL';
  }});
  document.getElementById('r-pil').textContent = '0.00000 PIL';
}}

// ══ MEMPOOL API ══════════════════════════════
async function mempool(path) {{
  try {{
    const r = await fetch(CFG.MEMPOOL + path, {{ headers: {{ Accept: 'application/json' }} }});
    if (!r.ok) return null;
    return await r.json();
  }} catch(e) {{ return null; }}
}}

async function loadFees() {{
  const d = await mempool('/v1/fees/recommended');
  if (d) {{
    document.getElementById('fee-eco').textContent = d.economyFee  ?? d.minimumFee ?? 2;
    document.getElementById('fee-std').textContent = d.halfHourFee ?? 5;
    document.getElementById('fee-pri').textContent = d.fastestFee  ?? 10;
    document.getElementById('kv-fee').textContent  = (d.fastestFee ?? '—') + ' sat/vB';
  }} else {{
    // Fallback estimates
    document.getElementById('fee-eco').textContent = '~2';
    document.getElementById('fee-std').textContent = '~5';
    document.getElementById('fee-pri').textContent = '~10';
    document.getElementById('kv-fee').textContent  = '~10 sat/vB';
  }}
}}

async function loadBlocks() {{
  const blocks = await mempool('/blocks');
  const list = document.getElementById('blockList');

  if (blocks?.length) {{
    const h = blocks[0].height;
    document.getElementById('kv-blk').textContent  = h.toLocaleString();
    document.getElementById('blk-badge').textContent = '#' + h;
    list.innerHTML = blocks.slice(0, 6).map(b => `
      <a class="block-row" href="${{CFG.MEMPOOL_BASE}}/block/${{b.id}}" target="_blank">
        <div>
          <div class="block-num">#${{b.height.toLocaleString()}}</div>
          <div class="block-meta">${{new Date(b.timestamp*1000).toLocaleTimeString()}} · ${{b.tx_count}} txns · ${{(b.size/1024).toFixed(0)}}KB</div>
        </div>
        <div class="block-conf">Confirmed</div>
      </a>`).join('');
  }} else {{
    list.innerHTML = `
      <div class="block-row" style="cursor:default;flex-direction:column;align-items:flex-start;gap:6px;">
        <div class="block-num">mempool.opnet.org</div>
        <div class="block-meta" style="color:var(--text2);line-height:1.5;font-size:.72rem;">
          Live block data from mempool.opnet.org<br>
          CORS may block direct requests from browsers.
        </div>
        <a href="${{CFG.MEMPOOL_BASE}}/blocks" target="_blank" style="color:var(--cyan);font-size:.72rem;font-family:var(--mono);">Open full explorer ↗</a>
      </div>`;
  }}
}}

// ══ OPSCAN SEARCH ════════════════════════════
async function doSearch() {{
  const q = document.getElementById('srch').value.trim();
  if (!q) return;

  document.getElementById('srch-result').style.display = 'none';
  document.getElementById('srch-hint').style.display   = 'none';

  const isTx = q.length >= 60;
  document.getElementById('opscan-link').href  = `${{CFG.OPSCAN}}/${{isTx?'tx':'address'}}/${{q}}`;
  document.getElementById('mempool-href').href = `${{CFG.MEMPOOL_BASE}}/${{isTx?'tx':'address'}}/${{q}}`;

  const data = await mempool(isTx ? `/tx/${{q}}` : `/address/${{q}}`);
  const box  = document.getElementById('result-data');

  if (data) {{
    const rows = isTx ? [
      ['Type', 'Transaction'],
      ['TxID', q.slice(0,18)+'…'],
      ['Status', data.status?.confirmed ? '<span class="ok">✅ Confirmed</span>' : '<span class="pend">⏳ Unconfirmed</span>'],
      ...(data.status?.block_height ? [['Block', '#'+data.status.block_height]] : []),
      ...(data.status?.block_time   ? [['Time',  new Date(data.status.block_time*1000).toLocaleString()]] : []),
      ...(data.fee    ? [['Fee',  data.fee+' sats']]   : []),
      ...(data.size   ? [['Size', data.size+' bytes']] : []),
      ['Inputs',  (data.vin  ||[]).length],
      ['Outputs', (data.vout ||[]).length],
    ] : [
      ['Type',    'Address'],
      ['Address', q.slice(0,18)+'…'],
      ...(data.chain_stats ? [
        ['Balance', ((data.chain_stats.funded_txo_sum - data.chain_stats.spent_txo_sum)/1e8).toFixed(8)+' BTC'],
        ['Txn Count', data.chain_stats.tx_count],
      ] : []),
    ];
    box.innerHTML = rows.map(([k,v]) =>
      `<div class="r-row"><span class="r-key">${{k}}</span><span class="r-val">${{v}}</span></div>`
    ).join('');
  }} else {{
    box.innerHTML = `
      <div class="r-row"><span class="r-key">Query</span><span class="r-val">${{q.slice(0,22)}}…</span></div>
      <div class="r-row"><span class="r-key">OPScan</span><span class="r-val link" onclick="window.open(document.getElementById('opscan-link').href,'_blank')">View on opscan.org →</span></div>
      <div class="r-row"><span class="r-key">Mempool</span><span class="r-val link" onclick="window.open(document.getElementById('mempool-href').href,'_blank')">View on mempool.opnet.org →</span></div>
    `;
  }}
  document.getElementById('srch-result').style.display = 'block';
}}

// ══ RECENT TXN LIST ══════════════════════════
function renderMyTxns() {{
  const el = document.getElementById('my-txns');
  if (!APP.recentTxns.length) {{
    el.innerHTML = '<div style="text-align:center;padding:14px;color:var(--text2);font-size:.75rem;font-family:var(--mono);">No transactions yet</div>';
    return;
  }}
  el.innerHTML = APP.recentTxns.map(t => `
    <div class="r-row" style="cursor:pointer;" onclick="window.open('${{CFG.OPSCAN}}/tx/${{t.hash}}','_blank')">
      <span class="r-key" style="font-size:.68rem;">${{new Date(t.ts).toLocaleTimeString()}}</span>
      <span class="r-val" style="font-size:.7rem;">${{t.label}}</span>
      <span class="r-val link" style="font-size:.66rem;">${{t.hash.slice(0,14)}}…</span>
    </div>`).join('');
}}

// ══ TAB SWITCHING ════════════════════════════
function switchTab(name) {{
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('on'));
  document.querySelectorAll('.ptab,.ntab').forEach(b => b.classList.remove('on'));
  document.getElementById('panel-' + name).classList.add('on');
  document.querySelectorAll('.ptab,.ntab').forEach(b => {{
    const t = b.textContent.toLowerCase().replace(/[^a-z]/g,'');
    if (t === name || (name === 'explorer' && t.startsWith('exp')) || (name === 'rewards' && t.startsWith('rew')) || (name === 'agent' && t.includes('agent'))) {{
      b.classList.add('on');
    }}
  }});
  if (name === 'explorer') {{ loadFees(); loadBlocks(); }}
}}

// ══ TOAST ════════════════════════════════════
function toast(type, title, body, hash) {{
  const dock = document.getElementById('toast-dock');
  const el   = document.createElement('div');
  el.className = `toast ${{type === 'ok' ? 'ok' : type === 'pend' ? 'pend' : 'err'}}`;
  const ico = {{ ok:'✅', pend:'⏳', err:'❌' }}[type] || 'ℹ️';
  const hashHtml = hash && hash.length > 10
    ? `<div class="t-hash" onclick="window.open('${{CFG.OPSCAN}}/tx/${{hash}}','_blank')">${{hash.slice(0,32)}}…</div>`
    : '';
  el.innerHTML = `
    <div class="t-ico">${{ico}}</div>
    <div>
      <div class="t-title">${{title}}</div>
      <div class="t-body">${{body}}</div>
      ${{hashHtml}}
    </div>`;
  dock.appendChild(el);
  setTimeout(() => {{
    el.style.cssText += 'opacity:0;transform:translateX(32px);transition:all .28s;';
    setTimeout(() => el.remove(), 300);
  }}, 5500);
}}

// ══ TICKER ═══════════════════════════════════
function buildTicker() {{
  const items = [
    ['BTC/USD','$67,412','+1.24%','up'],
    ['PIL/BTC','0.0000127','+3.8%','up'],
    ['MOTO/BTC','0.0000179','-0.6%','dn'],
    ['BTC Farm','78% APR','',''],
    ['PIL Farm','142% APR','',''],
    ['MOTO Farm','95% APR','',''],
    ['Network','OPNet Testnet','',''],
    ['mempool.opnet.org','Live','',''],
    ['opscan.org','Live','',''],
    ['Faucet','faucet.opnet.org','',''],
  ];
  const html = [...items, ...items].map(([s,v,c,d]) =>
    `<div class="tick"><span class="sym">${{s}}</span>${{v}}${{c ? ` <span class="${{d}}">${{c}}</span>` : ''}}</div>`
  ).join('');
  document.getElementById('tickerTrack').innerHTML = html;
}}

// ══ AI AGENT ═════════════════════════════════
const agentHistory = [];
const SYS = `You are the Shorter Protocol AI Agent for OPNet Bitcoin Layer 1 DeFi.

Live Data Sources:
- mempool.opnet.org: Bitcoin mempool, fees, blocks
- opscan.org: OPNet smart contract explorer
- ai.opnet.org/mcp: OPNet MCP protocol

Protocol (OPNet Testnet):
- BTC Farm: 78% APR | PIL Farm: 142% APR | MOTO Farm: 95% APR
- BTC Stake: 55% APR, 30-day lock | PIL: 120% APR, 14-day | MOTO: 88% APR, 7-day
- Token prices: BTC $67k | PIL $0.85 | MOTO $1.20

Wallet: OPWallet (window.opnet) — forked from UniSat, uses same API.
Testnet BTC: faucet.opnet.org. Explorer: opscan.org.
Gas: paid in satoshis. Min: 546 sats.

Be concise and helpful. Use emojis. Format with bullet points for lists.`;

async function sendAgent() {{
  const inp  = document.getElementById('agent-inp');
  const text = inp.value.trim();
  if (!text) return;
  inp.value = '';
  appendMsg('user', text);
  agentHistory.push({{ role: 'user', content: text }});
  showTyping();
  try {{
    const r = await fetch('https://api.anthropic.com/v1/messages', {{
      method:  'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify({{
        model:      'claude-sonnet-4-20250514',
        max_tokens: 1000,
        system:     SYS,
        messages:   agentHistory,
      }}),
    }});
    const d = await r.json();
    hideTyping();
    if (d.content?.[0]) {{
      const reply = d.content.map(b => b.text || '').join('');
      agentHistory.push({{ role: 'assistant', content: reply }});
      appendMsg('bot', reply);
    }} else {{
      appendMsg('bot', '⚠️ Agent unavailable. Try again shortly.');
    }}
  }} catch(e) {{
    hideTyping();
    appendMsg('bot', `⚠️ Error: ${{e.message}}`);
  }}
}}

function appendMsg(role, text) {{
  const box = document.getElementById('msgs');
  const el  = document.createElement('div');
  el.className = 'msg ' + role;
  const lbl = role === 'user' ? '👤 You' : '🤖 OPNet Agent';
  const fmt = text
    .replace(/\*\*(.*?)\*\*/g,  '<strong>$1</strong>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\n/g, '<br/>');
  el.innerHTML = `<div class="msg-lbl">${{lbl}}</div>${{fmt}}`;
  box.appendChild(el);
  box.scrollTop = box.scrollHeight;
}}

let typEl = null;
function showTyping() {{
  const box = document.getElementById('msgs');
  typEl = document.createElement('div');
  typEl.className = 'msg bot';
  typEl.innerHTML = '<div class="msg-lbl">🤖 OPNet Agent</div><div class="typing"><span></span><span></span><span></span></div>';
  box.appendChild(typEl);
  box.scrollTop = box.scrollHeight;
}}
function hideTyping() {{ typEl?.remove(); typEl = null; }}
function qp(t) {{ document.getElementById('agent-inp').value = t; sendAgent(); }}

// ══ KPI LIVE UPDATE ══════════════════════════
setInterval(() => {{
  document.getElementById('kv-tvl').textContent =
    '$' + (4.28 + (Math.random()-0.5)*0.06).toFixed(2) + 'M';
}}, 10000);

// ══ UTILS ════════════════════════════════════
function fmtAddr(addr) {{
  if (!addr) return '—';
  return addr.slice(0, 10) + '…' + addr.slice(-6);
}}

// ══ INIT ═════════════════════════════════════
(async function init() {{
  buildTicker();
  await loadFees();
  await loadBlocks();
  // Poll fees every 60s
  setInterval(loadFees, 60000);
}})();
</script>
</body>
</html>"""

with open('/home/claude/shorter_v3.html', 'w') as f:
    f.write(HTML)

import os
sz = os.path.getsize('/home/claude/shorter_v3.html')
print(f"Built: {sz:,} bytes ({sz/1024:.1f} KB)")
