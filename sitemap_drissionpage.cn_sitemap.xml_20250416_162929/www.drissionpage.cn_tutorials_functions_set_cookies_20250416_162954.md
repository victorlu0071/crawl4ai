# Content from: https://www.drissionpage.cn/tutorials/functions/set_cookies

[跳到主要内容](https://www.drissionpage.cn/tutorials/functions/set_cookies#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/tutorials/functions/set_cookies)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/tutorials/functions/set_cookies)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索
  * [🌏️ 知识星球](https://www.drissionpage.cn/tutorials/xingqiu)
  * [🎞️ 视频教程](https://www.drissionpage.cn/tutorials/video)
  * [🗨️ 公众号](https://www.drissionpage.cn/tutorials/gongzhonghao)
  * [📚 离线文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=11372029&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [👍 浏览器插件](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=11372024&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [❓ 常见问题](https://www.drissionpage.cn/tutorials/QandA)
  * [🥬 功能示例](https://www.drissionpage.cn/tutorials/functions/new_browser)
    * [🥦 创建全新的浏览器](https://www.drissionpage.cn/tutorials/functions/new_browser)
    * [🥦 浏览器多开](https://www.drissionpage.cn/tutorials/functions/create_browsers)
    * [🥦 无头模式](https://www.drissionpage.cn/tutorials/functions/headless)
    * [🥦 设置 cookies](https://www.drissionpage.cn/tutorials/functions/set_cookies)


  * [](https://www.drissionpage.cn/)
  * 🥬 功能示例
  * 🥦 设置 cookies


本页总览
# 🥦 设置 cookies
## ✅️️ 设置 cookies[​](https://www.drissionpage.cn/tutorials/functions/set_cookies#️️-设置-cookies "✅️️ 设置 cookies的直接链接")
### 📌 页面对象中设置[​](https://www.drissionpage.cn/tutorials/functions/set_cookies#-页面对象中设置 "📌 页面对象中设置的直接链接")
任意页面对象都有`set.cookies()`方法，用于设置 cookies。
该方法接收多种格式的 cookies 信息，可设置一个或多个 cookies。
使用浏览器时，任意页面对象设置的 cookies 是所有标签页共用的（由`new_tab(new_context=True)`创建的标签页除外）。
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabcookies ='name1=value1; name2=value2; path=/; domain=.example.com;'tab.set.cookies(cookies)
```

### 📌 `SessionOptions`中设置[​](https://www.drissionpage.cn/tutorials/functions/set_cookies#-sessionoptions中设置 "-sessionoptions中设置的直接链接")
`SessionOptions`对象有`set_cookies()`方法，可接收一个或多个 cookies，用于`SessionPage`初始化时设置 cookies。
每次设置会覆盖之前所有 cookies 信息。
**示例：**
```
from DrissionPage import SessionOptionscookies ='name1=value1; name2=value2; path=/; domain=.example.com;'co = SessionOptions()co.set_cookies(cookies)
```

### 📌 删除 cookies[​](https://www.drissionpage.cn/tutorials/functions/set_cookies#-删除-cookies "📌 删除 cookies的直接链接")
页面对象用`set.cookies.remove()`和`set.cookies.clear()`删除和清空 cookies。
`SessionOptions`对象用`set_cookies(None)`清空 cookies。
具体用法详见使用文档有关章节。
## ✅️️ cookies 格式[​](https://www.drissionpage.cn/tutorials/functions/set_cookies#️️-cookies-格式 "✅️️ cookies 格式的直接链接")
### 📌 设置一个 cookie[​](https://www.drissionpage.cn/tutorials/functions/set_cookies#-设置一个-cookie "📌 设置一个 cookie的直接链接")
设置一个 cookie 时，可传入`Cookie`、`dict`或`str`类型。
`dict`和`str`需要有`name`和`value`字段。
`str`多个字段间用`';'`或`','`分隔，但不能两种同时出现。
**格式：**
```
# dict类型{'name':'abc','value':'123','domain':'.example.com',...}# str类型'name=abc; value=123; domain=.example.com; ...'
```

### 📌 设置多个 cookies[​](https://www.drissionpage.cn/tutorials/functions/set_cookies#-设置多个-cookies "📌 设置多个 cookies的直接链接")
设置多个时，可传入`CookieJar`、`list`、`tuple`、`str`、`dict`类型。
列表里面可以放`Cookie`、`str`或`dict`类型，多个 cookies 格式可以是不同的。
注意
列表中如果放`str`或`dict`，每个项都只能是一个 cookie。
**格式：**
```
# dict类型{'abc':'123','def':'456','domain':'.example.com',...}# str类型'abc=123; def=456; domain=.example.com; ...'# list或tuple类型['name=123; domain=.example.com; ...','name=abc; value=123; domain=.example.com; ...']
```

### 📌 说明[​](https://www.drissionpage.cn/tutorials/functions/set_cookies#-说明 "📌 说明的直接链接")
cookies 中只有`name`和`value`字段是必须的，但如果没有`domain`字段，添加到浏览器时会自动添加。
添加的内容根据调用`set.cookies()`方法的对象 url 而定。
比如一个 Tab 对象当前 url 为`'https://www.baidu.com'`，添加无指定域名的 cookies 时，会自动添加该字段，内容为`'www.baidu.com'`。
[上一页🥦 无头模式](https://www.drissionpage.cn/tutorials/functions/headless)
  * [✅️️ 设置 cookies](https://www.drissionpage.cn/tutorials/functions/set_cookies#️️-设置-cookies)
    * [📌 页面对象中设置](https://www.drissionpage.cn/tutorials/functions/set_cookies#-页面对象中设置)
    * [📌 `SessionOptions`中设置](https://www.drissionpage.cn/tutorials/functions/set_cookies#-sessionoptions中设置)
    * [📌 删除 cookies](https://www.drissionpage.cn/tutorials/functions/set_cookies#-删除-cookies)
  * [✅️️ cookies 格式](https://www.drissionpage.cn/tutorials/functions/set_cookies#️️-cookies-格式)
    * [📌 设置一个 cookie](https://www.drissionpage.cn/tutorials/functions/set_cookies#-设置一个-cookie)
    * [📌 设置多个 cookies](https://www.drissionpage.cn/tutorials/functions/set_cookies#-设置多个-cookies)
    * [📌 说明](https://www.drissionpage.cn/tutorials/functions/set_cookies#-说明)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/tutorials/functions/set_cookies)
  * [QQ群：391178600](https://www.drissionpage.cn/tutorials/functions/set_cookies)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
