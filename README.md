# Project-2
Internship Project 2

# 🔐 Basic Encryption & Decryption using Caesar Cipher

A simple Python project that demonstrates the fundamentals of **encryption** and **decryption** using the **Caesar Cipher** algorithm. This project was developed as **Project 2** during the **DecodeLabs Cyber Security Internship 2026**.

---

## 📌 Project Overview

The Caesar Cipher is one of the oldest and simplest encryption techniques. It works by shifting each letter in a message by a fixed number of positions in the alphabet.

This project allows users to:
- Encrypt a text message.
- Decrypt the encrypted message.
- Choose their own shift key.
- Preserve spaces, numbers, and special characters.

---

## 🚀 Features

- 🔒 Encrypt any text using Caesar Cipher.
- 🔓 Decrypt encrypted text back to the original message.
- 🔑 User-defined shift key.
- 🔠 Supports both uppercase and lowercase letters.
- 📝 Keeps spaces, numbers, and symbols unchanged.
- 💻 Simple command-line interface.

---

## 🛠️ Technologies Used

- Python 3

---

## 📂 Project Structure

```
Basic-Encryption-Decryption/
│
├── encryption.py      # Main Python program
├── README.md          # Project documentation
└── LICENSE            # (Optional)
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Basic-Encryption-Decryption.git
```

### 2. Navigate to the project folder

```bash
cd Basic-Encryption-Decryption
```

### 3. Run the program

```bash
python encryption.py
```

---

## 💻 Example Output

```
==================================================
      BASIC ENCRYPTION & DECRYPTION
            Caesar Cipher
==================================================

Enter your message: Hello World
Enter shift key (1-25): 3

==================================================
Original Message  : Hello World
Encrypted Message : Khoor Zruog
Decrypted Message : Hello World
==================================================
```

---

## 🔍 How Caesar Cipher Works

Suppose the shift key is **3**.

```
Original Alphabet:
ABCDEFGHIJKLMNOPQRSTUVWXYZ

Shifted Alphabet:
DEFGHIJKLMNOPQRSTUVWXYZABC
```

Example:

```
Original : HELLO
Encrypted: KHOOR
```

During decryption, the letters are shifted backward by the same key to recover the original message.

---

## 🎯 Learning Outcomes

This project helped in understanding:

- Basics of Cryptography
- Encryption Concepts
- Decryption Process
- ASCII Character Manipulation
- Python Loops
- Conditional Statements
- Functions
- User Input Handling
- String Processing

---

## 📖 Future Improvements

- Add Vigenère Cipher
- Add AES Encryption
- GUI using Tkinter
- File Encryption
- Password-Protected Encryption
- Save encrypted messages to a file

---

## 👨‍💻 Author

**Saira Muskan**
Cyber Security Student  
DecodeLabs Cyber Security Internship 2026

GitHub: https://github.com/sairamuskan52

---

## 📜 License

This project is created for educational purposes as part of the **DecodeLabs Cyber Security Internship 2026**.

Feel free to use and modify it for learning.
