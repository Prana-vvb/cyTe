# CyTe

Cyte is a command-line Python tool designed to encrypt/decrypt some text using basic ciphers
It currently offer:
1. Rotation/Caesar cipher
2. Vigenere cipher
3. Playfair cipher
4. Railfence cipher

There will be more ciphers added in the future and hopefully make it a 'Complex cipher Tool' :P

## Installation

To install, you can use either

```bash
gh repo clone Prana-vvb/cyTe
```
or
```bash
git clone https://github.com/Prana-vvb/cyTe.git
```

## Usage

Open up a terminal/command prompt/powershell window and cd to where you have installed the tool
Type in 
```bash
python3 cyTe.py -h
```
for the help window

It should display this text

```bash
usage: cyTe.py [-h] [--encrypt ENCRYPT] [--decrypt DECRYPT] [-rot ROTATION] [-v VIGENERE] [-p PLAYFAIR]
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

## Examples

```bash
$ py cyTe.py --encrypt Hello -rot 3
Encrypting "Hello" using Rotation cipher with key = 3
Result = Khoor

$ py cyTool.py --encrypt Hello -v key
Encrypting "Hello" using Vigenere cipher with keyword = "key"
Result = rijvs

$ py cyTe.py --decrypt Wdolr -rf 3
Decrypting "Wdolr" using Railfence cipher with depth = 3
Result = World

$ py cyTe.py --decrypt vnmtbz -p monarchy
Decrypting "vnmtbz" using Playfair cipher with keyword = "monarchy"
Result = worldx
```

## Contributing

Feel free to contribute to improve this tool. Here are some ways you can contribute:

### Bug Reports

If you encounter any bugs or unexpected behavior while using the tool, please [open an issue](https://github.com/Prana-vvb/cyTe/issues) on GitHub and provide as much detail as possible, including steps to reproduce the issue.

### Features

If you have ideas for new features or improvements like adding new ciphers or optimising the current ones, feel free to [open an issue](https://github.com/Prana-vvb/cyTe/issues) on GitHub to discuss them.

Or if you'd like to contribute directly to the codebase, you can fork the repository, make your changes, and submit a pull request.

When submitting a pull request, provide a clear description of the changes you've made and why they're necessary.

