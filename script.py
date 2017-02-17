#!/usr/bin/python3

import os, time

def clear():
    os.system("clear")
def sleep(t=1):
    time.sleep(t)


clear()

input("...")

os.system("firefox https://www.youtube.com/embed/t4HuZiUXBMA?rel=0?autoplay=1")


#os.system("okular meme2.png")
#os.system("okular meme3_but_also_how_i_really_feel_about_steaks.notAJoke.png")

clear()

input("PNG Parts:\n\tHeader\n\tIHDR Chunk: width, height, bitdepth, colortype, etc\n\tPLTE Chunk: Color Palette\n\tIDAT Chunk: Actual Image Data, file may contain multiple IDAT Chunks\n\tIEND Chunk: End Of Image")

print("\n\nPNG Header: ", end="")
print(b'\x89PNG\r\n\x1a\n')
print("\n\nPNG Header Block and IHDR Chunk: ", end="")
print(b'\x00\x00\x00\rIHDR\x00\x00\x02\x80\x00\x00\x01\x90\x08\x02\x00\x00\x01\xc6\x96v\xe4\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\tvpAg\x00\x00\x02\x80\x00\x00\x01\x90\x00\xec~X\xd5')
