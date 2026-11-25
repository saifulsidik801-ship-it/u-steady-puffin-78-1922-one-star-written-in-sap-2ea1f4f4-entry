import os

ENTRY = "One star. He waters me every Sunday whether I'm thirsty or drowning, then tells guests I'm 'low maintenance' while I sit here dying in a pot he bought because it matched the couch."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
