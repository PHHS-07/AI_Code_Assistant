---

# 🤖 AI Code Assistant

A Streamlit-based chatbot powered by Google Gemini (Generative AI) to generate, optimize, and explain source code in multiple programming languages. Perfect for developers, learners, and AI enthusiasts!

---

## 📌 Features

- 💬 Chat-based code assistant
- 🧠 Powered by Gemini 1.5 Flash (Google Generative AI)
- 🌐 Supports: Python, Java, C, HTML, CSS, JavaScript
- ⚙️ Code optimization
- 🧾 Code comment explanation
- 🧼 Clear chat functionality

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-code-assistant.git
cd ai-code-assistant
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Set Up Gemini API

- Go to https://makersuite.google.com/app
- Get your API key and paste it inside `app.py`:

```python
genai.configure(api_key="YOUR_API_KEY")
```

> 🔐 For security, consider storing the key in an environment variable or `.env` file using `python-dotenv`.

---

## 📦 Requirements

These are listed in `requirements.txt`:

```txt
streamlit
google-generativeai
protobuf>=3.20.3
```

Optional:

```txt
python-dotenv  # If you want to manage API keys securely
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Start the assistant using:

```bash
streamlit run app.py
```

### ✅ Example Prompts

- `Generate a Python function to check for prime numbers`
- `Optimize this Java code:` (paste code)
- `Write HTML for a contact form`
- `Explain this code:` (paste code with comments)

---

## ⚖️ License

This project is licensed under the **Apache License 2.0**. See the LICENSE file for details.

---

## 👤 Author

Created by **Hari Hara Sudhan P**

- GitHub: https://github.com/PHHS-07
- Email: phariharasudhan2004@gmail.com

---

## ⚠️ Disclaimer

This AI Code Assistant is intended for **educational and development purposes only**. Generated or optimized code should be **reviewed manually** before use in production environments. The assistant uses large language models and may produce incomplete or inaccurate results at times.
