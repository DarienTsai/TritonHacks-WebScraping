import sys

# we have list of strings
# --> HTML file

HTML_FORMAT = """
<!DOCTYPE html>
<html>
<title>Temporaray</title>
<body>
{}
</body>
</html>
"""

# void generate(ArrayList<Integer> dataList)
def generate(dataList):
    middle = ""
    for data in dataList:
        middle += "<div>{}</div>\n".format(data)

    with open("out.html", "w") as new_file:
        new_file.write(HTML_FORMAT.format(middle))


generate(["1", "2", "3"])