import streamlit as st
import uuid
import time
import os
import re

# --- PERSISTENCE ---
if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'
if 'audit_log' not in st.session_state:
    st.session_state.audit_log = []
if 'forensic_vault' not in st.session_state:
    st.session_state.forensic_vault = {}
if 'system_chatter' not in st.session_state:
    st.session_state.system_chatter = [f"[{time.strftime('%H:%M:%S')}] KERNEL: VINK Neon-Sentinel Active"]

def add_chatter(msg):
    st.session_state.system_chatter.append(f"[{time.strftime('%H:%M:%S')}] {msg}")
    if len(st.session_state.system_chatter) > 6: st.session_state.system_chatter.pop(0)

# --- ELECTRIFYING FRONTEND ENGINE ---
def inject_neon_ui():
    # Electrifying Neon Palette
    bg = "#1D0F32"
    card = "#2a1c4a"
    neon_blue = "#00f2ff" # High-voltage Cyan
    neon_glow = "rgba(0, 242, 255, 0.3)"
    text = "#ffffff"
    border = "#1a2433"

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300;500&display=swap');

    .stApp {{
        background: {bg};
        background-image: radial-gradient({neon_blue}15 1px, transparent 0);
        background-size: 40px 40px;
        color: {text} !important;
    }}

    /* ELECTRIFYING HEADERS */
    .vink-brand {{
        font-family: 'Orbitron', sans-serif;
        font-size: 4rem;
        font-weight: 900;
        color: {neon_blue};
        text-align: center;
        letter-spacing: 25px;
        text-shadow: 0 0 20px {neon_glow}, 0 0 40px {neon_glow};
        margin-bottom: 0px;
    }}
    
    .tactical-sub {{
        text-align: center;
        font-family: 'JetBrains Mono';
        font-size: 0.7rem;
        letter-spacing: 5px;
        color: {neon_blue};
        opacity: 0.7;
        margin-bottom: 40px;
    }}

    /* NEON GLASS CONTAINERS */
    .neon-card {{
        background: {card};
        border: 1px solid {border};
        border-radius: 12px;
        padding: 20px;
        transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
        position: relative;
        overflow: hidden;
    }}
    .neon-card:hover {{
        border-color: {neon_blue};
        box-shadow: 0 0 25px {neon_glow};
        transform: translateY(-5px);
    }}

    /* FORCE TOGGLE LABEL VISIBILITY */
    .stCheckbox label p {{
        color: #ffffff !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-weight: 700 !important;
        font-size: 0.8rem !important;
    }}

    .m-label {{ font-family: 'Orbitron'; color: {neon_blue}; font-size: 0.6rem; letter-spacing: 2px; }}
    .m-value {{ font-family: 'JetBrains Mono'; color: #ffffff; font-size: 1.8rem; font-weight: 700; }}

    /* BUTTONS & INPUTS */
    .stButton>button {{
        border: 1px solid {neon_blue} !important;
        background: transparent !important;
        color: {neon_blue} !important;
        font-family: 'Orbitron' !important;
        letter-spacing: 2px;
        border-radius: 4px;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background: {neon_blue}22 !important;
        box-shadow: 0 0 15px {neon_blue};
    }}
    
    textarea {{
        background: #000000 !important;
        color: {neon_blue} !important;
        border: 1px solid {border} !important;
        font-family: 'JetBrains Mono' !important;
    }}

    /* LEDGER STYLE */
    .audit-text {{ font-family: 'JetBrains Mono'; font-size: 0.8rem; color: {text}; }}
    </style>
    """, unsafe_allow_html=True)

st.set_page_config(page_title="VINK | NEON SENTINEL", layout="wide")
inject_neon_ui()

# --- HEURISTIC ENGINE ---
def scrub_protocol(text, active_rules):
    patterns = {
        "EMAIL": (r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', "R_EMAIL"),
        "IPV4": (r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', "R_IP"),
        "PHONE": (r'\b\d{10}\b', "R_PHONE"),
        "KEY": (r'\b[A-Za-z0-9+/]{32,}\b', "R_KEY")
    }
    sanitized = text
    detections = []
    for label, (pat, r_key) in patterns.items():
        if active_rules.get(r_key):
            matches = re.findall(pat, text)
            if matches:
                detections.append(f"{len(matches)}x {label}")
                sanitized = re.sub(pat, f"<{label}_REDACTED>", sanitized)
    return sanitized, detections

# --- HERO SECTION ---
st.markdown('<div class="vink-brand">VINK</div>', unsafe_allow_html=True)
st.markdown('<div class="tactical-sub">HEURISTIC PRIVACY ENFORCEMENT ENGINE</div>', unsafe_allow_html=True)

# --- ELECTRIFYING KPI HUD ---
k1, k2, k3, k4 = st.columns(4)
for col, (l, v) in zip([k1, k2, k3, k4], [("CORE_LOAD", "14%"), ("THREAT_ENTROPY", "0.002"), ("NEURAL_NODES", "512"), ("UPTIME", "100%")]):
    col.markdown(f"""
    <div class="neon-card">
        <div class="m-label">{l}</div>
        <div class="m-value">{v}</div>
        <div style="width:100%; height:2px; background:{l=='CORE_LOAD' and '#00f2ff33' or '#00f2ff11'}; margin-top:10px;"></div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- OPERATION CENTER ---
tab_guard, tab_detect = st.tabs(["[ 01 ] PRIVACY_ENFORCEMENT", "[ 02 ] NETWORK_DETECTIVE"])

with tab_guard:
    st.markdown("### CONFIGURE REDACTION POLICIES")
    
    # Containers removed - Standard column layout restored
    c1, c2, c3, c4 = st.columns(4)
    r_email = c1.toggle("NODE_EMAIL", True)
    r_phone = c2.toggle("NODE_PHONE", True)
    r_ip = c3.toggle("NODE_IP", False)
    r_keys = c4.toggle("NODE_KEYS", False)
    
    l, r = st.columns([3, 2])
    with l:
        st.markdown("### DATA INGESTION PIPELINE")
        raw_stream = st.text_area("RAW_BUFFER", height=200, placeholder="Awaiting packet ingestion...")
        if st.button("EXECUTE SANITIZATION"):
            if raw_stream:
                tid = f"TR-{str(uuid.uuid4())[:8].upper()}"
                rules = {"R_EMAIL": r_email, "R_PHONE": r_phone, "R_IP": r_ip, "R_KEY": r_keys}
                clean, sigs = scrub_protocol(raw_stream, rules)
                
                st.session_state.audit_log.insert(0, [time.strftime("%H:%M:%S"), tid, "CLEARED", ", ".join(sigs) if sigs else "STABLE"])
                st.session_state.forensic_vault[tid] = {"raw": raw_stream, "clean": clean}
                add_chatter(f"ENFORCEMENT: {tid} | Patterns: {len(sigs)}")
                
                st.markdown(f"""<div style="border-left:4px solid #00f2ff; padding:15px; background:#00f2ff11; margin:15px 0;">
                <b style="color:#00f2ff;">FORENSIC SUMMARY:</b> {len(sigs)} threats neutralized. Trace ID {tid} logged to vault.</div>""", unsafe_allow_html=True)
                st.code(clean, language="bash")

    with r:
        st.markdown("### REAL-TIME TELEMETRY")
        st.progress(0.4, text="Entropy Level")
        st.progress(0.9, text="System Trust")
        

with tab_detect:
    st.subheader("NEURAL DETECTIVE PATHWAYS")
    col_a, col_b = st.columns(2)
    col_a.metric("NODE LATENCY", "12ms", "OPTIMAL")
    col_b.metric("ANOMALY SHIFT", "0.004", "STABLE")
    
    if st.button("INITIATE DIAGNOSTIC SCAN"):
        with st.status("Scanning Neural Fabric..."):
            time.sleep(1)
            add_chatter("SCAN: Checking ingress nodes...")
        st.success("Integrity Verified.")

# --- THE DELIVERABLE: AUDIT LEDGER ---
st.divider()
st.subheader("📝 FORENSIC AUDIT LEDGER")
if st.session_state.audit_log:
    # Modern Column Layout
    h = st.columns([1, 2, 1, 3])
    labels = ["TIME", "TRACE_ID", "STATUS", "SIGNATURES"]
    for i, label in enumerate(labels): h[i].markdown(f"**{label}**")
    
    for row in st.session_state.audit_log:
        r_cols = st.columns([1, 2, 1, 3])
        r_cols[0].markdown(f'<div class="audit-text">{row[0]}</div>', unsafe_allow_html=True)
        r_cols[1].code(row[1])
        r_cols[2].markdown(f'<div style="color:#00f2ff; font-weight:bold;">{row[2]}</div>', unsafe_allow_html=True)
        r_cols[3].markdown(f'<div class="audit-text">{row[3]}</div>', unsafe_allow_html=True)

    st.divider()
    st.subheader(" DEEP VAULT INSPECTION")
    sel = st.selectbox("SELECT TRACE_ID", list(st.session_state.forensic_vault.keys()))
    if sel:
        v1, v2 = st.columns(2)
        v1.caption("ORIGINAL UNENCRYPTED SOURCE")
        v1.code(st.session_state.forensic_vault[sel]["raw"])
        v2.caption("SANITIZED HEURISTIC OUTPUT")
        v2.code(st.session_state.forensic_vault[sel]["clean"])
else:
    st.info("System Standby. Awaiting first packet ingestion for audit generation.")

st.divider()
st.markdown("### SYSTEM EVENT FEED")
chatter_text = "\n".join(st.session_state.system_chatter)
st.markdown(f'<div class="terminal-feed">{chatter_text}</div>', unsafe_allow_html=True)