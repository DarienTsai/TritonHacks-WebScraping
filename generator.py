import sys
import math

# HTML Template. We fill the "{}" areas with actual content
HTML_FORMAT = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Price Comparison App</title>
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="./css_template.css">
   
  </head>  
  <body>
     <!--Title-->
    <h1 id="title">Statistics Comparison of {}</h1>
    
    <!--Board-->
    <div id="board">
      {}
    </div>
  </body>
</html>
"""

# Single Picture
ITEM_FORMAT = """
      <div class="slide">
        <!--location-->
        <h2>{location}</h2>
        <!--average rating-->
        <div><strong>Average rating:</strong>{rating}</div>
        <!--average price-->
        <div><strong>Average price:</strong>{price}</div>
        <!--Image-->
        <div class="imageCollage">
          {images}
        </div>
      </div>
"""
#  Calculate the type of emoji to display for current rating.
def calculate_moons(score, multiplier):
  # 🌑🌘🌓🌖🌕
  MOON_EMOJIS = ["&#x1F311","&#x1F318", "&#x1F317", "&#x1F316", "&#x1F315"]
  score = math.floor(float(score) * multiplier + 0.25) / multiplier
  score_copy = score
  
  display_string = ""
  for i in range (5):
    if(score> 1):
      display_string += MOON_EMOJIS[4]
      score -= 1
    else:
      display_string += MOON_EMOJIS[int(score*4)]
      score = 0

  return (display_string, score_copy)

# Write findings to out.html
def generate(item, dataList):
    middle = ""
    for data in dataList:

        # Calculate average rating & price, display with moon emoji
        rating, rating_int = calculate_moons(data['rating'], 4)
        price, price_int = calculate_moons(data['price'], 5)

        # Insert image links and append to image string
        images_string = ""
        for url in data['images']:
            images_string += """<img src="{}">""".format(url) + "\n"

        middle += ITEM_FORMAT.format(location=data['location'], 
                  rating = rating + "(" + str(rating_int) + ")",
                  price  = price + "(" + str(price_int) + ")",
                  images = images_string)

    with open("out.html", "w+") as new_file:
        new_file.write(HTML_FORMAT.format(item, middle))