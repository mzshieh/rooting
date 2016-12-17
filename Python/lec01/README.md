## 第一講

### 發問用[聊天室](https://chatroom-mzshieh.c9users.io/)

### [免費入門書](http://automatetheboringstuff.com/)

### 隨便聊聊 Python

+   指令式程式設計
    +   一連串的指令
+   Python是啥?
    +   程式語言
        +   學 Python 2 還是 3?
    +   有直譯器
        +   寫完程式就可以執行，不用等。
    +   有互動式界面
        +   可以寫一行跑一行
    +   官方有附贈除錯器
        +   簡單堪用免記指令
    +   被許多人視為最適合初學者的程式語言
        +   不過我比較喜歡先教 Scratch
+   寫程式不需要懂太多數學
    +   多數場合用不到比四則運算更困難的數學
    +   但數學好是有用的
+   寫程式需要一定的創造力
+   出錯很正常
    +   不要緊張
+   下載與安裝 Python
    +   [官網](https://www.python.org/)
    +   Download Python 3
    +   [安裝套件](../install.md) 
+   互動世界面(Interactive Shell)
    +   執行 `python`
    +   執行 IDLE
    +   有 `>>>` 代表輸入給 shell，沒有的時候代表輸入給程式。
+   如何求助
    +   搜尋引擎
    +   Stackoverflow
+   問問題的方式
    +   解釋你想要做甚麼，不只是說你做了甚麼。能幫你的人才知道你有沒有走錯路。
    +   明確的指出甚麼地方有問題。比如說一開始就出錯，或是做了甚麼才出錯。
    +   將完整的錯誤訊息以及程式碼貼出。
        +   利用 [pastebin](http://pastebin.com/) 或 [gist](http://gist.github.com/) 來貼
    +   描述一下你已經做過哪些嘗試。代表你已經花了點力氣研究到底是怎麼一回事。
        +   這是有點關鍵。
    +   列出使用的 Python 版本以及開發環境。
        +   Python 2 跟 Python 3 有相當差異，有很多套件可能因為平台而有所不同。
    +   如果是改完部分 code 之後才產生的問題，請明確描述改了甚麼。
    +   給出可以重現問題的情境，前提盡量清楚。

### Python 基礎

+   算式
    +   運算子、運算元
+   運算
    +   `+`
    +   `-`
    +   `*`
    +   `**`
    +   `/`
    +   `//`
    +   `%`
    +   `()`
+   [優先順序](https://automatetheboringstuff.com/chapter1/#calibre_link-101)
    +   `()` > `**` > `*` = `/` = `//` = `%` > `+` = `-`
    +   大部分左邊的比較優先
    +   特例：指數運算 `**` 右邊的先
+   基礎的資料型態
    +   `int` 整數
    +   `float` 浮點數 (二進位科學記號表示法)
    +   `str` 字串
        +   `+` 是串接
        +   `*` 是重複
+   變數：儲存資料的箱子
    +   賦值 (Assignment)
    +   變數名稱限制 Variable name
+   函數 (Function)
    +   可以另外翻譯為「功能」
        +   通常也是一連串的指令
            +   小型程式
        +   會有執行的結果
    +   `print()`
        +   把資料印出來
        +   在很多程式設計課，這差不多就是你一開始能做的所有事情。
    +   `input()`
        +   從輸入讀個一行進來，型態是`str`(字串)。
    +   `len()`
        +   算個長度。現在能算的是`str`(字串)的長度
    +   `str()`
        +   把資料換成`str`(字串)
    +   `int()`
        +   把資料換成`int`(整數)
        +   無法轉換的會發生錯誤
    +   `float()`
        +   把資料換成`float`(浮點數)
        +   無法轉換的會發生錯誤
    +   `eval()`
        +   把一個`str`當作算式計算
        +   `eval(input())`

### 第一個程式

+   就一連串的指令
    +   一個指令也算
        +   `print('hello, world')`
+   要記得存檔
    +   存成 `.py`
+   執行
    +   用 IDLE 
    +   用終端機(?)
+   註解
    +   用 `#` 開頭的就是
    +   直譯器會當作沒看見
        +   因為是寫給人看的

### `pyautogui` 套件

+   現代人大多透過鍵盤與滑鼠操作電腦
    +   你能夠用程式操作鍵盤與滑鼠，那就能夠做許多人類能做的事情。
        +   通常都是你不太想自己做的無聊事。

+   安裝
    +   `pip install pyautogui`
        +   通常安裝套件是學 Python 最大的門檻
        +   每個人的機器都可能碰上不太一樣的狀況
        +   有問題的同學，可以帶電腦來
            +   不保證帶來就裝的好 orz

+   先`import pyautogui`

+   滑鼠相關
    +   取得畫面大小
        +   `width, height = pyautogui.size()`
    +   取得滑鼠座標
        +   `x, y = pyautogui.position()`
    +   The coordinate system
        +   上小下大
        +   左小右大
    +   移動
        +   絕對座標: `pyautogui.moveTo(x, y, duration)`
        +   相對座標: `pyautogui.moveRel(x, y, duration)`
        +   可省略 `duration`
    +   點擊
        +   `pyautogui.click()`
        +   `pyautogui.click(x, y)`
        +   `pyautogui.rightClick(x, y)`
        +   `pyautogui.doubleClick(x, y)`
    +   拖曳
        +   絕對座標: `pyautogui.dragTo(x, y, duration)`
        +   相對座標: `pyautogui.dragRel(x, y, duration)`
    +   滾輪
        +   `pyautogui.scroll(y)`

+   鍵盤相關
    +   打字
        +   `pyautogui.typewrite(text,delay)`
    +   按
        +   `pyautogui.press(key)`
        +   [Key table](https://automatetheboringstuff.com/chapter18/#calibre_link-36)
    +   熱鍵
        +   `pyautogui.hotkey(key1, key2, ..., keys)`
        +   範例: `pyautogui.hotkey('ctrl', 'c')`

### Task 1

+   畫個填滿顏色的三角形
+   畫個填滿棕色的矩形
+   畫棵聖誕樹
    +   [範例](https://scratch.mit.edu/projects/115904117/)

### Task 2

+   畫填滿綠色的圓
+   畫填滿棕色的傾斜長條
+   畫棵樹
    +   [範例](https://scratch.mit.edu/projects/115838437)

### Task 3

+   用 `pyautogui` 自由創作

### 流程控制

+   [流程圖](https://automatetheboringstuff.com/chapter2/#calibre_link-1903)
+   真假值 (Boolean Values)
    +   `True`
    +   `False`
    +   `true` 跟 `false` 是變數不是真假值
+   比較運算子
    +   `==`
        +   `float` 有精確度問題
    +   `!=`
    +   `<`
    +   `<=`
    +   `>`
    +   `>=`
    +   比較不同型態時
        +   `str` 與 `int`
        +   `int` 與 `float`
+   邏輯運算
    +   `and`
    +   `or`
    +   `not`
    +   優先順序: `not` > `and` > `or`

+   Conditions: 真假值運算式
+   替用真假值
    +   Truthy values
        +   非零的 `int`
        +   非零的 `float`
        +   非空的 `str`
    +   Falsey values
        +   `0`
        +   `0.0`
        +   `''`
    +   還有更多 truthy value 與 falsey value。先不討論。

### 選擇結構

+   Block of code
    +   要加 `:`
    +   縮排
        +   可用空白或是 tab
        +   建議用四個空白
            +   習俗，你不遵守會被討厭。
+   `if`
+   `else`
+   `elif`

### Task 4

`int()` is not ideal to convert `float` into `int`. Write a program that round a `float` into its closest integer.
+   Use `int()`, `input()` and `print()`
+   You may assume the input is always a valid `float`
+   If there are two closest integers, then output the even one.
    +   四捨、六入、五成雙
+   You might need to ask some questions in the [chatroom](https://chatroom-mzshieh.c9users.io)

### 重複結構

+   `while`
    +   `ctrl`+`C` to stop your (buggy) program
+   `for`
+   `range()`
    +   `range(n)`: `0`, `1`, ..., `n-1`
    +   `range(start,stop)`: `start`, `start+1`, ..., `stop-1`
        +   Math: `[start,stop)`
    +   `range(start,stop,step)`: `start`, `start+step`, ..., `start+k*step` where `k` is the maximum integer such that `start+k*step < stop`.
+   Nested loops
+   `break`
+   `continue`

### Task 5

+   Draw [Rokumonsen](https://www.google.com.tw/search?q=Rokumonsen)
+   Draw Ichimonsen (一文銭)
+   Draw Sanjurokumonsen (三十六文銭)

### Flow Control: Exception

+   It is complicated. We are not going to cover much about it.
    +   Official [tutorial](https://docs.python.org/3/tutorial/errors.html)
+   [Example code](lec08.py)

### Task 6

+   Ask user to input a 4-digit number such that
    +   Must be an integer.
        +  `'one two three four'` is not OK.
        +  `1234.0` is not OK.
        +  `1234` is OK.
    +   Any digit appears at most once
        +   `5566` is not OK.
    +   Leading zero is acceptable.
        +   `0123` is OK.
    +   User's input have four digits
        +   `123` is not OK.
+   Repeat until the user cooperates.

### 隨機亂數

+   `import random`
    +   `random.random()`
    +   `random.randint()`
