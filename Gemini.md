# GEMINI.md - Skills Mirage Project Memory

This file serves as the foundational mandate for the "Skills Mirage" project. It contains the system architecture, technical decisions, and operational workflows that must be preserved across sessions.

---

## 🏗 System Architecture & Mandates

### 1. Dual-Layer Integration
*   **Layer 1 (Market Dashboard)**: Live SQL database updated every 10 seconds via `backend/scraper.py`.
*   **Layer 2 (Worker Engine)**: Consumes Layer 1 signals (Hiring trends, AI tool mentions) to dynamically update worker risk scores and reskilling paths.
*   **Mandate**: A change in Layer 1 **must** propagate to Layer 2 in real-time.

### 2. Environment & Stability
*   **Target Version**: **Python 3.12** (Stable).
*   **Avoid**: Python 3.14 (Experimental) due to C-extension incompatibilities with `protobuf` and `streamlit`.
*   **Protobuf Hotfix**: Always export `PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python` in shell scripts to ensure portability across environments.

### 3. NLP Strategy
*   **Hybrid Approach**: Use heuristic/rule-based extraction (`backend/nlp_engine.py`) for core skill parsing. Use **Google Gemini 1.5 Flash** for high-level reasoning and bilingual chatbot support.
*   **Rationale**: Maximizes speed and portability while maintaining high-quality AI responses.

---

## 🔄 Core Methodologies

### 1. The AI Risk Score Formula
`Score = [Base Role Vulnerability (from L1)] + (Experience Factor) - (Extracted Skill Bonus)`
*   **Base Vulnerability**: Derived from % hiring decline and AI JD mentions.
*   **Skill Bonus**: -10 points for modern technical skills extracted from worker write-ups.

### 2. Context-Aware Chatbot (RAG)
*   **Logic**: The chatbot is "Injected" with a system prompt containing the user's specific risk metrics and real-time database counts.
*   **Mandate**: The chatbot must handle 5 specific query types: Risk Explanation, Job Safety, Time Constraints, Live City Stats, and Full Hindi Support.

---

## 📊 Data Pipeline Detail

1.  **Ingestion**: `backend/scraper.py` (Mock Scraper Simulation).
2.  **Storage**: SQLite (`skills_mirage.db`) using SQLAlchemy ORM.
3.  **API**: FastAPI (`backend/main.py`) serving JSON to the frontend.
4.  **UI**: Streamlit (`frontend/app.py`) for live data visualization.

---

## 📝 Historical Log & Decisions

*   **Mar 06, 2026**: Initial build completed for HACKaMINeD 2026.
*   **Decision**: Removed `spacy` to resolve build errors on macOS; replaced with heuristic NLP.
*   **Decision**: Optimized `run.sh` to handle concurrent background processes (Scraper + FastAPI + Streamlit).
*   **Correction**: Updated all `utcnow()` calls to `now(datetime.UTC)` to comply with Python 3.12+ standards.

---

## 🚀 Future Directives
*   **Employer-Side View**: Implement a dashboard for companies to see skill supply/demand gaps.
*   **Early Warning System**: Flag roles for proactive reskilling before hiring declines reach 30%.
