# Lesson 4-延伸 不同資料型態的比較

---

## ❓Section I. 為什麼不同資料型態比較會讓人困惑？

比較運算子可以用來判斷兩個值之間的關係，例如：

```python
>
<
>=
<=
==
!=
```

但是在 Python 裡，不同資料型態的資料不一定能直接比較大小。

例如：

```python
print(10 > 3)
```

執行結果：

```python
True
```

因為 `10` 和 `3` 都是數字，所以可以比較大小。

但是：

```python
print("10" > 3)
```

這樣會發生錯誤，因為 `"10"` 是文字，`3` 是數字。

---

## 🧠Section II. 先分清楚：資料看起來像數字，不代表它是數字

在 Python 中：

```python
10
```

是整數 `int`。

但是：

```python
"10"
```

是字串 `str`。

也就是說：

```python
10 == "10"
```

執行結果是：

```python
False
```

因為一個是數字，另一個是文字。

生活化理解：

> 數字 `10` 像是真的 10 元硬幣。
> 
> 
> 字串 `"10"` 像是紙上寫著「10」這兩個符號。
> 
> 它們看起來很像，但不是同一種東西。
> 

---

## 🔢Section III. 數字和數字可以比較

整數 `int` 和小數 `float` 可以直接比較。

範例：

```python
print(10 > 3.5)
print(5 == 5.0)
```

執行結果：

```python
True
True
```

因為 `int` 和 `float` 都是數值型態，Python 可以理解它們的大小關係。

---

## 🔤Section IV. 字串和字串也可以比較，但不是用數字大小比較

字串之間可以使用比較運算子，但是比較方式不是「數字大小」，而是依照字元順序比較。

範例：

```python
print("apple" < "banana")
```

執行結果：

```python
True
```

因為 Python 會從第一個字母開始比較，`a` 排在 `b` 前面。

但是要特別注意：

```python
print("10" < "2")
```

執行結果：

```python
True
```

這不是因為 10 小於 2，而是因為它們是字串，Python 會先比較第一個字元：

```
"10" 的第一個字元是 "1"
"2" 的第一個字元是 "2"
```

因為 `"1"` 排在 `"2"` 前面，所以結果是 `True`。

---

## ⚠️Section V. 數字和字串不能直接比較大小

錯誤範例：

```python
age = input("請輸入年齡：")
print(age >= 18)
```

如果使用者輸入：

```python
20
```

程式仍然會錯，因為 `input()` 讀進來的資料預設是字串。

也就是：

```python
age = "20"
```

不是：

```python
age = 20
```

所以要先轉型：

```python
age = int(input("請輸入年齡："))
print(age >= 18)
```

---

## ✅Section VI. 使用 `int()` 或 `float()` 轉成數字後再比較

如果要比較數字大小，請先確認資料是數字型態。

範例：

```python
score = input("請輸入分數：")
score = int(score)

print(score >= 60)
```

如果輸入：

```python
80
```

執行結果：

```python
True
```

也可以寫成一行：

```python
score = int(input("請輸入分數："))
print(score >= 60)
```

---

## 🧪Section VII. `==` 和 `!=` 比較時比較不容易出錯，但仍要注意型態

`==` 用來判斷兩個值是否相等。

範例：

```python
print(10 == 10)
print(10 == "10")
print("hello" != "Hello")
```

執行結果：

```python
True
False
True
```

說明：

| 程式 | 結果 | 原因 |
| --- | --- | --- |
| `10 == 10` | `True` | 兩邊都是數字 10 |
| `10 == "10"` | `False` | 一邊是數字，一邊是字串 |
| `"hello" != "Hello"` | `True` | 大小寫不同，所以不是同一個字串 |

---

## 🔁Section VIII. 布林值 `True` / `False` 的比較

布林值常常是比較運算後的結果。

範例：

```python
x = 10
print(x > 5)
```

執行結果：

```python
True
```

也可以直接比較布林值：

```python
print(True == True)
print(True == False)
```

執行結果：

```python
True
False
```

但是要注意：

```python
print(True == "True")
```

執行結果：

```python
False
```

因為 `True` 是布林值，`"True"` 是字串。

---

## 🧰Section IX. 常見錯誤整理

| 錯誤寫法 | 問題 | 建議修正 |
| --- | --- | --- |
| `input() >= 60` | `input()` 讀進來是字串，不能直接和數字比較 | `int(input()) >= 60` |
| `"10" > 3` | 字串和數字不能直接比較大小 | `int("10") > 3` |
| `"10" < "2"` | 字串比較不是數字大小比較 | `int("10") < int("2")` |
| `True == "True"` | 布林值和字串不是同一種資料 | 視情況使用布林值或字串 |

---

## 🧩Section X. 小練習

請判斷下列程式的結果。

### 練習 1

```python
print(5 > 3)
```

答案：

```python
True
```

---

### 練習 2

```python
print(5 == "5")
```

答案：

```python
False
```

---

### 練習 3

```python
print("10" < "2")
```

答案：

```python
True
```

原因：這是字串比較，不是數字大小比較。

---

### 練習 4

```python
score = input("請輸入分數：")
print(score >= 60)
```

答案：

```
會發生錯誤
```

原因：`score` 是字串，`60` 是整數，不能直接比較大小。

正確寫法：

```python
score = int(input("請輸入分數："))
print(score >= 60)
```

---

## 💯重點複習

1. `int` 和 `float` 都是數字，可以直接比較大小。
2. `str` 和 `str` 可以比較，但比較的是字元順序，不是數字大小。
3. `input()` 讀進來的資料預設是字串。
4. 如果要比較輸入的數字大小，通常要先使用 `int()` 或 `float()` 轉型。
5. `10` 和 `"10"` 看起來很像，但資料型態不同，所以不相等。
6. `True` 和 `"True"` 也不同，一個是布林值，一個是字串。

---

## 🧾一句話總結

> 比較之前，先確認兩邊是不是同一類型；如果要比數字大小，就先把資料轉成數字。
>