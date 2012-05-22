# 新手課程

	當學會爬說語(Python)後，你就不是麻瓜了 :)

## 開始之前

若你之前沒有學過任何程式語言，你可能會好奇什麼是程式。

程式其實就是成一連串的命令。

如果程式設計師是法師，那麼程式碼就是咒語，每個咒語都有不同的效果。
而在電腦執行程式碼就是用咒語施放法術。

咒語可以被抄寫成捲軸，想當然爾，程式碼也可以寫進文字檔，等需要時再使用。
那麼我們，也就是程式設計師是怎麼去設計程式呢? 首先，你必須有個目的。
然後確定需要什麼資料輸入，要產生的結果是什麼。

以買菜為例。 小明的媽媽叫他去買菜，對小明的吩咐是這樣的

	我拿1000元給你，如果菜的單價小於100塊，就買吧!

要把這轉換成程式碼，先思考一件事情要達成，必須拆成幾個步驟，再想辦法把他翻成英文，
你就獲得了最基本的邏輯架構，通常稱之為[pseudocode][1](虛擬碼)。

Python 的語法特性，大致上可以讓你"我手寫我口"。

本課程完成後，你會學會

- 資料型別: int, float, str, unicode, list, dict
- 運算子: ==, >=, <=, >=, >, <, !, not, or , and
- 控制: if..else, if..elif, if..continue, if..break
- 迴圈: while, for
- 輸入輸出print, raw_input

## 大綱

### 第一週 (8小時) : 第一隻程式以及字串

因為我們為非英文語系使用者者，所以相當容易遇到編碼問題。
這一週主要學習 Python 裡面的字串以及編碼問題。

#### 請閱讀

- [電腦做什麼事- 與直譯器互動](http://pydoing.blogspot.com/2008/10/blog-post_04.html)
- [Victor Python 介紹](http://python.ez2learn.com/intro.html)
- [Python 2.7 Tutorial - Using Interpreter](http://docs.python.org/tutorial/interpreter.html)
- [Victor Python 入門][1] 裡面的*註解*，*變數*，*輸入與輸出*，*字串*
- [Python 2.7 Tutorial - Strings](http://docs.python.org/tutorial/introduction.html#strings)
- [Victor - 瞭解Unicode](http://python.ez2learn.com/basic/unicode.html)

#### 完成作業

- `courses/novice/exercises/week1/1.py`
- `courses/novice/exercises/week1/2.py`
- `courses/novice/exercises/week1/3.py`

#### 選讀

- [PyCon US 2012 - Pragmatic Unicode, or, How do I stop the pain?](http://pyvideo.org/video/948/pragmatic-unicode-or-how-do-i-stop-the-pain)
- [All About Python and Unicode](http://boodebr.org/main/python/all-about-python-and-unicode)

### 第二週 (8小時)

這一週開始後的作業會採用*測試先行*(Test-Driven)的方式來引導, 那何謂測試先行呢?
其時就是你先把預期的結果寫出來，再想辦法把程式碼寫出。

最簡單的撰寫test 方式是使用斷言(assertion)，
等之後介紹過 function 會再介紹到其他更強大的測試工具。

下面是個範例

```
Python 2.7.2+ (default, Oct  4 2011, 20:03:08)
[GCC 4.6.1] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> answer = 1
# assert 測試, 錯誤訊息
>>> assert answer == 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

需要看懂上面在做什麼你需要讀完下面的 'Boolean Practice'

#### 請閱讀

- [電腦做什麼事 - 真假世界](http://pydoing.blogspot.com/2008/10/blog-post_6123.html)
- [數值運算](http://ez2learn.com/index.php/python-tutorials/python-tutorials/165-2009-02-11-13-09-18)
- [串列](http://ez2learn.com/index.php/python-tutorials/python-tutorials/166-list)
- [切片](http://ez2learn.com/index.php/python-tutorials/python-tutorials/167-slice)
- [Tuple](http://caterpillar.onlyfun.net/Gossip/Python/TupleType.html)
- [if 判斷句](http://ez2learn.com/index.php/python-tutorials/python-tutorials/171-if)
- [Learn Python in Hard Way: Boolean Practice](http://learnpythonthehardway.org/book/ex28.html)
- [More conditions](http://docs.python.org/tutorial/datastructures.html#more-on-conditions)
- [break and continue Statements, and else Clauses on Loops](http://docs.python.org/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)

註: python 裡的 True 在比較時會變成數字的1, False 會變成數值0, None 則就是 None, 你可以想一下面的答案是什麼

	- 1 == True
	- 1 is True
	- 0 == False
	- 0 is False
	- None == True
	- None is True
	- None == False
	- None is False

註: 要判斷一個元素有沒有在list 裡面可以用`in`, 要判斷一個字有沒有在一個字串內, 也可以用`in`

	Python 2.7.2+ (default, Oct  4 2011, 20:03:08)
	[GCC 4.6.1] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	>>> a=range(1,5)
	>>> 5 in a
	False
	>>> 4 in a
	True
	>>> a
	[1, 2, 3, 4]
	>>> '5' in a
	False
	>>> '4' in a
	False
	>>> '4' in '4string'
	True


- [for 迴圈](http://ez2learn.com/index.php/python-tutorials/python-tutorials/172-for)

note: 在 python 裡的for 指的是foreach, 如果你要真正的for, 可以用下面的方法來類比

	for index in range(0,5):
		print index

	# 輸出為
	# 0
	# 1
	# 2
	# 3
	# 4
	# 5

range 是一個function, 會產生一個[0,1,2,3,4] 的陣列, 細節請`pydoc range`

而如果你想要取得元素的index, 可以使用`enumerate`,

	mylist = [1,2,3,4,5,6]
	for index, value in enumerate(mylist):
		print index, value

	# 下面是結果
	# 0 1
	# 1 2
	# 2 3
	# 3 4
	# 4 5
	# 5 6

- [while 迴圈](http://ez2learn.com/index.php/python-tutorials/python-tutorials/173-while)
- [字典](http://ez2learn.com/index.php/python-tutorials/python-tutorials/168-dictionary)
- [Dictionaries](http://docs.python.org/tutorial/datastructures.html#dictionaries)
- [Looping Techniques](http://docs.python.org/tutorial/datastructures.html#looping-techniques)

#### 選讀

- [軟體設計必讀經典(11)反覆測試與修正，讓錯誤消失](http://www.ithome.com.tw/itadm/article.php?c=47536)

#### 完成作業

- `courses/novice/exercises/week2/1.py`
- `courses/novice/exercises/week2/2.py`
- `courses/novice/exercises/week2/3.py`
- `courses/novice/exercises/week2/4.py`
- `courses/novice/exercises/week2/5.py`

### 第三週 (8小時)

工欲善其事, 必先力其器。如果不會用debugger，就好像人類不會用火一樣。
Python 的 debugger 叫*PDB*，雖然沒有*GDB*那麼強大，但也堪用了。

本週你需要學會pdb, 進階的 list, dict 運用還有定義 function.
除此之外，會要熟撚`map`, `reduce`, filter`這三個非常有用的functional programming tool(在這個難度, 你可先不用懂什麼叫做functional programming)。

在 Python 裡面, Funciton 是*First-Class Function*。以新手來說, 只要記得有下列特性

1. Function 可以被當成 Funciton 的參數傳遞
1. Function 的回傳值可以是 Function
1. Function 可以被指派到變數
1. Function 可以不用指定名稱, 此類 Function 稱為*匿名函式*, 在 Python 裡使用`lambda`關鍵字定義

至於Closure在這個難度可以不用知道這是什麼.

#### 請閱讀

- [More on List](http://docs.python.org/tutorial/datastructures.html#more-on-lists)
- [Sets](http://docs.python.org/tutorial/datastructures.html#sets)
- [Dict Comprehensions](http://www.python.org/dev/peps/pep-0274/)
- [Define Function](http://docs.python.org/tutorial/controlflow.html#defining-functions)
- [More on Define Funciton](http://docs.python.org/tutorial/controlflow.html#more-on-defining-functions)
- [How to debug](http://hcliao.twbbs.org/signal-processing-using-python/how-to-debug)
- [Debuuging in Python](http://pythonconquerstheuniverse.wordpress.com/category/python-debugger/)

#### 選讀

- [Python Official Document - PDB](http://docs.python.org/library/pdb.html)
- [First Class Function in Wikipidia](https://en.wikipedia.org/wiki/First-class_function)
- [Closure in Wikipidia](http://en.wikipedia.org/wiki/Closure_(computer_science))
- [Closure 簡介](http://wiki.python.org.tw/Python/Cookbook/Closure)

#### 完成作業

- `courses/novice/exercises/week1/1.py`
- `courses/novice/exercises/week1/2.py`
- `courses/novice/exercises/week1/3.py `
- `courses/novice/exercises/week1/4.py`
- `courses/novice/exercises/week1/5.py`
- `courses/novice/exercises/week1/6.py`

### 第四週 (8小時)

### 第五週 (8小時)

[1]: https://en.wikipedia.org/wiki/Pseudocode
[2]: http://ez2learn.com/index.php/python-tutorials/python-tutorials
[3]: http://python.ez2learn.com/basic.html
