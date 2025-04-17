# Content from: https://www.drissionpage.cn/browser_control/get_elements/behavior

[跳到主要内容](https://www.drissionpage.cn/browser_control/get_elements/behavior#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/get_elements/behavior)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/get_elements/behavior)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/get_elements/behavior)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/get_elements/behavior)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/get_elements/behavior)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/get_elements/behavior)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🔎 查找元素
  * 🔦 行为模式


本页总览
# 🔦 行为模式
## ✅️ 等待元素[​](https://www.drissionpage.cn/browser_control/get_elements/behavior#️-等待元素 "✅️ 等待元素的直接链接")
由于网络、js 运行时间的不确定性，经常需要等待元素加载到 DOM 中才能使用。
浏览器所有查找元素操作都自带等待，时间默认跟随元素所在页面`timeout`属性（默认 10 秒），也可以在每次查找时单独设置，单独设置的等待时间不会改变页面原来设置。
### 📌 内置等待[​](https://www.drissionpage.cn/browser_control/get_elements/behavior#-内置等待 "📌 内置等待的直接链接")
```
from DrissionPage import Chromiumtab = Chromium().latest_tab# 设置查找元素超时时间为 5 秒tab.set.timeouts(5)# 使用页面超时时间来查找元素（5 秒）ele1 = tab.ele('search text')# 为这次查找页面独立设置等待时间（1 秒）ele1 = tab.ele('search text', timeout=1)# 查找后代元素，使用页面超时时间（5 秒）ele2 = ele1.ele('search text')# 查找后代元素，使用单独设置的超时时间（1 秒）ele2 = ele1.ele('some text', timeout=1)
```

### 📌 主动等待[​](https://www.drissionpage.cn/browser_control/get_elements/behavior#-主动等待 "📌 主动等待的直接链接")
页面对象的`wait.eles_loaded()`方法，可主动等待指定元素加载到 DOM。
用法详见等待章节。
## ✅️ 链式写法[​](https://www.drissionpage.cn/browser_control/get_elements/behavior#️-链式写法 "✅️ 链式写法的直接链接")
因为元素对象本身又可以查找对象，所有可实现多级链式操作，可使程序更简洁。
**示例：**
```
ele = tab.ele('#s_fm').ele('#su')
```

其中`ele()`可省略，简化写成：
```
ele = tab('#s_fm')('#su')
```

## ✅️ 找不到元素时[​](https://www.drissionpage.cn/browser_control/get_elements/behavior#️-找不到元素时 "✅️ 找不到元素时的直接链接")
### 📌 默认情况[​](https://www.drissionpage.cn/browser_control/get_elements/behavior#-默认情况 "📌 默认情况的直接链接")
默认情况下，找不到元素时不会立即抛出异常，而是返回一个`NoneElement`对象。
这个对象用`if`判断表现为`False`，调用其功能会抛出`ElementNotFoundError`异常。
这样可以用`if`判断是否找到元素，也可以用`try`去捕获异常。
查找多个元素找不到时，返回空的`list`。
**示例，用`if` 判断：**
```
ele = tab.ele('****')# 判断是否找到元素if ele:print('找到了。')ifnot ele:print('没有找到。')
```

**示例，用`try` 捕获：**
```
try:  ele.click()except ElementNotFoundError:print('没有找到。')
```

### 📌 立即抛出异常[​](https://www.drissionpage.cn/browser_control/get_elements/behavior#-立即抛出异常 "📌 立即抛出异常的直接链接")
如果想在找不到元素时立刻抛出异常，可以用以下方法设置。
此设置为全局有效，在项目开始时设置一次即可。
查找多个元素找不到时，依然返回空的`list`。
设置全局变量：
```
from DrissionPage.common import SettingsSettings.set_raise_when_ele_not_found(True)
```

**示例：**
```
from DrissionPage import Chromiumfrom DrissionPage.common import SettingsSettings.set_raise_when_ele_not_found(True)tab = Chromium().latest_tabtab.get('https://www.baidu.com')ele = tab('#abcd')# ('#abcd')这个元素不存在
```

输出：
```
DrissionPage.errors.ElementNotFoundError: 没有找到元素。method: ele()args: {'locator': '#abcd'}
```

### 📌 设置默认返回值[​](https://www.drissionpage.cn/browser_control/get_elements/behavior#-设置默认返回值 "📌 设置默认返回值的直接链接")
如果查找元素后要获取一个属性，但这个元素不一定存在，或者链式查找其中一个节点找不到，可以设置查找失败时返回的值，而不是抛出异常，可以简化一些采集逻辑。
使用浏览器页面对象的`set.NoneElement_value()`方法设置该值。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`value`| `Any`| `None`| 将返回的设定值  
`on_off`| `bool`| `True`| `bool`表示是否启用  
**返回：**`None`
**示例**
比如说，遍历页面上一个列表中多个对象，但其中有些元素可能缺失某个子元素，可以这样写：
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.set.NoneElement_value('没找到')for li in tab.eles('t:li'):  name = li('.name').text  age = li('.age').text  phone = li('.phone').text
```

这样，假如某个子元素不存在，不会抛出异常，而是返回`'没找到'`这个字符串。
[上一页🔦 相对定位](https://www.drissionpage.cn/browser_control/get_elements/relative)[下一页🔦 在结果列表中筛选](https://www.drissionpage.cn/browser_control/get_elements/filter)
  * [✅️ 等待元素](https://www.drissionpage.cn/browser_control/get_elements/behavior#️-等待元素)
    * [📌 内置等待](https://www.drissionpage.cn/browser_control/get_elements/behavior#-内置等待)
    * [📌 主动等待](https://www.drissionpage.cn/browser_control/get_elements/behavior#-主动等待)
  * [✅️ 链式写法](https://www.drissionpage.cn/browser_control/get_elements/behavior#️-链式写法)
  * [✅️ 找不到元素时](https://www.drissionpage.cn/browser_control/get_elements/behavior#️-找不到元素时)
    * [📌 默认情况](https://www.drissionpage.cn/browser_control/get_elements/behavior#-默认情况)
    * [📌 立即抛出异常](https://www.drissionpage.cn/browser_control/get_elements/behavior#-立即抛出异常)
    * [📌 设置默认返回值](https://www.drissionpage.cn/browser_control/get_elements/behavior#-设置默认返回值)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/get_elements/behavior)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/get_elements/behavior)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
