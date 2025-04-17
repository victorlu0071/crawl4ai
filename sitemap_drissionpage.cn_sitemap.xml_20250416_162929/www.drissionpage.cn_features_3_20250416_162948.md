# Content from: https://www.drissionpage.cn/features/3

[跳到主要内容](https://www.drissionpage.cn/features/3#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/features/3)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/features/3)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🔥 新版本介绍](https://www.drissionpage.cn/features/3)
    * [💥 4.1 功能介绍](https://www.drissionpage.cn/features/4.1)
    * [💥 4.0 功能介绍](https://www.drissionpage.cn/features/4)
    * [💥 3.2 功能介绍](https://www.drissionpage.cn/features/3)
  * [💖 特性](https://www.drissionpage.cn/features/)
  * [🌟 特性演示](https://www.drissionpage.cn/features/3)


  * [](https://www.drissionpage.cn/)
  * 🔥 新版本介绍
  * 💥 3.2 功能介绍


本页总览
# 💥 3.2 功能介绍
3.2 对比 3.1 有相当大的变化。既对底层逻辑进行了梳理，修复了许多问题，提高了稳定性，也对用户 api 进行了整合。
期待大佬们体验并提出意见建议。
沟通方式：
  * QQ 群：897838127
  * [点击提交 Issues](https://gitee.com/g1879/DrissionPage/issues)


## ✅️️ 特性改变[​](https://www.drissionpage.cn/features/3#️️-特性改变 "✅️️ 特性改变的直接链接")
### 📌 `WebPage`不再自动切换模式[​](https://www.drissionpage.cn/features/3#-webpage不再自动切换模式 "-webpage不再自动切换模式的直接链接")
旧版本中，调用非当前模式独有的方法，会先自动切换模式。比如在 d 模式调用`post()`方法，会自动切换到 s 模式。
3.2 中，只有显式调用`change_mode()`时才会切换模式。因此，可以在 s 模式时控制浏览器，不会产生冲突。使用更灵活。
### 📌 `WebPage`的标签页对象也可以切换模式[​](https://www.drissionpage.cn/features/3#-webpage的标签页对象也可以切换模式 "-webpage的标签页对象也可以切换模式的直接链接")
`WebPage`的`get_tab()`方法现在返回`WebPageTab`对象，也能切换模式。创建时默认处于 d 模式。
### 📌 更改找不到元素时返回值[​](https://www.drissionpage.cn/features/3#-更改找不到元素时返回值 "📌 更改找不到元素时返回值的直接链接")
旧版本中，查找不到元素会返回`None`，3.2 版中会返回一个`NoneElement`对象。
该对象用`if`判断表现为`False`，调用其功能会抛出`ElementNotFoundError`异常。这样可以用`if`判断是否找到元素，也可以用`try`去捕获异常。
查找多个元素找不到时，依然返回空的`list`，这点和旧版本一致。
示例，当我们查找一个不存在的元素时：
```
ele = page.ele('****')
```

❌ 当前版本用`None`判断的方式将不可用：
```
if ele isNone:print('没有找到。')
```

⭕ 正确做法：
```
# 用if判断ifnot ele:print('没有找到。')if ele:print('找到了。')
```

```
# 用try捕获try:  ele.click()except ElementNotFoundError:print('没有找到。')
```

### 📌 部分方法调整[​](https://www.drissionpage.cn/features/3#-部分方法调整 "📌 部分方法调整的直接链接")
  * `run_js()`方法参数顺序作了调整
  * `drag()`和`drag_to()`方法删除了`shake`参数
  * 元素对象去除`wait_ele()`方法，改用`wait.****()`方法等待自身属性改变
  * `ChromiumPage`的`to_tab()`、`close_tabs()`、`close_other_tabs()`方法可接收标签页对象
  * `ActionChains`导入路径改为`from DrissionPage.common import ActionChains`
  * `Keys`导入路径改为`from DrissionPage.common import Keys`


### 📌 下载默认使用浏览器[​](https://www.drissionpage.cn/features/3#-下载默认使用浏览器 "📌 下载默认使用浏览器的直接链接")
避免不了解 DownloadKit 的用户以为点击后程序没有反应。
现在点击后默认用浏览器下载到程序当前路径，可用`download_set.save_path()`设置保存位置。
## ✅️️ api 整合[​](https://www.drissionpage.cn/features/3#️️-api-整合 "✅️️ api 整合的直接链接")
随着功能的增加，同类 api 也越来越多，比如`ChromiumPage`以`set_`开头的方法就有 9 个，元素点击的方式有 5 种。如何这些同类的 api 全堆在一起，会显得十分凌乱。
因此，3.2 版对大量 api 做了整合，避免提示界面越来越臃肿，也增强了开发灵活性。
旧版的 api 目前还将保留，但将在以后的版本中舍弃。
旧版：
```
page.set_timeouts(20,30,40)
```

新版：
```
page.set.timeouts(20,30,40)
```

### 📌 浏览器页面对象[​](https://www.drissionpage.cn/features/3#-浏览器页面对象 "📌 浏览器页面对象的直接链接")
旧版| 新版| 说明  
---|---|---  
set_timeouts()| set.timeouts()| 超时设置  
set_session_storage()| set.session_storage()| session storage 设置  
set_local_storage()| set.local_storage()| local storage 设置  
set_user_agent()| set.user_agent()| user agent 设置  
set_cookies()| set.cookies()| cookies 设置  
set_headers()| set.headers()| headers 设置  
set_page_load_strategy.****()| set.load_strategy.****()| 页面加载策略设置  
set_window.****()| set.window.****()| 浏览器大小位置设置  
set_main_tab()| set.main_tab()| 主 tab 设置  
wait_loading()| wait.load_start()| 等待页面加载开始  
wait_ele().****()| wait.ele_****()| 等待元素变成某种状态  
scroll_to_see()| scroll.to_see()| 把元素滚动到视口  
hide_browser()| set.window.hide()| 隐藏浏览器  
show_browser()| set.window.show()| 显示浏览器  
to_front()| set.tab_to_front()| 设置某个标签页到激活状态  
### 📌 元素对象[​](https://www.drissionpage.cn/features/3#-元素对象 "📌 元素对象的直接链接")
旧版| 新版| 说明  
---|---|---  
wait_ele().****()| wait.****()| 等待元素变成某种状态  
r_click()| click.right()| 右键点击元素  
m_click()| clikc.middle()| 中键点击元素  
r_click_at()| click.right_at()| 带偏移量中键点击元数据  
click_at()| click.left_at()| 带偏移量左键点击元素  
set_attr()| set.attr()| 设置 attribute 属性  
set_prop()| set.prop()| 设置 property 属性  
set_innerHTML()| set.innerHTML()| 设置 innerHTML 内容  
midpoint| locations.midpoint| 获取元素中点在页面位置  
client_location| locations.viewport_location| 获取元素左上角在视口位置  
client_midpoint| locations.viewport_midpoint| 获取元素中点在视口位置  
is_selected| states.is_selected| 获取元素是否被选中  
is_displayed| states.is_displayed| 获取元素是否显示  
is_enabled| states.is_enabled| 获取元素是否可操作  
is_alive| states.is_alive| 获取元素是否仍然在 DOM 内  
is_in_viewport| states.is_in_viewport| 获取元素是否在视口内  
pseudo_before| pseudo.before| 获取 before 伪元素内容  
pseudo_after| pseudo.after| 获取 after 伪元素内容  
obj_id| ids.obj_id| 获取元素 object id  
node_id| ids.node_id| 获取元素 node id  
backend_id| ids.backend_id| 获取元素 backend id  
doc_id| ids.doc_id| 获取元素 doc id  
## ✅️️ 新增功能[​](https://www.drissionpage.cn/features/3#️️-新增功能 "✅️️ 新增功能的直接链接")
### 📌 拦截上传控件填写路径[​](https://www.drissionpage.cn/features/3#-拦截上传控件填写路径 "📌 拦截上传控件填写路径的直接链接")
之前的版本中，要上传文件需要开发者先在 DOM 内找到文件上传控件，有些经过伪装后实时加载的`<input>`元素并不好找，有时也会由 js 控制。
新版本中，再也无需费心查找上传控件，只要设置好要上传的路径，然后点击触发文本选择框，程序会自动拦截选择框，并把路径输入到控件，非常便利。
示例：
```
# 设置要上传的文件路径page.set.upload_files('demo.txt')# 点击触发文件选择框按钮btn_ele.click()# 等待路径填入page.wait.upload_paths_inputted()
```

点击按钮后，文本选择框被拦截不会弹出，但可以看到文件路径已经传入其中。
由于此动作是异步输入，需显式等待输入完成才进行下一步操作。
### 📌 优先读取项目路径 ini 文件[​](https://www.drissionpage.cn/features/3#-优先读取项目路径-ini-文件 "📌 优先读取项目路径 ini 文件的直接链接")
旧版本中默认 ini 文件存放在 DrissionPage 安装目录下，修改要通过代码进行，给调试带来不便。新版会优先在用户项目文件夹下查找`'dp_configs.ini'`文件并使用，使开发时可方便地手动更改配置。项目打包也可以直接打包而不会造成找不到文件问题。
`easy_set`方法中增加`configs_to_here()`方法，调用该方法可直接把默认 ini 文件复制到当前路径。
### 📌 查找元素增加或语法[​](https://www.drissionpage.cn/features/3#-查找元素增加或语法 "📌 查找元素增加或语法的直接链接")
查找元素增加`@|`语法，用于或关系匹配多个属性：
```
page('@|class=xxx@|name=abc')
```

或语法`@|`不能跟与语法`@@`共同生效。
### 📌 找不到元素时可抛出异常[​](https://www.drissionpage.cn/features/3#-找不到元素时可抛出异常 "📌 找不到元素时可抛出异常的直接链接")
找不到元素时，除了返回`NoneElement`对象，也可设置直接抛出异常。
```
from DrissionPage.easy_set import raise_when_ele_not_foundraise_when_ele_not_found(True)
```

该设置是全局设置，设置后整个项目都会生效。
**示例：**
```
from DrissionPage import SessionPagefrom DrissionPage.easy_set import raise_when_ele_not_foundraise_when_ele_not_found(True)page = SessionPage()page.get('https://www.baidu.com')ele = page('****')
```

上面的代码会抛出`ElementNotFound`异常。
### 📌 新增一批异常[​](https://www.drissionpage.cn/features/3#-新增一批异常 "📌 新增一批异常的直接链接")
新增一批异常，调用位置：
```
from DrissionPage.errors import ElementLossError
```

  * `AlertExistsError`：调用页面功能若存在未处理的弹出框则抛出
  * `ContextLossError`：页面被刷新后仍调用其中的元素时抛出
  * `ElementLossError`：元素因页面或自身被刷新而失效时抛出
  * `CallMethodError`：调用 cdp 时产生的异常
  * `TabClosedError`：标签页关闭后仍调用其功能时抛出
  * `ElementNotFoundError`：找不到元素抛出
  * `JavaScriptError`：JavaScript 运行错误
  * `NoRectError`：对没有大小和位置信息的元素获取这些信息时抛出


### 📌 新增的方法和属性[​](https://www.drissionpage.cn/features/3#-新增的方法和属性 "📌 新增的方法和属性的直接链接")
`ChromiumPage`：
名称| 说明  
---|---  
run_cdp_loaded()| 执行 cdp 命令，执行前等待页面加载完成  
run_js_loaded()| 执行 js 语句，执行前等待页面加载完成  
wait.load_complete()| 等待页面加载完毕  
wait.upload_paths_inputted()| 等待上传文件路径输入到文件选择框  
rect.browser_location| 获取浏览器左上角在屏幕上坐标  
rect.page_location| 获取页面左上角在屏幕上坐标  
rect.viewport_location| 获取视口在屏幕上坐标  
rect.browser_size| 获取浏览器大小  
rect.page_size| 获取页面大小  
rect.viewport_size| 获取视口大小，不含滚动条  
rect.viewport_size_with_scrollbar| 获取视口大小，含滚动条  
remove_ele()| 从页面上移除一个元素  
get_frame()| 获取一个`ChromiumFrame`对象  
`SessionPage`新增一系列设置方法：
名称| 说明  
---|---  
set.header()| 设置一个 header 值  
set.proxies()| 设置代理  
set.auth()| 设置登录信息  
set.hooks()| 设置回调方法  
set.params()| 设置连接参数  
set.cert()| 设置证书  
set.stream()| 设置是否使用流式响应内容  
set.trust_env()| 设置是否信任环境  
set.max_redirects()| 设置最大重定向次数  
set.max_redirects()| 添加适配器  
`ChromiumElement`：
名称| 说明  
---|---  
locations.screen_location| 获取元素左上角在屏幕上的坐标  
locations.screen_midpoint| 获取元素中间点在屏幕上的坐标  
locations.screen_click_point| 获取元素点击点在屏幕上的坐标  
locations.click_point| 获取元素点击点在页面上的坐标  
locations.viewport_click_point| 获取元素点击点在视口上的坐标  
states.is_covered| 获取元素是否被覆盖  
click.at()| 带偏移量点击元素，可指定按键  
wait.covered()| 等待元素被覆盖  
wait.covered()| 等待元素不被覆盖  
### 📌 命令行工具[​](https://www.drissionpage.cn/features/3#-命令行工具 "📌 命令行工具的直接链接")
新增支持命令行工具。
  * `--set-browser-path`（`-p`）：设置配置文件中的浏览器路径
  * `--set-user-path`（`-u`）：设置配置文件中的用户数据路径
  * `--configs-to-here`（`-c`）：复制默认配置文件到当前路径
  * `--launch-browser`（`-l`）：启动浏览器，传入端口号，0表示用配置文件中的值


```
dp --set-browser-path '/Application/Goolge Chrome.app/Contents/MacOS/Google Chrome'
```

## ✅️️ 优化和问题修复[​](https://www.drissionpage.cn/features/3#️️-优化和问题修复 "✅️️ 优化和问题修复的直接链接")
  * 对程序底层和业务逻辑进行了重新梳理，优化程序逻辑，大幅增强稳定性
  * 新旧版本完全隔离，新版以后开发可放飞自我，无需担心影响以前用`MixPage`开发的程序
  * 现在会返回开发者能看懂的异常信息
  * 修复页面加载和退出触发弹窗引起的问题
  * 修复`<iframe>`加载时可能出现的 500 错误
  * 修复异域`<iframe>`点击问题
  * 没有位置和大小信息的元素在获取这些信息时，现在会抛出异常
  * 修复内存没有正确释放的问题
  * 修复点击被固定栏遮挡问题
  * 接管新出现的`<iframe>`会自动等待内容加载
  * 修复`<iframe>`在同域和异域间互相跳转时会卡住的问题
  * 修复`<iframe>`内元素截图出现偏移问题


[上一页💥 4.0 功能介绍](https://www.drissionpage.cn/features/4)[下一页💖 特性](https://www.drissionpage.cn/features/)
  * [✅️️ 特性改变](https://www.drissionpage.cn/features/3#️️-特性改变)
    * [📌 `WebPage`不再自动切换模式](https://www.drissionpage.cn/features/3#-webpage不再自动切换模式)
    * [📌 `WebPage`的标签页对象也可以切换模式](https://www.drissionpage.cn/features/3#-webpage的标签页对象也可以切换模式)
    * [📌 更改找不到元素时返回值](https://www.drissionpage.cn/features/3#-更改找不到元素时返回值)
    * [📌 部分方法调整](https://www.drissionpage.cn/features/3#-部分方法调整)
    * [📌 下载默认使用浏览器](https://www.drissionpage.cn/features/3#-下载默认使用浏览器)
  * [✅️️ api 整合](https://www.drissionpage.cn/features/3#️️-api-整合)
    * [📌 浏览器页面对象](https://www.drissionpage.cn/features/3#-浏览器页面对象)
    * [📌 元素对象](https://www.drissionpage.cn/features/3#-元素对象)
  * [✅️️ 新增功能](https://www.drissionpage.cn/features/3#️️-新增功能)
    * [📌 拦截上传控件填写路径](https://www.drissionpage.cn/features/3#-拦截上传控件填写路径)
    * [📌 优先读取项目路径 ini 文件](https://www.drissionpage.cn/features/3#-优先读取项目路径-ini-文件)
    * [📌 查找元素增加或语法](https://www.drissionpage.cn/features/3#-查找元素增加或语法)
    * [📌 找不到元素时可抛出异常](https://www.drissionpage.cn/features/3#-找不到元素时可抛出异常)
    * [📌 新增一批异常](https://www.drissionpage.cn/features/3#-新增一批异常)
    * [📌 新增的方法和属性](https://www.drissionpage.cn/features/3#-新增的方法和属性)
    * [📌 命令行工具](https://www.drissionpage.cn/features/3#-命令行工具)
  * [✅️️ 优化和问题修复](https://www.drissionpage.cn/features/3#️️-优化和问题修复)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/features/3)
  * [QQ群：391178600](https://www.drissionpage.cn/features/3)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
