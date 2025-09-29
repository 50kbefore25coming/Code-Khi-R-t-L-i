import sys

def main():
    s = sys.stdin.read().strip()
    if s.lower().endswith('.py'):
        print("yes")
    else:
        print("no")

if __name__  == "__main__":
    main()