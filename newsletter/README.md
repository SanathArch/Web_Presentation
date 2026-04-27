# 📧 Green Arch Network Newsletter System

## Overview

This professional newsletter system is designed for architecture, engineering, and design professionals. It automatically generates email content based on your JSON configuration file, with templated HTML for consistent branding.

---

## 📁 File Structure

```
newsletter/
├── README.md                    # This file - Instructions
├── newsletter_config.json       # Your customized settings
├── newsletter_template.html     # Email HTML template
├── generate_email.py           # Python script for email generation
├── email_logs/                 # Email processing logs
│   └── .gitkeep
└── drafts/                     # Saved draft emails
    └── .gitkeep
```

---

## ⚙️ Configuration File (`newsletter_config.json`)

### Required Fields

| Field | Description | Example |
|-------|-------------|---------|
| `newsletter_name` | Email subject/name | "The Daily Architect" |
| `publisher` | Your company name | "Green Arch Network" |
| `website` | Your website URL | "https://yourcompany.com" |
| `contact.email` | Support email | "newsletter@yourcompany.com" |
| `contact.phone` | Support phone | "+1-555-BUILD" |
| `contact.address` | Physical address | "123 Arch St, NY" |
| `subscription_url` | Subscribe link | "https://yourcompany.com/newsletter-signup" |
| `social_media` | Social arrays | ["Linkedin", "Twitter", "Facebook"] |

### Optional Fields

| Field | Description | Example | Default |
|-------|-------------|---------|---------|
| `social_media_icons` | Icon URLs | ["https://cdn..."] | [] |
| `custom_css` | Additional CSS | "{}" | "{}" |

---

## 📝 Email Template Structure

The template supports these variables (use `{{key}}` syntax):

### Content Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{newsletter_name}}` | Email subject | "Architecture Weekly" |
| `{{publisher}}` | Company name | "Green Arch Network" |
| `{{summary}}` | Issue summary line | "Innovation, AI, & Design" |
| `{{content_body}}` | Main content (from config) | "Latest articles..." |
| `{{editor_note}}` | Editor's note | "Important: Read policy!" |

### Contact Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{contact.email}}` | Support email | "contact@company.com" |
| `{{contact.website}}` | Website URL | "https://company.com" |
| `{{contact.phone}}` | Phone number | "+1-555-1234" |
| `{{contact.address}}` | Mailing address | "123 Street, City" |

### Social Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{social_media}}` | Social platform list | ["LinkedIn"] |
| `{{social_links}}` | Social profile URLs | ["https://linkedin.com/company"] |
| `{{social_handles}}` | Social handles | ["@greenarch"] |

### Dynamic Date Variables

| Variable | Description |
|----------|-------------|
| `{{current_year}}` | Current year (e.g., "2025") |
| `{{current_month}}` | Month number (e.g., "12") |
| `{{current_day}}` | Day of month (e.g., "23") |
| `{{date_format}}` | Formatted date |
| `{{month_name}}` | Full month name |
| `{{month_abbr}}` | Abbreviated month name |

---

## 🛠️ How to Use

### Step 1: Configure Settings

Edit `newsletter_config.json` with your settings:

```json
{
    "newsletter_name": "Architecture Weekly",
    "publisher": "Green Arch Network", 
    "website": "https://greenarchnetwork.com",
    "contact.email": "newsletter@greenarchnetwork.com",
    "contact.phone": "+1-555-BUILD",
    "contact.address": "123 Architecture Blvd, NY, USA",
    "subscription_url": "https://greenarchnetwork.com/newsletter-signup",
    "social_media": ["LinkedIn", "Twitter", "Facebook"],
    "social_links": [
        "https://linkedin.com/company/greenarch",
        "https://twitter.com/greenarchnet",
        "https://facebook.com/greenarchnetwork"
    ],
    "social_handles": ["@greenarchnet", "@ga_network", "greenarch"]
}
```

### Step 2: Populate Content

Create the content in `newsletter_config.json`:

```json
{
    "content": {
        "intro": "Welcome to the latest edition!",
        "articles": [
            {
                "title": "AI in Architecture",
                "summary": "How AI is transforming design...",
                "link": "https://greenarchnetwork.com/ai-architecture",
                "image": "https://images.unsplash.com/ai-design.jpg"
            },
            {
                "title": "Sustainable Design",
                "summary": "Green building practices...",
                "link": "https://greenarchnetwork.com/sustainability",
                "image": "https://images.unsplash.com/green-building.jpg"
            }
        ],
        "editor_note": "Important: Please read our editorial policy before sharing."
    }
}
```

### Step 3: Generate Email

Run the Python script:

```bash
python generate_email.py
```

This will:
- Parse configuration
- Load template
- Populate content
- Generate HTML
- Save to `email_logs/latest_email.html`

---

## 🔧 Python Script (`generate_email.py`)

### What It Does

1. Reads `newsletter_config.json`
2. Loads `newsletter_template.html`
3. Replaces all `{{variable}}` placeholders
4. Formats date variables
5. Generates final email HTML
6. Saves to output folder

### Output: `email_logs/latest_email.html`

---

## 🎨 Custom CSS

Add custom styling in `newsletter_config.json`:

```json
{
    "custom_css": {
        "styles": [
            "body { background: #f5f5f5; }",
            ".header { padding: 40px 20px; }"
        ]
    }
}
```

---

## ✅ Best Practices

### Template Design

- Keep emails under 150KB (Gmail limit)
- Use table-based layout (email client compatibility)
- Include alt text for images
- Test on multiple email clients

### Content Guidelines

- Keep subject under 50 characters
- Use engaging intro
- Include unsubscribe link (required)
- Mobile-responsive design
- Avoid spam triggers

---

## 🧪 Testing

### Manual Testing Checklist

- [ ] Open in Gmail
- [ ] Open Outlook
- [ ] Test on mobile
- [ ] Check image loading
- [ ] Verify all links work
- [ ] Check unsubscribe link

### Automated Testing

Use email testing tools like:
- Email on Acid
- Litmus
- Mailtrap (sandbox testing)

---

## 📧 Sending Options

### Built-in Tools (Python)

```python
# Send via SMTP
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('your_email@gmail.com', 'password_or_app_code')
```

### Third-Party Services

- **Mailchimp**: Integration via API
- **Constant Contact**: Drag-and-drop editor
- **SendGrid**: Developer-friendly
- **HubSpot**: CRM integration

### Manual Sending

1. Save generated email to file
2. Drag onto email client (Gmail, Outlook)
3. Send to subscriber list

---

## 🐛 Troubleshooting

### Issue: Button Not Working

**Solution**: Update `social_links` and `subscription_url` in config.

```json
{
    "subscription_url": "https://yourdomain.com/newsletter-signup",
    "social_links": ["https://linkedin.com/company/yourcompany"]
}
```

### Issue: Email Too Large

**Solution**: Compress images, use links instead

```python
# Image compression
from PIL import Image

img = Image.open('large.jpg')
img.thumbnail((400, 200))  # Width x Height
img.save('small.jpg')
```

### Issue: Images Not Loading

**Solution**: Use HTTPS URLs or inline data URIs

```html
<image src="https://example.com/logo.png" />
```

---

## 📚 Additional Resources

### Templates

- [MJML Templates](https://mjml.io/) - Email template framework
- [Litmus Templates](https://litmus.com/templates) - Industry templates
- [HubSpot Email Templates](https://hubspot.com/email-templates)

### Email Marketing Tools

- Mailchimp
- Constant Contact
- SendGrid
- Brevo (formerly Sendinblue)
- HubSpot Email

### Best Practices

- [Email Marketing Best Practices](https://www.campaignmonitor.com/guides/best-practices-for-creating-newsletters/)
- [Email Standards Group](http://www.emailstandards.com/)

---

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-01-01 | Initial release |
| 1.0.1 | 2025-01-15 | Fixed email generation bug |
| 1.1.0 | 2025-02-01 | Added custom CSS support |
| 1.2.0 | 2025-03-15 | Added social media links |

---

## 📞 Support

- **Email**: support@greenarchnetwork.com
- **Website**: https://greenarchnetwork.com
- **Documentation**: https://docs.greenarchnetwork.com/newsletter

---

## 🔒 Disclaimer

This newsletter system is for educational and business purposes. Always comply with:

- **CAN-SPAM Act** (US)
- **GDPR** (EU)
- **CASL** (Canada)

Ensure you have proper consent and include unsubscribe options.

---

**Made with ❤️ by Green Arch Network**

Last updated: 2025-03-15