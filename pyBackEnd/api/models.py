from django.db import models


# Create your models here.
# 创建岗位模型
class JobInfo(models.Model):
    id = models.AutoField('id', primary_key=True)
    title = models.CharField('岗位名称', max_length=255, default='')
    address = models.CharField('城市', max_length=255, default='')
    type = models.CharField('职业', max_length=255, default='')
    educational = models.CharField('学历', max_length=255, default='')
    workExperience = models.CharField('工作经验', max_length=255, default='')
    workTag = models.TextField('工作标签', max_length=10000, default='')
    salary = models.CharField('工资', max_length=255, default='')
    salaryMonth = models.CharField('年终奖', max_length=255, default='')
    companyTags = models.TextField('福利', max_length=10000, default='')
    hrWork = models.CharField('hr职位', max_length=255, default='')
    hrName = models.CharField('hr名字', max_length=255, default='')
    practice = models.BooleanField('是否为实习岗位', max_length=255, default='')
    companyTitle = models.CharField("公司名称", max_length=255, default='')
    companyAvatar = models.CharField('公司logo', max_length=255, default='')
    companyNature = models.CharField("公司性质", max_length=255, default='')
    companyStatus = models.CharField('融资状态', max_length=255, default='')
    companyPeople = models.CharField('公司规模', max_length=255, default='')
    detailUrl = models.TextField("详情链接", max_length=10000, default='')
    companyUrl = models.TextField("公司链接", max_length=10000, default='')
    dist = models.CharField("行政区", max_length=255, default='')
    createTime = models.DateField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'db_jobInfo'


# 创建用户模型
class User(models.Model):
    id = models.AutoField('id', primary_key=True)
    userName = models.CharField('用户名', max_length=255, default='')
    password = models.CharField("密码", max_length=255, default='')
    educational = models.CharField('学历', max_length=255, default='')
    workExperience = models.CharField('工作经验', max_length=255, default='')
    address = models.CharField('意向城市', max_length=255, default='')
    work = models.CharField('意向工作', max_length=255, default='')
    avatar = models.FileField("头像", upload_to='avatar', default="avatar/defaultAvatar.jpg")
    createTime = models.DateField('创建时间', auto_now_add=True)

    class Meta:
        db_table = "db_user"


# 创建历史记录模型
class History(models.Model):
    id = models.AutoField('id', primary_key=True)
    job = models.ForeignKey(JobInfo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField("访问次数", default=1)

    class Meta:
        db_table = "db_history"


# 搜索记录
class SearchHistory(models.Model):
    id = models.AutoField("id", primary_key=True)
    searchTitle = models.CharField("搜索词", max_length=255, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField("搜索次数", default=1)

    class Meta:
        db_table = "db_searchHistory"
