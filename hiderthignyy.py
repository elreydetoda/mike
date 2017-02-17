#!/usr/bin/python3
#Author: WonkeyMonkey

#DON'T JUDGE MY CODE I DID THIS IN AN HOUR

import sys, binascii
png_header = b'\x89PNG\r\n\x1a\n'


#TODO: support multiple IDAT blocks

try:
    filename = sys.argv[1]
except IndexError:
    filename = input("Filename: ")
    
with open(filename, "rb") as file:
    if file.read(8) == png_header:
        print("\nValid PNG Header Found")

        imageData = [png_header]
        chunkData = {}
        totalIDATSize = 0
        firstIDATLoc = -1

        print("Loading Image Data...")
        while True:
            buffer = file.read(4)
            if buffer==b'':
                print("Warning! EOF Reached Before IEND")
                break
            
            size = int(binascii.hexlify(buffer), 16)
            ty = file.read(4)
            data = file.read(size)
            crc = file.read(4)

            imageData.append(buffer)
            imageData.append(ty)
            imageData.append(data)
            imageData.append(crc)

            ty = ty.decode()
            if chunkData.get(ty, None)==None:
                chunkData[ty]=1
            else:
                chunkData[ty]+=1

            if ty=="IDAT":
                totalIDATSize+=size
                if firstIDATLoc == -1:
                    firstIDATLoc = len(imageData)-2

            if ty=="IEND":
                break


        for key in chunkData.keys():
            print("%s Chunks: %s" % (key, chunkData[key]))
        print("Total IDAT Size: %s" % (totalIDATSize))

        if len(sys.argv) > 2:
            if sys.argv[2].lower() == "w":


                message = ""
                while (len(message) <= 0) or (len(message) > 126):
                    message = input("Message: ")

                
                idat = imageData[firstIDATLoc]
                idat[:len(idat)-len(message)]
                imageData[firstIDATLoc] = idat+message.encode()

                with open("outputMeme.png", 'wb') as outputfile:
                    for chunks in imageData:
                        outputfile.write(chunks)

        
    else:
        print("\nInvalid PNG Header Found! Fatal!")
        exit(0)
    

