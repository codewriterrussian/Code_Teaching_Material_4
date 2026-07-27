# Lesson 2 補充講義：input()、print(input()) 與 bool() 常見混淆

## 補充目標

1. 在 Jupyter Notebook 裡，`input()` 和 `print(input())` 有什麼差別？
2. `True` / `False` 和 `"True"` / `"False"` 有什麼不同？
3. 為什麼 `bool("False")` 的結果是 `True`？

---

## Section I. Jupyter Notebook 裡的 `input()` 和 `print(input())`

在 Jupyter Notebook 裡，學生常常會看到兩種寫法：

```python
input()
```

和：

```python
print(input())
```

它們看起來很像，但意思不一樣。

---

## Section II. `input()`：讀取輸入，並把結果留在最後一行顯示

在 Jupyter Notebook 中，如果一個 cell 的最後一行是：

```python
input()
```

你輸入：

```
hello
```

Jupyter 可能會顯示：

```python
'hello'
```

注意這裡有引號：

```python
'hello'
```

這不是因為你輸入了引號，而是因為 Jupyter 在顯示「這個值本身」。

它用引號提醒你：

> 這是一個字串 `str`
> 

也就是說：

```python
input()
```

做了兩件事：

1. 等你輸入資料
2. 把輸入結果作為一個值留下來

---

## Section III. `print(input())`：先讀取輸入，再印出來

請看：

```python
print(input())
```

如果你輸入：

```
hello
```

輸出會是：

```
hello
```

這次通常不會看到引號。

因為 `print()` 是把內容「印出來給人看」，不是顯示 Python 的原始資料樣子。

---

## Section IV. `input()` 和 `print(input())` 的差別

| 寫法 | 做的事情 | 在 Jupyter 裡可能看到 |
| --- | --- | --- |
| `input()` | 讀取輸入，回傳一個值 | `'hello'` |
| `print(input())` | 讀取輸入，再印出來 | `hello` |

重點：

```python
input()
```

是「取得資料」。

```python
print(input())
```

是「取得資料後，再顯示出來」。

---

## Section V. 日常生活理解：飲料店點餐機

可以想像成飲料店點餐機。

### `input()`

像是機器問你：

> 請輸入飲料名稱：
> 

你輸入：

```
奶茶
```

機器把這個資料收到程式裡。

也就是：

```python
"奶茶"
```

---

### `print(input())`

像是機器問你：

> 請輸入飲料名稱：
> 

你輸入：

```
奶茶
```

機器再把你剛剛輸入的內容顯示在螢幕上：

```
奶茶
```

---

## Section VI. `True` / `False` 不是文字

Python 裡的布林值是：

```python
True
False
```

它們代表「成立」和「不成立」。

注意：它們不是文字，所以不需要加引號。

| 寫法 | 型態 | 意思 |
| --- | --- | --- |
| `True` | `bool` | 真的、成立 |
| `False` | `bool` | 假的、不成立 |
| `"True"` | `str` | 文字 `"True"` |
| `"False"` | `str` | 文字 `"False"` |

請看：

```python
print(type(True))
print(type("True"))
```

輸出：

```
<class 'bool'>
<class 'str'>
```

所以：

```python
True
```

和：

```python
"True"
```

看起來很像，但對 Python 來說是完全不同的東西。

---

## Section VII. 大小寫也很重要

在 Python 裡，布林值一定要寫成：

```python
True
False
```

不能寫成：

```python
true
false
```

錯誤示範：

```python
x = true
print(x)
```

這樣會出錯，因為 Python 不認得小寫的 `true`。

正確寫法：

```python
x = True
print(x)
```

輸出：

```
True
```

---

## Section VIII. `bool()` 不是在讀文字意思，而是在看「有沒有東西」

很多人看到：

```python
bool("False")
```

會以為結果是：

```python
False
```

但其實結果是：

```python
True
```

原因是：

```python
"False"
```

是一段文字，而且裡面有內容。

所以 Python 會把它當成：

```python
True
```

---

## Section IX. 記住這句話

`bool()` 在轉換資料時，通常不是看「文字的意思」，而是看：

> 這個東西是不是空的？
> 

空的東西通常是：

```python
False
```

有東西通常是：

```python
True
```

---

## Section X. 最常見的 bool 判斷

| 資料 | 結果 | 原因 |
| --- | --- | --- |
| `bool(0)` | `False` | 數字 0 |
| `bool(1)` | `True` | 不是 0 |
| `bool(-1)` | `True` | 不是 0 |
| `bool("")` | `False` | 空字串 |
| `bool(" ")` | `True` | 裡面有一個空白 |
| `bool("0")` | `True` | 這是文字，不是數字 0 |
| `bool("False")` | `True` | 這是文字，而且不是空的 |
| `bool([])` | `False` | 空串列 |
| `bool([0])` | `True` | 串列裡有東西 |

---

## Section XI. 容易混淆比較 1：數字 `0` 和文字 `"0"`

```python
print(bool(0))
print(bool("0"))
```

輸出：

```
False
True
```

原因：

```python
0
```

是數字 0，所以是 `False`。

```python
"0"
```

是文字，而且裡面有一個字，所以是 `True`。

---

## Section XII. 容易混淆比較 2：布林值 `False` 和文字 `"False"`

```python
print(bool(False))
print(bool("False"))
```

輸出：

```
False
True
```

原因：

```python
False
```

本來就是布林值的「假」。

```python
"False"
```

是文字，不是布林值。

只要文字不是空的，通常就是 `True`。

---

## Section XIII. 容易混淆比較 3：空字串 `""` 和空白字串 `" "`

```python
print(bool(""))
print(bool(" "))
```

輸出：

```
False
True
```

原因：

```python
""
```

裡面完全沒有東西。

```python
" "
```

裡面有一個空白，所以不是空的。

---

## Section XIV. 小練習 1：Jupyter 顯示差別

請先猜猜看，這兩段程式在 Jupyter Notebook 裡顯示起來有什麼不同。

### A

```python
input()
```

輸入：

```
cat
```

Jupyter 可能顯示：

```python
'cat'
```

### B

```python
print(input())
```

輸入：

```
cat
```

輸出：

```
cat
```

差別：

A 是讓 Jupyter 顯示「值本身」，所以會看到字串的引號。

B 是用 `print()` 印出文字內容，所以不會看到引號。

---

## Section XV. 小練習 2：判斷型態與 bool 結果

請先不要執行，先猜輸出結果。

```python
print(type(True))
print(type("True"))
print(bool(False))
print(bool("False"))
```

答案：

```
<class 'bool'>
<class 'str'>
False
True
```

---

## Section XVI. 今日補充重點

這份補充只要記住四句話：

第一，`input()` 是取得輸入，`print(input())` 是取得輸入後再印出來。

第二，`True` 和 `False` 是布林值，不是文字。

第三，`"True"` 和 `"False"` 是字串，因為它們有引號。

第四，`bool("False")` 是 `True`，因為 `"False"` 是一段有內容的文字。