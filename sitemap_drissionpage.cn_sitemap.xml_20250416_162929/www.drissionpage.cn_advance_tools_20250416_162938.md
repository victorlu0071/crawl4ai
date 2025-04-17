# Content from: https://www.drissionpage.cn/advance/tools

[跳到主要内容](https://www.drissionpage.cn/advance/tools#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/advance/tools)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/advance/tools)
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
  * ⚙️ 实用工具


本页总览
# ⚙️ 实用工具
`DrissionPage.common`路径可导入几个小工具。
## ✅️️ `make_session_ele()`[​](https://www.drissionpage.cn/advance/tools#️️-make_session_ele "️️-make_session_ele的直接链接")
此方法用于获取页面对象、元素对象或 html 文本的静态版本，或以其为基准搜索元素。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`html_or_ele`| `str``ChromiumElement``ChromiumPage``ChromiumTab``WebPage``MixTab``ChromiumFrame``ShdownRoot`| 必填| html文本、元素或页面对象  
`loc`| `str``Tuple[str, str]`| `None`| 定位元组或字符串，为`None`时不在下级查找，返回根元素  
`index`| `int`| `1`| 获取第几个元素，从`1`开始，可传入负数获取倒数第几个，`None`获取所有  
返回类型| 说明  
---|---  
`SessionElement`| `index`为数字时返回静态元素对象  
`SessionElementsList`| `index`为`None`时返回静态元素对象组成的列表  
**示例：**
```
from DrissionPage.common import make_session_elehtml ='''<html><body><div>abc</div></body></html>'''ele = make_session_ele(html)print(ele.text)
```

**输出：**
```
abc
```

## ✅️️ `get_blob()`[​](https://www.drissionpage.cn/advance/tools#️️-get_blob "️️-get_blob的直接链接")
此方法用于获取指定 blob 资源内容。
注意
  * 如果资源在异域`<iframe>`元素内，必须获取该`<iframe>`元素对象，再把该对象传入才能获取到
  * 本方法只能用于获取静态的资源，流媒体不可以


参数名称| 类型| 默认值| 说明  
---|---|---|---  
`page`| `ChromiumPage``ChromiumTab``WebPage``MixTab``ChromiumFrame`| 必填| 该资源所在的页面对象  
`url`| `str`| 必填| blob 资源 url  
`as_bytes`| `bool`| `True`| 是否以`bytes`类型返回  
返回类型| 说明  
---|---  
`str`| `as_bytes`参数为`False`时以 base64 格式返回  
`bytes`| `as_bytes`参数为`True`时以字节数据返回  
## ✅️️ `configs_to_here()`[​](https://www.drissionpage.cn/advance/tools#️️-configs_to_here "️️-configs_to_here的直接链接")
此方法用于把默认 ini 文件复制到当前路径。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`save_name`| `str`| `None`| 指定文件名，为`None`则命名为`'dp_configs.ini'`  
**返回：** `None`
## ✅️️ `wait_until()`[​](https://www.drissionpage.cn/advance/tools#️️-wait_until "️️-wait_until的直接链接")
此方法用于等待传入的方法返回值不为假。超时则抛出`TimeoutError`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`function`| `callable`| 必填| 要执行的方法  
`kwargs`| `dict`| `None`| 方法参数  
`timeout`| `float`| `10`| 超时时间（秒）  
**返回：** `Any`
## ✅️️ `tree()`[​](https://www.drissionpage.cn/advance/tools#️️-tree "️️-tree的直接链接")
此方法用于打印页面或元素结构。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`ele_or_page`| 所有页面和元素对象| 必填| 页面或元素对象  
`text`| `bool`| `False`| 是否打印元素文本  
`show_js`| `bool`| `False`| 打印文本时是否打印`<script>`标签内容  
`show_css`| `bool`| `False`| 打印文本时是否打印`<style>`标签内容  
**返回：** `None`
## ✅️️ `Keys`[​](https://www.drissionpage.cn/advance/tools#️️-keys "️️-keys的直接链接")
这是快速获取特殊按键和组合键的类。
## ✅️️ `By`[​](https://www.drissionpage.cn/advance/tools#️️-by "️️-by的直接链接")
与 selenium 的`By`类一致，方便项目迁移。
[上一页⚙️ 打包程序](https://www.drissionpage.cn/advance/packaging)[下一页⚙️ 与其它项目对接](https://www.drissionpage.cn/advance/docking)
  * [✅️️ `make_session_ele()`](https://www.drissionpage.cn/advance/tools#️️-make_session_ele)
  * [✅️️ `get_blob()`](https://www.drissionpage.cn/advance/tools#️️-get_blob)
  * [✅️️ `configs_to_here()`](https://www.drissionpage.cn/advance/tools#️️-configs_to_here)
  * [✅️️ `wait_until()`](https://www.drissionpage.cn/advance/tools#️️-wait_until)
  * [✅️️ `tree()`](https://www.drissionpage.cn/advance/tools#️️-tree)
  * [✅️️ `Keys`](https://www.drissionpage.cn/advance/tools#️️-keys)
  * [✅️️ `By`](https://www.drissionpage.cn/advance/tools#️️-by)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/advance/tools)
  * [QQ群：391178600](https://www.drissionpage.cn/advance/tools)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
