# Content from: https://www.drissionpage.cn/features/features_demos/change_mode

[跳到主要内容](https://www.drissionpage.cn/features/features_demos/change_mode#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/features/features_demos/change_mode)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/features/features_demos/change_mode)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🔥 新版本介绍](https://www.drissionpage.cn/features/features_demos/change_mode)
  * [💖 特性](https://www.drissionpage.cn/features/)
  * [🌟 特性演示](https://www.drissionpage.cn/features/features_demos/change_mode)
    * [⭐ 与 requests 对比](https://www.drissionpage.cn/features/features_demos/requests)
    * [⭐ 与 selenium 对比](https://www.drissionpage.cn/features/features_demos/selenium)
    * [⭐ 模式切换](https://www.drissionpage.cn/features/features_demos/change_mode)
    * [⭐ 获取元素属性](https://www.drissionpage.cn/features/features_demos/get_ele_attr)
    * [⭐ 下载文件](https://www.drissionpage.cn/features/features_demos/download)


  * [](https://www.drissionpage.cn/)
  * 🌟 特性演示
  * ⭐ 模式切换


# ⭐ 模式切换
用浏览器登录网站，然后切换到 requests 读取网页。两者会共享登录信息。
```
from DrissionPage import Chromium# 创建页面对象tab = Chromium().latest_tab # 访问个人中心页面（未登录，重定向到登录页面）tab.get('https://gitee.com/profile')# 输入账号密码登录tab.ele('@id:user_login').input('您的用户名')tab.ele('@id:user_password').input('您的密码\n')tab.wait.load_start()# 切换到 s 模式tab.change_mode()# 登录后 session 模式的输出print('登录后title：', tab.title,'\n')
```

**输出：**
```
登录后title： 个人资料 - 码云 Gitee.com
```

[上一页⭐ 与 selenium 对比](https://www.drissionpage.cn/features/features_demos/selenium)[下一页⭐ 获取元素属性](https://www.drissionpage.cn/features/features_demos/get_ele_attr)
作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/features/features_demos/change_mode)
  * [QQ群：391178600](https://www.drissionpage.cn/features/features_demos/change_mode)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
