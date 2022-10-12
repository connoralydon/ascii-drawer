# ascii-drawer

### example:

original image:

<img src="corgi.jpeg" alt="corgi in field, smiling" width="200"/>

corresponding ascii art:

[corgi.txt](corgi.txt)

```bash

pip install -r requirements.txt

python ascii-script.py image_path invert(optional, default 0) new_width(optional, default 100)

python ascii-script.py corgi.jpeg 0 100

python ascii-script.py corgi.jpeg 1

python ascii-script.py https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12213218/German-Shepherd-on-White-00.jpg 
# to grab web links to images

```

### steps
1. convert image to correct width
1. convert image to grayscale 
1. convert each gray scale pixel into ascii character with similar density

[using this tutorial](https://www.youtube.com/watch?v=v_raWlX7tZY)
