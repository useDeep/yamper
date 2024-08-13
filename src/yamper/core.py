import os
from .lexer.lexer import Lexer
from .parser.parser import Parser

def to_html(md_file, output_file=None, template="standard-light"):

    if not template:
        template = "standard-light"
    template= template.strip()
    md_file= md_file.strip()
    try:
        with open(md_file, 'r') as file:
            lex= Lexer(file)
            # for i in lex.tokenize():
            #     print(i)
            parser= Parser(lex.tokenize())
            renderer= parser.parse()
            html_content= renderer.to_html()
            # print(html_content)
    except FileNotFoundError:
        print(f"Error: The file '{md_file}' was not found. Please check the file path.")
        return None
    except OSError as e:
        print(f"Error: An OS error occurred while trying to open the file '{md_file}'.\nDetails: {e}")
        return None
    
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    template_path = os.path.join(os.path.dirname(__file__), 'templates', f'{template}.html')
    title = os.path.splitext(os.path.basename(md_file))[0]

    with open(template_path, 'r') as template_file:
        template_content= template_file.read()
    html_content= template_content.replace('{{data}}', html_content)
    html_content= html_content.replace('{{title}}', title)

    if output_file:
        output_file= output_file.strip()
        output_file_path = os.path.abspath(os.path.join(os.path.dirname(md_file), output_file))
        try:
            with open(output_file_path, 'w') as file:
                file.write(html_content)
        except OSError as e:
            print(f"Error: An OS error occurred while trying to write to the file '{output_file}'.\nDetails: {e}")
            return None
        print(f"HTML is generated at: {output_file}")
    else:
        return html_content


def to_tokens(md_file, output_file=None):
    md_file= md_file.strip()
    try:
        with open(md_file, 'r') as file:
            lex= Lexer(file)
            tokens= list(lex.tokenize())
    except FileNotFoundError:
        print(f"Error: The file '{md_file}' was not found. Please check the file path.")
        return None
    except OSError as e:
        print(f"Error: An OS error occurred while trying to open the file '{md_file}'.\nDetails: {e}")
        return None


    if output_file:
        output_file= output_file.strip()
        output_file_path = os.path.abspath(os.path.join(os.path.dirname(md_file), output_file))
        try:
            with open(output_file_path, 'w') as file:
                for tok in tokens:
                    file.write(str(tok) + "\n")
        except OSError as e:
            print(f"Error: An OS error occurred while trying to write to the file '{output_file}'.\nDetails: {e}")
            return None
        print(f"Tokens are generated at: {output_file}")
    else:
        return tokens



# filepathref= '/home/deepak/projects/yamper/example.md'

# html= to_tokens(filepathref, ' hello.html   ')
# print(html)