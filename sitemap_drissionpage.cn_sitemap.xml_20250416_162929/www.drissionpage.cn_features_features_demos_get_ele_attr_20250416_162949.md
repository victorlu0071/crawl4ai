# Content from: https://www.drissionpage.cn/features/features_demos/get_ele_attr

[跳到主要内容](https://www.drissionpage.cn/features/features_demos/get_ele_attr#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/features/features_demos/get_ele_attr)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/features/features_demos/get_ele_attr)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🔥 新版本介绍](https://www.drissionpage.cn/features/features_demos/get_ele_attr)
  * [💖 特性](https://www.drissionpage.cn/features/)
  * [🌟 特性演示](https://www.drissionpage.cn/features/features_demos/get_ele_attr)
    * [⭐ 与 requests 对比](https://www.drissionpage.cn/features/features_demos/requests)
    * [⭐ 与 selenium 对比](https://www.drissionpage.cn/features/features_demos/selenium)
    * [⭐ 模式切换](https://www.drissionpage.cn/features/features_demos/change_mode)
    * [⭐ 获取元素属性](https://www.drissionpage.cn/features/features_demos/get_ele_attr)
    * [⭐ 下载文件](https://www.drissionpage.cn/features/features_demos/download)


  * [](https://www.drissionpage.cn/)
  * 🌟 特性演示
  * ⭐ 获取元素属性


# ⭐ 获取元素属性
```
foot = tab.ele('#footer-left')# 用 id 查找元素first_col = foot.ele('css:>div')# 使用 css selector 在元素的下级中查找元素（第一个）lnk = first_col.ele('text:命令学')# 使用文本内容查找元素text = lnk.text # 获取元素文本href = lnk.attr('href')# 获取元素属性值print(text, href,'\n')# 简洁模式串联查找text = tab('@id:footer-left')('css:>div')('text:命令学').textprint(text)
```

**输出：**
```
Git 命令学习 https://oschina.gitee.io/learn-git-branching/Git 命令学习
```

[上一页⭐ 模式切换](https://www.drissionpage.cn/features/features_demos/change_mode)[下一页⭐ 下载文件](https://www.drissionpage.cn/features/features_demos/download)
作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/features/features_demos/get_ele_attr)
  * [QQ群：391178600](https://www.drissionpage.cn/features/features_demos/get_ele_attr)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
