# pymuxkali
This is a python script by which you can install Kali Nethunter (Kali Linux) in your termux application without rooted phone.

## Usage
### How To Use pymuxkali
1. Install Dependencies In Termux `pkg update -y && pkg install git python -y`
2. Git Clone Repo `git clone https://github.com/RaynerSec/pymuxkali`
3. Change Directory `cd pymuxkali`
4. Run script `python install.py <options>`
### pymuxkali options
```
usage: install.py [-f] [-m] [-u] [-h]

optional arguments:
  -f, --full       Install Kali Nethunter In Termux Full Version.
  -m, --minimal    Install Kali Nethunter In Termux Minimal Version.
  -u, --uninstall  Uninstall Kali Nethunter In Termux.
  -h, --help       Show This Help Message And Exit.
```
