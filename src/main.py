import sys
sys.path.insert(0, "/home/rahul/workspace/github.com/rahulsane/static-site-generator")
from public.textnode import *
def main() -> None:
    dummy_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(dummy_node)

if __name__ == "__main__":
    main()