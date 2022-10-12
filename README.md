# ascii-drawer

## steps
1. convert image to correct width
1. convert image to grayscale 
1. convert each gray scale pixel into ascii character with similar density




```bash

pip install -r requirements.txt

python ascii-script.py image_path invert(optional, default 0) new_width(optional, default 100)

python ascii-script.py corgi.jpeg 0 100

python ascii-script.py corgi.jpeg 1

```