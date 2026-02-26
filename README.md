# 🤖 AI Data Analyst - Multi-Agent System  
### Built by Akash R

An intelligent multi-agent AI system that analyzes CSV datasets, generates business insights, validates reasoning, and produces structured reports automatically.

---

## 🚀 Features

- Upload any CSV file
- Automatic statistical analysis (mean, median, min, max, mode, unique count)
- Multi-agent reasoning using LangGraph
- Business-level report generation
- Logical validation via Monitor agent
- Chart visualization using Chart.js
- Export report as text file

---

## 🏗️ Architecture

This system uses a 5-Agent workflow powered by LangGraph:

Planner → Understanding → Analyst → Monitor → Reporter

### Agent Responsibilities

1. Planner Agent  
   Decides what type of analysis should be performed.

2. Understanding Agent  
   Explains dataset in simple language.

3. Analyst Team Agent  
   Uses real computed analytics to explain trends.

4. Monitor Agent  
   Reviews analysis and checks for logical issues.

5. Reporter Agent  
   Generates final structured business report.

---

## 📊 Analytics Engine

Numeric Columns:
- Mean
- Median
- Minimum
- Maximum

Categorical Columns:
- Mode
- Unique value count

Analytics are computed using Pandas and passed to LLM agents to ensure grounded reasoning.

---

## 🛠️ Tech Stack

Backend:
- FastAPI
- Uvicorn
- Pandas
- LangGraph
- OpenAI SDK
- OpenRouter API

Frontend:
- HTML
- Chart.js

---

## 📂 Project Structure

project/
│
├── backend/
│   ├── api.py
│   ├── engine.py
│
├── frontend/
│   ├── index.html
│
├── requirements.txt

---

## ⚙️ Installation

1️⃣ Clone Repository

git clone <repo-url>  
cd project  

2️⃣ Install Dependencies

pip install -r requirements.txt  

3️⃣ Create .env File

OPENROUTER_API_KEY=your_key_here  

---

## ▶️ Run the Application

uvicorn main:api --reload  

Open in browser:

http://localhost:8000  

---

## 🧠 LLM Model Used

meta-llama/llama-3.3-70b-instruct:free  
Accessed via OpenRouter API

---

## 📈 Example Workflow

1. Upload CSV  
2. Backend computes analytics  
3. Agents collaborate  
4. Monitor validates reasoning  
5. Business report generated  
6. Mean values visualized in chart  

---

## 🔐 Stability Features

- Safe CSV encoding fallback (utf-8, latin1, ISO-8859-1)
- Skips corrupted lines
- Empty-response fallback handling
- Typed agent state management
- Structured multi-agent pipeline

---

## 🎯 What This Project Demonstrates

- Multi-agent orchestration
- LLM + backend integration
- Real-data grounded AI
- Structured AI pipelines
- Production-style FastAPI setup
- Business-ready AI reporting system

---

## 🔮 Future Improvements

- Advanced visualizations
- PDF export
- Authentication system
- Cloud deployment (AWS/GCP)
- Persistent memory
- SQL database integration
- Domain-specific agent specialization
- Model switching support

---

## 👨‍💻 Author

Akash R  
B.Tech - Artificial Intelligence & Data Science  
India

Focused on building real-world AI systems.
