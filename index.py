from IPython import get_ipython
from IPython.display import display, SVG
import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.youtube.com/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the svg file naming "myyoutube.svg" 
url.svg("myyoutube.svg", scale = 8)

# Display the generated QR code
display(SVG('myyoutube.svg'))
