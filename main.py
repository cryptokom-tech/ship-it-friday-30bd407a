from pathlib import Path

ENTRY = "feat: Friday 4:59pm, pushing to prod because the tests passed in a dream I had last night."
TARGET = Path("/output/entry.txt")


def validate_entry(value: str) -> bytes:
    encoded = value.encode("utf-8")
    decoded = encoded.decode("utf-8")
    if decoded != value:
        raise ValueError("entry must round-trip as UTF-8")
    if not 1 <= len(decoded) <= 159:
        raise ValueError("entry length must be between 1 and 159 characters")
    if "\n" in decoded or "\r" in decoded:
        raise ValueError("entry must be a single line")
    return encoded


def main() -> None:
    payload = validate_entry(ENTRY)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(payload)
    if TARGET.read_bytes() != payload:
        raise RuntimeError("read-back verification failed")


if __name__ == "__main__":
    main()
