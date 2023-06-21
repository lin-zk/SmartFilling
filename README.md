# 智填 - 基于数据库管理的网址信息标记库

![智填](https://github.com/lin-zk/SmartFilling/blob/main/SmartFilling_project/picture/icon/main.png)

## 项目简介
智填是一款基于数据库管理的网址信息标记库，旨在帮助用户高效管理网址信息和相关事务记录。该项目提供了管理员操作和用户操作两种模式，分别具有不同的功能和界面。

在管理员操作模式下，系统管理员可以通过管理员账号管理独立数据库 "user.db"，并使用管理员后台GUI进行账号管理。管理员操作模式支持以下功能：
- 管理员账号的手动添加和注销
- 后台密码修改和查看
- 实时更新用户的最新登录时间

在用户操作模式下，每个用户都拥有一个以账号命名的独立数据库和用户主页面GUI。用户操作模式支持以下功能：
- 可视化数据库操作界面嵌入用户主页面
- 增加记录、删除记录、刷新同步数据库、清空记录、修改记录等操作
- 自动更新修改时间
- 直接跳转到记录的网址或本地路径

本系统还提供了登录和注册的GUI界面，并与账号管理数据库连接，可以同步写入数据和更新登录时间。

## 功能特性
- 管理员操作模式：
  - 管理员账号管理
  - 后台GUI界面
  - 手动增加和注销账号
  - 后台密码修改和查看
  - 实时更新用户最新登录时间

- 用户操作模式：
  - 用户独立数据库
  - 用户主页面GUI界面
  - 可视化数据库操作界面
  - 增加记录、删除记录、刷新同步数据库、清空记录、修改记录
  - 自动更新修改时间
  - 网址信息直接跳转
  - 存储网址标记信息

## 技术要求
- Python 3.x
- SQLite

## 安装指南
1. 克隆本项目到本地:  
`git clone https://github.com/lin-zk/SmartFilling`
2. 打开项目路径下的`SmartFilling_v0.0.8`文件夹
3. 双击`智填.lnk`即可运行程序
4. 具体使用指南点击登录页面下的`帮助`即可查看
5. 项目路径下的`SmartFilling_project`文件夹存放项目源码


## 授权信息
本项目采用 [MIT 许可证](LICENSE)。

## 作者信息
- 作者：林政慷
- 联系方式：1751740699@qq.com
- GitHub：https://github.com/lin-zk

---

请注意，当前版本的智填仅作为标记库使用，数据库是使用本地SQLite数据库。数据安全性有待进一步提升。该项目在实现数据库云端化以及多端访问功能方面有未来版本的计划，同时还计划嵌入多平台登录、扫码登录等多样化功能。
