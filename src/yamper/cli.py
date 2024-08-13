import argparse
import os
import sys
from .core import to_html, to_tokens

def main():
    parser= argparse.ArgumentParser(description="yamper: markdown to HTML converter")

    parser.add_argument('markdown_filepath', help="The Markdown filepath")
    parser.add_argument('--out', help= 'Output file name')
    parser.add_argument('-t', '--template', choices= ["standard-light", "standard-dark", "plain"] ,help="Choose an existing HTML template")
    parser.add_argument('--tokens', action="store_true", help="Output tokens instead of HTML")

    args= parser.parse_args()


    try:
        if args.tokens:
            tokens = to_tokens(args.markdown_filepath, args.out)
            if tokens:
                print(tokens)  
            else:
                # print(f"Tokens are written to: {args.out}")
                # tokens are written to the file
                pass
        else:
            html_content = to_html(args.markdown_filepath, args.out, args.template)
            if html_content:
                print("First 100 characters of the HTML content:")
                print(html_content[:500] + "..." if len(html_content) > 100 else html_content)
            else:
                # print(f"HTML content has been written to: {args.out}")
                # html is written to the file
                pass
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)



if __name__== "__main__":
    main()