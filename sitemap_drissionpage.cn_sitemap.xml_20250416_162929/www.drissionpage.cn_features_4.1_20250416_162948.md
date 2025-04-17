# Content from: https://www.drissionpage.cn/features/4.1

[跳到主要内容](https://www.drissionpage.cn/features/4.1#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/features/4.1)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/features/4.1)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🔥 新版本介绍](https://www.drissionpage.cn/features/4.1)
    * [💥 4.1 功能介绍](https://www.drissionpage.cn/features/4.1)
    * [💥 4.0 功能介绍](https://www.drissionpage.cn/features/4)
    * [💥 3.2 功能介绍](https://www.drissionpage.cn/features/3)
  * [💖 特性](https://www.drissionpage.cn/features/)
  * [🌟 特性演示](https://www.drissionpage.cn/features/4.1)


  * [](https://www.drissionpage.cn/)
  * 🔥 新版本介绍
  * 💥 4.1 功能介绍


本页总览
# 💥 4.1 功能介绍
4.1 的最主要变化在于用`Chromium`对象替代`ChromiumPage`和`WebPage`对象。
从 DrissionPage 诞生的时候开始，就存在`DriverPage`和`MixPage`对象（后来的`ChromiumPage`和`WebPage`）用于控制浏览器。
这是因为 DrissionPage 最开始是基于 selenium 开发的。
selenium 只能通过切换焦点的方式操作标签页，无法同时操作多个。
所以一个 Page 对象对应一个 Driver 对象就足够了。
但随着新版的开发，基于 selenium 的设计逐渐被替换，Page 对象作为最后的遗留，不足也日渐显现：
  * 它是浏览器和一个标签页的合体，在概念上不容易理解
  * 它在管理标签页的开关、查找时候容易造成混淆
  * 它代码结构臃肿，不利于后续功能开发


而它的唯一优点，是在创建的时候可以少写一行代码。
因此，在 4.1，会刻意淡化 Page 对象的存在感，而改用`Chromium`对象作为程序入口。
由于已有大量项目使用`ChromiumPage`和`WebPage`进行开发，这两个对象仍然保留，功能不会有太大变化。
## ✅️ `Chromium`对象[​](https://www.drissionpage.cn/features/4.1#️-chromium对象 "️-chromium对象的直接链接")
`Chromium`对象用于连接浏览器，管理标签页和全局运行参数。
### 📌 连接浏览器[​](https://www.drissionpage.cn/features/4.1#-连接浏览器 "📌 连接浏览器的直接链接")
```
from DrissionPage import Chromiumbrowser = Chromium()
```

### 📌 标签页操作[​](https://www.drissionpage.cn/features/4.1#-标签页操作 "📌 标签页操作的直接链接")
```
from DrissionPage import Chromiumbrowser = Chromium()tab1 = browser.latest_tab # 获取最后激活的标签页对象tab2 = browser.get_tab(title='DrissionPage')# 获取指定标签页tab3 = browser.new_tab()# 新建标签页browser.activate_tab(tab2)# 将tab2提到最前面tab1.close()# 关闭标签页
```

### 📌 浏览器操作[​](https://www.drissionpage.cn/features/4.1#-浏览器操作 "📌 浏览器操作的直接链接")
```
from DrissionPage import Chromiumbrowser = Chromium()browser.set.cookies({'abc':'123'})# 设置cookiesbrowser.set.download_path('C:\\tmp')# 设置下载路径# 更多详见相关章节
```

## ✅️ api 变化[​](https://www.drissionpage.cn/features/4.1#️-api-变化 "✅️ api 变化的直接链接")
  * `WebPageTab`改名为`MixTab`
  * `SessionPage`、`ChromiumPage`和`WebPage`初始化时删除`timeout`提示，以后会废弃
  * `activate_tab()`取代`set.tab_to_front()`
  * 所有对象增加`find()`方法，用于同时匹配多个定位符
  * 页面对象增加`console`属性，可读取控制台信息
  * Frame 对象增加`set.property()`、`set.style()`、`link`
  * Tab 对象的`close()`方法增加`others`参数
  * `quit()`增加`del_data`参数
  * `cookies()`删除`as_dict`参数，增加`as_dict()`、`as_json`和`as_str()`方法
  * 浏览器页面和元素对象的`s_ele()`和`s_eles()`方法增加`tiemout`参数
  * 浏览器页面和元素对象增加`rect.scroll_position`属性
  * 元素对象增加`get_frame()`方法
  * 元素对象增加`timeout`属性
  * `parent()`和 shadow-root 内查找方法增加`timeout`参数
  * 动作链删除`db_click()`，各点击方法增加`times`参数
  * `wait.new_tab()`增加`curr_tab`参数
  * 滚动增加`scroll()`方法
  * `ChromiumOptions`增加`new_env()`方法，ini 文件增加`new_env`参数，用于指定必须用新环境
  * `ChromiumOptions`增加`is_headless`属性
  * `auto_port()`方法删除`tmp_path`参数
  * `wait.alert_closed()`增加`timeout`参数


## ✅️ 行为变化[​](https://www.drissionpage.cn/features/4.1#️-行为变化 "✅️ 行为变化的直接链接")
  * `Chromium`只返回`MixTab`类型的标签页对象
  * `ChromiumFrame`对象默认改为单例
  * `MixTab`和`MixPage`的`post()`方法必返回`Response`对象
  * 部分等待方法会返回调用者，方便链式操作
  * 元素对象各种动作返回元素本身，便于链式操作
  * 打印`NoneElement`改成详细信息
  * `src()`方法可获取`<link>`指向的文件内容
  * 录像改为 H.265 编码
  * `shadow_root`属性增加等待附加到元素（超时 10 秒）
  * `set.cookies()`忽略过期 cookie
  * `timeout`属性不再接受赋值


## ✅️ 优化和问题修复[​](https://www.drissionpage.cn/features/4.1#️-优化和问题修复 "✅️ 优化和问题修复的直接链接")
  * 优化连接浏览器失败报错
  * 优化`css_path`
  * 修复`new_tab()`在访客模式和隐私模式的问题
  * 修复 Frame 对象滚动填入`tuple`定位符报错问题
  * 修复`states.is_displayed`有些情况下不正确问题
  * 修复元素`link`属性不正确的问题
  * 修复 shadow-root 内用 css 找元素的一个问题
  * 修复异域`<iframe>`内元素屏幕坐标不准问题
  * 修复`new_tab=True`时下载路径不正确问题
  * 修复`attr()`填入大写字母无法获取问题


[下一页💥 4.0 功能介绍](https://www.drissionpage.cn/features/4)
  * [✅️ `Chromium`对象](https://www.drissionpage.cn/features/4.1#️-chromium对象)
    * [📌 连接浏览器](https://www.drissionpage.cn/features/4.1#-连接浏览器)
    * [📌 标签页操作](https://www.drissionpage.cn/features/4.1#-标签页操作)
    * [📌 浏览器操作](https://www.drissionpage.cn/features/4.1#-浏览器操作)
  * [✅️ api 变化](https://www.drissionpage.cn/features/4.1#️-api-变化)
  * [✅️ 行为变化](https://www.drissionpage.cn/features/4.1#️-行为变化)
  * [✅️ 优化和问题修复](https://www.drissionpage.cn/features/4.1#️-优化和问题修复)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/features/4.1)
  * [QQ群：391178600](https://www.drissionpage.cn/features/4.1)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
