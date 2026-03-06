# Skills Mirage: India's First Open Workforce Intelligence System

**Skills Mirage** is a dual-layer AI system built for HACKaMINeD 2026. It bridges the gap between shifting job market signals and worker reskilling needs in India. By analyzing real-time data from Naukri and LinkedIn, it provides workers with a personalized "AI Risk Score" and a localized, week-by-week reskilling path using free resources like NPTEL and SWAYAM.

---

## 🚀 Key Features

### Layer 1: Job Market Dashboard (The Signal)
*   **Live Hiring Trends**: Real-time volume tracking across 20+ Tier-2 and Tier-3 Indian cities.
*   **Skills Intelligence**: Identification of the top 20 rising and declining skills week-over-week.
*   **AI Vulnerability Index**: A 0–100 score for job roles based on hiring declines and AI tool mentions in JDs.

### Layer 2: Worker Intelligence Engine (The Solution)
*   **Personalized Risk Scoring**: Analyzes worker write-ups (100–200 words) using NLP to extract implicit skills and calculate vulnerability.
*   **Localized Reskilling Paths**: Generates week-by-week learning schedules with direct links to free courses (NPTEL, SWAYAM, PMKVY) verified against city-specific hiring demand.
*   **Context-Aware Chatbot**: A bilingual (English + Hindi) assistant that answers queries about job safety, specific city data, and course recognition.

---

## 🛠 Tech Stack

*   **Backend**: FastAPI (Python 3.14 compatible)
*   **Frontend**: Streamlit
*   **Database**: SQLite (SQLAlchemy)
*   **AI/NLP**: 
    *   Google Gemini 1.5 Flash (via LangChain)
    *   Rule-based Heuristic NLP for Skill Extraction
*   **Visualizations**: Plotly / Pandas

---

## 📦 Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/skills-mirage.git
    cd skills-mirage
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key**:
    *   Create a `.env` file in the root directory.
    *   Add your Gemini API Key (see [WIKI.md](./WIKI.md) for detailed steps):
        ```env
        GEMINI_API_KEY=your_free_tier_key_here
        ```

4.  **Run the application**:
    ```bash
    chmod +x run.sh
    ./run.sh
    ```

---

## 📊 Evaluation Criteria Alignment

*   **Live Data**: Dashboard uses a background scraper simulation that updates every 10 seconds.
*   **Integration**: Changes in Layer 1 market signals (e.g., a drop in BPO hiring) immediately reflect in Layer 2 risk scores.
*   **Hindi Support**: Chatbot handles Hindi inputs and responds in Hindi natively.
*   **Localized Paths**: Reskilling suggestions are matched to the user's specific city and current market demand.

---

## 📄 License
This project is open-source under the MIT License.
