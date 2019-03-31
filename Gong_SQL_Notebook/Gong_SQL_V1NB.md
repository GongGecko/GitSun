# SQL学习笔记(Gong_SQL_V1NB)。

[TOC]

## 第S01章(SQL简介)

@import "廖雪峰SQL教程01.jpg"

### 第01节(关系数据库概述)

@import "廖雪峰SQL教程03.jpg"

```

SQL:结构化查询语言Structured Query Language

@import "廖雪峰SQL教程02.png"

print('............................S010101............................')
定义列数据类型:

INT                  整型                 4字节整数类型
BIGINT               长整型               8字节整数类型
REAL                 浮点型               4字节浮点数
DOUBLE               浮点型               8字节浮点数
DECIMAL(M,N)         高精度小数           由用户指定精度的小数
CHAR(N)              定长字符串           存储指定长度的字符串
VARCHAR(N)           变长字符串           存储可变长度的字符串
BOOLEAN              布尔类型             存储True或者False
DATE                 日期类型             存储日期
TIME                 时间类型             存储时间
DATETIME             日期和时间类型       存储日期+时间
print('............................S010101............................')


各个数据库各自扩展通常称为“方言”。

SQL操作数据库能力：
DDL：Data Definition Language
DML：Data Manipulation Language
DQL：Data Query Language

本教程约定：SQL关键字总是大写,以示突出,表名和列名均使用小写。

```

### 第02节(安装MySQL)

@import "廖雪峰SQL教程04.jpg"

```

如果不知道采用哪种引擎,总是选择InnoDB

Linux上安装MySQL,apt-get install mysql-server

```

## 第S02章(关系模型)

@import "廖雪峰SQL教程05.jpg"

```

表的行称为记录(Record),记录是一个逻辑意义上的数据。

表的列称为字段(Column),同个表每行记录都拥有相同字段。

通常字段应避免允许为NULL。

```

### 第01节(主键)

@import "廖雪峰SQL教程06.jpg"

```

通过字段唯一区分,这个字段称为主键,一般命名为id。

记录一旦插入到表中,主键最好不要再修改。

不使用任何业务相关字段作为主键,常见id字段类型：

1.自增整数类型

2.全局唯一GUID类型


两个或更多字段设为主键,称为联合主键。尽量不使用联合主键。

```

### 第02节(外键)

@import "廖雪峰SQL教程07.jpg"

```

通过字段把数据与另一张表关联,这种列称为外键。

定义外键约束:students表,classes表

ALTER TABLE students
ADD CONSTRAINT fk_class_id
FOREIGN KEY (class_id)
REFERENCES classes (id);

外键约束名称fk_class_id
FOREIGN KEY (class_id)指定class_id作为外键
REFERENCES classes (id)指定外键关联到classes表的id列


通过定义外键约束,关系数据库可以保证无法插入无效数据;外键约束会降低数据库性能;
外键也可以不设置约束,仅靠应用程序的逻辑来保证。如此,class_id仅是普通列,只起到外键作用


删除外键约束:

ALTER TABLE students
DROP FOREIGN KEY fk_class_id;

注意:删除外键约束并没有删除外键这列


多对多关系通过中间表,关联两个一对多关系;
某些应用会把大表拆分,把经常读取和不经常读取字段分开,以获得更高性能。

```

### 第03节(索引)

@import "廖雪峰SQL教程08.jpg"

```

索引是关系数据库中对某一列或多列的值进行预排序的数据结构。
使用索引,数据库系统直接定位到符合条件的记录,加快了查询速度。关系数据库会自动对主键创建主键索引。
索引效率取决于索引列值的散列程度。缺点是插入、更新和删除记录,需要同时修改索引。

创建索引：score列

ALTER TABLE students
ADD INDEX idx_score (score);
# 索引名称idx_score

索引多列
ALTER TABLE students
ADD INDEX idx_name_score (name, score);


唯一索引
ALTER TABLE students
ADD UNIQUE INDEX uni_name (name);

唯一约束,并不唯一索引
ALTER TABLE students
ADD CONSTRAINT uni_name UNIQUE (name);
# name列没有索引,但有唯一性保证

```

## 第S03章(在线SQL)

@import "廖雪峰SQL教程09.jpg"

## 第S04章(查询数据)

@import "廖雪峰SQL教程10.jpg"

### 第01节(基本查询)

@import "廖雪峰SQL教程11.jpg"

```

-- 双减号开头注释


-- 查询students表所有数据

SELECT * FROM students;
# SELECT是关键字,表示执行一个查询;*表示所有列

SELECT 1;
# 判断数据库连接是否有效

```

### 第02节(条件查询)

@import "廖雪峰SQL教程12.jpg"

```

-- 按条件查询students:

SELECT * FROM students WHERE score >= 80;

SELECT * FROM students WHERE name >= 'abc' AND gender = 'M';
# 字符串用单引号,根据ASCII码比较;中文字符根据数据库设置比较

SELECT * FROM students WHERE NOT class_id = 2;
SELECT * FROM students WHERE class_id <> 2;
# 两者等价,NOT不常用

SELECT * FROM students WHERE (score < 80 OR score > 90) AND gender = 'M';
# 不加括号,条件运算按NOT、AND、OR优先级进行

SELECT * FROM students WHERE name LIKE 'ab%'
# LIKE相似判断,%表示任意字符,匹配'ab'、'abc'、'abcd'

```

### 第03节(投影查询)

@import "廖雪峰SQL教程13.jpg"

```

只返回指定列的操作称为投影查询

-- 投影查询,并将列名重命名:score列

SELECT id, score points, name FROM students;
# points为score列的别名;结果集列的顺序可以和原表不同

```

### 第04节(排序)

@import "廖雪峰SQL教程14.jpg"

```

-- 按score从低到高

SELECT id, name, gender, score FROM students ORDER BY score;
# 默认排序ASC(升序),可以省略,即ORDER BY score ASC和ORDER BY score一致

SELECT id, name, gender, score FROM students ORDER BY score DESC;
# DESC(倒序)


-- 按score, gender排序

SELECT id, name, gender, score FROM students ORDER BY score DESC, gender;
# 先按score列倒序,分数相同,再按gender列排序


-- 带WHERE条件的ORDER BY

SELECT id, name, gender, score
FROM students
WHERE class_id = 1
ORDER BY score DESC;
# ORDER BY子句放WHERE子句后面

```

### 第05节(分页查询)

@import "廖雪峰SQL教程15.jpg"

```

-- 查询第1页

SELECT id, name, gender, score
FROM students
ORDER BY score DESC
LIMIT 3 OFFSET 0;
# 结果集从0号记录开始,最多取3条;SQL记录集索引从0开始
# 查询第N页记录集,LIMIT设定为pageSize,OFFSET为pageSize*(pageIndex-1)
# OFFSET可选,只写LIMIT 15,等于LIMIT 15 OFFSET 0


SELECT id, name, gender, score
FROM students
ORDER BY score DESC
LIMIT 3 OFFSET 20;
# Empty result set
# OFFSET超过最大数量,得到空结果集


在MySQL中,LIMIT 15 OFFSET 30可以简写LIMIT 30, 15
使用LIMIT <M> OFFSET <N>分页,随着N越大,查询效率越低。

```

### 第06节(聚合查询)

@import "廖雪峰SQL教程16.jpg"

```

-- 使用聚合查询

SELECT COUNT(*) FROM students;
SELECT COUNT(*) num FROM students;
# 设置结果集列名为num
# COUNT(*)表示查询所有列的行数,COUNT(*)和COUNT(id)实际上一样
# 查询结果是一个二维表,只是只有一行一列


SUM 	计算某一列的合计值,该列必须为数值类型
AVG 	计算某一列的平均值,该列必须为数值类型
MAX 	计算某一列的最大值,该列可以是字符类型
MIN 	计算某一列的最小值,该列可以是字符类型


-- 使用聚合查询计算男生平均成绩:

SELECT AVG(score) average FROM students WHERE gender = 'M';
# 没有匹配到任何行,COUNT()、SUM()返回0,MAX()、MIN()、AVG()返回NULL

SELECT AVG(score) average FROM students WHERE gender = 'X';
# average
# NULL


-- 按class_id分组,分组聚合

SELECT COUNT(*) num FROM students GROUP BY class_id;
SELECT class_id, COUNT(*) num FROM students GROUP BY class_id;
SELECT name, class_id, COUNT(*) num FROM students GROUP BY class_id;
# AlaSQL不严格执行SQL标准,上述SQL在浏览器可以正常执行,但在MySQL、Oracle等环境下将报错

SELECT class_id, gender, COUNT(*) num FROM students GROUP BY class_id, gender;
输出:
class_id	gender	num
1			 M        2
1 			 F        2
2 			 F        1
2 			 M        2
3 			 F        2
3 			 M        1

```

### 第07节(多表查询)

@import "廖雪峰SQL教程17.jpg"

```

-- FROM students, classes:

SELECT * FROM students, classes;
# 结果集列数是两表列数之和,行数是两表行数之积;多表查询又称笛卡尔查询


-- set alias:

SELECT
    students.id sid,
    students.name,
    students.gender,
    students.score,
    classes.id cid,
    classes.name cname
FROM students, classes;


-- set table alias:

SELECT
    s.id sid,
    s.name,
    s.gender,
    s.score,
    c.id cid,
    c.name cname
FROM students s, classes c;
WHERE s.gender = 'M' AND c.id = 1;

```

### 第08节(连接查询)

@import "廖雪峰SQL教程18.jpg"

```

-- 选出所有学生,同时返回班级名称:# name列存储在classes表中

SELECT s.id, s.name, s.class_id, c.name class_name, s.gender, s.score
FROM students s
INNER JOIN classes c
ON s.class_id = c.id;
# 先确定主表
# 根据students表的class_id对应classes表id,列相同的行连接


INNER JOIN
LEFT OUTER JOIN
RIGHT OUTER JOIN
FULL OUTER JOIN
# 见图(廖雪峰SQL教程18.jpg),重要

```

## 第S05章(修改数据)

**增查改删,CRUD:增加(Create)、读取查询(Retrieve)、更新(Update)、删除(Delete)**

### 第01节(INSERT)

@import "廖雪峰SQL教程19.jpg"

```

-- 添加新记录

INSERT INTO students (class_id, name, gender, score) VALUES (2, '大牛', 'M', 80);
# 字段顺序不必和数据库表字段顺序一致,但VALUES子句需依次写出对应字段的值;字段有默认值,可以不写


-- 添加多条新记录
INSERT INTO students (class_id, name, gender, score) VALUES
  (1, '大宝', 'M', 87),
  (2, '二宝', 'M', 81);

```

### 第02节(UPDATE)

@import "廖雪峰SQL教程20.jpg"

```

-- 更新id=1的记录;更新id=5,6,7的记录

UPDATE students SET name='大牛', score=66 WHERE id=1;
UPDATE students SET name='小牛', score=77 WHERE id>=5 AND id<=7;

-- 更新字段可用表达式

UPDATE students SET score=score+10 WHERE score<80;
# 80分以下同学成绩加10分


WHERE条件没有匹配,UPDATE语句不会报错,也不会有记录更新;UPDATE语句可以没有WHERE条件
执行UPDATE语句,最好先SELECT语句测试WHERE条件是否筛选出期望的记录集,然后再UPDATE更新

UPDATE students SET score=60;
# 整个表所有记录都会被更新

使用MySQL,UPDATE语句会返回更新的行数以及WHERE条件匹配的行数。

```

### 第03节(DELETE)

@import "廖雪峰SQL教程21.jpg"

```

-- 删除id=1的记录;删除id=5,6,7的记录

DELETE FROM students WHERE id=1;
DELETE FROM students WHERE id>=5 AND id<=7;


WHERE条件没有匹配,DELETE语句不会报错,也不会有记录被删除;
和UPDATE类似,不带WHERE条件的DELETE语句会删除整个表数据

执行DELETE语句,最好先SELECT语句测试WHERE条件是否筛选出期望的记录集,然后再DELETE删除
使用MySQL,DELETE语句会返回删除的行数以及WHERE条件匹配的行数。

```

## 第S06章(MySQL)

@import "廖雪峰SQL教程22.jpg"

```

命令提示符>>>mysql -u root -p>>>root口令>>>正确,连接MySQL Server,提示符变为mysql>

快捷方式:MySQL 8.0 Command Line Client - Unicode;输exit断开与MySQL Server连接;


MySQL Server是真正的MySQL服务器;MySQL Client是命令行客户端;
MySQL Client可执行程序是**mysql**,MySQL Server可执行程序是**mysqld**

MySQL Client输入SQL语句通过TCP连接发送到MySQL Server;默认端口号3306,若本机为127.0.0.1:3306


假设远程MySQL Server的IP地址是10.0.1.99,则:

mysql -h 10.0.1.99 -u root -p
# -h指定IP或域名

```

### 第01节(管理MySQL)

@import "廖雪峰SQL教程23.jpg"

```

MySQL Workbench是图形客户端,以可视化图形界面查询、创建和修改数据库表;


列出所有数据库,创建新数据库,删除数据库
mysql> SHOW DATABASES;
mysql> CREATE DATABASE test;
mysql> DROP DATABASE test;


information_schema、mysql、performance_schema和sys是系统库,不要改动,其余是用户创建的数据库。
删除数据库将导致该数据库的所有表全部被删除。

对数据库操作,首先切换为当前数据库
mysql> USE test;

列出当前数据库的所有表;查看表结构;查看创建表;创建表;删除表;
mysql> SHOW TABLES;
mysql> DESC students;
mysql> SHOW CREATE TABLE students;
mysql> CREATE TABLE students;
mysql> DROP TABLE students;


表新增列;修改列;删除列
ALTER TABLE students ADD COLUMN birth VARCHAR(10) NOT NULL;
ALTER TABLE students CHANGE COLUMN birth birthday VARCHAR(20) NOT NULL;
ALTER TABLE students DROP COLUMN birthday;


mysql> EXIT
Bye
# EXIT断开客户端和服务器的连接,MySQL服务器仍继续运行

```

### 第02节(实用SQL语句)

@import "廖雪峰SQL教程24.jpg"

```

插入或替换
REPLACE INTO students (id, class_id, name, gender, score) VALUES (1, 1, '小明', 'F', 99);


插入或更新
INSERT INTO students (id, class_id, name, gender, score) VALUES (1, 1, '小明', 'F', 99) ON DUPLICATE KEY UPDATE name='小明', gender='F', score=99;


插入或忽略
INSERT IGNORE INTO students (id, class_id, name, gender, score) VALUES (1, 1, '小明', 'F', 99);


快照
-- 对class_id=1进行快照,存储为新表students_of_class1,表结构和SELECT表结构完全一致
CREATE TABLE students_of_class1 SELECT * FROM students WHERE class_id=1;


写入查询结果集
-- 创建表statistics
CREATE TABLE statistics (
    id BIGINT NOT NULL AUTO_INCREMENT,
    class_id BIGINT NOT NULL,
    average DOUBLE NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO statistics (class_id, average) SELECT class_id, AVG(score) FROM students GROUP BY class_id;
# INSERT语句的列和SELECT语句的列要对应

```

## 第S07章(事务)

@import "廖雪峰SQL教程25.jpg"

```

多条语句作为整体进行操作,称为数据库事务

数据库事务ACID4个特性：
•A：Atomic,原子性,将所有SQL作为原子工作单元执行,要么全部执行,要么全部不执行；
•C：Consistent,一致性,事务完成后,所有数据状态一致,即A账户只要减去100,B账户必定加上了100；
•I：Isolation,隔离性,如果有多个事务并发执行,每个事务作出的修改必须与其他事务隔离；
•D：Duration,持久性,即事务完成后,对数据库数据的修改被持久化存储。

单条SQL语句,数据库系统自动将其作为一个事务执行,这种事务被称为隐式事务。
多条SQL语句,使用BEGIN开启,COMMIT提交,这种事务被称为显式事务。COMMIT语句执行失败,整个事务也失败。

BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;


-- 用ROLLBACK回滚事务,主动让整个事务失败
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
ROLLBACK;


脏读(Dirty Read)/不可重复读(Non Repeatable Read)/幻读(Phantom Read)
Isolation Level/Read Uncommitted/Read Committed/Repeatable Read/Serializable

```

### 第01节(Read Uncommitted)

@import "廖雪峰SQL教程26.jpg"

```

Read Uncommitted是隔离级别最低的事务级别,一个事务会读到另一个事务更新但未提交的数据。
如果另一个事务回滚,那么当前事务读到的数据就是脏数据,这就是脏读(Dirty Read)。

SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

```

### 第02节(Read Committed)

@import "廖雪峰SQL教程27.jpg"

```

Read Committed隔离级别,一个事务可能遇到不可重复读(Non Repeatable Read)问题。

SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

```

### 第03节(Repeatable Read)

@import "廖雪峰SQL教程28.jpg"

```

Repeatable Read隔离级别,一个事务可能遇到幻读(Phantom Read)问题。

SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

```

### 第04节(Serializable)

@import "廖雪峰SQL教程29.png"

```

Serializable是最严格的隔离级别,所有事务按照次序依次执行,脏读、不可重复读、幻读都不会出现。
但串行执行,效率大大下降,没有特别重要情景,一般不使用Serializable隔离级别

在MySQL中,没有指定隔离级别,如果使用InnoDB默认隔离级别是Repeatable Read。

```

*****
*****

## 第S81章(附录)

### 第01节(XXX)


## 第K01章(安装或升级到MySQL 8)

`MySQL 8 Cookbook(Gong_Book)`

### 第01节(引言)
### 第02节(使用YUM / APT安装MySQL)
### 第03节(使用RPM或DEB文件安装MySQL 8.0)
### 第04节(使用通用二进制文件在Linux系统上安装MySQL)
### 第05节(启动或停止MySQL 8的运行)
### 第06节(卸载MySQL 8)
### 第07节(用systemd管理MySQL服务器)
### 第08节(从MySQL 8.0降级)
### 第09节(升级到MySQL 8.0)
### 第10节(安装MySQL工具集)


## 第K02章(使用MySQL)

`MySQL 8 Cookbook(Gong_Book)`

### 第01节(引言)
### 第02节(使用命令行客户端连接到MySQL)
### 第03节(创建数据库)
### 第04节(创建表)
### 第05节(插入、更新和删除行)
### 第06节(加载示例数据)
### 第07节(查询数据)
### 第08节(对结果排序)
### 第09节(对结果分组(聚合函数))
### 第10节(创建用户)
### 第11节(授予和撤销用户的访问权限)
### 第12节(查询数据并保存到文件和表中)
### 第13节(将数据加载到表中)
### 第14节(表关联)
### 第15节(存储过程)
### 第16节(函数)
### 第17节(触发器)
### 第18节(视图)
### 第19节(事件)
### 第20节(获取有关数据库和表的信息)


## 第K03章(使用MySQL(进阶))

`MySQL 8 Cookbook(Gong_Book)`

### 第01节(引言)
### 第02节(使用JSON)
### 第03节(公用表表达式(CTE))
### 第04节(生成列(generated column))
### 第05节(窗口函数)


## 第K04章(配置MySQL)

`MySQL 8 Cookbook(Gong_Book)`

### 第01节(引言)
### 第02节(使用配置文件)
### 第03节(使用全局变量和会话变量)
### 第04节(在启动脚本中使用参数)
### 第05节(配置参数)
### 第06节(更改数据目录)


## 第K05章(事务)

`MySQL 8 Cookbook(Gong_Book)`

### 第01节(引言)
### 第02节(执行事务)
### 第03节(使用保存点)
### 第04节(隔离级别)
### 第05节(锁)


## 第K06章(二进制日志)

`MySQL 8 Cookbook(Gong_Book)`

### 第01节(引言)
### 第02节(使用二进制日志)
### 第03节(二进制日志的格式)
### 第04节(从二进制日志中提取语句)
### 第05节(忽略要写入二进制日志的数据库)
### 第06节(迁移二进制日志)


## 第K07章(备份)

`MySQL 8 Cookbook(Gong_Book)`

### 第01节(引言)
### 第02节(使用mysqldump进行备份)
### 第03节(使用mysqlpump进行备份)
### 第04节(使用mydumper进行备份)
### 第05节(使用普通文件进行备份)
### 第06节(使用XtraBackup进行备份)
### 第07节(锁定实例进行备份)
### 第08节(使用二进制日志进行备份)


## 第K08章(恢复数据)

`MySQL 8 Cookbook(Gong_Book)`

### 第01节(引言)
### 第02节(从mysqldump和mysqlpump中恢复)
### 第03节(使用myloader从mydumper中恢复)
### 第04节(从普通文件备份中恢复)
### 第05节(执行时间点恢复)


## 第K09章(复制)

`MySQL 8 Cookbook(Gong_Book)`

### 第01节(引言)
### 第02节(准备复制)
### 第03节(设置主主复制)
### 第04节(设置多源复制)
### 第05节(设置复制筛选器)
### 第06节(将从库由主从复制切换到链式复制)
### 第07节(将从库由链式复制切换到主从复制)
### 第08节(设置延迟复制)
### 第09节(设置GTID复制)
### 第10节(设置半同步复制)


## 第K10章(表维护)

`MySQL 8 Cookbook(Gong_Book)`

### 第01节(引言)
### 第02节(安装Percona工具包)
### 第03节(修改表结构)
### 第04节(在数据库之间移动表)
### 第05节(使用在线模式更改工具修改表)
### 第06节(归档表)
### 第07节(克隆表)
### 第08节(分区修剪和指定)
### 第09节(管理分区)
### 第10节(分区信息)
### 第11节(有效地管理生存时间和软删除行)


## 第K11章(管理表空间)

`MySQL 8 Cookbook(Gong_Book)`

### 第01节(引言)
### 第02节(更改InnoDB REDO日志文件的数量或大小)
### 第03节(调整InnoDB系统的表空间大小)
### 第04节(在数据目录之外创建独立表空间)
### 第05节(将独立表空间复制到另一个实例)
### 第06节(管理UNDO表空间)
### 第07节(管理通用表空间)
### 第08节(压缩InnoDB表)


## 第K12章(日志管理)

`MySQL 8 Cookbook(Gong_Book)`

### 第01节(引言)
### 第02节(管理错误日志)
### 第03节(管理通用查询日志和慢查询日志)
### 第04节(管理二进制日志)


## 第K13章(性能调优)

`MySQL 8 Cookbook(Gong_Book)`

### 第01节(引言)
### 第02节(explain计划)
### 第03节(基准查询和服务器)
### 第04节(添加索引)
### 第05节(不可见索引)
### 第06节(降序索引)
### 第07节(使用pt-query-digest分析慢查询)
### 第08节(优化数据类型)
### 第09节(删除重复和冗余索引)
### 第10节(检查索引的使用情况)
### 第11节(控制查询优化器)
### 第12节(使用索引提示(hint))
### 第13节(使用生成列为JSON建立索引)
### 第14节(使用资源组)
### 第15节(使用performance_schema)
### 第16节(使用sys schema)


## 第K14章(安全)

`MySQL 8 Cookbook(Gong_Book)`

### 第01节(引言)
### 第02节(安全安装)
### 第03节(限定网络和用户)
### 第04节(使用mysql_config_editor进行无密码认证)
### 第05节(重置root密码)
### 第06节(使用X509设置加密连接)
### 第07节(设置SSL复制)
















*****
*****

```Python

print('............................END............................')
print('............................END............................')
print('............................END............................')

```


