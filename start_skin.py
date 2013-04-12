# -*- coding: utf-8 -*-
import StringIO
from PIL import Image
startimage = Image.open("steve.png")
startimage.convert("RGBA");
