import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000/api"

st.set_page_config(page_title="Skills Mirage", layout="wide")
st.title("Skills Mirage: Workforce Intelligence System")

tab1, tab2 = st.tabs(["Layer 1: Market Dashboard", "Layer 2: Worker Engine"])

with tab1:
    st.header("Live Job Market Dashboard")
    try:
        trends_resp = requests.get(f"{API_URL}/dashboard/hiring-trends").json()
        vuln_resp = requests.get(f"{API_URL}/dashboard/vulnerability").json()
        
        d_tab1, d_tab2, d_tab3 = st.tabs(["Hiring Trends", "Skills Intelligence", "AI Vulnerability Index"])
        
        with d_tab1:
            st.subheader("Hiring Volume Trends")
            col_t1, col_t2 = st.columns(2)
            with col_t1:
                if trends_resp["sector_trends"]:
                    df_sectors = pd.DataFrame(trends_resp["sector_trends"])
                    fig1 = px.bar(df_sectors, x="sector", y="count", title="Hiring by Sector")
                    st.plotly_chart(fig1, use_container_width=True)
            with col_t2:
                if trends_resp["city_trends"]:
                    df_cities = pd.DataFrame(trends_resp["city_trends"])
                    fig2 = px.bar(df_cities, x="city", y="count", title="Hiring by City")
                    st.plotly_chart(fig2, use_container_width=True)
                
        with d_tab2:
            st.subheader("Skills Demand")
            st.write("Top rising and declining skills (Simulated based on Job Postings)")
            col_s1, col_s2 = st.columns(2)
            col_s1.metric("Top Rising Skill", "Python", "+42%")
            col_s2.metric("Top Declining Skill", "Basic Data Entry", "-35%")
            
        with d_tab3:
            st.subheader("AI Vulnerability Index")
            st.markdown("**Methodology**: Score (0-100) calculated using 1) Hiring volume decline 2) AI Tool mentions in Job Descriptions.")
            if vuln_resp:
                df_vuln = pd.DataFrame(vuln_resp)
                st.dataframe(df_vuln.sort_values("score", ascending=False), height=250)
                
                cities = df_vuln["location"].unique()
                if len(cities) > 0:
                    selected_city = st.selectbox("View Heatmap for City", cities)
                    city_data = df_vuln[df_vuln["location"] == selected_city]
                    fig3 = px.bar(city_data, x="job_category", y="score", title=f"Risk Score by Role in {selected_city}", color="score", color_continuous_scale="Reds")
                    st.plotly_chart(fig3, use_container_width=True)
                
    except Exception as e:
        st.error(f"Error connecting to Layer 1 API. Ensure backend is running. {e}")

with tab2:
    st.header("Worker Intelligence Engine")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Worker Profile")
        job_title = st.text_input("Current Job Title", "Senior Executive, BPO")
        city = st.selectbox("City", ["Pune", "Jaipur", "Indore", "Bangalore", "Mumbai", "Delhi", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad", "Surat", "Lucknow", "Kanpur", "Nagpur", "Visakhapatnam", "Bhopal", "Patna", "Ludhiana", "Agra", "Nashik"])
        exp_years = st.number_input("Years of Experience", min_value=0, max_value=50, value=8)
        writeup = st.text_area("Write-up (100-200 words)", "I manage a team of 15 agents taking inbound calls. I am good at communication and reporting in Excel. I want to learn data analysis and move toward a technical role.")
        
        analyze_btn = st.button("Generate Risk Score & Path")
        
    with col2:
        if analyze_btn:
            payload = {
                "job_title": job_title,
                "city": city,
                "exp_years": exp_years,
                "writeup": writeup
            }
            try:
                res = requests.post(f"{API_URL}/worker/analyze", json=payload).json()
                st.session_state["worker_context"] = res
                st.session_state["worker_profile"] = payload
            except Exception as e:
                st.error(f"Error connecting to API. {e}")
                
        if "worker_context" in st.session_state:
            ctx = st.session_state["worker_context"]
            
            st.subheader(f"Personal AI Risk Score: {ctx['risk_score']} / 100")
            hiring_trend = ctx['base_metrics']['hiring_trend']
            ai_mentions = ctx['base_metrics']['ai_mentions']
            st.write(f"- Hiring in {st.session_state['worker_profile']['city']} for similar roles: **{hiring_trend:.1f}%**")
            st.write(f"- AI Tool mentions in JDs: **{ai_mentions:.1f}%** increase")
            
            st.write("**Extracted Insights from Write-up:**")
            st.write(f"- **Skills**: {', '.join(ctx['insights']['skills']) if ctx['insights']['skills'] else 'None'}")
            st.write(f"- **Aspirations**: {', '.join(ctx['insights']['aspirations'])}")
            
            st.subheader(f"Reskilling Path → Target Role: {ctx['target_role']}")
            st.write("*(Role verified as actively hiring and low risk in L1)*")
            for step in ctx['reskilling_path']:
                st.markdown(f"- **{step['week']}**: [{step['course']}]({step['url']}) via {step['provider']} ({step['location']})")
                
            st.divider()
            
            st.subheader("AI Career Chatbot (EN/HI)")
            
            if "messages" not in st.session_state:
                st.session_state["messages"] = []
                
            for m in st.session_state["messages"]:
                st.chat_message(m["role"]).write(m["content"])
                
            prompt = st.chat_input("Ask a question (e.g., 'Why is my risk score so high?')")
            if prompt:
                st.session_state["messages"].append({"role": "user", "content": prompt})
                st.chat_message("user").write(prompt)
                
                chat_payload = {
                    "message": prompt,
                    "context": {
                        "profile": st.session_state["worker_profile"],
                        "market": st.session_state["worker_context"]
                    }
                }
                
                try:
                    chat_res = requests.post(f"{API_URL}/worker/chat", json=chat_payload).json()
                    bot_resp = chat_res["response"]
                    st.session_state["messages"].append({"role": "assistant", "content": bot_resp})
                    st.chat_message("assistant").write(bot_resp)
                except Exception as e:
                    st.error("Error communicating with Chatbot.")
