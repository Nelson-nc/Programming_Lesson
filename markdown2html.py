import markdown

markdown_filename = input("Please enter the markdown filename/path: ")

if markdown_filename != "":
    with open(markdown_filename, "r", encoding="utf-8") as f:
        text = f.read()

    html_file = markdown.markdown(text)
    html_name = markdown_filename[:-3] + ".html"

    with open(html_name, "w", encoding="utf-8") as f:
        f.write(html_file)
else:
    print("No file inputed")
