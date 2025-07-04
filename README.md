# 🤖 AI Code Assistant

An interactive AI-powered coding assistant built using **Streamlit** and **Google Gemini API**.  
It helps you **generate**, **optimize**, and **explain code** in various programming languages.

---

## ✨ Features

- 🧠 **Code Generation** — Supports Python, Java, C, HTML, CSS, JavaScript
- 🛠️ **Code Optimization** — Improves your existing code automatically
- 📖 **Explanation** — Extracts and explains comments from code
- 💬 **Follow-up Questions** — Handles general queries with AI
- 🧼 **Clear Chat** — Reset conversation anytime

---

## 🖼️ Screenshot

![Screenshot](assets/screenshot.png)  
*(Add your own image at `assets/screenshot.png`)*

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/PHHS-07/ai-code-assistant.git
cd ai-code-assistant
'''
2. Install dependencies
'''bash
pip install -r requirements.txt
'''

3. Add your Gemini API key
Edit the line in main.py:

python
'''
genai.configure(api_key="YOUR_API_KEY")
'''
💡 For better security, consider using a .env file and os.environ.

🧪 Run the App

'''bash
streamlit run main.py
'''

📄 License

This project is licensed under the Apache License 2.0.
See the LICENSE file for full details.

🌐 Optional: Deploy on Streamlit Cloud

 1.Push this project to GitHub

 2.Go to streamlit.io/cloud

 3.Connect your GitHub repository

 4.Choose main.py as the entry point

 5.Add your Gemini API key as a secret environment variable

👨‍💻 Author
Developed by PHHS-07 – powered by Google Gemini & Streamlit.
