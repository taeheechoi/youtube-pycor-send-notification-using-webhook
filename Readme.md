# Epicor Automation using Python - Sending a notification to chat platform using webhook. 

<!-- ABOUT THE PROJECT -->

## About The Project

This project is for the Youtube channel Pycor where developers can learn how to integrate with Epicor ERP software in Python. 

The intention of this project is to help developers to send a notification to chat platform such as Teams, Slack and Hangout using webhook.

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Python 3.10
- Python Packages: requests (2.28.1), Python-dotenv (0.20.0)
- VS Code

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/taeheechoi/youtube-pycor-send-notification-using-webhook.git .
   ```
2. Create a virtual environment and activate it
   ```sh
   python -m venv venv
   venv\scripts\activate
   ```
3. Install packages
   ```sh
   pip install -r requirements.txt
4. Rename .env-example to .env and configure it
   ```
   WEBHOOK_URL=your webhook url
   ```
5. Create log folder for logging results

6. Update run.bat with a correct project folder
   ```sh
   C:\project-folder\venv\Scripts\python.exe main.py
   ```

