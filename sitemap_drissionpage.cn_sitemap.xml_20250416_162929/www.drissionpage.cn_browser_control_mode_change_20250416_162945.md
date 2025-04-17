# Content from: https://www.drissionpage.cn/browser_control/mode_change

[跳到主要内容](https://www.drissionpage.cn/browser_control/mode_change#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/mode_change)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/mode_change)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/mode_change)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/mode_change)
    * [🛰️ 元素交互](https://www.drissionpage.cn/browser_control/ele_operation)
    * [🛰️ 获取元素信息](https://www.drissionpage.cn/browser_control/get_ele_info)
    * [🛰️ iframe 操作](https://www.drissionpage.cn/browser_control/iframe)
    * [🛰️ 动作链](https://www.drissionpage.cn/browser_control/actions)
    * [🛰️ 模式切换](https://www.drissionpage.cn/browser_control/mode_change)
    * [🛰️ 等待](https://www.drissionpage.cn/browser_control/waiting)
    * [🛰️ 监听网络数据](https://www.drissionpage.cn/browser_control/listener)
    * [🛰️ 获取控制台信息](https://www.drissionpage.cn/browser_control/console)
    * [🛰️ 截图和录像](https://www.drissionpage.cn/browser_control/screen)
    * [🛰️ 上传文件](https://www.drissionpage.cn/browser_control/upload)
    * [🛰️ Page 对象](https://www.drissionpage.cn/browser_control/pages)
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/mode_change)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/mode_change)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 模式切换


本页总览
# 🛰️ 模式切换
`MixTab`和`WebPage`有两种模式，d 模式用于控制浏览器，s 模式使用`requests`收发数据包。
两种模式访问页面和提取数据的逻辑是一致的，使用同一套 api。
每个标签页对象创建时都处于 d 模式。
使用`change_mode()`方法进行切换。模式切换的时候会同步登录信息。
s 模式下仍然可以控制浏览器，但因为共用 api，`ele()`等两种模式共用的方法，查找对象是`requests`的结果，而非浏览器。
因此 s 模式下要控制浏览器，只能调用 d 模式独有的功能。
在切换模式前已获取的元素对象则可继续操作。
Tips
切换到 s 模式后，如不再需要浏览器，可以用`close()`或`quit()`方法关闭标签页或浏览器。标签页对象继续用于收发数据包。
## ✅️️ 示例[​](https://www.drissionpage.cn/browser_control/mode_change#️️-示例 "✅️️ 示例的直接链接")
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('http://DrissionPage.cn')print(tab.title)# 打印d模式下网页titletab.change_mode()# 切换到s模式，切换时会自动访问d模式的urlprint(tab.title)# 打印s模式下网页title
```

**输出：**
```
DrissionPage官网DrissionPage官网
```

## ✅️️ 相关属性和方法[​](https://www.drissionpage.cn/browser_control/mode_change#️️-相关属性和方法 "✅️️ 相关属性和方法的直接链接")
### 📌️ `mode`[​](https://www.drissionpage.cn/browser_control/mode_change#️-mode "️-mode的直接链接")
此属性返回当前模式。`'d'`或`'s'`。
**类型：**`str`
### 📌 `change_mode()`[​](https://www.drissionpage.cn/browser_control/mode_change#-change_mode "-change_mode的直接链接")
此方法用于切换运行模式。
切换模式时默认复制当前 cookies 到目标模式，且使用当前 url 进行跳转。
注意
切换模式时只同步 cookies，不同步 headers，如果网站要求特定的 headers 才能访问，就会卡住直到超时。 这时可以设置`go`为`False`，切换 s 模式后再自己构造 headers 访问。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`mode`| `str``None`| `None`| 接收`'s'`或`'d'`，以切换到指定模式接收`None`则切换到与当前相对的另一个模式  
`go`| `bool`| `True`| 目标模式是否跳转到原模式的 url  
`copy_cookies`| `bool`| `True`| 切换时是否复制 cookies 到目标模式  
**返回：**`None`
### 📌 `cookies_to_session()`[​](https://www.drissionpage.cn/browser_control/mode_change#-cookies_to_session "-cookies_to_session的直接链接")
此方法用于复制浏览器当前页面的 cookies 到`Session`对象。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`copy_user_agent`| `bool`| `True`| 是否复制 user agent 信息  
**返回：**`None`
### 📌 `cookies_to_browser()`[​](https://www.drissionpage.cn/browser_control/mode_change#-cookies_to_browser "-cookies_to_browser的直接链接")
此方法用于把`Session`对象的 cookies 复制到浏览器。
**参数：** 无
**返回：**`None`
## ✅️️ 说明[​](https://www.drissionpage.cn/browser_control/mode_change#️️-说明 "✅️️ 说明的直接链接")
  * 主要的 api 两种模式是共用的，如`get()`，d 模式下控制浏览跳转，s 模式下控制`Session`对象跳转
  * s 模式下获取的元素对象为`SessionElement`，d 模式下为`ChromiumElement`等
  * `post()`方法无论在哪种模式下都能使用
  * s 模式下也能控制浏览器，但只能使用 d 模式独有功能控制


[上一页🛰️ 动作链](https://www.drissionpage.cn/browser_control/actions)[下一页🛰️ 等待](https://www.drissionpage.cn/browser_control/waiting)
  * [✅️️ 示例](https://www.drissionpage.cn/browser_control/mode_change#️️-示例)
  * [✅️️ 相关属性和方法](https://www.drissionpage.cn/browser_control/mode_change#️️-相关属性和方法)
    * [📌️ `mode`](https://www.drissionpage.cn/browser_control/mode_change#️-mode)
    * [📌 `change_mode()`](https://www.drissionpage.cn/browser_control/mode_change#-change_mode)
    * [📌 `cookies_to_session()`](https://www.drissionpage.cn/browser_control/mode_change#-cookies_to_session)
    * [📌 `cookies_to_browser()`](https://www.drissionpage.cn/browser_control/mode_change#-cookies_to_browser)
  * [✅️️ 说明](https://www.drissionpage.cn/browser_control/mode_change#️️-说明)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/mode_change)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/mode_change)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
