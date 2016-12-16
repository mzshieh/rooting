## 第一講

### 發問用[聊天室](https://chatroom-mzshieh.c9users.io/)

### 隨便聊聊 Python

+   指令式程式設計
    +   一連串的指令
+   Python是啥?
    +   程式語言
        +   學 Python 2 還是 3?
    +   有直譯器
        +   寫完程式就可以執行，不用等。
    +   有互動式
        +   可以寫一行跑一行
    +   官方有附贈除錯器
        +   簡單堪用免記指令
    +   被許多人視為最適合初學者的程式語言
        +   不過我比較喜歡先教 Scratch
+   寫程式不需要懂太多數學
    +   多數場合用不到比四則運算更困難的數學
    +   但數學好是有用的
+   寫程式需要一定的創造力
+   下載與安裝 Python
    +   [官網](https://www.python.org/)
    +   Download Python 3
    +   Optional task: install python to your own computer
        +   All computers in the classroom are ready for use. 
        +   Installing packages: [see this](../install.md) 
+   The Interactive Shell
    +   Run `python`
    +   Run IDLE
    +   Has `>>>`
+   How to Find Help
    +   Search engine
    +   Stackoverflow
+   Asking Smart Programming Questions
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

### Python Basics

+   Expression
    +   Operands and operators
+   ERRORS ARE OKAY!
+   Arithmetic operators
    +   `+`
    +   `-`
    +   `*`
    +   `**`
    +   `/`
    +   `//`
    +   `%`
    +   `()`
+   [Precedence](https://automatetheboringstuff.com/chapter1/#calibre_link-101)
    +   `()` > `**` > `*` = `/` = `//` = `%` > `+` = `-`
    +   Special case: Right `**` > Left `**`
+   (Some) Data types
    +   Integer
    +   Floating-point number
    +   String
        +   Addition? No, it's concatenation.
        +   Multiplication? No, it's replication.
+   Storing Values in Variables
    +   Assignment
    +   Variable name
+   The first program
    +   Comments
        +   Starting with `#`
        +   Interpreter will ignore the comments
+   (Some) Functions
    +   A sequence of instructions
        +   A mini-program in a program
    +   `print()`
        +   Display the value between `(` and `)`
        +   Almost the only thing you can do in the first programming course.
    +   `input()`
        +   Read a string from the interactive shell.
    +   `len()`
        +   Calculate the length of a `string`
    +   `str()`
        +   Convert things into `string`
    +   `int()`
        +   Convert things into `int`
    +   `float()`
        +   Convert things into `float`
    +   `eval()`
        +   Try `eval(input())`

### `pyautogui`

+   The computers mainly receive inputs from human via the mouse and the keyboard.
    +   If your program controls the mouse and the keyboard, then it can do a lot of things (just like the human beings).

+   Installation
    +   `pip install pyautogui`
        +   You might have trouble to install this package on your own computer.
        +   Report the problem to the teaching assistants if you cannot handle it.

+   Mouse
    +   Get the size of the screen
        +   `width, height = pyautogui.size()`
    +   Get the position of the mouse
        +   `x, y = pyautogui.position()`
    +   The coordinate system
        +   Top-left: (1,1)
        +   Bottom-right: `pyautogui.size()`
    +   Move
        +   To: `pyautogui.moveTo(x, y, duration)`
            +   You may ignore `duration`
        +   Relative: `pyautogui.moveRel(x, y, duration)`
    +   Click
        +   `pyautogui.click(x, y)`
        +   `pyautogui.rightClick(x, y)`
        +   `pyautogui.doubleClick(x, y)`
    +   Drag
        +   To: `pyautogui.dragTo(x, y, duration)`
        +   Relative: `pyautogui.dragRel(x, y, duration)`
    +   Scroll
        +   `pyautogui.scroll(y)`

+   Keyboard
    +   Type
        +   `pyautogui.typewrite(text,delay)`
    +   Press
        +   `pyautogui.press(key)`
        +   [Key table](https://automatetheboringstuff.com/chapter18/#calibre_link-36)
    +   Hot key
        +   `pyautogui.hotkey(key1, key2, ..., keys)`
        +   Example: `pyautogui.hotkey('ctrl', 'c')`

+   Try `gui = pyautogui` then `gui.moveTo(1,1)`

### Task 1

+   Draw a triangle
    +   Green
    +   Filled
+   Draw a rectangle
    +   Brown
    +   Filled
+   Draw a christmass tree
    +   [Example](https://scratch.mit.edu/projects/115904117/)

### Task 2

+   Draw a circle
    +   Green
    +   Filled
+   Draw a tilt rectangle
    +   Brown
    +   Filled
+   Draw a tree
    +   [With branches](https://scratch.mit.edu/projects/115838437)

### Task 3

+   Do whatever you want via using `pyautogui`

+   [概觀](http://scratch-tw.strikingly.com/)
    +   動畫
        +   [Star Wars: The Force Awakens](https://scratch.mit.edu/projects/88652984/)
    +   故事
    +   遊戲
        +   [Coin Man](https://scratch.mit.edu/projects/24538490/) by [Flapjax404](https://scratch.mit.edu/users/Flapjax404/)
            +   你們可以兩分鐘內結束這遊戲嗎?
                +   老師小時候從玩遊戲作弊開始認真學電腦的
    +   藝術
    +   音樂
    +   模擬
        +   [彈性碰撞模型](https://scratch.mit.edu/projects/115525445/)
+   [Scratch 專案範本](https://scratch.mit.edu/studios/137903/)
    +   請試著分類，並找出自己比較有興趣的部份。
+   [網站](https://scratch.mit.edu/)
    +   開帳號
        +   請記得自己的帳號資訊
    +   上傳[帳號資訊](http://goo.gl/forms/c5xsUHOwSzXUESPZ2) to the instructor
+   [離線編輯器](https://scratch.mit.edu/scratch2download/)
    +   網路很方便
+   [Community Guidelines](https://scratch.mit.edu/community_guidelines)
+   設計日誌
    +   [Paper](http://bit.ly/designjournal-paper)
    +   [Blog](http://bit.ly/designjournal-blog)
+   [Scratch 卡片](https://scratch.mit.edu/info/cards)
    +   小抄(?)
    +   [中文版](https://drive.google.com/file/d/0BxGSeFLcAOM5T0NsWHJhYXRvYjQ/view)
        +   由 http://scratch-tw.strikingly.com/ 提供
+   [Scratch Surprise](https://scratch.mit.edu/studios/460431/)
    +   Sprite and Stage
    +   Blocks
        +   Command
        +   Event
        +   Value
        +   Predicate
        +   Flow control

### 回顧

+   [Slide (PDF)](snp_base.pdf)
+   [Slide (PowerPoint)](snp_base.pptx)

### Explore More

+   Scratch Studio
    +   加入專案到工作室
    +   對專案發表評論
+   Programmed to Dance
    +   [Video 1](http://www.vimeo.com/28612347)
    +   [Video 2](http://www.vimeo.com/28612585)
    +   [Video 3](http://www.vimeo.com/28612800)
    +   [Video 4](http://www.vimeo.com/28612970)
    +   作業: 用 Scratch 做個「會跳舞的教授貓」動畫
        +   可參考內建的教學
+   [Step-by-Step Studio](http://scratch.mit.edu/studios/475476)
+   [10 Blocks Studio](http://scratch.mit.edu/studios/475480)
    +   作業: 使用最多 10 塊積木做一個專案
    +   Note: 10 blocks studio 裡面有很多用超過時十個
+   My Studio
    +   之前開課的[工作室](https://scratch.mit.edu/studios/2923570/): https://scratch.mit.edu/studios/2923570/
    +   [Example 1](http://scratch.mit.edu/studios/211580)
    +   [Example 2](http://scratch.mit.edu/studios/138296)
    +   [Example 3](http://scratch.mit.edu/studios/138297)
    +   [Example 4](http://scratch.mit.edu/studios/138298)
+   [Debug it!](http://scratch.mit.edu/studios/475483)
    +   [Debug 1.1](https://scratch.mit.edu/projects/10437040/): 希望點下綠旗後，兩隻都在跳舞。可是現在的程式只有一隻會跳，該怎麼辦？
    +   [Debug 1.2](https://scratch.mit.edu/projects/10437249/): 希望按下綠旗後，貓咪能從舞台左邊走到右邊。可是按下去第一次會動，第二次以後就不會動了，該怎麼辦？
    +   [Debug 1.3](https://scratch.mit.edu/projects/10437366/): 希望空白鍵按下後貓咪能夠翻轉一圈。可是怎麼按貓咪就是不動，該怎麼辦？
    +   [Debug 1.4](https://scratch.mit.edu/projects/10437439/): 希望貓咪左右來回移動，可是他碰到邊緣後卻變得頭下腳上，該怎麼辦？
    +   [Debug 1.5](https://scratch.mit.edu/projects/10437476/): 希望按下去後貓咪能夠喵喵喵叫三聲：發出聲音跟顯示出對話框。可是他只叫一聲，而且對話泡泡顯示的方式不對。
+   [About me Studio](http://scratch.mit.edu/studios/475470)
    +   作業: 做個專案來自我介紹