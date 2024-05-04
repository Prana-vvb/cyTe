# Basic cipher Tool

Basic cipher Tool is a command-line Python tool designed to encrypt/decrypt some text using basic ciphers
It currently offer:
1.Rotation/Caesar cipher
2.Vigenere cipher
3.Playfair cipher
4.Railfence cipher

There will be more ciphers added in the future and hopefully make it a 'Complex cipher Tool' :P

## Installation

To install, you can use :

```bash
gh repo clone Prana-vvb/Basic-cipher-tool
git clone https://github.com/Prana-vvb/Basic-cipher-tool.git
```

## Usage

Open up a terminal/command prompt/powershell window and cd to where you have installed the tool
Type in 
```bash
python3 cyTool.py -h
```
for the help window

It should display this text

```bash
usage: cyTool.py [-h] [--encrypt ENCRYPT] [--decrypt DECRYPT] [-rot ROTATION] [-v VIGENERE] [-p PLAYFAIR]
                 [-rf RAILFENCE]

Basic ciphers encryption/decryption

options:
  -h, --help            show this help message and exit
  --encrypt ENCRYPT     Encrypt a text. Syntax: [--encrypt <text>]
  --decrypt DECRYPT     Decrypt a text. Syntax: [--decrypt <text>]
  -rot ROTATION, --rotation ROTATION
                        Rotation cipher key. Syntax: [-rot <key>], [--rotation <key>]
  -v VIGENERE, --vigenere VIGENERE
                        Vigenere cipher key. Syntax: [-v <key>], [--vigenere <key>]
  -p PLAYFAIR, --playfair PLAYFAIR
                        Playfair cipher key. Syntax: [-p <key>], [--playfair <key>]
  -rf RAILFENCE, --railfence RAILFENCE
                        Railfence cipher key. Syntax: [-rf <key>], [--railfence <key>]
```
