import sys

# we have list of strings
# --> HTML file

HTML_FORMAT = """

<!DOCTYPE html>
<html>
<head>

  <title>Temporaray</title>
  <link type="text/css" rel="stylesheet" href="styles.css"/>

</head>

<body>

  <div id="display">
    {}
  </div>

</body>
</html>

"""

ITEM_FORMAT = """
<div class="result">
    <h1 class="loc">{place}</h1>

    <div class="rating">
        <h1>
            {rating}/5
        </h1>
        <p>Quality</p>
    </div>

    <div class="price">
        <h1>
            {price}/3
        </h1>
        <p>Expense</p>
    </div>
</div>
"""

# TODO: Create CSS file to properly format the columns

# void generate(ArrayList<Integer> dataList)
def generate(dataList):
    middle = ""
    for data in dataList:
        middle += "<div>{}</div>\n".format(data)

    with open("out.html", "w") as new_file:
        new_file.write(HTML_FORMAT.format(middle))


generate(["1", "2", "3"])