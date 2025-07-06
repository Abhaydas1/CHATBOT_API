🤖 Streamlit Chatbot using OpenRouter & Gemini
Welcome to your friendly AI chatbot powered by OpenRouter and Google's gemini-2.5-flash-preview-05-20 model! This lightweight, interactive chatbot runs on Streamlit and features a simple yet elegant UI for engaging conversations with a powerful large language model.


🔧 Features
Chat with a cutting-edge LLM via OpenRouter

Beautifully styled user and assistant message bubbles

Adjustable creativity (temperature) control via sidebar

Real-time typing indicator with loading spinner

Reset chat history with a single click

Runs locally or can be deployed to the web

🚀 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone (https://github.com/Abhaydas1/Chat_bot)
cd streamlit-chatbot
2. Install Dependencies
Make sure you have Python 3.8+ and Streamlit installed. You can install required packages with:

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing, simply install:

bash
Copy
Edit
pip install streamlit requests
3. Set Up API Key
Create a .env file or securely set your OpenRouter API key as an environment variable:

bash
Copy
Edit
export API_KEY='your_openrouter_api_key_here'
Or use the .streamlit/secrets.toml for Streamlit Cloud:

toml
Copy
Edit
[general]
API_KEY = "your_openrouter_api_key_here"
4. Run the App
bash
Copy
Edit
streamlit run app.py
🛠️ Configuration
Inside the app, you can control:

Temperature: Set from 0.0 (deterministic) to 1.0 (creative)

Clear Chat: Resets the session chat history

🧠 Model Info
Model: google/gemini-2.5-flash-preview-05-20

Provider: OpenRouter.ai

Max Tokens: 1024 (can be adjusted)

📁 Project Structure
bash
Copy
Edit
├── app.py              # Main Streamlit chatbot script
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .streamlit/
    └── secrets.toml    # API keys (optional for cloud)
📸 Screenshot
Customize this section with a real screenshot after deployment

🙌 Acknowledgements
Streamlit

OpenRouter API

Google Gemini Models
