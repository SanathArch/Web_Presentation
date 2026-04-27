"""
Newsletter Subscription Form (Frontend Component)
HTML/React Form for Email Collection
"""

SUBSCRIBE_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Subscribe to Architecture News</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            background: #f5f5f5;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 { color: #2c3e50; }
        .form-group { margin: 20px 0; }
        input[type="email"] {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            background: #27ae60;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }
        .message {
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
            display: none;
        }
        .success { background: #d4edda; color: #155724; }
        .error { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📧 Subscribe to Architecture News</h1>
        <p>Get daily updates on the latest architecture news, climate solutions, AI design, and more!</p>
        
        <form id="subscribe-form" onsubmit="handleSubscribe(event)">
            <div class="form-group">
                <label for="email">Email Address:</label>
                <input 
                    type="email" 
                    id="email" 
                    name="email" 
                    placeholder="Your email address"
                    required
                >
            </div>
            
            <button type="submit">Subscribe Now</button>
        </form>
        
        <div id="message" class="message"></div>
    </div>
    
    <script>
        async function handleSubscribe(event) {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const messageDiv = document.getElementById('message');
            
            if (!email) {
                showMessage('Please enter a valid email address.', 'error');
                return;
            }
            
            // Send to backend API
            try {
                const formData = { email: email };
                const response = await fetch('/api/subscribe', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData)
                });
                
                const data = await response.json();
                
                if (data.success) {
                    showMessage(data.message, 'success');
                    document.getElementById('email').value = '';
                } else {
                    showMessage(data.message || 'Subscription failed', 'error');
                }
            } catch (error) {
                showMessage('Network error. Please try again.', 'error');
            }
        }
        
        function showMessage(text, type) {
            const messageDiv = document.getElementById('message');
            messageDiv.textContent = text;
            messageDiv.className = 'message ' + type;
            messageDiv.style.display = 'block';
            
            // Auto hide after 5 seconds
            setTimeout(() => {
                messageDiv.style.display = 'none';
            }, 5000);
        }
    </script>
</body>
</html>
"""

print("✅ Subscribe Form Component Created!")
print("File: H:/My Drive/Proffessional_Practice/Website/newsletter/subscribe_form.py")
print("\nPreview HTML content saved to file.")