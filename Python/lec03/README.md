## 第三講

### 發問用[聊天室](https://chatroom-mzshieh.c9users.io/)

### [免費Python入門網路書](http://automatetheboringstuff.com/)

+   [紙本中文版](https://www.tenlong.com.tw/items/9864762729?item_id=1026244)

### APCS

+   [Cloud 9](https://c9.io/)
    +   Terminal
        +   `touch`
            +   製造空白檔案
            +   `touch some.py`
            +   `touch input.txt`
        +   `ls`
            +   確認目錄下檔案
        +   `cat`
            +   確認檔案內容
            +   `cat some.py`
            +   `cat input.txt`
        +   `python3`
            +   直接執行是 shell ，可按 ctrl+d 結束
            +   `python3 some.py` 執行 `some.py` 程式碼
            +   用 `<` 可以將檔案轉變為程式的輸入。
                +   `python3 some.py < input.txt`

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

+   用文字介面畫聖誕樹

### 例外處理

+   我們先碰最簡單的
    +   官方[教學](https://docs.python.org/3/tutorial/errors.html)
+   [範例程式碼](lec03-ex.py)

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

### `list`, `tuple`

+   用`type()`查型態
+   清單 `list`
    +   空清單: `[]`
    +   不見得要放同樣型態的資料
        +   `[12, 3.4, None, True, 'string', print]`
    +   存取`x`從`0`數起的的第`i`筆資料: `x[i]`
        +   `i`稱作索引值(index)
        +   試試看 `[123,456][1]`
        +   試試看 `[12, 3.4, None, True, 'string', print][5]('hello world')`
        +   試試看 `[123,456][1.0]`
    +   清單的資料可修改 (mutable)
+   多元組 `tuple`
    +   空: `()`
    +   單元素 `tuple`: `(element,)`
        +   試試看 `type(('str'))`
        +   試試看`type(('str',)`
    +   `(12, 3.4, None, True, 'string', print)`
    +   多元組的資料不可修改 (immutable)
+   形態轉換：`list()`、`tuple()`
    +   `list(('a','b','c'))`
    +   `tuple(['d','e','f'])`
    +   `list('hello')`
    +   `tuple('hello')`
+   `in`
+   `not in`
+   Auto boxing & auto unboxing
    +   [code](lec03-1.py)
+   負索引值(Negative index): `some_list[-1]`
+   片段(Slice): 試試看`print([0,1,2,3,4][1:3])`
    +   Inclusive, exclusive
+   串接 `+`
+   重複 `*`
+   `index()`
    +   `print([0,1,2,0].index(0))`
+   `insert(pos,val)`: 將 `val` 插入到第 `pos` 個位置
    +   令 `a = [0,1,2]`。此時執行 `a.insert(1,3)` 會?
+   `append(val)`
+   `pop()`：移除最後一筆資料並且取得該資料的值
+   `pop(pos)`: 移除第`pos`筆資料並且取得該資料的值。
+   `remove(val)`: 移除第一個值為 `val` 的資料。
    +   令 `a = [1,0,0,1]`。
        +   執行 `a.remove(1)` 會如何？
        +   執行 `a.remove(2)` 會如何？
+   `sort()`：將 `list` 內的資料由小到大排好。

### `str`

+   跳脫字元(Escape Characters): [Table](https://automatetheboringstuff.com/chapter6/#calibre_link-40)
    +   `'\n'`
    +   `'\t'`
    +   `'\r'`
    +   `'\\'`
+   索引值:
    +   `print('123'[0])`
    +   `print('123'[-1])`
+   `index()`
    +   `print('123123123'.index('312'))`
+   片段：
    +   `print('abcde'[2:])`
    +   `print('abcde'[:2])`
    +   `print('abcde'[1:3])`
+   `in` 、 `not in`
    +   `print('abc' in 'zabcy')`
    +   `print('gg' not in 'zabcy')`
+   `upper()`
+   `lower()`
+   `isupper()`, `islower()`, `isdecimal()`, `isalpha()`, `isalnum()`
    +   `'123.0'.isdecimal()`
+   `join(list_str)`
    +   `', '.join([str(i) for i in range(10)])`
+   `split()`
+   `split(string)`
    +   `'<a href="https://automatetheboringstuff.com/">'.split('"')`
+   `startswith(string)`, `endswith(string)`
+   `strip()`, `rstrip()`, `lstrip()`

### Task 9

+   寫個[猜數字](https://zh.wikipedia.org/wiki/%E7%8C%9C%E6%95%B0%E5%AD%97)

### Task 10

+   寫個程式幫忙你猜數字

### 字典 `dict`

+   `list` 使用的索引值為 `int`
    +   從 `0` 到 `len()-1`
    +   從 `-len()` 到 `-1`
+   字典的索引直稱為 keys (類似單字的概念).
    +   單字: key
    +   定義: value
    +   字典是一些 key-value pairs 所構成的集合
+   `instructor = {'Name': 'MZ', 'Height': 178, 'Weight': 108}`
    +   `print(instructor['Name'])`
    +   `print(instructor['age'])`
+   空字典: `{}`
+   `keys()`
+   `values()`
+   `items()`
+   `in`
    +   `print('MZ' in instructor)`
    +   `print('Name' in instructor)`
    +   `print(('Name','MZ') in instructor)`
+   `get(key,val)`: 如果 `key` 不存在字典裡，就回傳 `val` ，否則回傳 `key` 所對應的 value。

### Function definition

+   `def fn(arg,*args,**kwargs):`
    +   `arg` 為個數固定的參數
    +   `args` 為一個 `list` ，可以傳遞不定數量的參數
    +   `kwargs` 為一個 `dict` ，可以傳遞特定名稱的參數
    +   可以用 `*my_list` 指定將 `my_list` 當作 `args` 傳入
    +   可以用 `**my_dict` 指定將 `my_dict` 當作 `kwargs` 傳入
    +   善用 `[]`、`len()`、`get()`
