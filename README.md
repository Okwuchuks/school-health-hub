# School Health Hub (SHH)

A secure, offline-first Electronic Health Record (EHR) system designed specifically for boarding schools. Built with Python, PySide6, and AES-256 encryption to ensure student health data is protected and accessible even without internet connectivity.

## 🎯 Overview

School Health Hub is a desktop application that enables healthcare professionals in boarding schools to efficiently manage student health records with enterprise-grade security. The system operates seamlessly offline, making it ideal for schools in areas with limited or unreliable internet connectivity.

## ✨ Key Features

- **Offline-First Architecture**: Full functionality without internet connectivity
- **AES-256 Encryption**: Military-grade encryption for all sensitive health data
- **Modern Desktop UI**: Intuitive interface built with PySide6
- **Student Health Records**: Comprehensive management of student medical information
- **Secure Storage**: Local database with encrypted data at rest
- **Access Control**: Role-based permissions for healthcare staff
- **Audit Trails**: Track all access to health records for compliance

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **GUI Framework**: PySide6 (Qt for Python)
- **Encryption**: AES-256 via cryptography library
- **Architecture**: Modular design with separated concerns (UI, Logic, Database, Security)

## 📋 Requirements

- Python 3.8+
- PySide6
- cryptography

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Okwuchuks/school-health-hub.git
cd school-health-hub

python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

school-health-hub/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── ruff.toml              # Code linting configuration
├── LICENSE                # MIT License
├── assets/                # Images and application resources
├── ui/                    # User interface components
│   └── main_window.py     # Main application window
├── database/              # Database operations and models
├── logic/                 # Business logic and processing
└── security/              # Encryption and security utilities

Directory Details
ui/: Contains all PySide6 GUI components and window definitions
database/: Handles data storage, retrieval, and database operations
logic/: Core business logic for health record management
security/: Encryption, decryption, and security-related functions
assets/: Images, icons, and other UI resources
🔐 Security
This application implements robust security measures:

AES-256 Encryption: All sensitive student health data is encrypted using AES-256
Encrypted Database: Local SQLite database with encrypted fields
Access Control: User authentication and role-based permissions
Secure Key Management: Cryptographic keys are managed securely
No Internet Required: Reduces attack surface by operating offline
👤 Author
Ifende Daniel

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🤝 Contributing
Contributions are welcome! Please feel free to:

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request
📊 Code Quality
This project uses Ruff for code linting and formatting. Configuration is available in ruff.toml.

Formatting Standard
Line length: 120 characters
Indent width: 4 spaces
Enabled checks: E (errors), F (Pyflakes), W (warnings), I (imports)
🐛 Issues & Bug Reports
If you encounter any issues or bugs, please open an issue on the GitHub Issues page.

📚 Documentation
For more detailed documentation on specific components:

UI Module: See ui/ directory for interface documentation
Database: See database/ directory for data models
Security: See security/ directory for encryption details
✅ Roadmap
Future enhancements may include:

Web-based companion portal for parents/guardians
Sync capabilities when internet is available
Advanced reporting and analytics
Integration with school management systems
Mobile application support
Multi-school organization management
📞 Support
For questions or support, please:

Open an issue on GitHub
Contact the development team
Check existing documentation and wiki
Note: This application handles sensitive student health information. Always follow HIPAA, FERPA, and local data protection regulations when deploying and using this system.

Built with ❤️ for school healthcare professionals.