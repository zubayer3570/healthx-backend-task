# Project Overview

## Technologies Used
- **Server:** FastAPI  
- **Database:** MySQL  
- **ORM:** SQLAlchemy  

#### The project is built in PyCharm

## 🚀 Getting Started (Run Locally)

### 1. Environment Setup

Make sure your `.env` file includes the MySQL database connection string in the following format:

#### For example (.env):

DB_URL=mysql+mysqlconnector://root:12345678@localhost:3306/healthx


### 2. Run Development Server

You can start the development server using either of the following commands:

<pre><code>fastapi dev main.py</code></pre>

or

<pre><code>uvicorn main:app --reload</code></pre>

### 3. Test the app

Go to this URL in your browser

http://127.0.0.1:8000/docs

