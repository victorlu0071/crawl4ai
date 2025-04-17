# Content from: https://www.drissionpage.cn/browser_control/upload

[跳到主要内容](https://www.drissionpage.cn/browser_control/upload#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/upload)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/upload)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/upload)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/upload)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/upload)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/upload)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 上传文件


本页总览
# 🛰️ 上传文件
上传文件有两种方式：
  * 拦截文件输入框，自动填入路径
  * 找到`<input>`元素，填入文件路径


## ✅️️ 自然的交互[​](https://www.drissionpage.cn/browser_control/upload#️️-自然的交互 "✅️️ 自然的交互的直接链接")
传统自动化工具的文件上传，需要开发者在 DOM 里找到文件上传控件，然后用元素对象的`input()`方法填入路径。
有些上传控件是临时加载的，有些藏得很深，找起来费时费力。
本库提供一种自然的文件上传方式，无需在 DOM 里找控件，只要自然地点击触发文件选择框，程序就能主动截获，并填写设定好的路径，开发更省事。
### 📌 `click.to_upload()`[​](https://www.drissionpage.cn/browser_control/upload#-clickto_upload "-clickto_upload的直接链接")
浏览器元素对象拥有此方法，用于上传文件到网页。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`file_paths`| `str``Path``list``tuple`| 必填| 文件路径，如果上传框支持多文件，可传入列表或字符串，字符串时多个文件用`\n`分隔  
`by_js`| `bool`| `False`| 是否用 js 方式点击，逻辑与`click()`一致  
**返回：**`None`
**示例**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabele = tab('#uploadButton')ele.click.to_upload(r'C:\text.txt')
```

### 📌 手动方式[​](https://www.drissionpage.cn/browser_control/upload#-手动方式 "📌 手动方式的直接链接")
上面的方法使用默认点击方式触发上传，假如页面要求其它触发方式，可自行手动写上传逻辑。
**步骤：**
  * 设置要上传的文件路径，多路径传入`list`、`tuple`或以`\n`分隔的字符串
  * 点击会触发文件选择框的按钮
  * 调用等待录入语句，确保输入完整


**示例：**
```
# 设置要上传的文件路径tab.set.upload_files('demo.txt')# 点击触发文件选择框按钮btn_ele.click()# 等待路径填入tab.wait.upload_paths_inputted()
```

点击按钮后，文本选择框被拦截不会弹出，但可以看到文件路径已经传入其中。
由于此动作是异步输入，需显式等待输入完成才进行下一步操作。
### 📌 注意事项[​](https://www.drissionpage.cn/browser_control/upload#-注意事项 "📌 注意事项的直接链接")
如果您要操作的上传控件在一个异域的`<iframe>`，那必需用这个`<iframe>`对象来设置上传路径，而不能用页面对象设置。
❌ 错误做法：
```
tab.set.upload_paths('demo.txt')tab.get_frame(1).ele('@type=file').click()tab.wait.upload_paths_inputted()
```

⭕ 正确做法：
```
iframe = tab.get_frame(1)iframe.set.upload_paths('demo.txt')iframe.ele('@type=file').click()iframe.wait.upload_paths_inputted()
```

如果`<iframe>`和主页面是同域的，则用域名对象和`<iframe>`对象设置均可。
## ✅️️ 传统方式[​](https://www.drissionpage.cn/browser_control/upload#️️-传统方式 "✅️️ 传统方式的直接链接")
传统方式，需要开发者在 DOM 里找到文件上传控件，然后用元素对象的`input()`方法填入路径。
文件上传控件是`type`属性为`'file'`的`<input>`元素进行输入，把文件路径输入到元素即可，用法与输入文本一致。
稍有不同的是，无论`clear`参数是什么，都会清空原控件内容。
如果控件支持多文件上传，多个路径用`list`、`tuple`或以`\n`分隔的字符串传入。
```
upload = tab('tag:input@type=file')# 传入一个路径upload.input('D:\\test1.txt')# 传入多个路径，方式 1paths ='D:\\test1.txt\nD:\\test2.txt'upload.input(paths)# 传入多个路径，方式 2paths =['D:\\test1.txt','D:\\test2.txt']upload.input(paths)
```

如果`<input>`元素很好找，这种方式是很简便的。
有些`<input>`是临时加载的，或者经过修饰隐藏很深，找起来很费劲。
万一有些上传是用 js 控制的，这种方式未必能奏效。
[上一页🛰️ 截图和录像](https://www.drissionpage.cn/browser_control/screen)[下一页🛰️ Page 对象](https://www.drissionpage.cn/browser_control/pages)
  * [✅️️ 自然的交互](https://www.drissionpage.cn/browser_control/upload#️️-自然的交互)
    * [📌 `click.to_upload()`](https://www.drissionpage.cn/browser_control/upload#-clickto_upload)
    * [📌 手动方式](https://www.drissionpage.cn/browser_control/upload#-手动方式)
    * [📌 注意事项](https://www.drissionpage.cn/browser_control/upload#-注意事项)
  * [✅️️ 传统方式](https://www.drissionpage.cn/browser_control/upload#️️-传统方式)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/upload)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/upload)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
