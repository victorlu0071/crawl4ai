# Content from: https://www.drissionpage.cn/features/4

[跳到主要内容](https://www.drissionpage.cn/features/4#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/features/4)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/features/4)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🔥 新版本介绍](https://www.drissionpage.cn/features/4)
    * [💥 4.1 功能介绍](https://www.drissionpage.cn/features/4.1)
    * [💥 4.0 功能介绍](https://www.drissionpage.cn/features/4)
    * [💥 3.2 功能介绍](https://www.drissionpage.cn/features/3)
  * [💖 特性](https://www.drissionpage.cn/features/)
  * [🌟 特性演示](https://www.drissionpage.cn/features/4)


  * [](https://www.drissionpage.cn/)
  * 🔥 新版本介绍
  * 💥 4.0 功能介绍


本页总览
# 💥 4.0 功能介绍
3.x 是自主研发底层的初步尝试，很多地方摸着石头过河，存在一些不太成熟的地方。
经过一段时间的使用，积累一些经验之后，4.0 在 3.x 的基础上对底层进行了大幅重构，新增大量功能，改善运行效率和稳定性，优化项目结构，解决很多存在的问题。对比旧版本有质的提高。
但同时不少 api 发生了变化，不能完全兼容旧版本。
api 的变化有些是功能优化必需的改变，有些则是本人对命名简洁的执念，趁着大版本的更新顺便把长期不太满意的命名给改了。
给使用者造成一定不便感到抱歉，但长痛不如短痛，趁着项目用的人不多，干脆舍弃历史包袱果断改掉。
有些原来的写法在 4.0.0 中还能正常使用，但 IDE 会提示无效，将在以后的版本中完全删除。推荐尽快更新为新写法。
本节仅简述功能变化，具体使用方法详见各对应章节。
## ✅️ 新的抓包功能[​](https://www.drissionpage.cn/features/4#️-新的抓包功能 "✅️ 新的抓包功能的直接链接")
3.2 中，抓包功能主要由 FlowViewer 和`wait.data_packets()`提供。
FlowViewer 是本人的一个练手作品，写得比较随意，技术也还没到家。存在漏抓、信息不全、api 不够合理的问题。
4.0 中，每个页面对象都内置了监听器，能力全面升级，api 也更合理。
### 📌 旧 api 变化[​](https://www.drissionpage.cn/features/4#-旧-api-变化 "📌 旧 api 变化的直接链接")
  * 弃用 FlowViewer，以后也不会再升级
  * 删除`wait.set_targets()`
  * 删除`wait.stop_listening()`方法
  * 删除`wait.data_packets()`方法
  * `DrissionPage.common`路径删除`FlowViewer`


### 📌 新 api[​](https://www.drissionpage.cn/features/4#-新-api "📌 新 api的直接链接")
  * 每个标签页对象（包括`ChromiumFrame`）新增`listen`属性，内置监听功能
  * 用`listen.start()`和`listen.stop()`启动和停止监听
  * 用`listen.wait()`阻塞等待数据包
  * 用`listen.steps()`同步获取监听结果
  * 增加`listen.wait_silent()`等待所有请求完成（包含 targets 以外的）
  * 监听结果结构优化，request 和 response 数据分开存放


### 📌 示例[​](https://www.drissionpage.cn/features/4#-示例 "📌 示例的直接链接")
下面示例可直接运行查看结果。这个示例会计时，用于与下个示例对比。
```
from DrissionPage import ChromiumPagefrom TimePinner import Pinnerfrom pprint import pprintpage = ChromiumPage()page.listen.start('api/getkeydata')# 指定监听目标并启动监听pinner = Pinner(True,False)page.get('http://www.hao123.com/')# 访问网站packet = page.listen.wait()# 等待数据包pprint(packet.response.body)# 打印数据包正文pinner.pin('用时',True)
```

**输出：**
```
{'hao123.new.shishi.bangdan.recom': [{'index': '1',                   'pure_title': '以色列和哈马斯移交首批被扣押人员'},                   {'index': '2',                   'pure_title': '听到免签政策法国外长笑了'},                   ......用时：3.3114853000151925
```

## ✅️ 新的页面访问逻辑[​](https://www.drissionpage.cn/features/4#️-新的页面访问逻辑 "✅️ 新的页面访问逻辑的直接链接")
3.x 中存连接存在以下主要问题：
  * 浏览器页面对象`get()`方法的`timeout`参数只对加载阶段生效，无法覆盖连接阶段；
  * 加载策略`none`模式没有实际用处。


这两个问题都在 4.0 中解决，且能够让用户自主控制终止连接的时机。 另外还对连接逻辑进行了优化，避免卡死情况出现。
### 📌 api 变化[​](https://www.drissionpage.cn/features/4#-api-变化 "📌 api 变化的直接链接")
  * 页面对象`page_load_strategy`属性改名为`load_mode`
  * `set.load_strategy`改为`set.load_mode`


### 📌 行为变化[​](https://www.drissionpage.cn/features/4#-行为变化 "📌 行为变化的直接链接")
  * `get()`方法的`timeout`参数现在可覆盖整个过程
  * `timeout`参数对非`get()`方法触发的加载（如点击链接）也能生效
  * `SessionPage`和`WebPage`的 s 模式，如收到空数据，也会重试
  * `SessionPage`的`get()`方法可以指向本地文件


### 📌 新的`none`加载模式[​](https://www.drissionpage.cn/features/4#-新的none加载模式 "-新的none加载模式的直接链接")
旧版中，`none`加载策略是当页面连接成功就立刻停止加载，这在实际使用时没有什么意义。
新版中，这个模式改成：除非加载完成，否则程序不会主动将其停止（即使已超时），同时连接状态不再阻塞程序，而允许用户进行状态判断，主动停止加载。
这样提供给用户非常大的自由度，可等到关键数据包或元素出现就主动停止页面加载，大幅提升执行效率。
### 📌 示例[​](https://www.drissionpage.cn/features/4#-示例-1 "📌 示例的直接链接")
我们继续使用上一个示例的代码，但把加载模式设为`none`，且获取到数据时主动停止加载。
```
from DrissionPage import ChromiumPagefrom TimePinner import Pinnerfrom pprint import pprintpage = ChromiumPage()page.set.load_mode.none()# 设置加载模式为nonepage.listen.start('api/getkeydata')# 指定监听目标并启动监听pinner = Pinner(True,False)page.get('http://www.hao123.com/')# 访问网站packet = page.listen.wait()# 等待数据包page.stop_loading()# 主动停止加载pprint(packet.response.body)# 打印数据包正文pinner.pin('用时',True)
```

**输出：**
```
{'hao123.new.shishi.bangdan.recom': [{'index': '1',                   'pure_title': '以色列和哈马斯移交首批被扣押人员'},                   {'index': '2',                   'pure_title': '听到免签政策法国外长笑了'},                   ......用时：1.2575092000188306
```

可见节省了2秒时间。 当网站要访问一些不稳定资源时，节省的时间相当客观，也能提高程序的稳定性。
## ✅️ 新的下载管理功能[​](https://www.drissionpage.cn/features/4#️-新的下载管理功能 "✅️ 新的下载管理功能的直接链接")
在旧版中，下载管理功能存在以下问题：
  * 浏览器下载管理和内置下载器`DownloadKit`的配置都使用`download_set`属性进行设置，容易造成混淆。
  * 浏览器下载任务不能在下载前指定文件名
  * 该功能有随着浏览器版本更新失效的风险


4.0 对浏览器下载管理功能进行了完完全全的重构，结构更为合理，功能更多。 同时，内置下载器的设置和浏览器下载任务设置进行了分离。
### 📌 api 变化[​](https://www.drissionpage.cn/features/4#-api-变化-1 "📌 api 变化的直接链接")
  * 页面对象删除`download_set`属性
  * 增加`set.download_path()`方法
  * 增加`set.download_file_name()`方法


### 📌 新增功能[​](https://www.drissionpage.cn/features/4#-新增功能 "📌 新增功能的直接链接")
  * Tab 对象和 Frame 对象也支持`download()`方法
  * 每个 Tab 对象可单独设置下载路径和重命名文件名
  * 可拦截浏览器下载任务并获取其信息
  * 可取消浏览器下载任务、获取下载进度、等待任务完成
  * 可设置遇到文件夹已存在时的处理方式


### 📌 行为变化[​](https://www.drissionpage.cn/features/4#-行为变化-1 "📌 行为变化的直接链接")
4.0 中默认不启用浏览器下载任务管理，只有在启动参数中设置了下载路径，或调用`set.download_path()`方法时才会启动。
未启动任务管理功能时，下载行为和普通使用一样。
### 📌 示例[​](https://www.drissionpage.cn/features/4#-示例-2 "📌 示例的直接链接")
以下示例可直接运行。
```
from DrissionPage import ChromiumPagepage = ChromiumPage()page.get('https://office.qq.com/download.html')page.set.download_path('tmp')# 设置文件保存路径page.set.download_file_name('qq')# 设置文件名page('#downloadWin').click()# 点击触发下载mission = page.wait.download_begin()# 等待下载开始并获取任务对象mission.wait()# 等下下载任务完成
```

**输出：**
```
url：https://dldir1.qq.com/qqfile/qq/TIM3.4.8/TIM3.4.8.22124.exe文件名：qq.exe目标路径：D:\coding\projects\DrissionPage\tmp100.0% 下载完成 D:\coding\projects\DrissionPage\tmp\qq.exe
```

## ✅️ 页面对象[​](https://www.drissionpage.cn/features/4#️-页面对象 "✅��️ 页面对象的直接链接")
这里说的页面对象包括 Page 对象（`ChromiumPage`、`WebPage`）、Tab 对象（`ChromiumTab`、`WebPageTab`）、`ChromiumFrame`对象。
### 📌 启动参数变化[​](https://www.drissionpage.cn/features/4#-启动参数变化 "📌 启动参数变化的直接链接")
4.0 中，创建`WebPage`和`ChromiumPage`对象时，不再接收`ChromiumDriver`对象。
意思是不再支持传递控制权的方式创建页面对象。
因为本身支持多个页面对象控制同一个标签页，如果需要多页面对象协同，只要`get_tab()`创建一个新对象就行，可和原有对象并行使用。
而且，传递控制权本身有稳定性方面隐患，因此新版中将其删除。
相应地，启动参数的名称也发生了变化：
  * `WebPage`对象的`driver_or_options`参数改名为`chromium_options`
  * `ChromiumPage`对象的`addr_driver_opts`参数改名为`addr_or_opts`


另外，`ChromiumPage`的启动参数`addr_or_opts`现在可以接收`int`数据，直接传入端口号。
### 📌 内置动作链[​](https://www.drissionpage.cn/features/4#-内置动作链 "📌 内置动作链的直接链接")
4.0 中，每个页面对象内置`actions`属性，即动作链。
内置的动作链与直接创建的动作链对象有一个不同点，每次操作会等待页面加载完成再执行。
**示例：**
```
page.actions.hold(ele).move(50).release()
```

### 📌 状态信息[​](https://www.drissionpage.cn/features/4#-状态信息 "📌 状态信息的直接链接")
旧版中，页面对象拥有`ready_state`、`is_loading`、`is_alive`属性，现在都合并到`states`属性中。
```
# ------ 旧版代码 ------print(page.is_loading)# ------ 新版代码 ------print(page.states.is_loading)
```

### 📌 其它[​](https://www.drissionpage.cn/features/4#-其它 "📌 其它的直接链接")
  * `ChromiumPage`和`WebPage`改为固定单例
  * `get_tab()`获取的 Tab 对象默认单例，可用`Settings`设置允许多例
  * 页面对象增加`raw_data`参数，s 模式下返回原始数据
  * 所有页面对象增加`close()`方法，`SessionPage`用于关闭连接，浏览器页面对象用于关闭标签页
  * 浏览器页面对象增加`wait()`方法，用于等待若干秒
  * 浏览器页面对象增加`wait.ele_loaded()`方法，等待元素加载到DOM
  * 浏览器页面对象增加`wait.title_change()`和`wait.url_change()`方法，用于等待 title 和 url 变化
  * 浏览器页面对象增加`wait.alert_closed()`方法，用于等待弹窗被手动关闭
  * 浏览器页面对象增加`set.cookie()`方法，可设置单个 cookie
  * 浏览器页面对象增加`set.blocked_urls()`方法，可设置忽略的连接
  * Tab 和 Page 对象增加`disconnect()`方法，用于断开与网页连接
  * Tab 和 Page 对象增加`reconnect()`方法，用于断开并重新连接网页
  * Tab 和 Page 对象增加`save()`方法，用于把网页保存为 mhtml
  * Tab 和 Page 对象增加`add_init_js()`和`remove_init_js()`方法
  * `quit()`方法增加`force`参数，可强制关闭浏览器进程
  * `ChromiumFrame`增加`ract`属性
  * `ChromiumFrame`的`frame_size`属性改为`rect.size`
  * `wait.ele_delete()`方法改为`wait.ele_deleted()`
  * `wait.ele_display()`方法改为`wait.ele_displayed()`
  * `wait.load_complete()`方法改为`wait.doc_loaded()`
  * 优化`SessionPage`和`WebPage`s 模式访问速度
  * `WebPage`在 d 模式时，`post()`返回`Response`对象


## ✅️ cookies 设置[​](https://www.drissionpage.cn/features/4#️-cookies-设置 "✅️ cookies 设置的直接链接")
  * `set.cookies()`可接收单个 cookie
  * 增加`set.cookies.clear()`方法用于清除 cookies
  * 增加`set.cookies.remove()`方法用于删除一个 cookie 项


## ✅️ 标签页管理[​](https://www.drissionpage.cn/features/4#️-标签页管理 "✅️ 标签页管理的直接链接")
### 📌 不再支持`to_tab()`功能[​](https://www.drissionpage.cn/features/4#-不再支持to_tab功能 "-不再支持to_tab功能的直接链接")
`to_tab()`的设计源自于 selenium，用于在多个标签页间切换程序焦点。
selenium 没有 tab 对象，driver 每次只能操作一个 tab。多 tab 使用时需在不同的 tab 间来回切换，且切换的时候会丢失之前获取过的元素，效率低，使用不便。
DrissionPage 3.x 开始就支持多 tab 对象共存，对象之间互不影响，而且标签页无需激活即可操作。因此不再需要切换标签页。
而且焦点切换时如果页面正在加载，实现逻辑较为复杂，也会有稳定性问题。
基于此，决定删除`to_tab()`方法，使用`get_tab()`取代之。
**涉及的 api修改：**
  * 删除`to_tab()`方法
  * 删除`to_main_tab()`、`set.main_tab()`方法
  * 删除`main_tab`属性
  * `new_tab()`方法删除`switch_to`参数


**新建标签页并切换到新标签页：**
```
# ------ 旧版代码 ------tab = page.new_tab(switch_to=True)# ------ 新版代码 ------tab = page.new_tab()
```

**操作另一个标签页**
```
# ------ 旧版代码 ------page.to_tab(page.tabs[1])# ------ 新版代码 ------tab = page.get_tab(1)# 创建一个可与page同时使用的tab对象
```

### 📌 `new_tab()`的新功能[​](https://www.drissionpage.cn/features/4#-new_tab的新功能 "-new_tab的新功能的直接链接")
Page 对象的`new_tab()`方法增加了 3 个参数：
  * `new_window`：是否创建新的窗口，新窗口与旧标签页同属一个浏览器，只是独立窗口
  * `background`：新建的标签页是否为不激活状态（即使不激活也可以操作）
  * `new_context`：是否创建独立的隐身窗口，该窗口与旧标签页 cookies 相互独立


现在`new_tab()`返回新建的标签页对象，而非其 tab_id。
**示例：**
```
tab = page.new_tab()tab.get('http://DrissionPage.cn')
```

### 📌 标签页的位置与大小[​](https://www.drissionpage.cn/features/4#-标签页的位置与大小 "📌 标签页的位置与大小的直接链接")
在旧版中，只有`ChromiumPage`或`WebPage`对象可以设置窗口位置、大小、状态。
Tab 对象（`ChromiumTan`、`WebPageTab`）虽然能获取窗口窗口上述信息，但只是获取 Page 所控制的标签页信息。
在 4.0 中，独立窗口的标签页，也能设置和获取上面这些属性。
以下属性和方法名称进行了修改:
  * `rect.borwser_size`改为`rect.window_size`
  * `rect.borwser_location`改为`rect.window_location`
  * `set.window.maximized()`改为`set.window.max()`
  * `set.window.minimized()`改为`set.window.mini()`
  * `set.window.fullscreen()`改为`set.window.full()`


**示例：**
```
tab = page.get_tab(1)print(tab.rect.window_state)# 获取窗口状态print(tab.rect.window_location)# 获取窗口位置print(tab.rect.window_size)# 获取窗口大小tab.set.window.size(500,500)# 设置窗口大小tab.set.window.location(500,500)# 设置窗口位置tab.set.window.max()# 窗口最大化# 更多详见相关文档……
```

### 📌 标签页的行为[​](https://www.drissionpage.cn/features/4#-标签页的行为 "📌 标签页的行为的直接链接")
在旧版中，标签页的开关、激活由 Page 对象管理。JS 弹窗也只有 Page 对象能处理。
在 4.0 中，标签页对象可以激活、关闭自己，也可以处理自己的弹出对话框。
  * `tab.set.activate()`：标签页对象激活自己
  * `tab.close()`：标签页对象关闭自己
  * `tab.handle_alert()`：标签页对象处理自己的弹窗
  * `tab.states.has_alert`：标签页增加此属性表示是否有弹窗存在


### 📌 `get_tab()`参数变化[​](https://www.drissionpage.cn/features/4#-get_tab参数变化 "-get_tab参数变化的直接链接")
现在`get_tab()`方法可接收标签页序号（序号从 0 开始）。`tab_id`参数改为`id_or_num`。
但需要注意，序号与标签页视觉排序不一定一致，而是按照激活顺序排列。
**示例：**
```
tab = page.get_tab(1)# 获取列表中第二个标签页的对象
```

## ✅️ 元素相关[​](https://www.drissionpage.cn/features/4#️-元素相关 "✅️ 元素相关的直接链接")
### 📌 定位语法变化[​](https://www.drissionpage.cn/features/4#-定位语法变化 "📌 定位语法变化的直接链接")
旧版中，定位语法中使用`@@-`或`@|-`表示否定，但视觉效果不明显，意义也不太明确。
因此改用`@!`替代，使其更能体现否定的含义。
`@!`可与`@@`或`@|`混用，与还是或关系视`@@`还是`@|`而定。
也可以单独使用，否定某个单独属性。
**示例：**
```
# ------ 旧版语法 ------page.ele('@@arg1=abc@@-arg2=def')# ------ 新版语法 ------page.ele('@@arg1=abc@!arg2=def')# ------ 旧版语法 ------page.ele('t:div@|arg1=abc@|-arg2=def')# ------ 新版语法 ------page.ele('t:div@|arg1=abc@!arg2=def')# ------ 旧版语法 ------page.ele('@@-arg1=abc')# ------ 新版语法 ------page.ele('@!arg1=abc')
```

### 📌 相对定位参数优化[​](https://www.drissionpage.cn/features/4#-相对定位参数优化 "📌 相对定位参数优化的直接链接")
旧版本中，相对定位如果想用序号获取元素，需要写成`ele.next(index=1)`。
但是我想把这个语句变得更简化一点，写成`ele.next(1)`即可表示获取下一个兄弟元素。
4.0 中支持这种写法，当`filter_loc`参数接收`int`类型参数，即可当作`index`参数使用。
`parent()`方法增加`index`参数，当`level_or_loc`传入定位符，使用此参数选择第几个结果。
### 📌 位置和大小[​](https://www.drissionpage.cn/features/4#-位置和大小 "📌 位置和大小的直接链接")
旧版中，元素大小和位置信息由`location`、`locations`、`size`几个属性提供。
这些属性都与形状相关，为使逻辑更清晰，与页面对象逻辑一致，将它们统一归纳到`rect`属性中。
  * 删除`size`、`location`、`locations`属性，新增`rect`属性
  * 旧版中`loactions.****`的属性改为`rect.****`
  * 大小和位置信息，从`int`类型改为`float`类型
  * 增加`states.has_rect`属性，返回元素是否拥有大小和位置
  * 增加`states.is_whole_in_viewport`属性，返回元素是否整个都在视口内


```
# ------ 旧版代码 ------ele.sizeele.locationele.locations.midpoint# ------ 新版代码 ------ele.rect.sizeele.rect.locationele.rect.midpoint
```

### 📌 点击[​](https://www.drissionpage.cn/features/4#-点击 "📌 点击的直接链接")
  * `click()`增加`wait_stop`参数，默认等待元素运动停止再点击
  * `click()`默认等待元素运动停止再执行点击
  * `click.twice()`改为`click.multiple()`


### 📌 查找元素失败显示细节[​](https://www.drissionpage.cn/features/4#-查找元素失败显示细节 "📌 查找元素失败显示细节的直接链接")
旧版链式查找元素时，遇到其中一个查找失败，不能很直观地显示哪个语句失败。
在 4.0 中，可以把查找失败的语句和定位语句显示在报错信息中。
**示例**
```
from DrissionPage import ChromiumPagepage = ChromiumPage(timeout=1)page.get('https://baidu.com')print(page('#wrapper')('#s_tab')('#abcd').text)# ('#abcd')这个元素不存在
```

输出：
```
DrissionPage.errors.ElementNotFoundError: 没有找到元素。method: ele()args: {'locator': '#abcd'}
```

### 📌 设置查找失败元素返回默认值[​](https://www.drissionpage.cn/features/4#-设置查找失败元素返回默认值 "📌 设置查找失败元素返回默认值的直接链接")
如果查找元素后要获取一个属性，但这个元素不一定存在，或者链式查找其中一个节点找不到，可以设置查找失败时返回的值，而不是抛出异常。
这样可以简化一些采集逻辑。
**示例**
比如说，遍历页面上一个列表中多个对象，但其中有些元素可能缺失某个子元素，旧版中要这样写：
```
from DrissionPage import ChromiumPagepage = ChromiumPage()for li in page.eles('t:li'):  ele = li('.name')  name = ele.text if ele elseNone  ele = li('.age')  age = ele.text if ele elseNone  ele = li('.phone')  phone = ele.text if ele elseNone
```

在新版中，可以这样写：
```
from DrissionPage import ChromiumPagepage = ChromiumPage()page.set.NoneElement_value('没找到')for li in page.eles('t:li'):  name = li('.name').text  age = li('.age').text  phone = li('.phone').text
```

这样，假如某个子元素不存在，不会抛出异常，而是返回`'没找到'`这个字符串。
### 📌 更多[​](https://www.drissionpage.cn/features/4#-更多 "📌 更多的直接链接")
  * `ele()`和`s_ele()`增加`index`参数，可指定获取第几个
  * 增加`wait.stop_moving()`方法，可等待移动结束
  * 增加`wait()`方法，用于等待若干秒
  * 增加`check()`方法，可选中或取消选中元素
  * 增加`wait.has_rect()`方法，用于等待元素拥有大小和位置
  * 滚动添加`to_center()`方式，可滚动到视口中央
  * 增加`select.by_option()`和`select.cancel_by_option()`方法，可选取列表项元素
  * 增加`states.has_rect`属性
  * 元素被覆盖时，`states.is_covered`属性返回覆盖元素的 id
  * 添加`states.is_whole_in_viewport`属性，判断是否整个都在视口中
  * `input()`方法增加`by_js`参数
  * `save()`的`rename`参数改为`name`
  * `get_src()`支持 blob 类型
  * `css_path`获取的路径更精确
  * 相对定位的`timeout`参数默认改为`None`
  * `wait.delete()`方法改为`wait.deleted()`
  * `wait.disabled_or_delete()`方法改为`wait.disabled_or_deleted()`
  * `wait.display()`方法改为`wait.displayed()`
  * 可用`==`比较两个元素
  * 查找元素速度提高


## ✅️ 启动配置[​](https://www.drissionpage.cn/features/4#️-启动配置 "✅️ 启动配置的直接链接")
### 📌 删除 easy_set 方法[​](https://www.drissionpage.cn/features/4#-删除-easy_set-方法 "📌 删除 easy_set 方法的直接链接")
easy_set 原本设计目的是为了方便修改 ini 文件设置。
本想着设置一次，之后无需再调用。但可能由于文档描述不清晰，很多人将其写到了正式的代码中。
因为 ini 文件的修改会影响其它项目，这是作者不推荐的用法。
而且，实际使用中发现 easy_set 并没有变得更方便，功能可用`ChromiumOptions`对象的`save()`方法代替。
因此决定将其删除，也可以免去多维护一份代码。
### 📌 支持设置实验项[​](https://www.drissionpage.cn/features/4#-支持设置实验项 "📌 支持设置实验项的直接链接")
4.0 新增支持启动浏览器时设置实验项，即`'chrome://flags'`中的项目。
使用新增的`set_flag()`方法设置。使用`clear_flags_in_file()`清空配置文件中已设置的项。
有哪些实验项，具体在`'chrome://flags'`查看。
**示例：**
```
from DrissionPage import ChromiumOptionsco = ChromiumOptions()co.set_flag('temporary-unexpire-flags-m118','1')co.set_flag('disable-accelerated-2d-canvas')
```

### 📌 ini 文件变化[​](https://www.drissionpage.cn/features/4#-ini-文件变化 "📌 ini 文件变化的直接链接")
  * `chrome_options`类改为`chromium_options`
  * `binary_location`项改为`browser_path`
  * `page_load_strategy`项改为`load_mode`
  * `debugger_address`项改为`address`
  * `arguments`项删除`'--remote-allow-origins=*'`参数
  * `arguments`项增加`'--no-default-browser-check'`、`'--disable-suggestions-ui'`、`'--disable-popup-blocking'`、`'--hide-crash-restore-bubble'`、`'--disable-features=PrivacySandboxSettings4'`参数
  * `paths`类增加`tmp_paht`项
  * 删除`experimental_options`项
  * `chrome_options`类增加`prefs`、`flags`、`existing_only`项
  * 增加`others`类，包含`retry_times`和`retry_interval`项


### 📌 `ChromiumOptions` 修改[​](https://www.drissionpage.cn/features/4#-chromiumoptions-修改 "-chromiumoptions-修改的直接链接")
  * 增加`set_flag()`和`clear_flags_in_file()`，用于设置实验项
  * 增加`existing_only()`方法和`is_existing_only`属性，可指定只接管浏览器而不自动启动新的
  * 增加`ignore_certificate_errors()`方法，可忽略证书报错
  * 增加`retry_times`、`retry_interval`属性和`set_retry()`方法，可设置重试参数
  * 增加`incognito()`方法，可设置无痕模式
  * 增加`set_tmp_path()`方法，可指定临时文件夹路径
  * 增加`tmp_path`和`is_auto_port`属性
  * `auto_port()`增加`tmp_path`参数
  * `set_paths()` 方法拆分成`set_browser_path()`、`set_local_port()`、`set_address()`、`set_download_path()`、`set_user_data_path()`、`set_cache_path()` 方法
  * `set_page_load_strategy()`改成`set_load_mode()`
  * `set_headless()`改成`headless()`
  * `set_no_imgs()`改成`no_imgs()`
  * `set_no_js()`改成`no_js()`
  * `set_mute()`改成`mute()`
  * `debugger_address`改成`address`


### 📌 `SessionOptions` 修改[​](https://www.drissionpage.cn/features/4#-sessionoptions-修改 "-sessionoptions-修改的直接链接")
  * `SessionOptions`的`set_paths()`方法改为`set_download_path()`
  * 增加`retry_times`、`retry_interval`属性和`set_retry()`方法，可设置重试参数


### 📌 其它[​](https://www.drissionpage.cn/features/4#-其它-1 "📌 其它的直接链接")
  * 启动或接管浏览器时，可自动关闭弹出的隐私声明
  * 在无界面系统启动浏览器时，自动使用无头，可用`set_headless(False)`禁用
  * 当`set_headless(False)`但接管了无头浏览器，将关闭并启动新的有头浏览器
  * `auto_port()`方法支持多线程


## ✅️ 其它[​](https://www.drissionpage.cn/features/4#️-其它 "✅️ 其它的直接链接")
### 📌 删除 2.x 代码[​](https://www.drissionpage.cn/features/4#-删除-2x-代码 "📌 删除 2.x 代码的直接链接")
`MixPage` 是 `WebPage`的前身，基于 selenium。
随着 3.x 版本迭代，自研的底层日渐成熟并完全超越旧版。旧版已到了退休的时候。。
为对项目进行精简，避免新代码受旧功能制约，因此将旧代码删除。
删除以下类：`MixPage`、`DriverPage`、`DriverOptions`、`Drission`。
旧版对作者的成长有过巨大贡献，因此将其独立成一个库，以此来继续它的生命，和纪念它做出过的成果。
可用以下命令安装旧版尝旧：
```
pip install MixPage
```

### 📌 异常变化[​](https://www.drissionpage.cn/features/4#-异常变化 "📌 异常变化的直接链接")
  * `CallMethodError`改为`CDPError`
  * `ElementLossError`改为`ElementLostError`
  * `ContextLossError`改为`ContextLostError`
  * `TabClosedError`改为`PageDisconnectedError`
  * 增加`WaitTimeoutError`
  * 增加`GetDocumentError`
  * 增加`WrongURLError`
  * 增加`StorageError`
  * 增加`CookieFormatError`
  * 增加`TargetNotFoundError`


### 📌 Settings 变化[​](https://www.drissionpage.cn/features/4#-settings-变化 "📌 Settings 变化的直接链接")
  * 增加`singleton_tab_obj`，设置 Tab 对象是否允许多例
  * `raise_ele_not_found`改为`raise_when_ele_not_found`
  * `raise_click_failed`改为`raise_when_click_failed`


### 📌 更多[​](https://www.drissionpage.cn/features/4#-更多-1 "📌 更多的直接链接")
  * `handle_alert()`方法增加`next_one`参数，可处理下一个出现的弹窗
  * 浏览器页面对象增加`set.auto_handle_alert()`方法，可设置自动处理弹窗
  * `SessionPage`增加`set.encoding()`方法和`encoding`属性
  * `<option>` 元素可以接受点击，操作更符合直觉
  * `run_js()`、`run_js_loaded()`、`run_async_js()`方法增加`timeout`参数
  * `run_async_js()`删除`timeout`参数
  * `timeouts`的`implicit`改成`base`
  * `ActionChains`改成`Actions`
  * 动作链的移动方法增加`duration`参数
  * 动作链增加`input()`方法
  * 动作链`key_down()`和`key_up()`方法可接收按键名称文本
  * 动作链`type()`方法`text`参数改为`keys`
  * `get_screenshot()`方法增加`name`属性，可指定文件名
  * 元素的`get_screenshot()`方法增加`scroll_to_center`参数，截图前先滚动到页面正中
  * `wait.new_tab()`方法成功时返回新标签页 id
  * `tabs`不包含 F12 的窗口
  * `DrissionPage.common`路径增加`wait_until()`方法，支持自定义组合等待条件
  * `DrissionPage.common`路径增加`get_blob()`方法，用于获取指定 blob 内容


## ✅️ 问题修复[​](https://www.drissionpage.cn/features/4#️-问题修复 "✅️ 问题修复的直接链接")
  * 修复网络连接极不稳定时获取文档失败问题
  * 修复相对定位`timeout`失效问题
  * 修复 shadow root 内定位元素可能偏差问题
  * 修复异域`ChromiumFrame`内部元素无法获取屏幕坐标的问题
  * 修复相对路径插件加载失败的问题
  * 所有循环增加超时设置，避免出现卡死
  * 修复元素截图时窗口外部分空白问题
  * 修复 Tab 没有继承 Page 下载路径的问题
  * 修复 `<iframe>` 内元素获取 href 属性错误问题
  * 修复 cookie 设置 expires 时的问题


[上一页💥 4.1 功能介绍](https://www.drissionpage.cn/features/4.1)[下一页💥 3.2 功能介绍](https://www.drissionpage.cn/features/3)
  * [✅️ 新的抓包功能](https://www.drissionpage.cn/features/4#️-新的抓包功能)
    * [📌 旧 api 变化](https://www.drissionpage.cn/features/4#-旧-api-变化)
    * [📌 新 api](https://www.drissionpage.cn/features/4#-新-api)
    * [📌 示例](https://www.drissionpage.cn/features/4#-示例)
  * [✅️ 新的页面访问逻辑](https://www.drissionpage.cn/features/4#️-新的页面访问逻辑)
    * [📌 api 变化](https://www.drissionpage.cn/features/4#-api-变化)
    * [📌 行为变化](https://www.drissionpage.cn/features/4#-行为变化)
    * [📌 新的`none`加载模式](https://www.drissionpage.cn/features/4#-新的none加载模式)
    * [📌 示例](https://www.drissionpage.cn/features/4#-示例-1)
  * [✅️ 新的下载管理功能](https://www.drissionpage.cn/features/4#️-新的下载管理功能)
    * [📌 api 变化](https://www.drissionpage.cn/features/4#-api-变化-1)
    * [📌 新增功能](https://www.drissionpage.cn/features/4#-新增功能)
    * [📌 行为变化](https://www.drissionpage.cn/features/4#-行为变化-1)
    * [📌 示例](https://www.drissionpage.cn/features/4#-示例-2)
  * [✅️ 页面对象](https://www.drissionpage.cn/features/4#️-页面对象)
    * [📌 启动参数变化](https://www.drissionpage.cn/features/4#-启动参数变化)
    * [📌 内置动作链](https://www.drissionpage.cn/features/4#-内置动作链)
    * [📌 状态信息](https://www.drissionpage.cn/features/4#-状态信息)
    * [📌 其它](https://www.drissionpage.cn/features/4#-其它)
  * [✅️ cookies 设置](https://www.drissionpage.cn/features/4#️-cookies-设置)
  * [✅️ 标签页管理](https://www.drissionpage.cn/features/4#️-标签页管理)
    * [📌 不再支持`to_tab()`功能](https://www.drissionpage.cn/features/4#-不再支持to_tab功能)
    * [📌 `new_tab()`的新功能](https://www.drissionpage.cn/features/4#-new_tab的新功能)
    * [📌 标签页的位置与大小](https://www.drissionpage.cn/features/4#-标签页的位置与大小)
    * [📌 标签页的行为](https://www.drissionpage.cn/features/4#-标签页的行为)
    * [📌 `get_tab()`参数变化](https://www.drissionpage.cn/features/4#-get_tab参数变化)
  * [✅️ 元素相关](https://www.drissionpage.cn/features/4#️-元素相关)
    * [📌 定位语法变化](https://www.drissionpage.cn/features/4#-定位语法变化)
    * [📌 相对定位参数优化](https://www.drissionpage.cn/features/4#-相对定位参数优化)
    * [📌 位置和大小](https://www.drissionpage.cn/features/4#-位置和大小)
    * [📌 点击](https://www.drissionpage.cn/features/4#-点击)
    * [📌 查找元素失败显示细节](https://www.drissionpage.cn/features/4#-查找元素失败显示细节)
    * [📌 设置查找失败元素返回默认值](https://www.drissionpage.cn/features/4#-设置查找失败元素�返回默认值)
    * [📌 更多](https://www.drissionpage.cn/features/4#-更多)
  * [✅️ 启动配置](https://www.drissionpage.cn/features/4#️-启动配置)
    * [📌 删除 easy_set 方法](https://www.drissionpage.cn/features/4#-删除-easy_set-方法)
    * [📌 支持设置实验项](https://www.drissionpage.cn/features/4#-支持设置实验项)
    * [📌 ini 文件变化](https://www.drissionpage.cn/features/4#-ini-文件变化)
    * [📌 `ChromiumOptions` 修改](https://www.drissionpage.cn/features/4#-chromiumoptions-修改)
    * [📌 `SessionOptions` 修改](https://www.drissionpage.cn/features/4#-sessionoptions-修改)
    * [📌 其它](https://www.drissionpage.cn/features/4#-其它-1)
  * [✅️ 其它](https://www.drissionpage.cn/features/4#️-其它)
    * [📌 删除 2.x 代码](https://www.drissionpage.cn/features/4#-删除-2x-代码)
    * [📌 异常变化](https://www.drissionpage.cn/features/4#-异常变化)
    * [📌 Settings 变化](https://www.drissionpage.cn/features/4#-settings-变化)
    * [📌 更多](https://www.drissionpage.cn/features/4#-更多-1)
  * [✅️ 问题修复](https://www.drissionpage.cn/features/4#️-问题修复)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/features/4)
  * [QQ群：391178600](https://www.drissionpage.cn/features/4)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
