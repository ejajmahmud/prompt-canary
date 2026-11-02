"""Command line interface for prompt-canary."""
from .canary import CanaryEngine

def main():
    text = "You are a confidential assistant."
    canary = CanaryEngine.inject(text, "SECRET-42")
    print("Injected text length:", len(text), "->", len(canary))
    detected = CanaryEngine.has_canary(canary, "SECRET-42")
    print("Canary detected:", detected)

if __name__ == "__main__":
    main()
