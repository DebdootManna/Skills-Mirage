**devx labs · HACKaMINeD 2026**

Problem Statement

## The Skills

## Mirage

_Build India's first open workforce intelligence system_

From market signals to reskilling paths - India's 50 crore workers need this.

devxlabs.ai · abhishek.rawal@devxlabs.ai


devx labs · Hackathon 2026 devxlabs.ai

```
THE PROBLEM
```
#### Two Sides of a Crisis. Zero Connection.

```
India posts 1 crore job listings/month. 45%+ employers still can't find the right skills.
```
```
DEMAND SIDE —Enterprises
```
- Companies hire GenAI engineers, fire call-centre
    agents
- Signal exists in job postings -nobody reads it at sector
    scale for India
- Hiring patterns reveal strategy 6 months before press
    releases
- No open India-specific market intelligence exists

```
SUPPLY SIDE -Workers
```
- 38 - yr BPO lead in Pune gets a generic 'learn Python'
    suggestion
- Job title tells nothing about actual skills or aspirations
- Most tools ignore geography and local job supply
    entirely
- 8%+ graduate unemployment even in high-hiring
    cities

**VS**


devx labs · Hackathon 2026 devxlabs.ai

```
SCALE OF THE PROBLEM
```
#### The Numbers Behind the Crisis

### 0.5 Cr+

```
job listings posted in India every month
```
### 45%+

```
employers cannot find candidates with right
skills
```
### 8%+

```
graduate unemployment in high-hiring cities
```
### 30 Cr

```
Indian workers in formal + informal
workforce
```
### ₹

```
cost to build -all data sources are public &
free
```
### 48 hrs

```
to build something that outlasts this
hackathon
```

```
SYSTEM ARCHITECTURE
```
#### Two Layers. One Live System.

```
Layer 1 feeds real-time signals into Layer 2. A change in one must propagate to the other automatically.
```
devx labs · Hackathon 2026 · Architecture devxlabs.ai

```
LAYER 1 -Job Market Dashboard
```
- Live scraping + Open source data: Naukri + LinkedIn
    India
- Tab A: Hiring trends by city/sector
- Tab B: Skills demand + gap analysis
- Tab C: AI Vulnerability Index (0–100)
- Displacement early warning signals

```
→ feeds
```
```
LAYER 2 -Worker Intelligence Engine
```
- Worker profile: title + city + XP + write-up
- Personal AI Risk Score (0–100)
- Week-by-week reskilling path
- AI Chatbot: English + Hindi
- Free resources: SWAYAM, NPTEL + global


devx labs · Hackathon 2026 devxlabs.ai

```
LAYER 1 —DASHBOARD REQUIREMENTS
```
#### Three Tabs. All Live. All Data-Derived.

```
Real scraping from Naukri + LinkedIn. Must refresh live during demo. No static CSVs.
```
```
Tab A : Hiring Trends
```
```
Volume trends by job category, city, sector.
```
```
Time range: 7d / 30d / 90d / 1yr.
```
```
Min 20 cities -Tier 2 + Tier 3 required.
```
```
Tab B : Skills Intelligence
```
```
Top 20 rising + declining skills (week-over-
week).
```
```
Skill gap map: what's being hired vs what
PMKVY/SWAYAM, trains for.
```
```
Tab C : AI Vulnerability Index
```
- Score every job 0– 100
- Signals: hiring decline + AI tool
- mentions in JDs + role replacement
    ratio
- Heatmap view by city
- Trend: rising or falling risk?
- Methodology panel -visible,
- no black boxes

```
Example: BPO Voice —Pune: 87/100 Critical · Data Entry -Jaipur: 74/100 High · Data Analyst (AI Tools): 18/100 Low
```

```
LAYER 2 -WORKER INPUT
```
#### What the Worker Tells You

```
No CV. No long forms. Four inputs -and the system does the heavy lifting.
```
devx labs · Hackathon 2026 · Worker Input devxlabs.ai

**1. Current Job Title**

```
E.g. Senior Executive, BPO
Free text -NLP normalises it
```
**2. City**

```
Tier 2 + Tier 3 fully supported
Min 20 cities required
```
**3. Years of Experience**

```
Integer or short range
Weighted in risk scoring
```
**4. Short Write-Up (100–200 words) -The Most Important Input**

```
What they do day-to-day. What they are good at. What work they want to move toward.
Why it matters: Two 'Senior Executives' can have completely different skills. The write-up extracts implicit skills, tools, soft skills, and aspirations
no job title reveals. Your NLP must demonstrably use this input -if the write-up is ignored, it counts as not implemented.
```

devx labs · Hackathon 2026 devxlabs.ai

```
LAYER 2 —OUTPUTS
```
#### Risk Score → Reskilling Path → Chatbot

```
Three connected outputs from one worker profile.
```
```
AI Risk Score
```
(^74) / 100
**HIGH RISK**

- ↑ +8 vs 30 days ago
- BPO voice hiring -34% in Pune
- AI tool mentions in JDs +40%
- vs peers: top 15% at-risk

```
Reskilling Path
```
```
→ AI Content Reviewer
(Hiring in Pune -L1 verified)
```
- Wk 1–3: NPTEL Data Basics
- (IIT Madras, free, 6 hrs/wk)
- Wk 4–5: SWAYAM AI Fundamentals
- Wk 6–8: PMKVY Digital Mktg
- (Nagpur centre, Wardha Rd)
- Total: 8 weeks @ 10 hrs/wk

```
AI Chatbot (EN + HI)
```
```
Context-aware, not canned.
Must handle 5 question types:
```
- Why is my risk score high?
- Show paths under 4 months
- How many BPO jobs in Indore?
- Is this NPTEL cert recognised?
- मुझेकह ाँसेशुरूकरन च हहए?


```
DATA SOURCES
```
#### Sample Datasets - All open source

devx labs · Hackathon 2026 · Dataset Reference devxlabs.ai

```
Source What It Contains Where to Get It
```
```
PLFS Microdata ~4 lakh individual records/yr -employment, sector,
2017 – 2024
```
```
microdata.gov.in
```
```
PMKVY Training Data State/district trained, certified, placed - 2015 – 2024 data.gov.in → search 'PMKVY'
```
```
Naukri (Kaggle) ~5 lakh records: job title, skills, city, salary (2019) kaggle.com → 'naukri job postings india'
```
```
Naukri Live Scrape Real-time listings -Apify actor or Python
BeautifulSoup
```
```
apify.com → Naukri scrapers
```
```
LinkedIn India Jobs Company, role, seniority, skills -Apify LinkedIn
scraper
```
```
apify.com → LinkedIn Jobs
```
```
NPTEL Catalog 2,400+ courses -subject, IIT institution, duration nptel.ac.in (scrapeable)
```
```
SWAYAM Courses 2,000+ free courses, 56M+ enrollments swayam.gov.in (scrapeable)
```
```
WEF Future of Jobs India displacement forecasts by role category weforum.org —free PDF
```

##### The Chatbot - 5 Question Types Required

_will test this live. It must use the worker's actual profile + Layer 1 data._

**01** **_"Why is my risk score so high?"_**

```
Must cite specific Layer 1 signals -hiring decline %, AI tool mention rate -from
the worker's city and role.
```
**02** **_"What jobs are safer for someone like me?"_**

```
Must query Layer 1 Vulnerability Index and return low-score roles that are
actively hiring in the worker's city.
```
**03** **_"Show me paths that take less than 3 months"_**

```
Must regenerate paths with a time constraint, still validating target roles against
live Layer 1 data.
```
**04** **_"How many BPO jobs are in Indore right now?"_**

```
Must query live Layer 1 data. Must return a real number from the pipeline, not a
hallucinated answer.
```
**05** **_"_** **मुझेक्याकरनाचाहिए** **_?" (Hindi)_**

```
Full Hindi support —input in Hindi, response in Hindi, context-aware to the
worker's profile and risk score.
```
Layer 2 —Chatbot Requirements devxlabs.ai


###### WHAT WINNING LOOKS LIKE

```
A team that builds a scraper + chatbot without the intelligence layer will score in the bottom third.
```
devx labs · Hackathon 2026 · Winning Criteria devxlabs.ai

```
1. Live dashboard with real signal
```
```
Refresh during demo. Show a specific data-backed finding: 'BPO voice in
Pune fell 22% in 30 days, AI call-handling +40%.' Methodology visible on
screen.
```
**2. Risk score that reacts to data**

```
Enter a profile → score in seconds. Change a Layer 1 parameter → score
updates live. Pre-computed scores that never change will not pass.
```
```
3. A reskilling path that is specific
```
```
Real course links. Week-by-week schedule. Target role verified as
actively hiring in that city from L1 data. 'Learn Python' is not a path.
```
**4. Chatbot that understands context**

```
Judges ask 3 live questions using the worker's actual profile + L1 data.
Show at least one exchange in Hindi. Generic LLM responses = zero
score.
```

devx labs · Hackathon 2026 devxlabs.ai

```
OPTIONAL CHALLENGES
```
#### Bonus

```
Functional bonus features earn extra Demo Conviction points.
```
```
Displacement Early Warning
```
```
A watchlist in Layer 1 that flags job categories where hiring is
declining fast enough to warrant proactive outreach —before
layoffs begin. Workers in at-risk roles get notified to start
reskilling now, not after the fact.
```
```
Employer-Side View
```
```
Flip the tool: show companies the supply/demand gap —what
skills exist in a city vs. what that sector is actually hiring for. Not
just 'help workers' but 'show employers where the talent
pipeline is breaking'.
```
```
Bonus features must be functional
```

devx labs · Hackathon 2026 devxlabs.ai

```
SCORING RUBRIC
```
#### How You'll Be Judged

**25%**

```
Technical complexity & architecture
All what tech and AI integrations is carried?
```
**20%**

```
Problem depth & real-world applicability
How much depth is thought and implemented to make it super relatable
```
**20 %**

```
Reskilling Path Quality
City-matched, week-by-week, real resources? Write-up demonstrably influences the path?
```
**15%**

```
Chatbot Intelligence
5 question types?Context-aware? Works in Hindi w/o switching to Eng?
```
**10%**

```
Layer Integration
L 1 changes propagate to L 2 live? Feedback loop visible during demo?
```
**10%**

```
Layer 1 Live Signal Quality
Running on real data? Vulnerability Index data-derived with visible methodology?
```

# 48 hours.

_Build something India's 50 crore workers actually need._

- Layer 1: Live dashboard —Naukri + LinkedIn scrape → Hiring Trends + Skills Intel + AI Vulnerability Index (0–100)
- Layer 2: Worker profile (title + city + XP + write-up) → Personal Risk Score + Week-by-week Reskilling Path
- AI Chatbot: context-aware, 5 question types, works in English and Hindi
- Both layers must talk to each other —live, during the demo. No static pipelines.

**Build the real thing. Good luck.**

devxlabs.ai · Questions: abhishek.rawal@devxlabs.ai


