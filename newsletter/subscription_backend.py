"""
Newsletter Subscription Backend API
Handles email collection and subscriber management
"""

import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from datetime import datetime
import json
import os
import sqlite3
import threading
import time
import schedule

# Import news generator
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from news_generator import news_generator

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"
ADMIN_EMAIL = "admin@architecture-news.com"

# Storage Configuration
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'newsletter_data')
DB_PATH = os.path.join(DATA_DIR, 'subscribers.db')
MOCK_EMAIL_LOG_PATH = os.path.join(DATA_DIR, 'sent_emails.log')

# Database initialization
def init_database():
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status TEXT DEFAULT 'active',
        last_opened TIMESTAMP
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS news_issues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        issue_date DATE NOT NULL,
        content TEXT,
        subject TEXT,
        status TEXT DEFAULT 'draft',
        sent_at TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database initialized at", DB_PATH)

def mock_send_email(recipient, content, subject):
    """Mocks sending an email by writing it to a log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] To: {recipient} | Subject: {subject}\n{content}\n{'-'*50}\n"
    with open(MOCK_EMAIL_LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    print(f"✅ Mock email saved for {recipient}")

# Subscribe API endpoint
@app.route('/api/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    email = data.get('email', '').strip().lower()
    
    if not email:
        return jsonify({'success': False, 'message': 'Email is required'}), 400
    
    if '@' not in email:
        return jsonify({'success': False, 'message': 'Invalid email format'}), 400
    
    # Check if already subscribed
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT email FROM subscribers WHERE email = ?', (email,))
        if cursor.fetchone():
            return jsonify({
                'success': False,
                'message': 'Email already subscribed'
            }), 409
        
        # Add subscriber
        cursor.execute(
            'INSERT INTO subscribers (email, subscribed_at) VALUES (?, ?)',
            (email, datetime.now().isoformat())
        )
        conn.commit()
        
        # Welcome email
        send_welcome_email(email)
        
        return jsonify({
            'success': True,
            'message': f"Welcome! Daily news will arrive at {email}.",
            'subscriber': email
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
    finally:
        conn.close()

# Daily newsletter sending
@app.route('/api/send-daily', methods=['POST'])
def send_daily_endpoint():
    return send_daily_newsletter()

def send_daily_newsletter():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get active subscribers
    cursor.execute("SELECT email FROM subscribers WHERE status = 'active'")
    subscribers = cursor.fetchall()
    
    # Generate tropical news content dynamically
    try:
        newsletter_data = news_generator.generate_newsletter()
        news_content = newsletter_data.get('summary', "News generation failed.")
    except Exception as e:
        print(f"❌ Failed to generate news: {e}")
        news_content = "Today's Tropical Architecture updates are currently unavailable. We'll be back tomorrow!"
    
    for subscriber in subscribers:
        email = subscriber[0]
        
        # Send newsletter
        try:
            mock_send_email(email, news_content, "Tropical Architecture Daily News")
            # For real email, you would replace mock_send_email with your actual send_email logic
            # send_email(email, news_content, "Tropical Architecture Daily News")
        except Exception as e:
            print(f"❌ Failed to send to {email}: {e}")
    
    conn.close()
    return jsonify({
        'success': True,
        'sent_count': len(subscribers),
        'subscribers': [s[0] for s in subscribers]
    })

# Send welcome email
def send_welcome_email(recipient):
    body = f"""
Congratulations on subscribing to Tropical Architecture News!

You will receive daily updates every morning at 6 AM on:
• The latest tropical architecture and design news
• Passive cooling and ventilation breakthroughs
• Vernacular materials and climate adaptation
• Flood-resilient and equatorial urbanism
• Green energy in tropical climates

Thank you for subscribing!

Best regards,
The Tropical Architecture Initiative Team
"""
    # Use mock email
    mock_send_email(recipient, body, "Welcome to Tropical Architecture News!")

def update_frontend_news():
    """Run the node scraper to update the frontend intelligence feed."""
    import subprocess
    print("🔄 Updating frontend intelligence feed...")
    try:
        # Run node news-scraper.js from the root directory
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        subprocess.run(['node', 'news-scraper.js'], cwd=root_dir, check=True)
        print("✅ Frontend intelligence feed updated successfully.")
    except Exception as e:
        print(f"❌ Failed to update frontend feed: {e}")

def run_scheduler():
    """Run background scheduler for daily emails and feed updates."""
    # Schedule the job every day at a specific time (e.g., 06:00)
    schedule.every().day.at("06:00").do(send_daily_newsletter)
    schedule.every().day.at("06:00").do(update_frontend_news)
    
    print("✅ Background scheduler started")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    init_database()
    
    # Start scheduler thread
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
    
    print("✅ Newsletter system backend running on http://localhost:5000")
    print(f"   Subscribe: POST /api/subscribe")
    print(f"   Send Daily: POST /api/send-daily")
    
    # Run Flask app
    app.run(host='0.0.0.0', port=5000)