# Content from: https://www.drissionpage.cn/browser_control/get_elements/simplify

[跳到主要内容](https://www.drissionpage.cn/browser_control/get_elements/simplify#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/get_elements/simplify)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/get_elements/simplify)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/get_elements/simplify)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/get_elements/simplify)
      * [🔦 概述](https://www.drissionpage.cn/browser_control/get_elements/intro)
      * [🔦 定位语法](https://www.drissionpage.cn/browser_control/get_elements/syntax)
      * [🔦 页面或元素内查找](https://www.drissionpage.cn/browser_control/get_elements/find_in_object)
      * [🔦 相对定位](https://www.drissionpage.cn/browser_control/get_elements/relative)
      * [🔦 行为模式](https://www.drissionpage.cn/browser_control/get_elements/behavior)
      * [🔦 在结果列表中筛选](https://www.drissionpage.cn/browser_control/get_elements/filter)
      * [🔦 简化写法](https://www.drissionpage.cn/browser_control/get_elements/simplify)
      * [🔦 语法速查表](https://www.drissionpage.cn/browser_control/get_elements/sheet)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/get_elements/simplify)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/get_elements/simplify)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🔎 查找元素
  * 🔦 简化写法


本页总览
# 🔦 简化写法
为进一步精简代码，定位语法都可以用简化形式来表示，使语句更短，链式操作时更清晰。
## ✅️ 定位符语法简化[​](https://www.drissionpage.cn/browser_control/get_elements/simplify#️-定位符语法简化 "✅️ 定位符语法简化的直接链接")
  * 定位语法都有其简化形式
  * 页面和元素对象都实现了`__call__()`方法，所以`page.ele('****')`可简化为`page('****')`
  * 查找方法都支持链式操作


示例：
```
# 查找tag为div的元素ele = tab.ele('tag:div')# 原写法ele = tab('t:div')# 简化写法# 用xpath查找元素ele = tab.ele('xpath://****')# 原写法ele = tab('x://****')# 简化写法# 查找text为'something'的元素ele = tab.ele('text=something')# 原写法ele = tab('tx=something')# 简化写法
```

简化写法对应列表
原写法| 简化写法| 说明  
---|---|---  
`@id`| `#`| 表示 id 属性，简化写法只在语句最前面且单独使用时生效  
`@class`| `.`| 表示 class 属性，简化写法只在语句最前面且单独使用时生效  
`text`| `tx`| 按文本匹配  
`@text()`| `@tx()`| 按文本查找，与 @ 或 @@ 配合使用时  
`tag`| `t`| 按标签类型匹配  
`@tag()`| `@t()`| 按元素名查找，与 @ 或 @@ 配合使用时  
`xpath`| `x`| 用 xpath 方式查找元素  
`css`| `c`| 用 css selector 方式查找元素  
## ✅️ shadow root 简化[​](https://www.drissionpage.cn/browser_control/get_elements/simplify#️-shadow-root-简化 "✅️ shadow root 简化的直接链接")
一般获取元素的 shadow root 元素，用`ele.shadow_root`属性。
由于此属性经常用于大量链式操作，名字太长影响可读性，因此可简化为`ele.sr`
**示例：**
```
txt = ele.sr('t:div').text
```

## ✅️ 相对定位参数简化[​](https://www.drissionpage.cn/browser_control/get_elements/simplify#️-相对定位参数简化 "✅️ 相对定位参数简化的直接链�接")
相对定位时，有时需要获取当前元素后某个元素，而不关心该元素是什么类型，一般是这样写：`ele.next(index=2)`。
但有一种简化的写法，可以直接写作`ele.next(2)`。
当第一个参数`filter_loc`接收数字时，会自动将其视作序号，替代`index`参数。因此书写可以稍微精简一些。
**示例：**
```
ele2 = ele1.parent(2)ele2 = ele1.next(2)('tx=****')ele2 = ele1.before(2)# 如此类推
```

[上一页🔦 在结果列表中筛选](https://www.drissionpage.cn/browser_control/get_elements/filter)[下一页🔦 语法速查表](https://www.drissionpage.cn/browser_control/get_elements/sheet)
  * [✅️ 定位符语法简化](https://www.drissionpage.cn/browser_control/get_elements/simplify#️-定位符语法简化)
  * [✅️ shadow root 简化](https://www.drissionpage.cn/browser_control/get_elements/simplify#️-shadow-root-简化)
  * [✅️ 相对定位参数简化](https://www.drissionpage.cn/browser_control/get_elements/simplify#️-相对定位参数简化)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/get_elements/simplify)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/get_elements/simplify)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
