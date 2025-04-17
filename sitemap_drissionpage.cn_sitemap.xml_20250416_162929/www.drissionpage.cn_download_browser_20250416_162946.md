# Content from: https://www.drissionpage.cn/download/browser

[跳到主要内容](https://www.drissionpage.cn/download/browser#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/download/browser)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/download/browser)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/download/browser)
  * [🛫 SessionPage](https://www.drissionpage.cn/download/browser)
  * [🧰 进阶使用](https://www.drissionpage.cn/download/browser)
    * [⬇️ 下载文件](https://www.drissionpage.cn/download/browser)
      * [⤵️ 概述](https://www.drissionpage.cn/download/intro)
      * [⤵️ download方法](https://www.drissionpage.cn/download/DownloadKit)
      * [⤵️ 浏览器下载](https://www.drissionpage.cn/download/browser)
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
  * ⬇️ 下载文件
  * ⤵️ 浏览器下载


本页总览
# ⤵️ 浏览器下载
本节介绍对浏览器下载任务进行设置的功能。
## ✅️ 概述[​](https://www.drissionpage.cn/download/browser#️-概述 "✅️ 概述的直接链接")
### 📌 功能[​](https://www.drissionpage.cn/download/browser#-功能 "📌 功能的直接链接")
DrissionPage 提供以下功能，用于对浏览器下载任务进行控制：
  * 每个 tab 对象可独立设置文件保存路径
  * 下载前可指定文件名称，实现文件重命名
  * 可设置存在同名文件时的处理方式
  * 可获取任务下载进度
  * 可等待下载任务结束
  * 可取消任务
  * 可拦截下载任务并获取其信息


## ⚠️ 注意事项[​](https://www.drissionpage.cn/download/browser#️-注意事项 "⚠️ 注意事项的直接链接")
### 📌 记得等待任务结束[​](https://www.drissionpage.cn/download/browser#-记得等待任务结束 "📌 记得等待任务结束的直接链接")
因技术原因，程序在下载结束时才能对其重命名，在这之前文件名是临时的任务 id。
因此必需等待下载完毕，文件名才能正确命名。无论是否指定文件名都一样。
**示例：**
```
tab = Chromium().latest_tabtab('#button').click()# 点击下载按钮tab.wait.download_begin()# 等待下载开始tab.wait.downloads_done()# 等待所有任务结束
```

### 📌 多 Tab 操作时推荐设置临时路径[​](https://www.drissionpage.cn/download/browser#-多-tab-操作时推荐设置临时路径 "📌 多 Tab 操作时推荐设置临时路径的直接链接")
程序需要把任务下载到一个指定位置，完成后再移动到目标路径。
因此，如果程序涉及多个 Tab 触发下载任务，最好给`Chromium`对象设置一个下载路径。
即使每个 Tab 对象都设置了自己的路径。
**示例：**
```
from DrissionPage import Chromiumbrowser = Chromium()browser.set.download_path('tmp')# 设置总路径tab1 = browser.get_tab(1)tab1.set.download_path('path1')tab2 = browser.get_tab(2)tab2.set.download_path('path2')
```

### 📌 启动下载管理功能[​](https://www.drissionpage.cn/download/browser#-启动下载管理功能 "📌 启动下载管理功能的直接链接")
本节介绍的下载管理功能默认不开启，此时触发下载任务和手动操作没有区别。
当启动配置中设置了下载路径，或调用`set.download_path()`方法时，管理功能才会启动。
使用`click.to_download()`方法会自动自动此功能。
## ✅️ `click.to_download()`[​](https://www.drissionpage.cn/download/browser#️-clickto_download "️-clickto_download的直接链接")
当预期点击元素后会触发下载，可使用此方法返回下载任务。
使用时可以同时设置下载路径、指定文件名名称。
注意
  * 有些下载任务是点击后弹出新标签页，在新标签页触发下载，此时必须设置`new_tab=True`
  * 点击后等待下载触发时间为页面对象`timeout`属性（默认10秒），如果需要更久的等待，用下文介绍的方法。


参数名称| 类型| 默认值| 说明  
---|---|---|---  
`save_path`| `str``Path`| 必填| 保存路径，为`None`保存在原来设置的，如未设置保存到当前路径  
`rename`| `str`| `None`| 重命名文件名，为`None`则不修改  
`suffix`| `str`| `None`| 指定文件后缀，为`None`则不修改  
`new_tab`| `bool`| `False`| 预期的下载是否在新标签页中触发  
`by_js`| `bool`| `False`| 是否用 js 方式点击，逻辑与`click()`一致  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时使用页面对象默认超时时间  
返回类型| 说明  
---|---  
`DownloadMission`| 下载任务对象  
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tab tab.get('https://im.qq.com/pcqq/index.shtml')ele = tab('全新体验版下载')ele.wait.has_rect()mission = ele.click.to_download(save_path='tmp', rename='QQ.exe')mission.wait()
```

`click.to_download()`方法能够应付多数情况，不是点击触发的下载任务或更复杂的情况，请根据下文介绍的配置方式使用。
## ✅️ 设置下载路径[​](https://www.drissionpage.cn/download/browser#️-设置下载路径 "✅️ 设置下载路径的直接链接")
### 📌 设置总下载路径[​](https://www.drissionpage.cn/download/browser#-设置总下载路径 "📌 设置总下载路径的直接链接")
使用`Chromium`对象的`set.download_path()`方法设置下载路径。不设置时，默认下载到程序当前路径。
`Chromium`对象设置下载路径后，后续新建的 Tab 对象均会使用该路径，之前建立的 Tab 对象使用的路径则不会改变。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| 必填| 下载路径  
**返回：**`None`
**示例：**
```
from DrissionPage import Chromiumbrowser = Chromium()browser.set.download_path(r'C:\tmp')
```

### 📌 设置 Tab 下载路径[​](https://www.drissionpage.cn/download/browser#-设置-tab-下载路径 "📌 设置 Tab 下载路径的直接链接")
使用方法与设置`Chromium`的一致，但只在当前 Tab 对象生效。
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.set.download_path(r'C:\tmp1')# 设置Tab下载路径
```

## ✅️ 设置文件名[​](https://www.drissionpage.cn/download/browser#️-设置文件名 "✅️ 设置文件名的直接链接")
使用`download_file_name()`方法，可在下载前设置文件名，实现下载文件的重命名。
设置的文件名可以不带后缀，程序会根据下载的文件自动补充后缀。
如设置的文件名带`'.'`，且后缀与网络文件不一致，程序会以网络文件的后缀为准。
如果想修改后缀名，设置`suffix`参数即可。
每次触发下载后，该设置会被清空。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| `None`| 文件名  
`suffix`| `str`| `None`| 文件后缀名，传入`''`可去除后缀  
**返回：**`None`
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.set.download_file_name('new_file')tab('t:a').click()# 点击一个会触发下载的链接mission = tab.wait.download_begin()mission.wait()# 记得等待任务触发和结束
```

## ✅️ 等待[​](https://www.drissionpage.cn/download/browser#️-等待 "✅️ 等待的直接链接")
### 📌 等待下载开始[​](https://www.drissionpage.cn/download/browser#-等待下载开始 "📌 等待下载开始的直接链接")
点击下载链接后，下载并不会瞬间触发，需要进行等待，才能将其捕获。
使用`wait.download_begin()`方法等待下载开始。
一般来说，标签页触发的下载任务用 Tab 对象进行等待，未被控制的标签页触发的下载，可由`Chromium`对象进行等待。
`cancel_it`参数为`True`时，捕获到任务时会将其取消，以便将返回的下载信息用于其它需要。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 超时时间（秒），`None`为页面默认等待时间  
`cancel_it`| `bool`| `False`| 是否取消该任务  
返回类型| 说明  
---|---  
`DownloadMission`| 等待成功且`cancel_it`为`False`时返回下载任务对象  
`dict`| 等待成功且`cancel_it`为`True`时返回下载任务信息  
`False`| 等待失败返回`False`  
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab('t:a').click()# 点击一个会触发下载的链接tab.wait.download_begin()
```

### 📌 等待所有下载任务结束[​](https://www.drissionpage.cn/download/browser#-等待所有下载任务结束 "📌 等待所有下载任务结束的直接链接")
用`Chromium`对象的`wait.downloads_done()`方法可等待浏览器所有下载任务结束。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时无限等待  
`cancel_if_timeout`| `bool`| `False`| 如超时是否取消未完成的任务  
返回类型| 说明  
---|---  
`bool`| 是否等待成功  
### 📌 等待某 Tab 所有下载任务结束[​](https://www.drissionpage.cn/download/browser#-等待某-tab-所有下载任务结束 "📌 等待某 Tab 所有下载任务结束的直接链接")
用 Tab 对象的`wait.downloads_done()`方法可等待该 Tab 对象触发点下载任务结束。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时无限等待  
`cancel_if_timeout`| `bool`| `False`| 如超时是否取消未完成的任务  
返回类型| 说明  
---|---  
`bool`| 是否等待成功  
## ✅️ 拦截下载任务[​](https://www.drissionpage.cn/download/browser#️-拦截下载任务 "✅️ 拦截下载任务的直接链接")
`wait.download_begin()`方法有个`cancel_it`参数，当为`True`时，会取消下载任务。
此时可使用该方法返回的任务信息进行下一步操作，如改用`download()`方法下载等。
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab('t:a').click()data = tab.wait.download_begin(cancel_it=True)tab.download(data.url)
```

## ✅️ 同名文件的处理[​](https://www.drissionpage.cn/download/browser#️-同名文件的处理 "✅️ 同名文件的处理的直接链接")
下载遇到同名文件时，可选择三种处理方式：自动重命名、覆盖、跳过。
使用`set.when_download_file_exists('****')`进行设置。
其中`****`可选`'rename'`、`'overwrite'`、`'skip'`。
也可选择它们的首字母`'r'`、`'o'`、`'s'`。
### 📌 自动重命名[​](https://www.drissionpage.cn/download/browser#-自动重命名 "📌 自动重命名的直接链接")
设置方法：`set.when_download_file_exists('rename')`
这种方式遇到已有同名文件时会自动将新文件重命名，方式是在后面加上序号。
假设保存路径已存在名为 'abc.zip' 的文件，再下载一个 'abc.zip' 时，新文件会自动重命名为 'abc_1.zip'。
之后再下载会命名为 'abc_2.zip'，如此类推。
### 📌 覆盖已有文件[​](https://www.drissionpage.cn/download/browser#-覆盖已有文件 "📌 覆盖已有文件的直接链接")
设置方法：`set.when_download_file_exists('overwrite')`
这种方式会把原有的同名文件替换成新下载的。
### 📌 跳过[​](https://www.drissionpage.cn/download/browser#-跳过 "📌 跳过的直接链接")
设置方法：`set.when_download_file_exists('skip')`
这种方式下，发现已有同名文件时会取消下载任务。
## ✅️ 任务管理[​](https://www.drissionpage.cn/download/browser#️-任务管理 "✅️ 任务管理�的直接链接")
`wait.download_begin()`方法会返回`DownloadMission`对象，用于浏览器下载任务的管理。
### 📌 获取任务信息[​](https://www.drissionpage.cn/download/browser#-获取任务信息 "📌 获取任务信息的直接链接")
可获取任务状态、进度、保存路径、文件名等信息。
属性名称| 类型| 说明  
---|---|---  
`url`| `str`| 返回任务网址  
`tab_id`| `str`| 触发任务的 Tab 对象 id  
`id`| `str`| 任务 id  
`folder`| `str`| 保存文件夹路径  
`name`| `str`| 文件名  
`tmp_path`| `str`| 临时文件保存路径  
`state`| `str`| 任务状态，'running', 'done', 'canceled', 'skipped'  
`total_bytes`| `int`| 总字节数  
`received_bytes`| `int`| 已接收字节数  
`final_path`| `str``None`| 最终完整路径，任务完成后才产生  
**示例：**
实时打印任务进度。
```
mission = tab.wait.download_begin()whilenot mission.is_done:print(f'\r{mission.rate}%', end='')
```

### 📌 等待任务结束[​](https://www.drissionpage.cn/download/browser#-等待任务结束 "📌 等待任务结束的直接链接")
使用`DownloadMission`对象的`wait()`方法，可等待任务结束。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`show`| `bool`| `True`| 是否打印下载信息  
`timeout`| `float`| `None`| 超时时间（秒），`None`为无限等待  
`cancel_if_timeout`| `bool`| `False`| 如超时是否取消该任务  
返回类型| 说明  
---|---  
`str`| 下载完成返回最终保存路径  
`False`| 超时或被取消返回`False`  
### 📌 取消任务[​](https://www.drissionpage.cn/download/browser#-取消任务 "📌 取消任务的直接链接")
使用`DownloadMission`对象的`cancel()`方法，可取消任务。
调用该方法，已下载的文件会被删除，即使是已完成的任务。
[上一页⤵️ download方法](https://www.drissionpage.cn/download/DownloadKit)[下一页⚙️ 配置文件的使用](https://www.drissionpage.cn/advance/ini)
  * [✅️ 概述](https://www.drissionpage.cn/download/browser#️-概述)
    * [📌 功能](https://www.drissionpage.cn/download/browser#-功能)
  * [⚠️ 注意事项](https://www.drissionpage.cn/download/browser#️-注意事项)
    * [📌 记得等待任务结束](https://www.drissionpage.cn/download/browser#-记得等待任务结束)
    * [📌 多 Tab 操作时推荐设置临时路径](https://www.drissionpage.cn/download/browser#-多-tab-操作时推荐设置临时路径)
    * [📌 启动下载管理功能](https://www.drissionpage.cn/download/browser#-启动下载管理功能)
  * [✅️ `click.to_download()`](https://www.drissionpage.cn/download/browser#️-clickto_download)
  * [✅️ 设置下载路径](https://www.drissionpage.cn/download/browser#️-设置下载路径)
    * [📌 设置总下载路径](https://www.drissionpage.cn/download/browser#-设置总下载路径)
    * [📌 设置 Tab 下载路径](https://www.drissionpage.cn/download/browser#-设置-tab-下载路径)
  * [✅️ 设置文件名](https://www.drissionpage.cn/download/browser#️-设置文件名)
  * [✅️ 等待](https://www.drissionpage.cn/download/browser#️-等待)
    * [📌 等待下载开始](https://www.drissionpage.cn/download/browser#-等待下载开始)
    * [📌 等待所有下载任务结束](https://www.drissionpage.cn/download/browser#-等待所有下载任务结束)
    * [📌 等待某 Tab 所有下载任务结束](https://www.drissionpage.cn/download/browser#-等待某-tab-所有下载任务结束)
  * [✅️ 拦截下载任务](https://www.drissionpage.cn/download/browser#️-拦截下载任务)
  * [✅️ 同名文件的处理](https://www.drissionpage.cn/download/browser#️-同名文件的处理)
    * [📌 自动重命名](https://www.drissionpage.cn/download/browser#-自动重命名)
    * [📌 覆盖已有文件](https://www.drissionpage.cn/download/browser#-覆盖已有文件)
    * [📌 跳过](https://www.drissionpage.cn/download/browser#-跳过)
  * [✅️ 任务管理](https://www.drissionpage.cn/download/browser#️-任务管理)
    * [📌 获取任务信息](https://www.drissionpage.cn/download/browser#-获取任务信息)
    * [📌 等待任务结束](https://www.drissionpage.cn/download/browser#-等待任务结束)
    * [📌 取消任务](https://www.drissionpage.cn/download/browser#-取消任务)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/download/browser)
  * [QQ群：391178600](https://www.drissionpage.cn/download/browser)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
