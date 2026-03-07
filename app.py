"""
Streamlit Web UI — DAL-Aware Agentic RAG for DO-178C Compliance
Run with: streamlit run app.py
"""

import streamlit as st
from src.agent.dal_agent import DALAwareAgent
from src.utils.config import DAL_LEVELS

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="DAL-Aware RAG | DO-178C Compliance",
    page_icon="🛩️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ───────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Syne:wght@400;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Syne', sans-serif;
    }
    .main { background-color: #0a0e1a; }
    .stApp { background-color: #0a0e1a; }

    .hero-title {
        font-family: 'Syne', sans-serif;
        font-size: 2.8rem;
        font-weight: 800;
        color: #e2e8f0;
        line-height: 1.1;
        margin-bottom: 0.2rem;
    }
    .hero-sub {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        color: #38bdf8;
        margin-bottom: 2rem;
        letter-spacing: 0.05em;
    }
    .dal-badge {
        display: inline-block;
        padding: 6px 18px;
        border-radius: 4px;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 600;
        font-size: 1rem;
        margin-bottom: 1rem;
    }
    .dal-a { background: #fef2f2; color: #dc2626; border: 1.5px solid #dc2626; }
    .dal-b { background: #fff7ed; color: #ea580c; border: 1.5px solid #ea580c; }
    .dal-c { background: #fefce8; color: #ca8a04; border: 1.5px solid #ca8a04; }
    .dal-d { background: #f0fdf4; color: #16a34a; border: 1.5px solid #16a34a; }

    .answer-box {
        background: #111827;
        border: 1px solid #1e293b;
        border-left: 3px solid #38bdf8;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        color: #cbd5e1;
        line-height: 1.7;
    }
    .citation-tag {
        display: inline-block;
        background: #1e293b;
        color: #38bdf8;
        border-radius: 4px;
        padding: 2px 10px;
        font-size: 0.75rem;
        font-family: 'JetBrains Mono', monospace;
        margin: 3px 3px 3px 0;
    }
    .chunk-card {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 6px;
        padding: 0.8rem 1rem;
        margin: 0.4rem 0;
        font-size: 0.8rem;
        color: #94a3b8;
        font-family: 'JetBrains Mono', monospace;
        line-height: 1.6;
    }
    .status-ok {
        color: #4ade80;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
    }
    .status-warn {
        color: #fb923c;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
    }
    div[data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid #1e293b;
    }
    .stButton > button {
        background: #38bdf8;
        color: #0a0e1a;
        font-family: 'Syne', sans-serif;
        font-weight: 700;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1.5rem;
        width: 100%;
    }
    .stButton > button:hover {
        background: #7dd3fc;
        color: #0a0e1a;
    }
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #111827;
        color: #e2e8f0;
        border: 1px solid #1e293b;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
    }
    .stSelectbox > div > div {
        background-color: #111827;
        color: #e2e8f0;
        border: 1px solid #1e293b;
    }
</style>
""", unsafe_allow_html=True)


# ── Session state ────────────────────────────────────────────
if "agent" not in st.session_state:
    st.session_state.agent = DALAwareAgent()
if "dal_set" not in st.session_state:
    st.session_state.dal_set = False
if "docs_ingested" not in st.session_state:
    st.session_state.docs_ingested = False
if "history" not in st.session_state:
    st.session_state.history = []


# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🛩️ DAL-Aware RAG")
    st.markdown('<p class="hero-sub">DO-178C Compliance Engine</p>', unsafe_allow_html=True)
    st.divider()

    st.markdown("**Step 1 — Set DAL Level**")
    dal_choice = st.selectbox(
        "Development Assurance Level",
        options=["A — Catastrophic", "B — Hazardous", "C — Major", "D — Minor"],
        index=0
    )
    dal_level = dal_choice[0]

    dal_colors = {"A": "dal-a", "B": "dal-b", "C": "dal-c", "D": "dal-d"}
    dal_descriptions = {
        "A": "Most stringent — flight control, engines",
        "B": "Hazardous failure conditions",
        "C": "Major failure — significant workload",
        "D": "Minor failure — slight workload increase"
    }
    st.markdown(
        f'<div class="dal-badge {dal_colors[dal_level]}">DAL-{dal_level}</div>',
        unsafe_allow_html=True
    )
    st.caption(dal_descriptions[dal_level])

    if st.button("Set DAL Context"):
        st.session_state.agent.set_dal(dal_level)
        st.session_state.dal_set = True
        st.session_state.current_dal = dal_level
        st.success(f"✅ DAL-{dal_level} context active")

    st.divider()
    st.markdown("**Step 2 — Load Documents**")
    docs_path = st.text_input("Documents folder path", value="data/sample_docs/")
    if st.button("Ingest Documents"):
        if not st.session_state.dal_set:
            st.error("Set DAL level first!")
        else:
            with st.spinner("Ingesting compliance documents..."):
                try:
                    st.session_state.agent.ingest_documents(docs_path)
                    st.session_state.docs_ingested = True
                    st.success("✅ Documents ingested")
                except Exception as e:
                    st.error(f"Error: {e}")

    st.divider()
    st.markdown("**System Status**")
    dal_status = f'<span class="status-ok">● DAL-{st.session_state.get("current_dal", "?")} active</span>' \
        if st.session_state.dal_set else '<span class="status-warn">○ DAL not set</span>'
    doc_status = '<span class="status-ok">● Documents loaded</span>' \
        if st.session_state.docs_ingested else '<span class="status-warn">○ No documents</span>'
    st.markdown(dal_status, unsafe_allow_html=True)
    st.markdown(doc_status, unsafe_allow_html=True)

    if st.session_state.history:
        st.divider()
        if st.button("🗑️ Clear History"):
            st.session_state.history = []
            st.rerun()


# ── Main area ────────────────────────────────────────────────
st.markdown('<div class="hero-title">DO-178C Compliance<br/>Query Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">// DAL-AWARE · CITATION-BACKED · LOCAL LLM</div>', unsafe_allow_html=True)

# Example queries
st.markdown("**Try an example query:**")
examples = [
    "What are the structural coverage requirements?",
    "What verification activities are required for DAL-A?",
    "What traceability requirements apply to my DAL?",
    "What are the independence requirements for reviews?",
]
cols = st.columns(2)
for i, example in enumerate(examples):
    if cols[i % 2].button(f"💬 {example}", key=f"ex_{i}"):
        st.session_state.prefill = example

# Query input
query = st.text_area(
    "Your compliance question",
    value=st.session_state.get("prefill", ""),
    height=80,
    placeholder="e.g. What are the structural coverage requirements for DAL-A software?"
)
if "prefill" in st.session_state:
    del st.session_state.prefill

col1, col2 = st.columns([3, 1])
run_query = col1.button("🔍 Run Compliance Query", use_container_width=True)

if run_query and query:
    if not st.session_state.dal_set:
        st.error("⚠️ Please set a DAL level in the sidebar first.")
    elif not st.session_state.docs_ingested:
        st.error("⚠️ Please ingest documents in the sidebar first.")
    else:
        with st.spinner("Querying compliance documents..."):
            try:
                response = st.session_state.agent.query(query)
                st.session_state.history.append({
                    "query": query,
                    "response": response
                })
            except Exception as e:
                st.error(f"Query failed: {e}")

# Results
if st.session_state.history:
    st.divider()
    for item in reversed(st.session_state.history):
        q = item["query"]
        r = item["response"]

        st.markdown(f"**❓ {q}**")
        st.markdown(
            f'<div class="dal-badge {dal_colors.get(r["dal_level"], "dal-a")}">DAL-{r["dal_level"]}</div>',
            unsafe_allow_html=True
        )

        # Citations
        if r.get("citations"):
            citation_html = "".join([f'<span class="citation-tag">📄 {c}</span>' for c in r["citations"]])
            st.markdown(f'**Citations:** {citation_html}', unsafe_allow_html=True)

        # Retrieved chunks
        with st.expander(f"📋 {len(r['answer_chunks'])} relevant compliance chunks"):
            for i, chunk in enumerate(r["answer_chunks"]):
                st.markdown(f'<div class="chunk-card"><b>Chunk {i+1}:</b><br/>{chunk[:400]}...</div>',
                            unsafe_allow_html=True)
        st.divider()
else:
    st.markdown("""
    <div class="answer-box">
    > System ready. Set your DAL level and ingest documents to begin.<br/>
    > All retrievals will be filtered to match your project's assurance level.<br/>
    > No data is sent externally — fully local inference via Phi-3-mini.
    </div>
    """, unsafe_allow_html=True)
