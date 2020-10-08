# Python Password Manager
>Note: This password manager was made as a project and is NOT intended for actual use. Please use more sophisticated and well-tested/trusted password managers to store sensitive data.


## AES Encryption

The encryption method used in this program comes from the python library [PyCryptoDome](https://pypi.org/project/pycryptodome/). This program uses AES encryption methods to store sensitive data (in this case passwords) into a json file.

## Hash Verification
 To authenticate the user, they are prompted to create a master password (that is also used to decrypt data) which is then stored using a SHA256 Hash Function and is verified at login. Whenever the user is prompted to verify their master password, the password they enter is compared to the hash of the stored master password and access if granted if the two hashes match.

## Requirements
- astroid (2.3.3)
- colorama (0.4.3)
- cursor (1.3.4)
- halo (0.0.28)
- isort (4.3.21)
- lazy-object-proxy (1.4.3)
- log-symbols (0.0.14)
- mccabe (0.6.1)
- pycryptodome (3.9.4)
- pylint (2.4.4)
- pyperclip (1.7.0)
- six (1.13.0)
- spinners (0.0.23)
- termcolor (1.1.0)
- typed-ast (1.4.0)
- wrapt (1.11.2)

#### To be executed in the terminal:
```shell
pip install astroid
pip install colorama
pip install cursor
pip install halo
pip install isort
pip install lazy-object-proxy
pip install log-symbols
pip install mccabe
pip install pycryptodome
pip install pylint
pip install pyperclip
pip install six
pip install spinners
pip install termcolor
pip install typed-ast
pip install wrapt
```

## Vulnerability
As mentioned at the top, this was made as a project and not intended for actual use. Below I demonstrate what any expert hacker can accomplish by exploiting a vulnerability. Just kidding, anyone can do this. Since the files are stored locally, they can easily be deleted without needing to enter any credentials and consequently all stored passwords are gone along with other data.

## Screenshots
[![Screenshot 1](https://github.com/anubhab-code/Password-Manager/blob/master/Screenshots/1.png "Screenshot 1")](https://github.com/anubhab-code/Password-Manager/blob/master/Screenshots/1.png "Screenshot 1")

[![Screenshot 2](https://github.com/anubhab-code/Password-Manager/blob/master/Screenshots/2.png "Screenshot 2")](https://github.com/anubhab-code/Password-Manager/blob/master/Screenshots/2.png "Screenshot 2")

[![Screenshot 3](https://github.com/anubhab-code/Password-Manager/blob/master/Screenshots/3.png "Screenshot 3")](https://github.com/anubhab-code/Password-Manager/blob/master/Screenshots/3.png "Screenshot 3")

[![Screenshot 4](https://github.com/anubhab-code/Password-Manager/blob/master/Screenshots/4.png "Screenshot 4")](https://github.com/anubhab-code/Password-Manager/blob/master/Screenshots/4.png "Screenshot 4")

[![Screenshot 5](https://github.com/anubhab-code/Password-Manager/blob/master/Screenshots/5.png "Screenshot 5")](https://github.com/anubhab-code/Password-Manager/blob/master/Screenshots/5.png "Screenshot 5")

