import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
   output = re.search(r"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)", s)
   if output:
     video_id = output.group(1)  
     return f"https://youtu.be/{video_id}"



if __name__ == "__main__":
    main()
