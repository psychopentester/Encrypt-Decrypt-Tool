# Encrypt-Decrypt-Tool

Encrypt-Decrypt Tool
A command-line encryption and decryption utility implementing the Caesar cipher algorithm. 
This tool provides an intuitive interface for performing classical cryptographic operations, it ideal for educational purposes and understanding fundamental encryption concepts.

📖 Overview
The Encrypt-Decrypt Tool is a Python-based application that demonstrates the principles of classical cryptography through the implementation of the Caesar cipher. 
It features automatic encryption detection, bidirectional text processing, and a user-friendly command-line interface suitable for both beginners and security enthusiasts.

🔐 Key Features
Text Encryption: Transform plaintext into cipher text using customizable shift values
Text Decryption: Reverse encrypted messages back to their original readable format
Intelligent Auto-Detection: Automatically identifies whether input text is encrypted or plaintext based on linguistic analysis
Interactive Command-Line Interface: Navigate through options using an intuitive menu-driven system
Format Preservation: Maintains original spacing, punctuation, and special characters during encryption/decryption operations

Caesar Cipher Algorithm
The Caesar cipher is a substitution cipher technique where each letter in the plaintext is replaced by a letter at a fixed number of positions down the alphabet. 
This shift value determines the encryption key.
Example with shift value of 4:
A → E
B → F
Psycho → Twcgls

The algorithm operates by:
Taking each alphabetic character from the input
Shifting it forward (encryption) or backward (decryption) by the specified number
Wrapping around the alphabet when necessary (Z shifts to A)
Preserving non-alphabetic characters unchanged

📋 Prerequisites
Python: Version 3.x or higher
Operating System: Windows, macOS, or Linux
Dependencies: None (uses only Python standard library)

💻 Installation
Step 1: Clone the Repository
bashgit clone https://github.com/yourusername/Encrypt-Decrypt-Tool.git
cd Encrypt-Decrypt-Tool
Step 2: Verify Python Installation
bashpython --version
Ensure Python 3.x is installed on your system.
Step 3: Run the Application
bashpython psycho_pentester.py

⚠️ Security Disclaimer
IMPORTANT: The Caesar cipher is a classical encryption technique that is NOT secure for protecting sensitive information in modern contexts. This tool is designed exclusively for:
Educational Purposes: Understanding basic cryptographic concepts
Academic Learning: Studying historical encryption methods
Penetration Testing Practice: Training in controlled environments
Basic Obfuscation: Non-critical text transformation

For Production Security
Do NOT use this tool for:
Protecting passwords or credentials
Encrypting confidential business data
Securing personal information
Any real-world security application

Thanks you !!
