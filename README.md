# IT Sales Customer Care Chatbot Demo

This is a small AWS-based demo chatbot for IT sales and customer care.

It uses:

- React frontend
- FastAPI backend
- Amazon Bedrock for AI response generation
- SQLite for simple lead storage
- Docker Compose for local demo

---

## Features

- IT services FAQ answering
- Sales recommendation
- Lead qualification conversation
- Simple lead database
- AWS Bedrock integration
- Demo-ready web UI

---

## Architecture

```text
Browser
  |
  v
React Chat UI
  |
  v
FastAPI Backend
  |
  +--> Amazon Bedrock
  |
  +--> Built-in IT Services Knowledge Base
  |
  +--> SQLite Leads DB
