# Learn Python In Hacker Way (用駭客的方式學 Python)

## 前言

我是 Hychen。

因為有人想學 Python ，所以我就來教了。
在這門課除了教你 Python ， 你還會學到一些軟體開發中會用到的工具，
以及開放源碼/自由軟體社群的工作模式。

本教材適合一人自學或是一人教多人使用(一個難度只能教一人)。

*聲明*

1. 若有任何錯誤，歡迎自由 Patch/Fork。

## 目標

學 Python ，學到什麼程度就看個人努力了。

## 文化與哲學

這邊說得 Hacker 指得是"泛指任何一類事務或領域中的專家或狂熱份子。"
開始前建議閱讀下面這兩篇

- [如何成為駭客][1]
- [提問的智慧][2]

下面這個是推薦的[Coding Style][6]，有時間再讀

- [PEP 8 - Coding Style][7]

## 如何使用本教材

你可以照著本教材上頭列的連結自學，也可以找個熟Python的人利用這份教材來指導你。
後面我將用`學徒`來稱呼想學 Python 的人，`老師` 來稱呼指導學生的人。

`學徒`將會需要使用Git來取得最新的內容, 還有繳交指定作業給老師做Code Review。
如果`學徒`或`老師`不曾用過Git，請先閱讀 [ihower][3] 的[Git and Github 演講投影片][4]。

課程講義依難度分為

- 新手(Novice):
	熟悉基本資料結構以及迴圈，內容在`courses/novice/README.md`
- 學徒(Apprentice):
	能使用Function, Class 來維護較大型的程式, 一些常用的函式庫，以及撰寫測試程式，內容在`courses/apprentice/README.md` (尚未完成)
- 老手(Adept):
	使用Decorator, Generator, Meta Class 來加速開發速度，熟悉特定領域的函式庫使用，例如做GUI的人會熟悉PyGTK, PyQT。
	內容在`courses/adept/README.md` (尚未完成)
- 專家(Expert): 無法提供，因為我不是
- 大師(Master): 無法提供，因為我不是

在學習的過程中，你可以使用`pydoc`來查Python文件，例如我想知道str.replace怎麼用，我就打

```
$ pydoc str.replace
```

另一種查文件的方式是在Interpreter中打`help`，像這樣

```
Python 2.7.2+ (default, Oct  4 2011, 20:03:08)
	[GCC 4.6.1] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	>>> help(str.replace)
```

## 開始

1. `老師`在 github 上 fork 此專案。
1. `學徒`在 github 上 fork `老師`的專案。
1. `學徒`依據課程大綱讀完講義上指定的閱讀項目，並且寫完指定的習題
1. `學徒`把指定的作業commit後，push 進自己的專案
1. `老師`Review`學徒的code，引導`學徒`思考寫出更好的code

## 作業繳交方式

每個課程下面都有一個`exercises`的目錄，下面會有各週的作業。 作業的檔名會是`.py`結尾，
學徒寫完作業後，commit 進自己的專案，並且在`老師`的專案開一個Issue Ticket，通知老師Review 程式碼。

[1]: http://www.angelfire.com/ok/leekawo/hacker.htm
[2]: https://code.google.com/p/smartquestions/wiki/WhenYouAsk
[3]: http://ihower.tw/blog/about
[4]: http://ihower.tw/blog/archives/5391
[5]: http://help.github.com/send-pull-requests/
[6]: http://mmdays.com/2007/04/24/coding-style/
[7]: http://www.python.org/dev/peps/pep-0008/
