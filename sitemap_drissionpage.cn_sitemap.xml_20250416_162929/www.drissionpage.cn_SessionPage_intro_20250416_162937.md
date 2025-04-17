# Content from: https://www.drissionpage.cn/SessionPage/intro

[跳到主要内容](https://www.drissionpage.cn/SessionPage/intro#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/SessionPage/intro)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/SessionPage/intro)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/intro)
  * [🛫 SessionPage](https://www.drissionpage.cn/SessionPage/intro)
    * [🛩️ 概述](https://www.drissionpage.cn/SessionPage/intro)
    * [🛩️ 创建页面对象](https://www.drissionpage.cn/SessionPage/create_obj)
    * [🛩️ 访问网页](https://www.drissionpage.cn/SessionPage/visit)
    * [🛩️ 获取页面信息](https://www.drissionpage.cn/SessionPage/get_page_info)
    * [🛩️ 查找元素](https://www.drissionpage.cn/SessionPage/get_ele)
    * [🛩️ 获取元素信息](https://www.drissionpage.cn/SessionPage/get_ele_info)
    * [🛩️ 页面设置](https://www.drissionpage.cn/SessionPage/settings)
    * [🛩️ 启动配置](https://www.drissionpage.cn/SessionPage/session_opt)
  * [🧰 进阶使用](https://www.drissionpage.cn/download/intro)


  * [](https://www.drissionpage.cn/)
  * 🛫 SessionPage
  * 🛩️ 概述


# 🛩️ 概述
`SessionPage`对象和`WebPage`对象的 s 模式，可用收发数据包的形式访问网页。
`SessionPage`是一个使用使用`Session`（requests 库）对象的页面，封装了网络连接和结果解析功能，使收发数据包也可以像操作页面一样便利。
**示例：**
获取 gitee 推荐项目第一页所有项目。
```
# 导入from DrissionPage import SessionPage# 创建页面对象page = SessionPage()# 访问网页page.get('https://gitee.com/explore/all')# 在页面中查找元素items = page.eles('t:h3')# 遍历元素for item in items[:-1]:# 获取当前<h3>元素下的<a>元素  lnk = item('tag:a')# 打印<a>元素文本和href属性print(lnk.text, lnk.link)
```

**输出：**
```
七年觐汐/wx-calendar https://gitee.com/qq_connect-EC6BCC0B556624342/wx-calendarThingsPanel/thingspanel-go https://gitee.com/ThingsPanel/thingspanel-goAPITable/APITable https://gitee.com/apitable/APITableIndexea/ideaseg https://gitee.com/indexea/ideasegCcSimple/vue-plugin-hiprint https://gitee.com/CcSimple/vue-plugin-hiprintwilliam_lzw/ExDUIR.NET https://gitee.com/william_lzw/ExDUIR.NETanolis/ancert https://gitee.com/anolis/ancertcozodb/cozo https://gitee.com/cozodb/cozo后面省略...
```

[上一页🛰️ Page 对象](https://www.drissionpage.cn/browser_control/pages)[下一页🛩️ 创建页面对象](https://www.drissionpage.cn/SessionPage/create_obj)
作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/SessionPage/intro)
  * [QQ群：391178600](https://www.drissionpage.cn/SessionPage/intro)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
