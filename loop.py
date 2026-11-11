#!/usr/bin/env python3
"""
Scary Drama / Film Prop - Terminal Text Looper
Used for on-camera horror/drama scenes to display relentless, looping distress text.
"""

import argparse
import os
import re
import sys
import time

# Ensure UTF-8 output in Windows consoles
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Enable Windows ANSI Virtual Terminal processing
os.system("")

# Set console title
try:
    if os.name == "nt":
        os.system("title DRAMA PROP - TERMINAL LOOP")
except Exception:
    pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TEXT_PATH = os.path.join(SCRIPT_DIR, "text.txt")

_SINGLE_BLOCK = (
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I DON’T WANT TO BE WITH THE ALIEN !!! "
    "I DON’T WANT TO BE WITH THE SPIRIT !!! "
    "I HATE THE ALIENS AND SPIRITS SO DEEP MORE THAN BOTTOMLESS PIT !!! "
    "GIVE ME BACK MY MONEY !!! GIVE ME BACK MY MONEY !!! GIVE ME BACK MY MONEY !!! GIVE ME BACK MY MONEY !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME, I WANT TO GO HOME, I WANT TO GO HOME !!! "
    "I WANT TO GO HOME !!! I WANT TO GO HOME !!! I WANT TO GO HOME !!! "
    "I WANT TO GO HOME !!! I WANT TO GO HOME !!! I WANT TO GO HOME !!! "
    "I WANT TO GO HOME !!! I WANT TO GO HOME !!! I WANT TO GO HOME !!! "
    "I WANT TO GO HOME !!! I WANT TO GO HOME !!! I WANT TO GO HOME !!! "
    "I WANT TO GO HOME !!! I WANT TO GO HOME !!! I WANT TO GO HOME !!! "
    "I WANT TO GO HOME !!! I WANT TO GO HOME !!! I WANT TO GO HOME !!! "
    "I WANT TO GO HOME !!! I WANT TO GO HOME !!! I WANT TO GO HOME !!! "
    "I WANT TO GO HOME !!! I WANT TO GO HOME !!! I WANT TO GO HOME !!! "
)

# 9 complete repetitions of the distress block ending with ellipsis
FALLBACK_TEXT = ((_SINGLE_BLOCK.strip() + " ") * 9).strip() + " …"


def load_text(custom_file: str | None = None) -> str:
    path = custom_file or DEFAULT_TEXT_PATH
    if path and os.path.isfile(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    return content
        except Exception:
            pass
    return FALLBACK_TEXT


COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "bold_red": "\033[1;91m",
    "none": "",
}
RESET = "\033[0m"


def get_phrases(text: str) -> list[str]:
    """Splits into dramatic phrases based on exclamation marks and punctuation."""
    parts = re.split(r"(?<=[!…])\s+", text.strip())
    return [p for p in parts if p]


def loop_phrases(phrases: list[str], delay: float, color_code: str):
    while True:
        for phrase in phrases:
            print(f"{color_code}{phrase}{RESET}")
            sys.stdout.flush()
            if delay > 0:
                time.sleep(delay)


def loop_words(text: str, delay: float, color_code: str):
    words = text.split()
    while True:
        for word in words:
            print(f"{color_code}{word}{RESET} ", end="", flush=True)
            if delay > 0:
                time.sleep(delay)


def loop_block(text: str, delay: float, color_code: str):
    while True:
        print(f"{color_code}{text}{RESET}\n")
        sys.stdout.flush()
        if delay > 0:
            time.sleep(delay)


def main():
    parser = argparse.ArgumentParser(
        description="Loop distress text continuously in a visible terminal."
    )
    parser.add_argument(
        "--file",
        type=str,
        default=None,
        help="Path to custom text file (defaults to text.txt in script folder)",
    )
    parser.add_argument(
        "--mode",
        choices=["words", "lines", "block"],
        default="words",
        help="Display mode: 'words' (word-by-word streaming), 'lines' (phrase by phrase), 'block' (entire text). Default: words",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.03,
        help="Delay in seconds between items (default: 0.03 for words; recommend 0.05-0.15 for lines)",
    )
    parser.add_argument(
        "--color",
        choices=list(COLORS.keys()),
        default="bold_red",
        help="Terminal color (default: bold_red)",
    )

    args = parser.parse_args()

    text = load_text(args.file)
    color_code = COLORS.get(args.color, "")
    phrases = get_phrases(text)

    try:
        if args.mode == "words":
            loop_words(text, args.delay, color_code)
        elif args.mode == "lines":
            delay = args.delay if args.delay != 0.03 else 0.08
            loop_phrases(phrases, delay, color_code)
        elif args.mode == "block":
            delay = args.delay if args.delay != 0.03 else 0.5
            loop_block(text, delay, color_code)
    except KeyboardInterrupt:
        print(f"\n{RESET}[Loop stopped by user]")
        sys.exit(0)


if __name__ == "__main__":
    main()
