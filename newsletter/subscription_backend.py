"""
Newsletter Subscription Backend API
Handles email collection and subscriber management
"""

import requests
from flask import Flask, request, jsonify
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from datetime import datetime
import json
import os
import sqlite3

# Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"
ADMIN_EMAIL = "admin@architecture-news.com"

# Database initialization
def init_database():
    conn = sqlite3.connect('subscribers.db')
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
    print("✅ Database initialized")

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
    conn = sqlite3.connect('subscribers.db')
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
def send_daily_newsletter():
    conn = sqlite3.connect('subscribers.db')
    cursor = conn.cursor()
    
    # Get active subscribers
    cursor.execute("SELECT email FROM subscribers WHERE status = 'active'")
    subscribers = cursor.fetchall()
    
    news_content = """
Architecture News Roundup - Daily Update
===================================

🏛️ TODAY'S TOP STORIES:
• AI in architectural design is revolutionizing building layouts
• Climate solutions show 37% reduction in energy consumption
• AI-generated designs show 40% energy efficiency improvements
• Smart cities using AI to optimize infrastructure

🌍 CLIMATE & SUSTAINABILITY:
• Green building materials market growing 23% annually
• AI-powered energy optimization systems now standard
• Solar glass integration increasing efficiency by 18%

✍️ EDITOR'S NOTE:
Artificial Intelligence continues to reshape architectural practice, 
bringing unprecedented efficiency while maintaining design excellence.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    for subscriber in subscribers:
        email = subscriber[0]
        
        # Send newsletter
        try:
            send_email(email, news_content, "Architecture News Daily")
            print(f"✅ Newsletter sent to {email}")
        except Exception as e:
            print(f"❌ Failed to send to {email}: {e}")
    
    return jsonify({
        'success': True,
        'sent_count': len(subscribers),
        'subscribers': subscribers
    })

# Send welcome email
def send_welcome_email(recipient):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient
    msg['Subject'] = "Welcome to Architecture News!"
    
    body = f"""
Congratulations on subscribing to Architecture News!

You will receive daily updates on:
• The latest architecture and design news
• Climate solutions and sustainable building
• AI in architecture and urban planning
• Green energy and smart city developments
• Building regulations and policy updates

Thank you for subscribing!

Best regards,
The Architecture News Team
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        s.starttls()
        s.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        s.sendmail(EMAIL_ADDRESS, [recipient], text)
        s.quit()
        print(f"✅ Welcome email to {recipient}")
    except Exception as e:
        print(f"❌ Failed to send welcome: {e}")

if __name__ == '__main__':
    init_database()
    print("✅ Newsletter system backend running on http://localhost:5000")
    print(f"   Subscribe: POST /api/subscribe")
    print(f"   Send Daily: POST /api/send-daily")