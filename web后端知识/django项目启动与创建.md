# django项目创建与启动

django源代码构建安装：

`pip install django==2.1.14 -i ...`

创建并运行Django项目：

~ 第一种方式：

` 1.django-admin startproject django1906`

2.使用pyCharm打开项目并创建虚拟环境

​	~ File ---> Settins --> Project --->

​	Project Interpreter ---> Add

​	~ Terminal --->

​	python -m venv venv --python=/usr/bin/

​	source venv/bin/activate

​	"venv/Scripts/activate"

3.安装项目所需依赖项  

​	~pip install django==2.1.15



4.运行项目

~ `python manage.py runserver`

~ Add Configuration --> + --> Python

--> Script Path (manage.py)

--> Parameters (runserver)

~ 第二种方式：

1. 用PyCharm创建一个普通Python项目

2. 安装Django所需的依赖项

   ~ `pip install djange==2.1.14`

3. 把python项目变成django项目

   ~ `django-admin startproject django1906 .`

   **注意后面有个点**

4. 运行项目



~ 第三种方式：

1. 克隆项目到本地

 ​~ 使用PyCharm的"get from version control"

 ~ `git clone git@gitee.com:liujhh/django1906.git`

1. 创建虚拟环境

   ~ Linux/macOS: source venv/bin/activate

   ~ Windows: "venv/Scripts/activate"

2. 重建依赖项

   ~ `pip install -r requirements.txt`


GitLab ---> Git私服



异步请求，局部刷新