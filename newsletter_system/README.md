# Newsletter Management System

A comprehensive Python-based newsletter subscriber management system with multi-storage backend support.

## Features

- ✉️ Email subscriber validation
- 📂 Multi-storage configuration backend support (SQLite, PostgreSQL, InMemory)
- 🎁 Welcome messages
- 📊 Status tracking (active, unsubscribed, bounced)
- 🔄 Real-time status updates
- 🗂️ File-based backup support
- 🔍 Email verification (format, DNS, MX records)
- 📝 Comprehensive logging and reporting

## Quick Start

```bash
# Make executable
chmod +x main.py

# Run the system
./main.py
```

## Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# venv\Scripts\activate  # On Windows

# Install requirements
pip install -r requirements.txt

# Run system
python main.py
```

## Usage

```bash
# List all subscribers
./main.py --list

# Add a new subscriber
./main.py subscribe user@example.com

# Check subscriber status
./main.py status user@example.com

# Unsubscribe a subscriber
./main.py unsubscribe user@example.com

# Send a newsletter
./main.py send newsletter.txt --subject "Monthly Update"

# Backup subscribers
./main.py backup backup_subscribers

# Show all available commands
./main.py --help
```

## Configuration

Create a `config.json` file:

```json
{
  "default_storage": "memory",
  "storage": {
    "memory": {},
    "sqlite": {
      "database": "newsletter.db"
    },
    "postgresql": {
      "host": "localhost",
      "port": 5432,
      "database": "newsletter",
      "user": "postgres",
      "password": "postgres"
    }
  },
  "email_validation": {
    "max_mx_records": 5,
    "timeout_seconds": 30
  }
}
```

## Backend Storage Backends

### Memory (default)
- Fastest performance
- No persistent storage
- Use for testing

### SQLite
- Simple file-based storage
- No server required
- Good for small-medium systems

### PostgreSQL
- Production-grade persistence
- ACID compliance
- High performance

## Project Structure

```
newsletter_system/
├── main.py              # Entry point
├── verify.py            # Email verification logic
├── subscriber.py        # Subscriber management (not created)
├── config.json          # Configuration
├── requirements.txt     # Python dependencies
├── backup_subscribers/  # Backup directory
└── subscribers/         # Storage directory

subscribers/
  └── user@example.com/
      ├── config.json    # Subscriber settings
      ├── welcome.txt    # Welcome message
      └── status.log     # Status updates
```

## Available Commands

- `--help`             Show help message
- `--list`             List all subscribers
- `--subscribe`        Add new subscriber
- `--unsubscribe`      Remove subscriber
- `--status`           Check subscriber status
- `--send`             Send newsletter
- `--backup`           Create backup
- `--restore`          Restore from backup

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

MIT License

## Support

For issues and feature requests, please open an issue on GitHub.

---

**Built with ❤️ for newsletter management**
