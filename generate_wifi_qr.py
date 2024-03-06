#!/usr/bin/env python3

import argparse
import wifi_qrcode_generator.generator


def generate_wifi_qr_code(ssid, password, authentication_type='WPA'):
    # Create the WiFi QR code payload
    qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
        ssid=ssid, hidden=False, authentication_type=authentication_type, password=password
    )
    qr_code.print_ascii()
    return qr_code


def main():
    parser = argparse.ArgumentParser(description="Generate QR code for WiFi auto-login")
    parser.add_argument("ssid", help="SSID of the WiFi network")
    parser.add_argument("password", help="Password of the WiFi network")
    parser.add_argument("--authentication_type", choices=["WPA", "WEP", "nopass"], default="WPA", help="Authentication type of the WiFi network (default: WPA)")
    args = parser.parse_args()

    ssid = args.ssid
    password = args.password
    authentication_type = args.authentication_type

    qr_code_img = generate_wifi_qr_code(ssid, password, authentication_type)
    qr_code_img.make_image().save('qr.png')
    print("WiFi QR Code generated successfully.")


if __name__ == "__main__":
    main()
