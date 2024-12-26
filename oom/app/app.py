import os

def create_large_file():
    with open("/data/large_file", "a") as f:
        while True:
            f.write("A" * 10**6)

if __name__ == "__main__":
    os.makedirs("/data", exist_ok=True)
    create_large_file()
