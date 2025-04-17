# Content from: https://www.drissionpage.cn/SessionPage/create_obj

[跳到主要内容](https://www.drissionpage.cn/SessionPage/create_obj#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/SessionPage/create_obj)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/SessionPage/create_obj)
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
  * 🛩️ 创建页面对象


本页总览
# 🛩️ 创建页面对象
## ✅️️ `SessionPage`初始化参数[​](https://www.drissionpage.cn/SessionPage/create_obj#️️-sessionpage初始化参数 "️️-sessionpage初始化参数的直接链接")
初始化参数| 类型| 默认值| 说明  
---|---|---|---  
`session_or_options`| `Session``SessionOptions`| `None`| 传入`Session`对象时使用该对象收发数据包；传入`SessionOptions`对象时用该配置创建`Session`对象；为`None`则从 ini 文件读取，为`False`则不从 ini 文件读取，而用内置默认配置  
## ✅️️ 直接创建[​](https://www.drissionpage.cn/SessionPage/create_obj#️️-直接创建 "✅️️ 直接创建的直接链接")
这种方式代码最简洁，程序会从配置文件中读取配置，自动生成页面对象。
```
from DrissionPage import SessionPagepage = SessionPage()
```

`SessionPage`无需控制浏览器，无需做任何配置即可使用。
直接创建时，程序默认读取 ini 文件配置，如 ini 文件不存在，会使用内置配置。
默认 ini 和内置配置信息详见 “进阶使用->配置文件的使用” 章节。
## ✅️️ 通过配置信息创建[​](https://www.drissionpage.cn/SessionPage/create_obj#️️-通过配置信息创建 "✅️️ 通过配置信息创建的直接链接")
如果需要在使用前进行一些配置，可使用`SessionOptions`。它是专门用于设置`Session`对象初始状态的类，内置了常用的配置。详细使用方法见 “启动配置” 一节。
### 📌 使用方法[​](https://www.drissionpage.cn/SessionPage/create_obj#-使用方法 "📌 使用方法的直接链接")
在`SessionPage`创建时，将已创建和设置好的`SessionOptions`对象以参数形式传递进去即可。
初始化参数| 类型| 默认值| 说明  
---|---|---|---  
`read_file`| `bool`| `True`| 是否从 ini 文件中读取配置信息  
`ini_path`| `str`| `None`| 文件路径，为`None`则读取默认 ini 文件  
注意
`Session`对象创建后再修改这个配置是没有效果的。
```
# 导入 SessionOptionsfrom DrissionPage import SessionPage, SessionOptions# 创建配置对象，并设置代理信息so = SessionOptions().set_proxies(http='127.0.0.1:1080')# 用该配置创建页面对象page = SessionPage(session_or_options=so)
```

Tips
您可以把配置保存到配置文件以后自动读取，详见 “启动配置” 章节。
### 📌 从指定 ini 文件创建[​](https://www.drissionpage.cn/SessionPage/create_obj#-从指定-ini-文件创建 "📌 从指定 ini 文件创建的直接链接")
以上方法是使用默认 ini 文件中保存的配置信息创建对象，你可以保存一个 ini 文件到别的地方，并在创建对象时指定使用它。
```
from DrissionPage import SessionPage, SessionOptions# 创建配置对象时指定要读取的ini文件路径so = SessionOptions(ini_path=r'./config1.ini')# 使用该配置对象创建页面page = SessionPage(session_or_options=so)
```

### 📌 不使用 ini 文件[​](https://www.drissionpage.cn/SessionPage/create_obj#-不使用-ini-文件 "📌 不使用 ini 文件的直接链接")
可以用以下方法，指定不使用 ini 文件的配置，而把配置写在代码中。
```
from DrissionPage import SessionPage, SessionOptionsso = SessionOptions(read_file=False)# read_file设为Falseso.set_retry(5)page = SessionPage(so)
```

## ✅️️ 传递控制权[​](https://www.drissionpage.cn/SessionPage/create_obj#️️-传递控制权 "✅️️ 传递控制权的直接链接")
当需要使用多个页面对象共同操作一个页面时，可在页面对象创建时接收另一个页面间对象传递过来的`Session`对象，以达到多个页面对象同时使用一个`Session`对象的效果。
```
from DrissionPage import SessionPage# 创建一个页面page1 = SessionPage()# 获取页面对象内置的Session对象session = page1.session# 在第二个页面对象初始化时传递该对象page2 = SessionPage(session_or_options=session)
```

[上一页🛩️ 概述](https://www.drissionpage.cn/SessionPage/intro)[下一页🛩️ 访问网页](https://www.drissionpage.cn/SessionPage/visit)
  * [✅️️ `SessionPage`初始化参数](https://www.drissionpage.cn/SessionPage/create_obj#️️-sessionpage初始化参数)
  * [✅️️ 直接创建](https://www.drissionpage.cn/SessionPage/create_obj#️️-直接创建)
  * [✅️️ 通过配置信息创建](https://www.drissionpage.cn/SessionPage/create_obj#️️-通过配置信息创建)
    * [📌 使用方法](https://www.drissionpage.cn/SessionPage/create_obj#-使用方法)
    * [📌 从指定 ini 文件创建](https://www.drissionpage.cn/SessionPage/create_obj#-从指定-ini-文件创建)
    * [📌 不使用 ini 文件](https://www.drissionpage.cn/SessionPage/create_obj#-不使用-ini-文件)
  * [✅️️ 传递控制权](https://www.drissionpage.cn/SessionPage/create_obj#️️-传递控制权)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/SessionPage/create_obj)
  * [QQ群：391178600](https://www.drissionpage.cn/SessionPage/create_obj)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
