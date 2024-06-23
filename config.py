import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1@localhost/lab3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)

GENDER_MAP = {
    1: '男',
    2: '女'
}

TITLE_MAP = {
    1: '博士后',
    2: '助教',
    3: '讲师',
    4: '副教授',
    5: '特任教授',
    6: '教授',
    7: '助理研究员',
    8: '特任副研究员',
    9: '副研究员',
    10: '特任研究员',
    11: '研究员'
}

PAPER_TYPE_MAP = {
    1: 'full paper',
    2: 'short paper',
    3: 'poster paper',
    4: 'demo paper'
}

PAPER_LEVEL_MAP = {
    1: 'CCF-A',
    2: 'CCF-B',
    3: 'CCF-C',
    4: '中文CCF-A',
    5: '中文CCF-B',
    6: '无级别'
}

PROJECT_TYPE_MAP = {
    1: '国家级项目',
    2: '省部级项目',
    3: '市厅级项目',
    4: '企业合作项目',
    5: '其它类型项目'
}

SEMESTER_MAP = {
    1: '春季学期',
    2: '夏季学期',
    3: '秋季学期'
}
