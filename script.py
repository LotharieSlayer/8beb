import os
# maxVal equals to number of Oizo's 8BEB NFTs +1 (there is currently 33 NFTs)
maxVal = 34

def dwl():
    for i in range(1,maxVal):
        os.system("curl \"https://assets.foundation.app/0xD62C83ed5524802a6e5e7cA2b350E404a6a204a0/"+str(i)+"/nft.mp4\" --output "+str(i)+".mp4")
    os.system("FOR /F \"tokens=*\" %G IN ('dir /b *.mp4') DO ffmpeg -y -i \"%G\" \"%~nG.wav\"")
def concat():
    f = open("concat.txt", "w+")
    for i in range(1,maxVal):
        f.write("file 'unfinished.wav'\n")
        if(i<10):
            f.write("file 'num/"+str(i)+".wav'\n")
        else:
            f.write("file 'num/"+str(str(i)[0]+"0")+".wav'\n")
            if(str(i)[1] != "0"):
                f.write("file 'num/"+str(str(i)[1])+".wav'\n")
        f.write("file '"+str(i)+".wav'\n")

    f.close()
    os.system("ffmpeg -y -f concat -safe 0 -i concat.txt -c copy unfinished1.wav")

dwl()
concat()
