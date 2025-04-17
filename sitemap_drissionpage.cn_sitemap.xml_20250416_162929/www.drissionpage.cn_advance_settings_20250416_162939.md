# Content from: https://www.drissionpage.cn/advance/settings

[跳到主要内容](https://www.drissionpage.cn/advance/settings#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/advance/settings)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/advance/settings)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/intro)
  * [🛫 SessionPage](https://www.drissionpage.cn/SessionPage/intro)
  * [🧰 进阶使用](https://www.drissionpage.cn/download/intro)
    * [⬇️ 下载文件](https://www.drissionpage.cn/download/intro)
    * [⚙️ 配置文件的使用](https://www.drissionpage.cn/advance/ini)
    * [⚙️ 全局设置](https://www.drissionpage.cn/advance/settings)
    * [⚙️ 命令行的使用](https://www.drissionpage.cn/advance/commands)
    * [⚙️ 异常的使用](https://www.drissionpage.cn/advance/errors)
    * [⚙️ 数据读取加速](https://www.drissionpage.cn/advance/accelerate)
    * [⚙️ 打包程序](https://www.drissionpage.cn/advance/packaging)
    * [⚙️ 实用工具](https://www.drissionpage.cn/advance/tools)
    * [⚙️ 与其它项目对接](https://www.drissionpage.cn/advance/docking)


  * [](https://www.drissionpage.cn/)
  * 🧰 进阶使用
  * ⚙️ 全局设置


本页总览
# ⚙️ 全局设置
有一些运行时的全局设置，可以控制程序某些行为。
## ✅️️ 使用方式[​](https://www.drissionpage.cn/advance/settings#️️-使用方式 "✅️️ 使用方式的直接链接")
全局设置在`DrissionPage.common`路径中。
以`set_****()`的方式对属性进行设置。
设置方法会返回`Settings`类本身，所以支持链式操作。
使用方法：
```
from DrissionPage.common import SettingsSettings.set_raise_when_wait_failed(True)# 设置等待失败时抛出异常Settings.set_language('en')# 设置报错使用英文Settings.set_raise_when_wait_failed(True).set_auto_handle_alert(True)# 链式操作
```

## ✅️️ 设置项[​](https://www.drissionpage.cn/advance/settings#️️-设置项 "✅️️ 设置项的直接链接")
### 📌 `set_raise_when_ele_not_found()`[​](https://www.drissionpage.cn/advance/settings#-set_raise_when_ele_not_found "-set_raise_when_ele_not_found的直接链接")
设置找不到元素时，是否抛出异常。初始为`False`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `bool`表示开或关  
**返回：**`Settings`
### 📌 `set_raise_when_click_failed()`[​](https://www.drissionpage.cn/advance/settings#-set_raise_when_click_failed "-set_raise_when_click_failed的直接链接")
设置点击失败时，是否抛出异常。初始为`False`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `bool`表示开或关  
**返回：**`Settings`
### 📌 `set_raise_when_wait_failed()`[​](https://www.drissionpage.cn/advance/settings#-set_raise_when_wait_failed "-set_raise_when_wait_failed的直接链接")
设置等待失败时，是否抛出异常。初始为`False`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `bool`表示开或关  
**返回：**`Settings`
### 📌 `set_singleton_tab_obj()`[​](https://www.drissionpage.cn/advance/settings#-set_singleton_tab_obj "-set_singleton_tab_obj的直接链接")
设置 Tab 对象是否使用单例模式。初始为`True`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `bool`表示开或关  
**返回：**`Settings`
### 📌 `set_cdp_timeout()`[​](https://www.drissionpage.cn/advance/settings#-set_cdp_timeout "-set_cdp_timeout的直接链接")
设置 cdp 执行超时（秒），初始为`30`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`second`| `float`| 必填| 秒数  
**返回：**`Settings`
### 📌 `set_browser_connect_timeout()`[​](https://www.drissionpage.cn/advance/settings#-set_browser_connect_timeout "-set_browser_connect_timeout的直接链接")
设置连接浏览器的超时时间（秒）。初始为`30`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`second`| `float`| 必填| 秒数  
**返回：**`Settings`
### 📌 `set_auto_handle_alert()`[​](https://www.drissionpage.cn/advance/settings#-set_auto_handle_alert "-set_auto_handle_alert的直接链接")
全局的自动处理弹出设置。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`accept`| `bool``None`| `True`| 为`None`时不自动处理，为`True`时自动接受，为`False`时自动取消。  
**返回：**`Settings`
### 📌 `set_language()`[​](https://www.drissionpage.cn/advance/settings#-set_language "-set_language的直接链接")
设置报错和提示信息语言。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`code`| `str`| 必填| 可选`'zh_cn'`、`'en'`  
**返回：**`Settings`
### 📌 `set_suffixes_list()`[​](https://www.drissionpage.cn/advance/settings#-set_suffixes_list "-set_suffixes_list的直接链接")
设置用于解析域名后缀的本地文件路径。
默认会连网获取，离线环境下使用内置文件，可对此属性赋值手动指定路径。
通常离线环境下打包使用时需要设置。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| 必填| 文件路径  
**返回：**`Settings`
## ✅️️ 示例[​](https://www.drissionpage.cn/advance/settings#️️-示例 "✅️️ 示例的直接链接")
此示例设置找不到元素时立刻抛出异常（如不设置返回`NoneElement`）。
可直接执行查看效果。
```
from DrissionPage import SessionPagefrom DrissionPage.common import SettingsSettings.set_raise_when_ele_not_found(True)page = SessionPage()page.get('https://www.baidu.com')ele = page('#abcd')
```

**输出：**
```
...前面省略...DrissionPage.errors.ElementNotFoundError: 没有找到元素。method: ele()args: {'locator': '#abcd'}
```

[上一页⚙️ 配置文件的使用](https://www.drissionpage.cn/advance/ini)[下一页⚙️ 命令行的使用](https://www.drissionpage.cn/advance/commands)
  * [✅️️ 使用方式](https://www.drissionpage.cn/advance/settings#️️-使用方式)
  * [✅️️ 设置项](https://www.drissionpage.cn/advance/settings#️️-设置项)
    * [📌 `set_raise_when_ele_not_found()`](https://www.drissionpage.cn/advance/settings#-set_raise_when_ele_not_found)
    * [📌 `set_raise_when_click_failed()`](https://www.drissionpage.cn/advance/settings#-set_raise_when_click_failed)
    * [📌 `set_raise_when_wait_failed()`](https://www.drissionpage.cn/advance/settings#-set_raise_when_wait_failed)
    * [📌 `set_singleton_tab_obj()`](https://www.drissionpage.cn/advance/settings#-set_singleton_tab_obj)
    * [📌 `set_cdp_timeout()`](https://www.drissionpage.cn/advance/settings#-set_cdp_timeout)
    * [📌 `set_browser_connect_timeout()`](https://www.drissionpage.cn/advance/settings#-set_browser_connect_timeout)
    * [📌 `set_auto_handle_alert()`](https://www.drissionpage.cn/advance/settings#-set_auto_handle_alert)
    * [📌 `set_language()`](https://www.drissionpage.cn/advance/settings#-set_language)
    * [📌 `set_suffixes_list()`](https://www.drissionpage.cn/advance/settings#-set_suffixes_list)
  * [✅️️ 示例](https://www.drissionpage.cn/advance/settings#️️-示例)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/advance/settings)
  * [QQ群：391178600](https://www.drissionpage.cn/advance/settings)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
