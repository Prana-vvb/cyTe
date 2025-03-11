import argparse
import sys
import lib.playfair as playfair
import lib.vignere as vignere
import lib.rot as rot
import lib.railfence as railfence


def createParse():
    parser = argparse.ArgumentParser(
        description='Basic ciphers encryption/decryption')

    parser.add_argument('--encrypt',
                        help='Encrypt a text. Syntax: [--encrypt <text>]',
                        default=None)
    parser.add_argument('--decrypt',
                        help='Decrypt a text. Syntax: [--decrypt <text>]',
                        default=None)
    parser.add_argument('-rot',
                        '--rotation',
                        help='''Rotation cipher key.
                        Syntax: [-rot <key>], [--rotation <key>]''')
    parser.add_argument('-v',
                        '--vigenere',
                        help='''Vigenere cipher key.
                        Syntax: [-v <key>], [--vigenere <key>]''')
    parser.add_argument('-p', '--playfair',
                        help='''Playfair cipher key.
                        Syntax: [-p <key>], [--playfair <key>]''')
    parser.add_argument('-rf', '--railfence',
                        help='''Railfence cipher key.
                        Syntax: [-rf <key>], [--railfence <key>]''')

    return parser


def main():
    p = createParse()
    args = p.parse_args()

    if len(sys.argv) > 1:
        if args.encrypt:
            if args.rotation:
                res = rot.encrypt(args.encrypt, int(args.rotation))
                print(f'Encrypting "{args.encrypt}" using Rotation cipher with key = {
                      args.rotation}')
                print(f'Result = {res}')
            elif args.vigenere:
                res = vignere.encrypt(args.encrypt, args.vigenere)
                print(f'Encrypting "{args.encrypt}" using Vigenere cipher with keyword = "{
                      args.vigenere}"')
                print(f'Result = {res}')
            elif args.playfair:
                res = playfair.encrypt(args.encrypt, args.playfair)
                print(f'Encrypting "{args.encrypt}" using Playfair cipher with keyword = "{
                      args.playfair}"')
                print(f'Result = {res}')
            elif args.railfence:
                res = railfence.encrypt(args.encrypt, int(args.railfence))
                print(f'Encrypting "{args.encrypt}" using Railfence cipher with depth = {
                      args.railfence}')
                print(f'Result = {res}')
        elif args.decrypt:
            if args.rotation:
                res = rot.decrypt(args.decrypt, int(args.rotation))
                print(f'Decrypting "{args.decrypt}" using Rotation cipher with key = {
                      args.rotation}')
                print(f'Result = {res}')
            elif args.vigenere:
                res = vignere.decrypt(args.decrypt, args.vigenere)
                print(f'Decrypting "{args.decrypt}" using Vigenere cipher with keyword = "{
                      args.vigenere}"')
                print(f'Result = {res}')
            elif args.playfair:
                res = playfair.decrypt(args.decrypt, args.playfair)
                print(f'Decrypting "{args.decrypt}" using Playfair cipher with keyword = "{
                      args.playfair}"')
                print(f'Result = {res}')
            elif args.railfence:
                res = railfence.decrypt(args.decrypt, int(args.railfence))
                print(f'Decrypting "{args.decrypt}" using Railfence cipher with depth = {
                      args.railfence}')
                print(f'Result = {res}')
    else:
        print("Welcome to CyTool!")
        print("Run 'py cyTool.py -h' for help")


if __name__ == "__main__":
    main()
