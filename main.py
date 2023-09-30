from igzgModule import *
from urllib.request import urlretrieve

class UrlMaker:
    def __init__(self):
        self.targetUrl = ""
        self.srcUrl = "" 
        self.driver = getDriver()
        self.elemSelector = "div.media img"
        self.javascriptCode = f"return document.querySelector('{self.elemSelector}')['src'];"

    def setTargetUrl(self,targetUrl):
        self.targetUrl = targetUrl
        return self

    def getSrcUrl(self):
        for retry in range(5):
            try:
                self.driver.get(self.targetUrl)
                waitElement(self.driver,self.elemSelector)
                self.driver.execute_script("window.stop();")
                srcUrl = self.driver.execute_script(self.javascriptCode)
            except Exception as e: print(e)
            else: break

        self.srcUrl = srcUrl
        return srcUrl

class ImageDownloader:
    def __init__(self):
        self.srcUrl = ""
        self.filePath = "./"

    def downloadImage(self,fileName:str='test.png'):
        urlretrieve(self.srcUrl, self.filePath + fileName)

    def setSrcUrl(self,srcUrl): 
        self.srcUrl = srcUrl
        return self
    
    def setFilePath(self,filePath): 
        self.filePath = "./" + filePath + '/'
        mkdirExistOk(self.filePath)
        return self    

class InputReader:
    def __init__(self):
        [self.imageType] = getConfig(["imageType"])
        self.inputList = getFileInput('input.txt')

        self.charDict = { x.split('\t')[0].strip().replace(' ','_'):[ y.strip().replace(': ','_') for y in x.split('\t')[1:]] for x in getFileInput("charDict") if x[0] != '#'}
        self.targetList = [self.charDict[x] for x in self.inputList if x in self.charDict.keys()]
        
        self.postfixType = ["_Icon", "_Item", "_Wish"]
        self.prefixType  = ["Namecard_Background_"]
        self.baseUrl = "https://genshin-impact.fandom.com/wiki/{}/Gallery?file={}{}.png"

    def getTargetUrl(self,inputLine):
        target = self.charDict[inputLine]

        if self.imageType in self.postfixType:
            targetUrl = self.baseUrl.format(target[0], target[0], inputReader.imageType)
        elif self.imageType in self.prefixType:
            targetUrl = self.baseUrl.format(target[0], self.imageType, target[1])
        else: targetUrl = ''

        return targetUrl
    
    def getFileName(self,inputLine):
        if self.imageType in self.postfixType:
            fileName = self.charDict[inputLine][0] + self.imageType + ".png"
        elif self.imageType in self.prefixType:
            fileName = self.imageType + self.charDict[inputLine][1] + ".png"
        else: fileName = ''

        return fileName

if __name__ == "__main__":
    inputReader     = InputReader()
    urlMaker        = UrlMaker()
    imageDownloader = ImageDownloader().setFilePath(inputReader.imageType)
    totalCnt        = len(inputReader.inputList)

    for idx,inputLine in enumerate(inputReader.inputList,start=1):
        strongPrint(f" [{idx}/{totalCnt}] {inputLine} ")

        targetUrl = inputReader.getTargetUrl(inputLine)
        fileName  = inputReader.getFileName(inputLine)
        srcUrl    = urlMaker.setTargetUrl(targetUrl).getSrcUrl()

        imageDownloader.setSrcUrl(srcUrl).downloadImage(fileName)
