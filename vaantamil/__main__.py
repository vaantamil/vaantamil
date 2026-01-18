# utilis/__main__.py
import sys
from .meimmayakkam import format_meimmayakkam_output, மெய்ம்மயக்கம்_சோதனை

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m utilis <TamilWord>")
        sys.exit(1)

    word = sys.argv[1]
    result = மெய்ம்மயக்கம்_சோதனை(word)
    print(result)

if __name__ == "__main__":
    main()
