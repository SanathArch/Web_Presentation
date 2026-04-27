#! /usr/bin/env python3
"""
Newsletter Management System - Complete Main Entry Point

This system handles:
1. Email subscriber validation
2. Multi-storage configuration
3. Welcome messages
4. Status tracking
5. Subscriber management
"""

import sys
import os
from pathlib import Path
import json

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from verify import SubscriberManager

def main():
    """Main entry point for newsletter management system"""
    
    print("=" * 60)
    print("  📧 NEWSLETTER MANAGEMENT SYSTEM")
    print("=" * 60)
    
    # Initialize manager
    manager = SubscriberManager()
    
    # Initialize counters
    valid_count = 0
    invalid_count = 0
    
    # Sample test emails
    valid_emails = [
        "subscriber1@example.com",
        "newsletter@test.com",
        "info@company.org"
    ]
    
    invalid_emails = [
        "invalid@.com",
        "@example.com",
        "test@.invalid",
        ".bad@domain.com"
    ]
    
    # Process valid emails
    print("\n✅ Processing Valid Emails:")
    for email in valid_emails:
        result = manager.save_subscriber(email)
        if result["valid"]:
            valid_count += 1
            print(f"  ✅ {email}")
        else:
            print(f"  ❌ {email}: {result['message']}")
    
    # Process invalid emails
    print("\n❌ Processing Invalid Emails:")
    for email in invalid_emails:
        result = manager.save_subscriber(email)
        if not result["valid"]:
            invalid_count += 1
            print(f"  ✅ Rejected: {email}")
            print(f"     Reason: {result['message']}")
        else:
            print(f"  ❌ Accepted (unexpected): {email}")
    
    # Summary
    print(f"\n{'==' * 30}")
    print("SUMMARY:")
    print(f"  Valid subscribers created: {valid_count}")
    print(f"  Invalid emails rejected: {invalid_count}")
    print(f"  Total emails processed: {valid_count + invalid_count}")
    
    # Show directory structure
    print(f"\n📁 Directory Structure:")
    print(f"  subscribers/")
    
    for email_file in manager.subscribers.iterdir():
        if email_file.is_dir():
            print(f"    {email_file.name}/")
            for file in email_file.iterdir():
                print(f"      - {file.name}")
    
    print("\n" + "=" * 60)
    print("  SYSTEM READY ✓")
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
