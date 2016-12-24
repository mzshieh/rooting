## 第二講

### 發問用[聊天室](https://chatroom-mzshieh.c9users.io/)

### APCS

+   [Cloud 9](https://c9.io/)
    +   Terminal
        +   `touch`
        +   `ls`
        +   `cat`
        +   `python3`
            +   ctrl+d
        +   用 `<` 可以將檔案轉變為程式的輸入。

### [免費入門書](http://automatetheboringstuff.com/)

+   [中文版](https://www.tenlong.com.tw/items/9864762729?item_id=1026244)

### Python 基礎

+   算式
    +   運算子、運算元
+   運算
    +   `+`、`-`、`*`、`**`、`/`、`//`、`%`、`()`
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
    +   變數名稱[限制](https://automatetheboringstuff.com/chapter1/#calibre_link-107)
+   `list`
    +   可以視為一些有編號的變數
    +   `a_list=[0,1,2,3,4]`
        +   `a_list[0]`為第一個
        +   `a_list[1]`為第二個
        +   `a_list[-1]`為最後一個
        +   `a_list[-2]`為倒數第二個
+   函數 (Function)
    +   可以另外翻譯為「功能」
        +   通常也是一連串的指令
            +   小型程式
        +   會有執行的結果
    +   `open()`
        +   開檔案
        +   `out = open('filename','wt')`
    +   `print()`
        +   把資料印出來
        +   在很多程式設計課，這差不多就是你一開始能做的所有事情。
        +   印到檔案
            +   `print('hi',file=out)`
        +   列印 `list`
            +   `print(*some_list)`
        +   間隔字串
            +   `print(123,456,sep=',')`
            +   內定是`' '`
        +   換行字串
            +   `print(123,456,end=' haha\n')`
            +   內定是`'\n'` (單一個換行)
    +   `input()`
        +   從輸入讀個一行進來，型態是`str`(字串)。
        +   `input().strip().split()`
            +   去除前後的空白字元之後，依據中間的空白切斷，成為一個`list`。
            +   `split(',')`可用`','`切開
            +   `[int(x) for x in input().strip().split()]`
                +   將整行以空白隔開的整數，讀入成一個`list`
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

### 指令式程式

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

### 流程控制

+   [流程圖](https://automatetheboringstuff.com/chapter2/#calibre_link-1903)
+   真假值 (Boolean Values)
    +   `True`、`False`
+   比較運算子
    +   `==`、`!=`
        +   `float` 有精確度問題，跟科學記號一樣。
    +   `<`、`<=`、`>`、`>=`
        +   比較不同型態時
            +   `str` 與 `int` 不能比較
            +   `int` 與 `float` 可以比較
        +   `str` 用字典順序
+   邏輯運算
    +   `and`、`or`、`not`
    +   優先順序: `not` > `and` > `or`

+   Conditions: 真假值運算式
+   替用真假值
    +   Truthy values
        +   非零的 `int`、非零的 `float`、非空的 `str`
    +   Falsey values
        +   `0`、`0.0`、`''`

### 選擇結構

+   Block of code
    +   要加 `:`
    +   縮排
        +   可用空白或是 tab
        +   建議用四個空白
            +   習俗，你不遵守會被討厭。
+   `if`
    +   `if` condition `:`
+   `else`
    +   `else:`
    +   不接 condition
+   `elif`
    +   `elif` condition `:`
+   常見用法：
```
if x<0:
    print('x is negative.')
elif x>0:
    print('x is positive.')
else:
    print('x is zero')
```

### Take Home

請寫一支程式判斷一個年份是否是閏年。閏年的相關定義可以參考[這裡](https://zh.wikipedia.org/wiki/閏年)。

### 重複結構

+   `while`
    +   `ctrl`+`C` 可中斷程式 (機制：製造紅字)
+   `for`
+   `range()`
    +   `range(n)`: `0`, `1`, ..., `n-1`
    +   `range(start,stop)`: `start`, `start+1`, ..., `stop-1`
        +   Math: `[start,stop)`
    +   `range(start,stop,step)`: 從 `start` 起每次加 `step` 直到等於或超過 `stop` 為止
+   巢狀結構 (Nested loops)
+   `break`
+   `continue`

### Task 5

+   畫 [Rokumonsen](https://www.google.com.tw/search?q=Rokumonsen)
+   畫 Ichimonsen (一文銭)
+   畫 Sanjurokumonsen (三十六文銭)

### 例外處理

+   我們先碰最簡單的
    +   官方[教學](https://docs.python.org/3/tutorial/errors.html)
+   [範例程式碼](lec01-ex.py)

### Task 6

+   請使用者輸入一個二位整數
    +   只包含阿拉伯數字
        +   不接受 `'one two three four'`
        +   不接受 `12.0`
        +   接受 `12`
    +   兩位數不可重複
        +   不接受`55`
    +   開頭是`0`可接受
        +   可接受 `01`
        +   不接受 `0`
    +   使用者必須輸入兩位
        +   不接受 `3`
+   直到使用者輸入合格資料才結束程式

### 隨機亂數

+   `import random`
    +   `random.random()`
    +   `random.randint()`

### Debugger

+   Breakpoint: 中段點 
    +   請記得打開 `source`
+   Go: 衝啊
+   Step (Into)
+   (Step) Over
+   (Step) Out
+   Quit: 結束

### Task 7

+   Guess a secret number from `0` to `9`
+   `5` chances

### 自訂函數/功能(Function)

+   簡化流程
+   重複運用
+   `def your_function()`
+   `return`
    +   `return` 或是 block 結束時跳回
    +   `None`: 沒 `return` 或是只有 `return` 時回傳的資料
+   `def your_function_with_parameter(parameter)`
    +   `parameter`: 參數
+   `def your_function_with_parameters(parameter1, parameter2)`
    +   參數可以傳好幾個
+   還可以有不定數量的參數
    +   更有彈性
    +   像是 `print()`
    +   以後再教如何宣告
+   有名稱的參數 (Keyword argument)
    +   `print(some_str, end='')`
    +   `print(some_str_1, some_str_2, sep=',')`
    +   以後再教如何宣告
+   Scope
    +   變數都是透過 assignment 定義
    +   全域變數 Global variable
        +   在 function 外定義的
        +   `global`
            +   function 內要寫全域變數時，要先加
            +   `global some_var`
            +   只是讀取的時候可不加
    +   區域變數 Local variable
        +   不是全域的就是啦
        +   只能在區域存取
    +   原則
        +   全域看不到區域
        +   你家看不到我家
        +   同名時區域優先

### Task 8

+   最大公因數