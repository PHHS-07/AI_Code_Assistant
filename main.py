import streamlit as st
import google.generativeai as genai
import re

st.set_page_config(page_title="AI Code Assistant", page_icon=r"C:\Users\phari\OneDrive\Desktop\devil\hari\bot-assistant (1).png")
# Initialize the Generative AI Client (replace with your own API key)
genai.configure(api_key="AIzaSyA0OhbD6o2GEoaIlwQnKv9SJKEk7C1phfs")
model = genai.GenerativeModel("gemini-1.5-flash")

# Helper function to handle chatbot responses
def get_assistant_response(prompt, language="Python"):
    if prompt.lower().startswith("optimize"):
        return optimize_code(prompt, language)
    elif any(word in prompt.lower() for word in ["code", "generate", "write"]):
        return generate_code(prompt, language)
    else:
        return handle_follow_up(prompt)

# Generate code
def generate_code(prompt, language="Python"):
    if language not in ["Python", "Java", "C", "HTML", "CSS", "Javascript"]:
        return "Language not supported."
    
    language_prompt = f"Write a {language.lower()} code for: {prompt}"
    response = model.generate_content(language_prompt)
    return response.text if response else "Unable to generate code at the moment."

# Follow-up query handler
def handle_follow_up(query):
    response = model.generate_content(query)
    return response.text if response else "Unable to provide a response."

# Optimize code
def optimize_code(code, language="Python"):
    optimize_prompt = f"Optimize this {language} code:\n{code}"
    response = model.generate_content(optimize_prompt)
    return response.text if response else "Optimization failed."

# Function to extract comments as explanation
def extract_comments_as_explanation(code):
    # Regular expression to match Python-style comments (# comment)
    comments = re.findall(r"#(.*)", code)
    explanation = "\n".join([comment.strip() for comment in comments])
    return explanation

# Streamlit UI
st.title("AI Code Assistant")
st.write("Chat with your code assistant for code generation, optimization, and explanations.")

# Initialize conversation history in session state
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Display conversation history
for entry in st.session_state.conversation:
    if entry["role"] == "user":
        st.write(f"**You:** {entry['content']}")
    elif entry["type"] == "code":
        # Show the code first
        st.code(entry['content'], language=entry.get("language", "python"))
        # Show the explanation (comments) below the code
        st.write(f"**Assistant Explanation:** {entry['explanation']}")
    else:
        st.write(f"**Assistant:** {entry['content']}")

# Input area for conversation
user_input = st.text_area("Ask the assistant anything:", key="user_input")
language = st.selectbox("Programming language:", ["Python", "Java", "C", "HTML", "CSS", "Javascript"])

if st.button("Send") and user_input:
    # Append user question to conversation
    st.session_state.conversation.append({"role": "user", "content": user_input})
    
    # Generate assistant response
    with st.spinner("Thinking..."):
        assistant_response = get_assistant_response(user_input, language)
    
    # Check if the response contains both code and explanation
    if "```" in assistant_response:
        # Attempt to split code from explanation
        parts = assistant_response.split("```")
        
        if len(parts) > 1:
            explanation = parts[0].strip()  # Explanation before code block
            code_block = parts[1].strip()  # Code after first ``` mark
            
            # Extract comments from the code block as explanation
            code_explanation = extract_comments_as_explanation(code_block)
            
            # Update conversation history with code and explanation separately
            st.session_state.conversation.append({
                "role": "assistant",
                "content": code_block,
                "explanation": code_explanation,
                "type": "code",
                "language": language.lower()
            })
            
            # Display the code in the code box
            st.code(code_block, language=language.lower())
            
            # Display the explanation (comments)
            code_explanation = st.write(f"**Assistant Explanation:**\n{code_explanation}")

        else:
            # If no valid code block found, treat the response as plain text
            st.session_state.conversation.append({"role": "assistant", "content": assistant_response, "type": "text"})
            st.write(f"**Assistant:** {assistant_response}")
    else:
        # Handle cases where no code block is detected
        st.session_state.conversation.append({"role": "assistant", "content": assistant_response, "type": "text"})
        st.write(f"**Assistant:** {assistant_response}")

# Clear chat functionality
if st.button("Clear Chat"):
    st.session_state.conversation = []
