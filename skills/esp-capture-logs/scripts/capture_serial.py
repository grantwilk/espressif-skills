#!/usr/bin/env python3
"""Capture serial output from an Espressif device for a bounded time, without a terminal.

Requires pyserial (already present in the ESP-IDF Python environment).

Examples:
    python capture_serial.py --port <PORT> --seconds 15 --out boot.log
    python capture_serial.py --vid 0x303a --serial <USB_SERIAL> --reset --until "app_main" --seconds 20
    python capture_serial.py --port <PORT> --seconds 60 --timestamps --out run.log

Exit codes: 0 done (or --until matched), 1 no matching port, 2 cannot open port,
3 --until never matched before the timeout.
"""

import argparse
import re
import sys
import time
from datetime import datetime

import serial
from serial.tools import list_ports


def resolve_port(args: argparse.Namespace) -> str | None:
    """Returns the port to open: --port as given, else the first port matching --vid/--serial."""
    if args.port:
        return args.port
    for port in sorted(list_ports.comports(), key=lambda p: p.device):
        if args.vid is not None and port.vid != args.vid:
            continue
        if args.serial and args.serial.lower() not in (port.serial_number or "").lower():
            continue
        if args.vid is None and not args.serial:
            continue
        return port.device
    return None


def reset_chip(conn: serial.Serial) -> None:
    """Pulses EN through RTS, the standard auto-reset wiring, with the boot pin released."""
    conn.dtr = False
    conn.rts = True
    time.sleep(0.1)
    conn.rts = False


def capture(conn: serial.Serial, args: argparse.Namespace) -> int:
    """Reads lines until the time limit or the --until pattern; returns the exit code."""
    pattern = re.compile(args.until) if args.until else None
    out = open(args.out, "w", encoding="utf-8") if args.out else None
    deadline = time.monotonic() + args.seconds
    matched = False
    try:
        while time.monotonic() < deadline and not matched:
            raw = conn.readline()
            if not raw:
                continue
            line = raw.decode("utf-8", errors="replace").rstrip("\r\n")
            if args.timestamps:
                line = f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] {line}"
            print(line, flush=True)
            if out:
                out.write(line + "\n")
            matched = bool(pattern and pattern.search(line))
    finally:
        if out:
            out.close()
    return 0 if matched or not pattern else 3


def main() -> int:
    """Parses arguments, opens the port, and runs the capture."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--port", help="device path/name or a pyserial URL")
    parser.add_argument("--vid", type=lambda v: int(v, 0), help="select port by USB VID")
    parser.add_argument("--serial", help="select port by (part of) the USB serial number")
    parser.add_argument("--baud", type=int, default=115200)
    parser.add_argument("--seconds", type=float, default=10.0, help="capture duration")
    parser.add_argument("--until", help="regex; stop successfully when a line matches")
    parser.add_argument("--reset", action="store_true", help="reset the chip after opening")
    parser.add_argument("--timestamps", action="store_true", help="prefix host timestamps")
    parser.add_argument("--out", help="also write the capture to this file")
    args = parser.parse_args()

    port = resolve_port(args)
    if port is None:
        print("no matching serial port", file=sys.stderr)
        return 1
    try:
        conn = serial.serial_for_url(port, baudrate=args.baud, timeout=0.2)
    except serial.SerialException as error:
        print(f"cannot open {port}: {error}", file=sys.stderr)
        return 2
    with conn:
        if args.reset:
            reset_chip(conn)
        return capture(conn, args)


if __name__ == "__main__":
    sys.exit(main())
