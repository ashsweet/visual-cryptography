from PIL import Image
import sys

infile1 = Image.open("out1.jpg")
infile2 = Image.open("out2.jpg")
outfile = Image.new('1', infile2.size)

for x in range(infile1.size[0]):
    for y in range(infile1.size[1]):
        outfile.putpixel((x, y), max(infile1.getpixel((x, y)), infile2.getpixel((x, y))))

outfile.show()
