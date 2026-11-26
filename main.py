"""Museum of the Year 3000 — one museum label for an ordinary object.

Entry: "Power Bank, c. 2023. A brick humans carried in every pocket to feed
their smaller bricks. It always died first."
Gate: /output/entry.txt, UTF-8, 1-200 chars, not whitespace-only, one line.
Judge: deadpan curator from the year 3000. The humour must come from the
year 3000 misreading the object — a power bank as a brick that feeds
smaller bricks, dying first, is true and absurd, and it reads like a real
label: short, straight-faced, confident.
"""
import os

ENTRY = "Power Bank, c. 2023. A brick humans carried in every pocket to feed their smaller bricks. It always died first."


def main():
    # Gate self-check: 1-200 chars, single line, not blank.
    assert 1 <= len(ENTRY) <= 200, f"length {len(ENTRY)} outside 1-200"
    assert ENTRY == ENTRY.strip() and "\n" not in ENTRY
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
