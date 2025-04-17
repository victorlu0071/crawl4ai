# Content from: https://www.drissionpage.cn/browser_control/screen

[跳到主要内容](https://www.drissionpage.cn/browser_control/screen#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/screen)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/screen)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/screen)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/screen)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/screen)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/screen)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 截图和录像


本页总览
# 🛰️ 截图和录像
## ✅️️ 页面截图[​](https://www.drissionpage.cn/browser_control/screen#️️-页面截图 "✅️️ 页面截图的直接链接")
使用页面对象的`get_screenshot()`方法对页面进行截图，可对整个网页、可见网页、指定范围截图。
对可视范围外截图需要 90 以上版本浏览器支持。
下面三个参数三选一，优先级：`as_bytes`>`as_base64`>`path`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| `None`| 保存图片的路径，为`None`时保存在当前文件夹  
`name`| `str`| `None`| 完整文件名，后缀可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`，为`None`时以用 jpg 格式  
`as_bytes`| `str``True`| `None`| 是否以字节形式返回图片，可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`、`None`、`True`不为`None`时`path`参数无效为`True`时选用 jpg 格式  
`as_base64`| `str``True`| `None`| 是否以 base64 形式返回图片，可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`、`None`、`True`不为`None`时`path`参数无效为`True`时选用 jpg 格式  
`full_page`| `bool`| `False`| 是否整页截图，为`True`截取整个网页，为`False`截取可视窗口  
`left_top`| `Tuple[int, int]`| `None`| 截取范围左上角坐标  
`right_bottom`| `Tuple[int, int]`| `None`| 截取范围右下角坐标  
返回类型| 说明  
---|---  
`bytes`| `as_bytes`生效时返回图片字节  
`str`| `as_bytes`和`as_base64`为`None`时返回图片完整路径  
`str`| `as_base64`生效时返回 base64 格式的字符串  
说明
如`path`为包含文件名的完整路径，`name`参数无效。
**示例：**
```
# 对整页截图并保存tab.get_screenshot(path='tmp', name='pic.jpg', full_page=True)
```

## ️️ ✅️️ 元素截图[​](https://www.drissionpage.cn/browser_control/screen#️️-️️-元素截图 "️️ ✅️️ 元素截图的直接链接")
使用元素对象的`get_screenshot()`方法对元素进行截图。
若元素范围超出视口，需 90 以上版本内核支持。
下面三个参数三选一，优先级：`as_bytes`>`as_base64`>`path`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| `None`| 保存图片的路径，为`None`时保存在当前文件夹  
`name`| `str`| `None`| 完整文件名，后缀可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`，为`None`时以用 jpg 格式  
`as_bytes`| `str``True`| `None`| 是否以字节形式返回图片，可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`、`None`、`True`不为`None`时`path`和`as_base64`参数无效为`True`时选用 jpg 格式  
`as_base64`| `str``True`| `None`| 是否以 base64 形式返回图片，可选`'jpg'`、`'jpeg'`、`'png'`、`'webp'`、`None`、`True`不为`None`时`path`参数无效为`True`时选用 jpg 格式  
`scroll_to_center`| `bool`| `True`| 截图前是否滚动到视口中央  
返回类型| 说明  
---|---  
`bytes`| `as_bytes`生效时返回图片字节  
`str`| `as_bytes`和`as_base64`为`None`时返回图片完整路径  
`str`| `as_base64`生效时返回 base64 格式的字符串  
说明
如`path`为包含文件名的完整路径，`name`参数无效。
**示例：**
```
img = tab('tag:img')img.get_screenshot()bytes_str = img.get_screenshot(as_bytes='png')# 返回截图二进制文本
```

## ✅️️ 页面录像[​](https://www.drissionpage.cn/browser_control/screen#️️-页面录像 "✅️️ 页面录像的直接链接")
使用页面对象的`screencast`功能，可以录取屏幕图片或视频。
### 📌 设置录制模式[​](https://www.drissionpage.cn/browser_control/screen#-设置录制模式 "📌 设置录制模式的直接链接")
录制模式一共有 5 种，通过`screencast.set_mode.xxx_mode()`设置。
模式| 说明  
---|---  
`video_mode()`| 持续录制页面，停止时生成没有声音的视频  
`frugal_video_mode()`| 页面有变化时才录制，停止时生成没有声音的视频  
`js_video_mode()`| 可生成有声音的视频，但需要手动启动  
`imgs_mode()`| 持续对页面进行截图  
`frugal_imgs_mode()`| 页面有变化时才保存页面图像  
### 📌 设置存放路径[​](https://www.drissionpage.cn/browser_control/screen#-设置存放路径 "📌 设置存放路径的直接链接")
使用`screencast.set_save_path()`设置录制结果保存路径。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`save_path`| `str``Path`| `None`| 保存图片或视频的路径  
**返回：**`None`
### 📌 `screencast.start()`[​](https://www.drissionpage.cn/browser_control/screen#-screencaststart "-screencaststart的直接链接")
此方法用于开始录制浏览器窗口。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`save_path`| `str``Path`| `None`| 保存图片或视频的路径  
**返回：**`None`
注意
保存路径必需设置，无论是用`screencast.set()`还是`screencast.start()`都可以。
### 📌 `screencast.stop()`[​](https://www.drissionpage.cn/browser_control/screen#-screencaststop "-screencaststop的直接链接")
此方法用于停止录取屏幕。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`video_name`| `str`| `None`| 视频文件名，为`None`时以当前时间名命  
`suffix`| `str`| `'mp4'`| 视频文件后缀  
`coding`| `str`| `'mp4v'`| 视频编码格式，仅`video_mode`模式有效，根据`cv2.VideoWriter_fourcc()`定义  
返回类型| 说明  
---|---  
`str`| 保存为视频时返回视频文件路径，否则返回保存图片的文件夹路径  
### 📌 注意事项[​](https://www.drissionpage.cn/browser_control/screen#-注意事项 "📌 注意事项的直接链接")
  * 使用`video_mode`和`frugal_video_mode`时，保存路径和保存文件名必需是英文。
  * 使用`video_mode`和`frugal_video_mode`时，需先安装 opencv 库。`pip install opencv-python`
  * 使用`js_video_mode`时，需用鼠标手动选择要录制的目标，才能开始录制
  * 使用`js_video_mode`时，如要对一个窗口进行录制，需在另一个窗口开始录制，否则如窗口出现跳转，会使录制失效


### 📌 示例[​](https://www.drissionpage.cn/browser_control/screen#-示例 "📌 示例的直接链接")
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.screencast.set_save_path('video')# 设置视频存放路径tab.screencast.set_mode.video_mode()# 设置录制tab.screencast.start()# 开始录制tab.wait(3)tab.screencast.stop()# 停止录制
```

[上一页🛰️ 获取控制台信息](https://www.drissionpage.cn/browser_control/console)[下一页🛰️ 上传文件](https://www.drissionpage.cn/browser_control/upload)
  * [✅️️ 页面截图](https://www.drissionpage.cn/browser_control/screen#️️-页面截图)
  * [️️ ✅️️ 元素截图](https://www.drissionpage.cn/browser_control/screen#️️-️️-元素截图)
  * [✅️️ 页面录像](https://www.drissionpage.cn/browser_control/screen#️️-页面录像)
    * [📌 设置录制模式](https://www.drissionpage.cn/browser_control/screen#-设置录制模式)
    * [📌 设置存放路径](https://www.drissionpage.cn/browser_control/screen#-设置存放路径)
    * [📌 `screencast.start()`](https://www.drissionpage.cn/browser_control/screen#-screencaststart)
    * [📌 `screencast.stop()`](https://www.drissionpage.cn/browser_control/screen#-screencaststop)
    * [📌 注意事项](https://www.drissionpage.cn/browser_control/screen#-注意事项)
    * [📌 示例](https://www.drissionpage.cn/browser_control/screen#-示例)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/screen)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/screen)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
