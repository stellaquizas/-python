#ecoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

kaoyan =[
    ['研招动态', ],
    ['招生简章', ],
    ['报考择校', '报考指南','报考经验','政策新闻','招生信息','择选院校','专业介绍'],
    ['备考准备', '备考经验','大纲解析','考研分数线','成绩查询','复试攻略','调剂指南'],
    ['公共课', '英语','政治','数学'],
    ['专业课', '计算机','教育学','心理学','历史学','其他', 'MBA', 'MPAcc'],
 ]

zuowen = [
    ['小学作文',],
    ['初中作文',],
    ['高中作文',],
    ['话题作文',],
    ['考试作文',],
    ['单元作文',],
    ['作文素材',],
]

qiuzhi = [
    ['求职资讯',],
    ['宣讲会', ],
    ['招聘信息', ],
    ['实习生', ],
    ['求职须知', '简历', '面试', '就职', '人际', '薪酬', '规章']
]

cet = [
    ['历年真题', '四级真题', '六级真题',],
    ['四级备考', '四级作文', '四级听力', '四级阅读', '四级翻译', '四级口语', '模拟试题'],
    ['六级备考', '六级作文', '六级听力', '六级阅读', '六级翻译', '六级口语', '模拟试题'],
    ['经验指导', '考试动态', '样题规定', '复习攻略', '高分经验', '名师指导'],
]

toeic = [
    ['历年真题',],
    ['分类资讯', '托业阅读', '托业听力', '托业词汇', '托业综合', '模拟试题'],
    ['经验指导', '备考资料', '复习攻略', '高分经验', '名师指导'],
]

bec = [
    ['备考资料',],
    ['热门动态',],
    ['模拟试题',],
    ['BEC初级', '听力辅导', '阅读辅导', '写作辅导', '口试辅导', '初级真题'],
    ['BEC中级', '听力辅导', '阅读辅导', '写作辅导', '口试辅导', '中级真题'],
    ['BEC高级', '听力辅导', '阅读辅导', '写作辅导', '口试辅导', '高级真题'],
]

sifa = [
    {'考试资讯': [
        ['报考指南', '司考指南', '司考政策'],
        ['考试动态', '司考动态', '编辑推荐'],
        ]},
    {'考试报名': [
        ['报名时间', ],
        ['报名条件', ],
        ['报名费用', ],
    ]},
    {'考试科目': [
        ['司考卷一', ],
        ['司考卷二', ],
        ['司考卷三', ],
        ['司考卷四', ],
    ]},
    {'备考辅导': [
        ['考试大纲', ],
        ['复习指导', ],
        ['心得技巧', '司考心得', '经验交流', '备考经验',],
    ]},
    {'真题资料': [
        ['卷一真题', ],
        ['卷二真题', ],
        ['卷三真题', ],
        ['卷四真题', ],
        ['模拟试题', ],
    ]},
]

jszg = [
    {
        '考试资讯':[
            ['考试指南',],
            ['考试动态',],
            ['政策法规',]
        ]
    },
    {
        '考试报名':[
            ['报名时间',],
            ['报名条件',],
            ['考试时间',],
            ['报名费用',]
        ]
    },
    {
       '中学教师':[
           ['综合素质','中学教师综合素质'],
           ['教育知识','中学教师教育知识与能力'],
           ['学科知识','中学教师学科知识'],
           ['教育学','中学教师教育学'],
           ['心理学','中学教师心理学'],
           ['历年真题','中学教师历年真题']
       ]
    },
    {
       '小学教师':[
           ['综合素质','小学教师综合素质'],
           ['教育知识','小学教师教育知识与能力'],
           ['教育学','小学教师教育学'],
           ['心理学','小学教师心理学'],
           ['历年真题','小学教师历年真题']
       ]
    },
    {
        '幼儿教师':[
            ['综合素质','幼儿教师综合素质'],
            ['保教知识','幼儿教师保教知识与能力'],
            ['教育学','幼儿教师教育学'],
            ['心理学','幼儿教师心理学'],
            ['历年真题','幼儿教师历年真题']
        ]
    },
    {
         '面试专题':[]
    },
    {
        '备考辅导':[
            ['考试大纲',],
            ['心得技巧',],
            ['经验交流',],
            ['模拟试题',]
        ]
    },
    {
        '互动问答':[]
    }

]

jsj=[
    {
        '考试动态':[
            ['考试报名',],
            ['考试大纲',],
            ['考试政策',],
            ['最新资讯',]
        ]
    },
    {
        '报考指南':[
            ['报名时间',],
            ['报名条件',],
            ['报名费用',],
            ['考试时间',],
            ['成绩查询',],
        ]
    },
    {
        '计算机一级':[
            ['考试辅导','计算机一级考试辅导'],
            ['模拟试题','计算机一级模拟试题'],
            ['历年真题','计算机一级历年真题']
        ]
    },
    {
        '计算机二级':[
            ['考试辅导', '计算机二级考试辅导'],
            ['模拟试题', '计算机二级模拟试题'],
            ['历年真题', '计算机二级历年真题']
        ]
    },
    {
        '计算机三级': [
            ['考试辅导', '计算机三级考试辅导'],
            ['模拟试题', '计算机三级模拟试题'],
            ['历年真题', '计算机三级历年真题']
        ]
    },
    {
        '计算机四级': [
            ['考试辅导', '计算机四级考试辅导'],
            ['模拟试题', '计算机四级模拟试题'],
            ['历年真题', '计算机四级历年真题']
        ]
    }
]

kj=[
    {
        '考试动态':[
            ['考试报名',],
            ['考试大纲',],
            ['考试政策',],
            ['考试资讯',]
        ]
    },
    {
        '考试指南':[
            ['报名时间',],
            ['报名条件',],
            ['报名费用',],
            ['考试时间',],
            ['成绩查询',]
        ]
    },
    {
        '会计基础':[
            ['考试辅导','会计基础考试辅导'],
            ['模拟试题','会计基础模拟试题'],
            ['历年真题','会计基础历年真题']
        ]
    },
    {
        '财经法规':[
            ['考试辅导','财经法规与职业道德考试辅导'],
            ['模拟试题','财经法规与职业道德模拟试题'],
            ['历年真题','财经法规与职业道德历年真题']
        ]
    },
    {
        '会计电算化':[
            ['考试辅导','会计电算化考试辅导'],
            ['模拟试题','会计电算化模拟试题'],
            ['历年真题','会计电算化历年真题']
        ]
    },
    {
        '复习指导':[
            ['考试经验',],
            ['技巧心得',],
            ['辅导资源',]
        ]
    }
]

xlzx = [
    {
        '考试动态':[
            ['考试报名',],
            ['考试大纲',],
            ['政策法规',],
            ['考试资讯',]
        ]
    },
    {
        '报考指南':[
            ['报名时间',],
            ['报名条件',],
            ['报名费用',],
            ['考试时间',],
            ['成绩查询',]
        ]
    },
    {
        '二级心理':[
            ['考试辅导','二级心理咨询师考试辅导'],
            ['模拟试题','二级心理咨询师模拟试题'],
            ['历年真题','二级心理咨询师历年真题']
        ]
    },
    {
        '三级心理': [
            ['考试辅导', '三级心理咨询师考试辅导'],
            ['模拟试题', '三级心理咨询师模拟试题'],
            ['历年真题', '三级心理咨询师历年真题']
        ]
    },
    {
        '专项辅导':[
            ['心理知识',],
            ['心理辅导',],
            ['心理测试',]
        ]
    },
    {
        '复习指导':[
            ['考试经验',],
            ['技巧心得',],
            ['辅导资料',]
        ]
    }
]

jzs=[
    {
        '考试动态':[
            ['考试报名',],
            ['考试大纲',],
            ['政策法规',],
            ['考试资讯',]
        ]
    },
    {
        '报考指南':[
            ['报名时间',],
            ['报名条件',],
            ['报名费用',],
            ['考试时间',],
            ['成绩查询',]
        ]
    },
    {
        '施工管理':[
            ['辅导资料',],
            ['模拟试题',],
            ['历年真题',]
        ]
    },
    {
        '工程法规':[
            ['辅导资料', ],
            ['模拟试题', ],
            ['历年真题', ]
        ]
    },
    {
        '管理实务':[
            ['建筑工程',],
            ['机电工程',],
            ['市政工程',],
            ['公路工程',],
            ['水电工程',],
            ['矿业工程',]
        ]
    },
    {
        '复习指导':[
            ['考试经验',],
            ['技巧心得',],
            ['考试辅导',]
        ]
    }
]

zk = [
    {
      '政策资讯':[
          ['中考政策',],
          ['中考资讯',],
          ['中考报名',],
          ['志愿填报',]
      ]
    },
    {
        '复习备考':[
            ['高分经验',],
            ['备考策略',],
            ['复习技巧',],
        ]
    },
    {
        '考前调整':[
            ['心理辅导',],
            ['中考饮食',],
            ['中考家长',]
        ]
    },
    {
        '科目指导':[
            ['中考语文',],
            ['中考数学',],
            ['中考英语',],
            ['中考物理',],
            ['中考化学',],
            ['中考政治',],
            ['中考历史',],
            ['中考地理',],
            ['中考生物',]
        ]
    },
    {
        '中考试题':[
            ['历年真题',],
            ['模拟试题',],
            ['期中末试题',]
        ]
    },
    {
        '真题作文':[
            ['满分作文',],
            ['作文题目',],
            ['作文指导',],
            ['英语作文',]
        ]
    }
]


pth = [
    {
        '考试动态':[
            ['考试报名',],
            ['考试时间',],
            ['报名时间',],
            ['考试大纲',],
            ['考试资讯',]
        ]
    },
    {
      '拼音':[
          ['拼音基础',],
          ['拼音教程',]
      ]
    },
    {
        '词语':[
            ['词语表',],
            ['轻声词语',],
            ['儿化词语',]
        ]
    },
    {
        '试题':[
            ['模拟试题',],
            ['历年真题',]
        ]
    },
    {
        '学习资料':[

        ]
    },
    {
        '朗读作品':[

        ]
    },

]
buxiban = [
    {
        '艺术':[
            ['舞蹈',],
            ['乐器',],
            ['美术',],
            ['声乐',],
            ['表演',],
            ['艺考',]
        ]
    },
    {
        '兴趣': [
            ['摄影',],
            ['DJ',],
            ['魔术',],
            ['书法',],
            ['风水',],
            ['国学',]
        ]
    },
    {
        '生活': [
            ['礼仪',],
            ['茶艺',],
            ['插花',],
            ['烹饪',],
            ['形体',],
            ['园艺',]
        ]
    },
]

kaozhengtiku = [
    {
        '建筑工程':[
            ['一级建造师',],
            ['二级建造师',],
            ['监理工程师',],
            ['咨询工程师',],
            ['造价工程师',],
            ['结构工程师',],
            ['电气工程师',],
            ['物业管理师']
        ]
    },
    {
        '财会经济':[
            ['经济师',],
            ['设计师',],
            ['初级会计师',],
            ['中级会计师',],
            ['注册会计师',],
            ['统计师',],
            ['审计师',],
            ['注册税务师']
        ]
    },
    {
        '医学卫生':[
            ['执业药师',],
            ['执业医师',],
            ['执业护士',],
            ['临床执业',],
            ['中西医执业',],
            ['中医执业',],
            ['主治',],
            ['检验']
        ]
    },
    {
        '外语考试':[
            ['英语四六级',],
            ['雅思',],
            ['托福',],
            ['GRE考试',],
            ['职称英语',],
            ['公共英语',],
            ['商务英语',],
            ['日语']
        ]
    },
    {
        '职业资格':[
            ['人力资源',],
            ['心理咨询师',],
            ['物流师',],
            ['公共营养师',],
            ['秘书资格',],
            ['证券经纪人',],
            ['电子商务',],
            ['国家司法']
        ]
    },
    {
        '学历教育':[
            [ '成人高考',],
            [ '自考',],
            [ 'MBA',],
            ['法律硕士',],
            [ '会计硕士',],
            [ '工程硕士',],
            ['公共硕士',],
            ['考研']
        ]
    },
    {
        '计算机考试':[
            [ '计算机等级',],
            [ '软件水平',],
            [ '微软认证',],
            [ 'Cisco认证',],
            ['Oracle认证',],
            [ '职称计算机',],
            ['Java认证',],
            [ '华为认证']
        ]
    },
]
cxy = [
    {
        '.NET技术':[
            ['.NET新手区',],
            ['ASP.NET',],
            ['C#',],
            ['.NET Core',],
            ['WinForm',],
            ['Silverlight',],
            ['WCF',],
            ['CLR'],
            ['WPF'],
            ['XNA'],
            ['Visual Studio'],
            ['ASP.NET MVC'],
        ]
    },
    {
        '编程语言': [
            ['Java', ],
            ['C++', ],
            ['PHP', ],
            ['Delphi', ],
            ['Python', ],
            ['Ruby', ],
            ['C语言', ],
            ['Erlang', ],
            ['Go', ],
            ['Swift', ],
            ['Scala', ],
            ['R语言', ],
        ]
    },
    {
        '软件设计': [
            ['架构设计', ],
            ['面向对象', ],
            ['设计模式', ],
            ['领域驱动设计', ],
        ]
    },
    {
        'Web前端': [
            ['Html/Css', ],
            ['JavaScript', ],
            ['jQuery', ],
            ['HTML5', ],
        ]
    },
    {
        '手机开发': [
            ['Android开发', ],
            ['iOS开发', ],
            ['Windows Phone', ],
            ['Windows Mobile', ],
            ['其他手机开发', ],
        ]
    },
    {
        '数据库技术': [
            ['SQL Server', ],
            ['Oracle', ],
            ['MySQL', ],
            ['NoSQL', ],
            ['大数据', ],
            ['其它数据库', ],
        ]
    },
    {
        '操作系统': [
            ['Windows', ],
            ['Windows Server', ],
            ['Linux', ],
            ['OS X', ],
            ['嵌入式', ],
        ]
    },
]
jr = [
    {
        '银行从业':[
        ]
    },
    {
        '基金从业': [
        ]
    },
    {
        '证券从业': [
        ]
    },
    {
        '经济师': [
        ]
    },
    {
        'CFA': [
        ]
    },
    {
        'ACCA': [
        ]
    },
]
