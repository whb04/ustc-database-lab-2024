# 教师教学科研工作统计系统

## 项目简介

> 2024 USTC 数据库系统与应用 实验3
>
> 此项目的所有代码均为AI生成

## 功能特性

- 教师信息管理：增删改查教师信息。
- 课程管理：增删改查课程信息，并关联教师。
- 论文管理：增删改查论文信息，并关联教师。
- 项目管理：增删改查项目信息，并关联教师。
- 教师教学科研工作统计：根据教师工号和年份范围查询并导出教师的教学科研工作情况，导出文件格式为 xlsx。
- 前端界面美观简洁，使用 Bootstrap 进行样式美化。

## 环境依赖

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Migrate
- openpyxl
- Bootstrap

## 安装步骤

1. 克隆项目代码到本地：

```bash
git clone https://github.com/whb04/ustc-database-lab-2024
cd ustc-database-lab-2024
```

2. 创建并激活虚拟环境：

```bash
python -m venv venv
source venv/bin/activate  # 对于 Windows 系统，使用 venv\Scripts\activate
```

3. 安装所需依赖：

```bash
pip install Flask SQLAlchemy Flask-Migrate WTForms
```

4. 初始化数据库：

修改 `config.py`

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/database'
# 将 user,password,database 替换为你的数据库用户名，密码，数据库名
```

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

5. 运行项目：

```bash
python run.py
```

## 使用说明

1. 打开浏览器，访问 `http://127.0.0.1:5000`，进入系统首页。
2. 在导航栏中可以看到教师、课程、论文、项目等管理模块，点击相应链接进入相应模块进行操作。
3. 在教师教学科研工作统计模块中，输入教师工号和年份范围，点击查询按钮，即可查看教师的教学科研工作情况。
4. 点击导出按钮，即可下载生成的 xlsx 文件，文件中包含教师的基本信息、教学情况、发表论文情况和承担项目信息。

## 文件结构

```plaintext
.
├── README.md
├── app
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   └── templates
│       ├── add_teacher.html
│       ├── base.html
│       ├── courses.html
│       ├── edit_course.html
│       ├── edit_paper.html
│       ├── edit_project.html
│       ├── edit_teacher.html
│       ├── index.html
│       ├── papers.html
│       ├── projects.html
│       ├── teacher_summary.html
│       └── teachers.html
├── config.py
└── run.py
```

## 贡献

欢迎提交 issue 或 pull request 来改进本项目。如有任何问题或建议，请联系项目维护者。
