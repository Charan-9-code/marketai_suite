# MarketAI Suite

## AI-Powered Sales & Marketing Platform using Groq

A complete web application that helps marketing and sales teams generate AI-based campaigns, sales pitches, and perform intelligent lead qualification.

---

## 🎯 Features

### 1️⃣ AI Marketing Campaign Generator
- Input: Product description, target audience, marketing platform
- Output: Campaign objective, 5 content ideas, 3 ad copy variations, CTAs

### 2️⃣ AI Sales Pitch Generator
- Input: Product/solution, customer persona
- Output: 30-second elevator pitch, value proposition, differentiators, CTA

### 3️⃣ Lead Qualification & Scoring System
- Input: Lead name, budget, business need, urgency
- Output: Lead score (0-100), category (Hot/Warm/Cold), reasoning, conversion probability

---

## 🛠️ Tech Stack

- **Backend:** Python + Flask
- **AI Model:** Groq API (LLaMA 3.3 70B)
- **Frontend:** HTML5, CSS3, JavaScript
- **Styling:** Pure CSS with modern gradients
- **Environment:** Python dotenv

---

## 📂 Project Structure

```
MarketAI/
│
├── app.py                  # Flask backend with Groq API integration
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API key)
│
├── templates/
│   ├── index.html          # Dashboard/landing page
│   ├── campaign.html       # Marketing campaign generator
│   ├── pitch.html          # Sales pitch generator
│   └── lead_scoring.html   # Lead qualification system
│
└── static/
    ├── style.css           # Modern gradient UI styling
    └── script.js           # JavaScript utilities
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Groq API key (get from: https://console.groq.com/)

### Step 1: Install Dependencies

```bash
cd MarketAI
pip install -r requirements.txt
```

### Step 2: Configure API Key

1. Open the `.env` file
2. Replace `your_groq_api_key_here` with your actual Groq API key:

```
GROQ_API_KEY=gsk_your_actual_api_key_here
```

### Step 3: Run the Application

```bash
python app.py
```

The server will start at: **http://localhost:5000**

---

## 📖 How to Use

1. **Open your browser** and navigate to `http://localhost:5000`
2. **Choose a tool** from the navigation menu:
   - Campaign Generator
   - Sales Pitch Generator
   - Lead Scoring
3. **Fill in the form** with your inputs
4. **Click Generate** and wait for AI to process
5. **Copy or use** the generated results

---

## 🧪 Sample Test Inputs

### Marketing Campaign Generator
```
Product: AI chatbot for customer service automation
Audience: E-commerce business owners, 25-50 years old
Platform: LinkedIn
```

### Sales Pitch Generator
```
Product: Cloud-based CRM with AI lead scoring
Persona: Sales Director at mid-size B2B SaaS company
```

### Lead Scoring
```
Lead Name: TechStart Inc.
Budget: $10,000 - $50,000
Business Need: Automate customer onboarding process
Urgency: High (1 month)
```

---

## 🎨 UI Features

- **Modern Gradient Design** with glassmorphism effects
- **Responsive Layout** for all screen sizes
- **Smooth Animations** and transitions
- **Professional Color Scheme** with purple/blue gradients
- **Clean Navigation** between tools

---

## 🔐 Security Notes

- Never commit your `.env` file with actual API keys to version control
- Add `.env` to `.gitignore` if using Git
- Keep your Groq API key confidential

---

## 📝 Assignment Submission Notes

This project demonstrates:
- ✅ Full-stack web development (Backend + Frontend)
- ✅ AI/ML integration (Groq LLaMA 3.3 70B)
- ✅ RESTful API design
- ✅ Modern UI/UX best practices
- ✅ Clean, commented, readable code
- ✅ Professional project structure

**Developed by:** [Your Name]  
**Course:** [Your Course]  
**Submission Date:** [Date]

---

## 🐛 Troubleshooting

**Error: "Groq API key not found"**
- Make sure you've created the `.env` file
- Verify the API key is correct (starts with `gsk_`)

**Error: "Module not found"**
- Run `pip install -r requirements.txt` again
- Make sure you're in the correct directory

**Port already in use**
- Close other applications using port 5000
- Or modify `app.py` to use a different port

---

## 📞 Support

For questions or issues:
- Check the code comments in `app.py`
- Review the Groq API documentation
- Verify all dependencies are installed

---

**Built with ❤️ for college project submission | Powered by Groq AI**
