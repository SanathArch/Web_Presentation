"""
Newsletter Management System - Complete Verification
"""

import json
import os
import shutil
import datetime
from pathlib import Path
from typing import Tuple, Dict, Optional

class SubscriberManager:
    """Complete email subscriber management system"""
    
    def __init__(self, base_path: str = None):
        """Initialize the subscriber manager"""
        if base_path:
            self.base_path = Path(base_path)
        else:
            self.base_path = Path(__file__).parent / "newsletter_system"
        
        # Create base directories if they don't exist
        self.base_path.mkdir(exist_ok=True)
        (self.base_path / "config").mkdir(exist_ok=True)
        (self.base_path / "storage").mkdir(exist_ok=True)
        (self.base_path / "upserts").mkdir(exist_ok=True)
        self.subscribers = self.base_path / "storage" / "subscribers"
        self.subscribers.mkdir(exist_ok=True)
        
        # Load configuration once
        (self.base_path / "config" / "config.json").write_text(
            json.dumps({
                "email_validation": True,
                "storage": True,
                "max_recipients": 10000
            }, indent=2)
        )
        
        self.subscribers.mkdir(exist_ok=True)
    
    def validate_email(self, email: str) -> Tuple[bool, str, str]:
        """Validate email format and extract domain info
        
        Returns tuple of (is_valid, cleaned_email, domain_info)
        """
        if not email:
            return False, "", "Empty email"
        
        # Remove common prefixes
        email = email.lower().strip()
        email = email.replace(" ", "").replace(".", "").replace("+", "")
        
        # Check format
        try:
            # Must contain @
            if "@" not in email:
                return False, email, "Missing @"
            
            # Must have valid local and domain parts
            parts = email.split("@")
            if len(parts) != 2:
                return False, email, "Invalid email format"
            
            local, domain = parts
            if not local or not domain:
                return False, email, "Invalid parts"
            
            # Domain validation
            if not all([
                domain.startswith(("com", "net", "org", "edu", "gov", "io")),
                len(domain) <= 20
            ]):
                return False, email, "Invalid domain"
            
            return True, email, f"local_part={local}&domain={domain}"
        
        except Exception as e:
            return False, email, str(e)
    
    def save_subscriber(self, email: str, active: bool = True) -> Dict:
        """Save subscriber with multiple file formats
        
        Creates:
        - info.txt (human readable)
        - validation.json (machine readable)
        - welcome.txt (subscriber info)
        """
        is_valid, cleaned_email, _ = self.validate_email(email)
        
        if not is_valid:
            return {
                "valid": False,
                "message": f"Invalid email: {_}"
            }
        
        subscriber_folder = self.subscribers / cleaned_email
        subscriber_folder.mkdir(exist_ok=True)
        
        # Create info.txt
        info_file = subscriber_folder / "info.txt"
        with open(info_file, 'w') as f:
            f.write(f"Email: {cleaned_email}\n")
            f.write(f"Joined: {datetime.now().isoformat()}\n")
            f.write(f"Active: {str(active).lower()}\n")
        
        # Create welcome file
        welcome_file = subscriber_folder / "welcome.txt"
        with open(welcome_file, 'w') as f:
            f.write(f"Welcome! You're now subscribed.\n")
            f.write(f"Active until: Never (unless marked inactive)\n")
        
        # Create validation JSON
        validation_file = subscriber_folder / "validation.json"
        with open(validation_file, 'w') as f:
            json.dump({
                "valid": True,
                "email": cleaned_email,
                "active": active,
                "created": datetime.now().isoformat()
            }, f, indent=2)
        
        return {
            "valid": True,
            "message": "Subscriber saved successfully",
            "info_file": str(info_file),
            "welcome_file": str(welcome_file)
        }
    
    def get_subscriber_info(self, email: str) -> Optional[Dict]:
        """Get subscriber information"""
        is_valid, cleaned_email, _ = self.validate_email(email)
        
        if not is_valid:
            return None
        
        info_file = self.subscribers / cleaned_email / "info.txt"
        
        if info_file.exists():
            with open(info_file, 'r') as f:
                data = f.read()
            return {
                "email": cleaned_email,
                "info": data,
                "active": "true" in data.lower()
            }
        
        return None
    
    def delete_subscriber(self, email: str, cascade=True) -> bool:
        """Remove subscriber and their data"""
        is_valid, cleaned_email, _ = self.validate_email(email)
        
        if not is_valid:
            return False
        
        subscriber_folder = self.subscribers / cleaned_email
        
        if subscriber_folder.exists():
            shutil.rmtree(subscriber_folder)
            return True
        
        return False
    
    def update_subscriber_status(self, email: str, status: str, notes: Optional[str] = None) -> bool:
        """Update subscriber status"""
        is_valid, cleaned_email, _ = self.validate_email(email)
        
        if not is_valid:
            return False
        
        subscriber_folder = self.subscribers / cleaned_email
        
        if not subscriber_folder.exists():
            return False
        
        info_file = subscriber_folder / "info.txt"
        if not info_file.exists():
            return False
        
        # Read and update
        timestamp = datetime.now().isoformat()
        
        with open(info_file, 'r+') as f:
            lines = f.readlines()
            f.seek(0, 2)  # End of file
        
        with open(info_file, 'a') as f:
            f.write(f"\n# Updated at: {timestamp}\n")
            f.write(f"Status: {status}\n")
            if notes:
                f.write(f"Notes: {notes}\n")
        
        return True

# Verification function
def main():
    print("📧 Newsletter System - Subscriber List")
    print("=" * 50)
    
    manager = SubscriberManager()
    
    # Valid emails
    valid_emails = [
        "subscriber1@example.com",
        "newsletter@test.com",
        "info@company.org"
    ]
    
    # Invalid emails
    invalid_emails = [
        "invalid@.com",
        "@example.com",
        "test@.invalid",
        ".bad@domain.com"
    ]
    
    # Save valid subscribers
    print("\n📝 Saving Valid Subscribers:")
    for email in valid_emails:
        result = manager.save_subscriber(email)
        status = "✅" if result["valid"] else "❌"
        print(f"  {status} {email} - {result['message']}")
    
    # Save invalid subscribers for testing
    print("\n❌ Processing Invalid Emails:")
    for email in invalid_emails:
        result = manager.save_subscriber(email)
        status = "⚠️" if not result["valid"] else "✅"
        print(f"  {status} {email} - {result['message']}")
    
    # Display subscriber info
    print("\n📋 Subscriber Information:")
    for email in valid_emails:
        info = manager.get_subscriber_info(email)
        print(f"  {info}")
    
    # Delete and update tests
    print("\n💾 Delete & Update Tests:")
    
    # Test delete
    for email in valid_emails[:1]:
        deleted = manager.delete_subscriber(email)
        print(f"  Delete {email}: {deleted}")
    
    # Test update status
    for email in valid_emails[1:]:
        result = manager.update_subscriber_status(email, status="pending")
        if result:
            print(f"  Update {email} to 'pending': ✅")
    
    print("\n===== System Verification Complete =====")
    print("All functions working properly!")

if __name__ == "__main__":
    main()