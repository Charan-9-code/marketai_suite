import streamlit as st
import os
import json
from groq import Groq

# ========================================
# MARKETAI SUITE - Hackathon-Ready App
# Tech Stack: Streamlit + Python + Groq (LLaMA 3.3 70B)
# Run: streamlit run app.py
# Prerequisites:
#   pip install streamlit groq
#   Set environment variable: export GROQ_API_KEY=your_groq_key_here
# ========================================

st.set_page_config(
    page_title="MarketAI Suite",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation
st.sidebar.title("📈 MarketAI Suite")
st.sidebar.markdown("**AI-powered Sales & Marketing Assistant**")
st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📣 Campaign Generator", "🎤 Sales Pitch Generator", "🔍 Lead Scoring"]
)

# Initialize Groq Client
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("❌ GROQ_API_KEY environment variable not set. Please set it before running the app.")
    st.info("Example: export GROQ_API_KEY='gsk_...'")
    st.stop()

try:
    client = Groq(api_key=api_key)
except Exception as e:
    st.error(f"Failed to initialize Groq client: {str(e)}")
    st.stop()

# Reusable Groq call function
def call_groq(prompt: str, temperature: float = 0.7, max_tokens: int = 1200) -> str:
    """Call Groq LLaMA 3.3 70B with error handling."""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are an expert sales and marketing strategist. Provide concise, professional, actionable, and business-focused outputs. Use clear structure, headings, and bullet points where appropriate."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=0.95
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"❌ Groq API Error: {str(e)}")
        return None

# ========================================
# PAGE 1: HOME / DASHBOARD
# ========================================
if page == "🏠 Home":
    st.title("MarketAI Suite")
    st.subheader("AI-powered Sales & Marketing Assistant")
    
    st.markdown("""
    Welcome to **MarketAI Suite** — your intelligent AI companion for marketing and sales teams.
    
    Leverage Groq's LLaMA 3.3 70B to:
    - Generate high-performing marketing campaigns
    - Create compelling sales pitches
    - Qualify and score leads instantly
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📣 Campaign Generator")
        st.write("Create targeted campaigns across LinkedIn, Instagram, Email & more.")
        st.caption("Multi-platform strategy • Content ideas • Ad copy")
    
    with col2:
        st.markdown("### 🎤 Sales Pitch Generator")
        st.write("Craft personalized elevator pitches and outreach messages.")
        st.caption("Value propositions • Differentiators • CTA")
    
    with col3:
        st.markdown("### 🔍 Lead Scoring")
        st.write("Score leads using BANT-like criteria with AI intelligence.")
        st.caption("0-100 score • Category • Next action")

    st.divider()
    st.markdown("**How to use:** Select a page from the sidebar and fill in the inputs to generate AI-powered outputs.")

# ========================================
# PAGE 2: CAMPAIGN GENERATOR
# ========================================
elif page == "📣 Campaign Generator":
    st.title("📣 AI Marketing Campaign Generator")
    st.markdown("Generate complete campaigns optimized for multiple platforms.")
    
    product_desc = st.text_area(
        "Product / Service Description",
        height=120,
        placeholder="e.g., AI-powered project management tool that automates task assignment and provides real-time analytics for remote teams."
    )
    
    target_audience = st.text_area(
        "Target Audience",
        height=80,
        placeholder="e.g., Mid-size SaaS companies in India, marketing managers aged 28-45, budget $5k-50k/month"
    )
    
    platforms = st.multiselect(
        "Marketing Platforms",
        ["LinkedIn", "Instagram", "Facebook", "Twitter/X", "Email", "YouTube", "TikTok"],
        default=["LinkedIn", "Instagram", "Email"]
    )
    
    if st.button("🚀 Generate Campaign", type="primary", use_container_width=True):
        if not product_desc.strip() or not target_audience.strip():
            st.warning("Please provide both product description and target audience.")
        else:
            with st.spinner("Generating campaign strategy..."):
                prompt = f"""
Generate a professional marketing campaign for the following:

Product: {product_desc}
Target Audience: {target_audience}
Platforms: {', '.join(platforms) if platforms else 'Multi-channel'}

Structure your response exactly with these headings:
Campaign Objective
5 Content Ideas
3 Ad Copy Variations
Call-To-Action Suggestions
Tracking & Measurement Metrics

Be concise, actionable, and business-focused.
"""
                result = call_groq(prompt, temperature=0.75, max_tokens=1500)
                if result:
                    st.markdown("### 📋 Generated Campaign")
                    st.markdown(result)

# ========================================
# PAGE 3: SALES PITCH GENERATOR
# ========================================
elif page == "🎤 Sales Pitch Generator":
    st.title("🎤 AI Sales Pitch Generator")
    st.markdown("Create persuasive, persona-tailored sales pitches.")
    
    product_name = st.text_input("Product / Solution Name", placeholder="e.g., MarketAI Pro")
    
    persona = st.text_area(
        "Customer Persona Description",
        height=100,
        placeholder="e.g., Head of Marketing at a Series B SaaS startup, struggling with lead qualification and campaign ROI measurement."
    )
    
    industry = st.selectbox(
        "Industry",
        ["Technology", "Finance", "Healthcare", "Retail & E-commerce", "Manufacturing", "Education", "Professional Services", "Other"]
    )
    
    company_size = st.selectbox(
        "Company Size",
        ["Small (1-50 employees)", "Medium (51-500 employees)", "Enterprise (500+ employees)"]
    )
    
    if st.button("🎯 Generate Pitch", type="primary", use_container_width=True):
        if not product_name.strip() or not persona.strip():
            st.warning("Product name and customer persona are required.")
        else:
            with st.spinner("Crafting personalized sales pitch..."):
                prompt = f"""
Create a professional sales pitch for:

Product: {product_name}
Customer Persona: {persona}
Industry: {industry}
Company Size: {company_size}

Output exactly these sections:
30-Second Elevator Pitch
Value Proposition
Key Differentiators (use bullet points)
Call-To-Action

Then provide:
Email Pitch (short version)
LinkedIn Message (concise outreach)

Keep language persuasive, benefit-focused, and professional.
"""
                result = call_groq(prompt, temperature=0.7, max_tokens=1400)
                if result:
                    st.markdown("### 💼 Generated Sales Pitch")
                    st.markdown(result)

# ========================================
# PAGE 4: LEAD SCORING
# ========================================
elif page == "🔍 Lead Scoring":
    st.title("🔍 AI Lead Scoring & Qualification")
    st.markdown("Score leads using AI analysis (inspired by BANT framework).")
    
    lead_name = st.text_input("Lead Name / Company", placeholder="e.g., Acme Corp - John Doe")
    
    budget_details = st.text_area(
        "Budget Details",
        height=80,
        placeholder="e.g., Annual marketing budget $120k, willing to spend up to $8k/month on tools."
    )
    
    business_need = st.text_area(
        "Business Need / Pain Points",
        height=100,
        placeholder="e.g., Struggling with low lead-to-opportunity conversion (only 12%). Need better qualification and personalization."
    )
    
    urgency = st.selectbox(
        "Urgency Level",
        ["Low", "Medium", "High"],
        index=1
    )
    
    if st.button("📊 Score Lead", type="primary", use_container_width=True):
        if not lead_name.strip() or not business_need.strip():
            st.warning("Lead name and business need are required.")
        else:
            with st.spinner("Analyzing lead quality..."):
                prompt = f"""
Analyze this sales lead and output **ONLY** valid JSON (no extra text):

Lead Name: {lead_name}
Budget: {budget_details}
Business Need: {business_need}
Urgency: {urgency}

Return JSON with exactly these keys:
{{
  "lead_score": integer between 0 and 100,
  "category": "Hot" (90+), "Warm" (75-89), "Lukewarm" (60-74), or "Cold" (<60),
  "explanation": detailed 3-4 sentence explanation of scoring,
  "conversion_probability": float 0-100,
  "next_action": specific recommended next step (1-2 sentences)
}}
"""
                result = call_groq(prompt, temperature=0.5, max_tokens=800)
                
                if result:
                    try:
                        # Clean and parse JSON
                        cleaned = result.strip()
                        if cleaned.startswith("```json"):
                            cleaned = cleaned.replace("```json", "").replace("```", "").strip()
                        data = json.loads(cleaned)
                        
                        score = int(data.get("lead_score", 50))
                        category = data.get("category", "Lukewarm")
                        prob = float(data.get("conversion_probability", 50))
                        
                        # Visual Score Display
                        col_score, col_prob = st.columns([2, 1])
                        
                        with col_score:
                            st.metric("Lead Score", f"{score}/100")
                            st.progress(score / 100.0)
                            
                            if score >= 90:
                                st.success(f"**Category: {category}** 🔥 Hot Lead")
                            elif score >= 75:
                                st.warning(f"**Category: {category}** 🌡️ Warm Lead")
                            elif score >= 60:
                                st.info(f"**Category: {category}** 🟡 Lukewarm Lead")
                            else:
                                st.error(f"**Category: {category}** ❄️ Cold Lead")
                        
                        with col_prob:
                            st.metric("Conversion Probability", f"{prob}%")
                        
                        st.markdown("### 📝 Scoring Explanation")
                        st.write(data.get("explanation", "No explanation provided."))
                        
                        st.markdown("### ✅ Recommended Next Action")
                        st.info(data.get("next_action", "Follow up via email."))
                        
                    except (json.JSONDecodeError, KeyError, ValueError) as e:
                        st.warning("Could not parse structured output. Showing raw response:")
                        st.markdown(result)
                        
                        # Fallback visual if score can be extracted
                        if "lead_score" in result.lower():
                            st.markdown("**Raw response shown above.**")

# Footer
st.sidebar.divider()
st.sidebar.caption("Built with ❤️ using Streamlit + Groq LLaMA 3.3 70B\nHackathon-ready • Local deployment")