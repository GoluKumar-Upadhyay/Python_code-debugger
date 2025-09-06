# 🐍 Gemini-Powered Python Debugging Assistant

![Flask](https://img.shields.io/badge/Flask-2.3.2-green?logo=flask) 
![LangChain](https://img.shields.io/badge/LangChain-🔥-blue?logo=chainlink) 
![Google Gemini](https://img.shields.io/badge/Gemini-2.5--flash-ff69b4?logo=google) 
![Python](https://img.shields.io/badge/Python-3.10+-yellow?logo=python)
![License](https://img.shields.io/badge/License-MIT-purple)

---

## 📌 Overview
This project is an **AI-powered debugging assistant** built with **Flask**, **LangChain**, and **Google Gemini**.  
It helps students debug Python code by giving **structured hints, analysis, and debugging steps** — **without revealing the direct solution**.  

👉 Perfect for **learning by doing** rather than just copy-pasting fixes.  

---

## ✨ Features
- 🐞 **Buggy Code Analysis** – Paste your Python code and get structured feedback.  
- 🎯 **Student Level Adaptation** – Explanations adjust based on `beginner`, `intermediate`, or `advanced`.  
- 📑 **Formatted Markdown Output** – Clear sections: Summary, Root Causes, Hints, Debugging Steps, Questions.  
- ⚡ **Gemini LLM Integration** – Uses **Google Gemini 2.5 Flash** via `google-genai`.  
- 🌐 **Web Interface** – Simple Flask frontend with HTML/CSS for input and results.  
- 🧠 **LangChain PromptTemplate** – Ensures consistent, structured responses.  

---

## 🛠️ Tech Stack
- **Backend:** [Flask](https://flask.palletsprojects.com/)  
- **AI Model:** [Google Gemini](https://ai.google.dev/) (`google-genai`)  
- **Prompt Management:** [LangChain](https://www.langchain.com/)  
- **Environment Management:** [python-dotenv](https://pypi.org/project/python-dotenv/)  
- **Frontend:** HTML5 + CSS3 (responsive with simple styling)  

---

## Proejct working image
![Screenshot_7-9-2025_15716_127 0 0 1](https://github.com/user-attachments/assets/886c5f2e-a054-4472-893d-bf41027d9083)

# 🐍 Python Debugger Web App

This project is a **Flask-based Python Debugger** that allows users to paste buggy Python code, select their experience level, and receive **personalized debugging suggestions** powered by the **Gemini API**.

---

## 📌 Features

- ✍️ **Code Input Box** – Paste your buggy Python code.  
- 🎚️ **Skill Level Selection** – Choose:
  - Beginner → Detailed step-by-step explanations.  
  - Intermediate → Balanced hints + best practices.  
  - Advanced → Concise debugging + optimization tips.  
- ⚡ **Gemini API Integration** – Analyzes the code and returns smart debugging feedback.  
- 🎨 **Dark-Themed UI** – Developer-friendly interface with clear sections.  

---

## 🖼️ Frontend: `index.html`

The `index.html` file acts as the **main input page** for the debugger.

### 🔹 Structure Overview

1. **Header Section**
   - Title: *Python Code Debugger*
   - Subtitle: Explains purpose (*static analysis + debugging suggestions*).

2. **Code Input Area**
   - Large text editor for pasting buggy Python code.
   - Preloaded example (e.g., Fibonacci function) for guidance.

3. **Skill Level Selection**
   - Options: **Beginner | Intermediate | Advanced**.
   - Ensures feedback is tailored to the user’s coding level.

4. **Action Button**
   - **“Analyze & Debug Code”** (green button).
   - On click → sends code + level choice to the Flask backend.

---

## ⚙️ Backend Flow

1. User enters buggy code + selects level → `index.html` form submission.  
2. Flask (`app.py`) captures inputs.  
3. Code + level are sent to **Gemini API**.  
4. API response (debugging hints) is displayed in `result.html`.  

---

## 📂 File Roles

- `index.html` → Input page (buggy code + skill level).  
- `result.html` → Output page (Gemini API debugging feedback).  
- `app.py` → Flask backend (handles requests + API calls).  

---


![Screenshot_7-9-2025_2020_127 0 0 1](https://github.com/user-attachments/assets/0368cc6d-5abc-466f-9491-8cd7d1534c53)

- `result.html` → Display Gemini’s debugging feedback.

## working video
https://github.com/user-attachments/assets/1413ca1d-5579-4730-87c4-6984f7e36ca0
------



## 📂Project Str

https://github.com/user-attachments/assets/4404c45f-6caa-4208-ad34-58234629a330
---

<img width="1053" height="311" alt="image" src="https://github.com/user-attachments/assets/148e6312-ffd3-4d1b-b561-171a652f27a0" />

----

## ⚙️ Setup & Installation

### 1. Clone Repo
```bash
git clone https://github.com/your-username/gemini-debug-assistant.git
cd gemini-debug-assistant



