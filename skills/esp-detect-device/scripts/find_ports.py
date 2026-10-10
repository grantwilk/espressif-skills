#!/usr/bin/env python3
"""List serial ports with the identifiers needed to recognize an Espressif device on any OS.

Requires pyserial (already present in the ESP-IDF Python environment).

Examples:
    python find_ports.py                       # human-readable list
    python find_ports.py --json                # machine-readable
    python find_ports.py --espressif --first   # print only the port of the first native-USB chip
    python find_ports.py --vid 0x303a --serial 08:92:72:C4:1C:18 --first
"""

import argparse
import json
import sys

from serial.tools import list_ports

ESPRESSIF_VID = 0x303A


def describe(port: "list_ports.ListPortInfo") -> dict:
    """Converts a pyserial port record into a plain dictionary."""
    return {
        "device": port.device,
        "vid": f"0x{port.vid:04x}" if port.vid is not None else None,
        "pid": f"0x{port.pid:04x}" if port.pid is not None else None,
        "serial": port.serial_number or None,
        "description": port.description,
        "manufacturer": port.manufacturer,
        "location": port.location,
        "espressif_native_usb": port.vid == ESPRESSIF_VID,
    }


def parse_args() -> argparse.Namespace:
    """Parses the command line."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--vid", type=lambda v: int(v, 0), help="only ports with this USB VID")
    parser.add_argument("--pid", type=lambda v: int(v, 0), help="only ports with this USB PID")
    parser.add_argument("--serial", help="only ports whose USB serial contains this text")
    parser.add_argument("--espressif", action="store_true", help="only VID 0x303a (native USB)")
    parser.add_argument("--json", action="store_true", help="print JSON")
    parser.add_argument("--first", action="store_true", help="print only the first match's device")
    return parser.parse_args()


def main() -> int:
    """Prints matching ports; exits 1 when nothing matches."""
    args = parse_args()
    vid = ESPRESSIF_VID if args.espressif else args.vid
    ports = [
        describe(p)
        for p in sorted(list_ports.comports(), key=lambda p: p.device)
        if (vid is None or p.vid == vid)
        and (args.pid is None or p.pid == args.pid)
        and (not args.serial or args.serial.lower() in (p.serial_number or "").lower())
    ]
    if not ports:
        print("no matching serial ports", file=sys.stderr)
        return 1
    if args.first:
        print(ports[0]["device"])
    elif args.json:
        print(json.dumps(ports, indent=2))
    else:
        for p in ports:
            print(
                f"{p['device']}  vid={p['vid']} pid={p['pid']} serial={p['serial']}  "
                f"{p['description']}"
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
