#!/bin/env python
# -*- coding: utf-8 -*- #
# Created And Coded by RC Chuah-(RaynerSec)

# Import Modules
import os
import sys
import argparse

# Install Kali Nethunter In Termux Full Version Function
def full():
    os.system("cd ${HOME} && curl -fsSL https://bit.ly/install-nethunter-full-termux | bash && rm -rf ${HOME}/kali-nethunter-daily-dev-rootfs-full-armhf.tar.xz && rm -rf ${HOME}/kali-nethunter-daily-dev-rootfs-full-arm64.tar.xz && rm -rf ${HOME}/kali-nethunter-daily-dev-rootfs-full-armhf.tar.xz.sha512sum && rm -rf ${HOME}/kali-nethunter-daily-dev-rootfs-full-arm64.tar.xz.sha512sum")

# Install Kali Nethunter In Termux Minimal Version Function
def minimal():
    os.system("cd ${HOME} && curl -fsSL https://bit.ly/install-nethunter-minimal-termux | bash && rm -rf ${HOME}/kali-nethunter-daily-dev-rootfs-minimal-armhf.tar.xz && rm -rf ${HOME}/kali-nethunter-daily-dev-rootfs-minimal-arm64.tar.xz && rm -rf ${HOME}/kali-nethunter-daily-dev-rootfs-minimal-armhf.tar.xz.sha512sum && rm -rf ${HOME}/kali-nethunter-daily-dev-rootfs-minimal-arm64.tar.xz.sha512sum")

# Install Kali Nethunter In Termux Nano Version Function
def nano():
    os.system("cd ${HOME} && curl -fsSL https://bit.ly/install-nethunter-nano-termux | bash && rm -rf ${HOME}/kali-nethunter-daily-dev-rootfs-nano-armhf.tar.xz && rm -rf ${HOME}/kali-nethunter-daily-dev-rootfs-nano-arm64.tar.xz && rm -rf ${HOME}/kali-nethunter-daily-dev-rootfs-nano-armhf.tar.xz.sha512sum && rm -rf ${HOME}/kali-nethunter-daily-dev-rootfs-nano-arm64.tar.xz.sha512sum")

# Uninstall Kali Nethunter In Termux Function
def uninstall():
    os.system("rm -rf ${HOME}/kali-arm64 && rm -rf ${HOME}/kali-armhf && rm -rf ${PREFIX}/bin/nh && rm -rf ${PREFIX}/bin/nethunter && sleep 1 && echo [+] Successfully Uninstalled ...")

# Main Function
def main():
    # Process Command Line Arguments
    parser = argparse.ArgumentParser(description='Kali-Nethunter-In-Termux Installer', add_help=False)
    parser.add_argument('-f', '--full', action='store_true', help='Install Kali Nethunter In Termux Full Version.')
    parser.add_argument('-m', '--minimal', action='store_true', help='Install Kali Nethunter In Termux Minimal Version.')
    parser.add_argument('-n', '--nano', action='store_true', help='Install Kali Nethunter In Termux Nano Version.')
    parser.add_argument('-u', '--uninstall', action='store_true', help='Uninstall Kali Nethunter In Termux.')
    parser.add_argument('-h', '--help', action='help', help='Show This Help Message And Exit.')
    # If No Arguments Provided, Display Usage Information
    if len(sys.argv) == 1:
      parser.print_help(sys.stderr)
      print("")
      sys.exit(1)
    # Parsing Command Line Arguments
    args = parser.parse_args()
    # Command Line Arguments
    if args.full:
      full()
    if args.minimal:
      minimal()
    if args.nano:
      nano()
    if args.uninstall:
      uninstall()

# Driver Code
if __name__ == "__main__":
    main()
