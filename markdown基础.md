# markdown练习

---

- 全球最大的同性交友网: github

  `渲染效果`

---

##1.字体设置/加粗/倾斜/加粗倾斜

```markdown
**加粗**
*倾斜*
***加粗倾斜***
或者*换成_
```

- **加粗**

- _倾斜_

- ***加粗倾斜***



## 2.表格建立

```markdown
|姓名|年龄|籍贯|
|--|--|--|
||||
||||
```

| 姓名   | 年龄   | 籍贯   |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |

## 3.超链接

```markdown
文字链接：
[文字](链接) 示例： [python](https://www.python.org)
地址链接：
<链接>       示例： <https://www.python.org>
```

[python](https://www.python.org)

<https://www.python.org>

## 4.图片

```markdown
![名称](图片地址) #地址可以是本地(最好使用根目录)或者网址链接
```
![本地](./xiaoniao.jpg)

![网址链接](https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3431468138,659289960&fm=26&gp=0.jpg)



## 5.小标题/分三级

```markdown
1.三级小标题
- 1
  - 2
    - 3

2.分割线

---

3.勾选项
-[ ] 勾选1
-[ ] 勾选2
-[ ] 勾选3
-[ ] 勾选4


```

- 2
   - 3
     - 4

---

-[ ] 勾选1
-[ ] 勾选2
-[ ] 勾选3
-[ ] 勾选4

---



## 6.引用

```markdown
>xxx: 话1
>yyy: 话2
>zzz: 话3
```

>xxx: 话1
>yyy: 话2
>zzz: 话3

## 7.代码语句

```markdown 
​```语言名称
	代码：
​```
```

```python
#注释语句
a = 10
print(a)
if a % 2 == 0:
    print('a是偶数')
#函数定义：
def iii(number):
    number = number**2
    return number
```



## 8.字体颜色

```markdown
$\color{red}{红色}$
$\color{#FF0000}{红色}$
$\color{rgb(255,0,0)}{红色}$
```

- $\color{red}{红色}$

- $\color{#FF0000}{红色}$

- $\color{rgb(255,0,0)}{红色}$

