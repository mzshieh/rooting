# Windows 7/8/10

請到: https://www.python.org/downloads/release/python-352/

移到最下面 選擇 Windows x86-64 executable installer 或者 Windows x86 executable installer 下載。

雙擊下載回來的檔案。

務必勾選 Add Ptyhon 3.5 to PATH。

安裝完成後，按下 <kbd> Win + R </kbd> 鍵入 `cmd` 按下 <kbd> Enter </kbd> 會出現俗稱的黑盒子。

在黑盒子內鍵入 pip 如有以下資訊代表成功了。


```
C:\Users\username> pip
Usage:
  pip <command> [options]

Commands:
...下略
```

如果之前已經自己裝過但是無法使用 pip 請解除安裝後照著以上步驟重新安裝。

# Linux Debian

開啟 terminal

```
apt-get install python3 python3-pip
```

權限如果不足記得使用 sudo

# Mac OS X

開啟 terminal

如果你已經安裝 Homebrew 可以跳過此步驟

安裝 Homebrew

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

安裝 Python3

```
brew install python3
```

# 安裝本課程需要使用的套件

如果你使用的作業系統是 Mac OS X 或者 Linux 請使用 pip3

首先升級 pip

```
Windows: python -m pip install --upgrade pip
Mac OS X or Linux: pip3 install --upgrade pip
```

開始安裝套件：

```
pip install send2trash
pip install requests
pip install beautifulsoup4
pip install selenium
pip install openpyxl
pip install PyPDF2
pip install imapclient
pip install twilio
pip install pillow
pip install pyautogui
```
