# AI Assistant

This is a personal project aimed at developing an AI assistant application with a web interface using Streamlit and OpenAI's GPT model. Currently, the project focuses on creating a simple chatbot similar to ChatGPT.

## Description

The AI Assistant uses the GPT model to generate responses to user inputs. The application interface is built using Streamlit.

## Setup

1. Install the required Python packages:

```bash
pip install langchain openai python-dotenv streamlit tiktoken
```

2. Set up your OpenAI API key in a `.env` file:

```bash
OPENAI_API_KEY=your-api-key
```

3. Run the Streamlit app:

```bash
streamlit run main.py
```

## Usage

The AI Assistant has a chat interface. You can send messages to the AI Assistant, and it will respond. You can also set a system role message that will be used to guide the AI's responses.

## Features

- Chat interface built with Streamlit
- AI responses generated with OpenAI's GPT-3 model
- System role message to guide AI responses
- Session state to keep track of the conversation
- Logging for debugging and development purposes

## To Do

- Implement error handling
- Improve UI
- Implement persistent storage for conversations
