﻿# Project Overview

## Technologies Used
- **Server:** FastAPI  
- **Database:** MySQL  
- **ORM:** SQLAlchemy  

#### The project is developed in PyCharm IDE

## 🚀 Getting Started (Run Locally)

#### First clone this repo, then enter into the project directory.

### First Clone the project
Run this command in your terminal
*<pre><code>git clone https://github.com/zubayer3570/healthx-backend-task.git</code></pre>

Then open the project directory. Then do the following.

### 1. Environment Setup

Run the command in the project terminal to create virtual environment
<pre><code>python -m venv .venv</code></pre>

Run the command to install all the dependencies
<pre><code>pip install -r requirements.txt</code></pre>

Create a .env file and add the MySQL database connection string in the following format,

DB_URL=mysql+mysqlconnector://&lt;username&gt;:&lt;password&gt;@localhost:3306/healthx

### 2. Run Development Server

You can start the development server using either of the following commands:

<pre><code>fastapi dev main.py</code></pre>

or

<pre><code>uvicorn main:app --reload</code></pre>

### 3. Test the app

Go to this URL in your browser to test the APIs

<pre><code>http://127.0.0.1:8000/docs</code></pre>
