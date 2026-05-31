import re
import os
from datetime import datetime

def create_sample_file():
    sample_text = """
    Hospital Staff Contact Directory
    =================================
    Dr. Priya Sharma - priya.sharma@cityhospital.com - Cardiology
    Nurse Kavya - kavya.nurse@cityhospital.com - ICU
    Admin Ravi - ravi.admin@cityhospital.com - Administration
    Dr. Kumar - kumar.doctor@gmail.com - Surgery
    Lab Tech - labtech@cityhospital.com - Laboratory
    Reception - reception@cityhospital.com - Front Desk
    Dr. Meena - meena@yahoo.com - Pediatrics
    Pharmacy - pharmacy.dept@cityhospital.com - Pharmacy
    Invalid entry - notanemail - skip this
    Another invalid - @nodomain - skip this
    HR Department - hr.department@cityhospital.com - Human Resources
    IT Support - itsupport@hospital.org - IT Department
    """
    with open("hospital_contacts.txt", "w") as f:
        f.write(sample_text)
    print("  ✅ Sample file 'hospital_contacts.txt' created!")

def extract_emails():
    print("=" * 55)
    print("   🏥 HOSPITAL EMAIL EXTRACTOR — Auto Task")
    print("=" * 55)
    print(f"   🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55)

    # Create sample file if not exists
    if not os.path.exists("hospital_contacts.txt"):
        print("\n  📄 Creating sample hospital contacts file...")
        create_sample_file()

    # Read input file
    print("\n  📖 Reading hospital_contacts.txt...")
    with open("hospital_contacts.txt", "r") as f:
        content = f.read()

    print(f"  ✅ File read successfully!")
    print(f"  📝 Total characters: {len(content)}")

    # Extract emails using regex
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, content)

    # Remove duplicates
    unique_emails = list(set(emails))
    unique_emails.sort()

    print(f"\n  🔍 Scanning for email addresses...")
    print(f"  📧 Found {len(emails)} emails ({len(unique_emails)} unique)")

    # Display found emails
    print("\n" + "=" * 55)
    print("  📧 EXTRACTED EMAIL ADDRESSES:")
    print("=" * 55)
    for i, email in enumerate(unique_emails, 1):
        domain = email.split("@")[1]
        if "cityhospital" in domain:
            tag = "🏥 Hospital"
        elif "gmail" in domain:
            tag = "📧 Gmail"
        elif "yahoo" in domain:
            tag = "📧 Yahoo"
        else:
            tag = "🌐 Other"
        print(f"  {i:2}. {email:<35} {tag}")

    # Save to output file
    output_file = f"extracted_emails_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(output_file, "w") as f:
        f.write("=" * 50 + "\n")
        f.write("  HOSPITAL EMAIL EXTRACTION REPORT\n")
        f.write(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Total Emails Found: {len(unique_emails)}\n\n")
        for i, email in enumerate(unique_emails, 1):
            f.write(f"{i}. {email}\n")
        f.write("\n" + "=" * 50 + "\n")
        f.write("Extraction Complete!\n")

    print("\n" + "=" * 55)
    print(f"  ✅ Emails saved to: {output_file}")
    print(f"  📊 SUMMARY:")
    print(f"     📧 Total emails found  : {len(emails)}")
    print(f"     ✨ Unique emails       : {len(unique_emails)}")
    print(f"     💾 Output file created : {output_file}")
    print(f"  🤖 Automation Complete!")
    print("=" * 55)

extract_emails()