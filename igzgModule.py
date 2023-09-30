

def mkdirExistOk(dirPath:str):
    import os
    os.makedirs(dirPath, exist_ok=True)

def getFileInput(filePath,toStr=False,failExit=True):
    import sys

    fileStr = ''
    fileList = []    
    try:
        if(toStr):
            fileStr = open(filePath, encoding='cp949').read()
        else: 
            fileList = [x.strip() for x in open(filePath, encoding='cp949').read().splitlines() if x != '']
    except UnicodeDecodeError:
        try:
            if(toStr):
                fileStr = open(filePath, encoding='utf-8').read()
            else: 
                fileList = [x.strip() for x in open(filePath, encoding='utf-8').read().splitlines() if x != '']
        except:
            print(f'{filePath} 파일 오류')
            if (failExit): sys.exit()
    except:
        print(f'{filePath} 파일 오류')
        if (failExit): sys.exit()

    if (toStr):
        return fileStr
    else:
        return fileList
    

def getConfig(configList:list, section:str='DEFAULT', configFilePath:str = 'config.txt'):
    import configparser
    import sys

    config = configparser.ConfigParser()
    try:
        config.read(configFilePath,encoding='cp949')
        resList = [ config['DEFAULT'][x] for x in configList]
    except UnicodeDecodeError:
        try:
            config.read(configFilePath,encoding='utf-8')
            resList = [ config['DEFAULT'][x] for x in configList]
        except:
            print(f'{configFilePath} 파일 오류')
            sys.exit()
    except:
        print(f'{configFilePath} 파일 오류')
        sys.exit()
    return resList

def waitElement(driver,selector:str):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

def getDriver():
    from selenium import webdriver

    options = webdriver.ChromeOptions()
    options.to_capabilities()['pageLoadStrategy'] = 'none'
    options.add_argument('user-agent==Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36')
    options.add_argument('--window-position=0,10')
    options.add_argument("--headless")
    # options.add_argument('--blink-settings=imagesEnabled=false')
    return webdriver.Chrome('D:/chromedriver/chromedriver.exe',options=options)

def strongPrint(strToPrint:str):
    from colorama import Back, Style, init
    init()

    print(Back.GREEN + Style.BRIGHT + strToPrint + Style.RESET_ALL)

if __name__ == "__main__":
    strongPrint(" > igzgModule ")