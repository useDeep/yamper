# yamper

yamper is a simple Markdown to HTML converter/compiler. It allows users to easily convert Markdown files to HTML, with options for different templates and token output.

## :star2: Features

### Available Features
- Headers
- Paragraphs
- Bold, Italic and strikethrough text
- Links
- Images
- Unordered lists
- Ordered lists
- Blockquotes
- Code blocks
- Inline code
- Horizontal rules
- GitHub emojis :wink:

### :construction: Features in Development
- Tables
- Alerts
- Footnotes
- Nested lists
- Nested quotes

## :package: Installation

You can install yamper using pip:

```bash
pip install yamper
```

## :computer: Usage

### Command Line Interface

yamper provides a command-line interface for easy conversion of Markdown files to HTML.

Basic usage:

```bash
yamper path/to/your/markdown_file.md
```

Options:

- `--out`: Specify the output file name
- `-t, --template`: Choose a template (options: "standard-light", "standard-dark", "plain")
- `--tokens`: Output tokens instead of HTML

Examples:

```bash
# Convert to HTML with default template
yamper ../path/input.md --out output.html

# Convert to HTML with dark template
yamper ../path/input.md --out output.html -t standard-dark

# Output tokens
yamper ../path/input.md --tokens --out tokens.txt
```

### :wrench: Using yamper in Your Python Projects

You can also use yamper in your Python projects by importing its functions:

```python
from yamper import to_html, to_tokens

# Convert Markdown to HTML and output to a new file
to_html('path/to/your/markdown_file.md', 'output.html', 'standard-dark')
or 
# Directly print the HTML content
html_content= to_html('path/to/your/markdown_file.md')
print(html_content)

# Get tokens from Markdown and output to a new file
tokens = to_tokens('path/to/your/markdown_file.md', 'tokens.txt')
or
# Directly print the tokens
to_tokens('path/to/your/markdown_file.md', 'tokens.txt')
print(tokens)
```

## :art: Templates

yamper currently offers three templates:

1. `standard-light` (default): A light theme with built-in styles and code highlighting using [Prism.js](https://prismjs.com/)
2. `standard-dark`: A dark theme with built-in styles and code highlighting using [Prism.js](https://prismjs.com/)
3. `plain`: A basic HTML output without any additional styling or code highlighting

## :gear: API Reference

### `to_html(md_file, output_file=None, template="standard-light")`

Converts a Markdown file to HTML.

- `md_file`: Path to the input Markdown file
- `output_file`: (Optional) Path to the output HTML file
- `template`: (Optional) Template to use for HTML output

Returns the HTML content as a string if `output_file` is not specified.

### `to_tokens(md_file, output_file=None)`

Generates tokens from a Markdown file.

- `md_file`: Path to the input Markdown file
- `output_file`: (Optional) Path to the output token file

Returns the list of tokens if `output_file` is not specified.

## :warning: Disclaimer

The HTML output generated by yamper is **not automatically sanitized**. This means that any potentially harmful or malicious content within the Markdown input will be directly reflected in the resulting HTML file. Users should be cautious when processing untrusted or user-generated content.

## :bulb: Recommendation

If you intend to display the generated HTML on a website or share it publicly, it is strongly advised to manually review and sanitize the content, or use a dedicated HTML sanitizer to mitigate potential security vulnerabilities.


## :handshake: Contributing

Contributions to yamper are welcome! Please feel free to submit a Pull Request.

## :scroll: License

This project is licensed under the GPL-3.0 license.