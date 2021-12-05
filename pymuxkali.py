#!/bin/env python
# -*- coding: utf-8 -*- #
# Created And Coded by RC Chuah-(RaynerSec)

# Import Modules
import os
import sys
import argparse

# Main Function
def main():
    # Process Command Line Arguments
    parser = argparse.ArgumentParser(description='Kali-Nethunter-In-Termux Installer', add_help=False)
    parser.add_argument('-f', '--full', action='store_true', help='Install Kali Nethunter In Termux Full Version.')
    parser.add_argument('-m', '--minimal', action='store_true', help='Install Kali Nethunter In Termux Minimal Version.')
    parser.add_argument('-u', '--uninstall', action='store_true', help='Uninstall Kali Nethunter In Termux.')
    parser.add_argument('-h', '--help', action='help', help='Show This Help Message And Exit.')
    # If No Arguments Provided, Display Usage Information
    if len(sys.argv)==1:
      parser.print_help(sys.stderr)
      print("")
      sys.exit(1)
    # Parsing Command Line Arguments
    args = parser.parse_args()
    # Command Line Arguments
    if args.full:
      os.system("cd ${HOME} && curl -fsSL https://bit.do/fNyso | bash && rm -rf ${HOME}/kalifs-armhf-full.tar.xz && rm -rf ${HOME}/kalifs-arm64-full.tar.xz && rm -rf ${HOME}/kalifs-armhf-full.sha512sum && rm -rf ${HOME}/kalifs-arm64-full.sha512sum")
    if args.minimal:
      os.system("cd ${HOME} && curl -fsSL https://bit.do/fNysW | bash && rm -rf ${HOME}/kalifs-armhf-minimal.tar.xz && rm -rf ${HOME}/kalifs-arm64-minimal.tar.xz && rm -rf ${HOME}/kalifs-armhf-minimal.sha512sum && rm -rf ${HOME}/kalifs-arm64-minimal.sha512sum")
    if args.uninstall:
      os.system("rm -rf ${HOME}/kali-arm64 && rm -rf ${HOME}/kali-armhf && rm -rf ${PREFIX}/bin/nh && rm -rf ${PREFIX}/bin/nethunter && sleep 1 && echo [+] Successfully Uninstalled ...")

# Driver Code
if __name__ == "__main__":
    main()
