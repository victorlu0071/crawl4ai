# Content from: https://www.drissionpage.cn/versions/4.0.x

[跳到主要内容](https://www.drissionpage.cn/versions/4.0.x#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/versions/4.0.x)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/versions/4.0.x)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [📒 v4.1](https://www.drissionpage.cn/versions/4.1.x)
  * [📒 v4.0](https://www.drissionpage.cn/versions/4.0.x)
  * [📒 v3.x](https://www.drissionpage.cn/versions/3x)
  * [📒 v1.5-v2.x](https://www.drissionpage.cn/versions/2x)
  * [📒 v0.x-v1.4](https://www.drissionpage.cn/versions/1x)
  * [📆 下一步计划](https://www.drissionpage.cn/versions/next)
  * [📖 关于项目](https://www.drissionpage.cn/versions/statement)


  * [](https://www.drissionpage.cn/)
  * 📒 v4.0


本页总览
# 📒 v4.0
## v4.0.5.6[​](https://www.drissionpage.cn/versions/4.0.x#v4056 "v4.0.5.6的直接链接")
  * 优化`auto_port()`逻辑
  * `set.cookies()`忽略过期的 cookie
  * 修复下载文件可能出现无写入权限报错
  * 修复`SessionPage`的 headers 设置问题
  * 修复链接以`'./'`开头时`ele.link`获取不准确的问题
  * 修复异域`<iframe>`跳转到同域时的问题


## v4.0.5.2[​](https://www.drissionpage.cn/versions/4.0.x#v4052 "v4.0.5.2的直接链接")
  * 增加视觉相对定位语法 [[详情](https://www.drissionpage.cn/get_elements/relative#%EF%B8%8F%EF%B8%8F-%E5%9F%BA%E4%BA%8E%E8%A7%86%E8%A7%89%E7%9B%B8%E5%AF%B9%E5%AE%9A%E4%BD%8D)]
  * 改进元素结果列表筛选功能 [[详情](https://www.drissionpage.cn/get_elements/filter)]
  * `wait.has_rect()`和`wait.covered()`返回具体信息
  * 删除元素获取任意属性语法
  * 删除之前声明废弃的参数、方法和属性
  * 修复`states.is_alive()`和`wait.deleted()`问题


## v4.0.4.25[​](https://www.drissionpage.cn/versions/4.0.x#v40425 "v4.0.4.25的直接链接")
  * 支持对`eles()`返回的列表进行筛选
  * `DrissionPage.common`新增`get_eles()`方法，可接收多个定位符获取多个元素 [[详情](https://www.drissionpage.cn/get_elements/find_in_object#%EF%B8%8F%EF%B8%8F-%E5%90%8C%E6%97%B6%E5%8C%B9%E9%85%8D%E5%A4%9A%E4%B8%AA%E5%AE%9A%E4%BD%8D%E7%AC%A6)]
  * `input()`输入前会自动等待元素可点击
  * `set.cookies()`接收`str`形式 cookies 时，只支持用`';'`做分隔符
  * 修复监听一个报错


## v4.0.4.23[​](https://www.drissionpage.cn/versions/4.0.x#v40423 "v4.0.4.23的直接链接")
  * 元素增加`states.is_clickable`属性和`wait.clickable()`、`set.style()`方法
  * `tree()`增加`text`、`show_js`、`show_css`参数
  * `wait.stop_moving()`参数顺序改变
  * `tab_ids`属性不再屏蔽插件标签页
  * 修复`SessionPage`的`get()`方法访问本地中文路径问题
  * 等待元素时可抛出页面断开异常


## v4.0.4.22[​](https://www.drissionpage.cn/versions/4.0.x#v40422 "v4.0.4.22的直接链接")
  * 动作链`scroll()`方法参数位置变化
  * 页面对象的`save()`方法可根据后缀自动判断类型
  * 中键单击返回 Tab 对象
  * `tab_ids`属性忽略插件 tab
  * 优化 cookies 设置逻辑
  * Frame 对象初始化时不再等待 url 变化
  * 修复全局代理时无法连接浏览器的问题
  * 修复截图文件名过长时的问题
  * 修复带 html 节点的 shadow root 获取不到子元素问题
  * 降低失去元素报错可能性


## v4.0.4.21[​](https://www.drissionpage.cn/versions/4.0.x#v40421 "v4.0.4.21的直接链接")
  * `add_ele()`的`outerHTML`参数改为`html_or_info`，可新增不插入到 DOM 的元素
  * `wait.ele_loaded()`改成`wait.eles_loaded()`，可等待多个元素全部或任一个加载
  * 取消无界面 Linux 自动无头功能
  * 调整`quit()`逻辑
  * 修复 prompt 无法输入的问题
  * 修复`WebPageTab`的`close()`报错问题
  * 修复下拉列表已选中元素再点击会取消的问题
  * 修复`run_js()`无法添加`dict`参数问题
  * 修复`set.cookies()`的一个问题


## v4.0.4.17[​](https://www.drissionpage.cn/versions/4.0.x#v40417 "v4.0.4.17的直接链接")
  * Page 对象的`set.auto_handle_alert()`增加`all_tabs`参数
  * 修复`ele.text`速度慢的问题
  * 修复在未访问网页时设置`'__Host-'`开头的 cookie 时出现的问题


## v4.0.4.16[​](https://www.drissionpage.cn/versions/4.0.x#v40416 "v4.0.4.16的直接链接")
  * `ChromiumPage`增加`browser_version`属性
  * `DataPacket.request`增加`cookies`属性
  * `wait_slient()`方法增加`limit`参数
  * `Keys`增加`CTRL_A`等 6 个组合键
  * 元素的`save()`方法增加`rename`参数
  * 元素的`input()`方法的`clear`参数默认值改为`False`
  * 动作链`type()`可接收键盘以外的字符
  * `get_tab()`和`get_tabs()`默认获取普通 tab
  * 修复动作链`wait()`问题


## v4.0.4.13[​](https://www.drissionpage.cn/versions/4.0.x#v40413 "v4.0.4.13的直接链接")
  * 动作链`wait()`增加随机功能
  * 当 tab 设置不为单例时，`latest_tab`返回 tab id
  * 修复新标签页重复创建连接问题
  * 修复等待新 tab 不正确问题


## v4.0.4.12[​](https://www.drissionpage.cn/versions/4.0.x#v40412 "v4.0.4.12的直接链接")
  * 元素增加获取任意属性方式
  * 调整`quit()`逻辑
  * 优化`set.cookies()`逻辑
  * 修复`get_tab()`问题
  * 修复`set_flags()`特定情况下出现的问题
  * 修复某`WebPage`在些情况下`get_tab()`时出现的问题


## v4.0.4.9[​](https://www.drissionpage.cn/versions/4.0.x#v4049 "v4.0.4.9的直接链接")
  * `get_tab()`方法增加几个参数
  * `find_tabs()`方法改为`get_tabs()`，且改为默认返回标签页对象
  * 设置`headers`时可接收从浏览器复制的文本格式
  * `common`路径增加`from_selenium()`和`from_playwright()`方法
  * `latest_tab`改为返回标签页对象
  * `tabs`属性改为`tab_ids`
  * 修复从文本生成的静态元素`link`属性报错问题
  * 修复保存的 mhtml 文件无法被浏览器解析问题


## v4.0.4.8[​](https://www.drissionpage.cn/versions/4.0.x#v4048 "v4.0.4.8的直接链接")
  * 增加`click.for_new_tab()`方法
  * `wait()`方法增加`scope`参数，可等待指定随机时间
  * `set.upload_files()`和`click.to_upload()`方法支持接收`Path`类型
  * `click.to_download()`增加`timeout`参数
  * 元素对象`page`属性改为指向总体的 Page对象，增加`owner`属性
  * 完善找 chrome 路径逻辑
  * 调整`quit()`逻辑
  * 修复处理有些下拉列表时报错问题
  * 修复页面用 css 查找元素时会找到文本的问题
  * 修复用 css 在元素下获取多个子元素时数量不正确问题
  * 修复在 ini 文件设置下载路径时报错问题
  * 修复`run_async_js()`报错问题
  * 修复`reconnect()`报错问题


## v4.0.4.5[​](https://www.drissionpage.cn/versions/4.0.x#v4045 "v4.0.4.5的直接链接")
  * 截图左上和右下参数可只接收其中一个
  * 配置对象`save()`可生成不存在的路径
  * 增加`click.to_upload()`和`click.to_download()`方法
  * `DrissionPage.common`增加`tree()`方法
  * 去除`upload()`方法
  * 修复`handle_alert()`
  * 修复一个 js 结果解析问题
  * 修复命令行问题


## v4.0.4.3[​](https://www.drissionpage.cn/versions/4.0.x#v4043 "v4.0.4.3的直接链接")
  * `ChromiumOptions`增加`clear_arguments()`、`clear_prefs()`和`clear_flags()`方法
  * 浏览器页面对象增加`upload()`方法
  * 浏览器页面对象增加`add_ele()`方法
  * `run_js()`方法可读取文件
  * `click.multiple()`改为`click.multi()`
  * 修复旧版 python 中`get()`报错问题


## v4.0.4.1[​](https://www.drissionpage.cn/versions/4.0.x#v4041 "v4.0.4.1的直接链接")
  * 打包程序即使不带上 ini 文件也不会报错
  * `SessionOptions`增加`clear_headers()`方法
  * `Settings`增加`cdp_timeout`属性
  * `prop()`改成`property()`，参数改为`name`
  * `get_cookies()`改为`cookies()`
  * `get_src()`改为`src()`
  * 删除`cookies`属性
  * `get_session_storage()`、`get_local_storage()`改为`session_storage()`、`local_storage()`
  * `pageLoad`改成`page_load`
  * `set_a_header()`、`remove_a_header()`、`set.header()`、`set.attr()`的参数改为`name`
  * 元素增加`value`属性和`set.value()`方法
  * `loc_or_ele`、`loc_or_str`等参数改为`locator`
  * 提高截图 jpg 格式画质
  * 修复 s 模式`timeout`参数失效问题
  * 修复`wait.has_rect()`等出现的问题
  * 修复找不到浏览器路径时报 ini 错误问题
  * 增加一些提示


## v4.0.3.4[​](https://www.drissionpage.cn/versions/4.0.x#v4034 "v4.0.3.4的直接链接")
此版本对项目进行了大量重构，新增了不少功能，改善了运行逻辑，优化了项目结构，解决了很多以前积累的问题。对比旧版本有质的提高。
但同时很多 api 产生了变化，不能完全兼容旧版本。
  * 改进抓包功能 
    * 页面对象新增`listen`属性，弃用`FlowViewer`
    * 删除`wait.set_targets()`删除
    * 删除`wait.stop_listening()`方法
    * 删除`wait.data_packets()`方法
    * `DrissionPage.common`路径删除`FlowViewer`
    * 用`listen.set_start()`和`listen.stop()`启动和停止监听
    * 用`listen.wait()`阻塞等待数据包
    * 用`listen.steps()`同步获取监听结果
    * 增加`listen.wait_silent()`等待所有请求完成（包含 targets 以外的）
    * 监听结果结构优化，request 和 response 数据分开存放
  * 重构连接逻辑 
    * 页面对象`page_load_strategy`属性改名为`load_mode`
    * `set.load_strategy`改为`set.load_mode`
    * `get()`方法的`timeout`参数现在可覆盖整个过程
    * `timeout`参数对非`get()`方法触发的加载（如点击链接）也能生效
    * `SessionPage`和`WebPage`的 s 模式，如收到空数据，也会重试
    * `SessionPage`的`get()`方法可以指向本地文件
    * 新的`none`加载模式
  * 改进下载管理功能 
    * 页面对象删除`download_set`属性
    * 增加`set.download_path()`方法
    * 增加`set.download_file_name()`方法
    * Tab 对象和 Frame 对象也支持`download()`方法
    * 每个 Tab 对象可单独设置下载路径和重命名文件名
    * 可拦截浏览器下载任务并获取其信息
    * 可取消浏览器下载任务、获取下载进度、等待任务完成
    * 可设置遇到文件夹已存在时的处理方式
    * 默认不启用浏览器下载任务管理
  * 页面对象改进 
    * `ChromiumPage`和`WebPage`改为固定单例
    * `get_tab()`获取的 Tab 对象默认单例，可用`Settings`设置允许多例
    * 浏览器页面对象启动时不再接收`ChromiumDriver`对象
    * `WebPage`对象的`driver_or_options`参数改名为`chromium_options`
    * `ChromiumPage`对象的`addr_driver_opts`参数改名为`addr_or_opts`
    * 页面对象内置动作链
    * `ready_state`、`is_loading`、`is_alive`属性合并到`states`属性中
    * 页面对象增加`raw_data`参数，s 模式下返回原始数据
    * 所有页面对象增加`close()`方法，`SessionPage`用于关闭连接，浏览器页面对象用于关闭标签页
    * 浏览器页面对象增加`wait()`方法，用于等待若干秒
    * 浏览器页面对象增加`wait.ele_loaded()`方法，等待元素加载到DOM
    * 浏览器页面对象增加`wait.title_change()`和`wait.url_change()`方法，用于等待 title 和 url 变化
    * 浏览器页面对象增加`wait.alert_closed()`方法，用于等待弹窗被手动关闭
    * 浏览器页面对象增加`set.blocked_urls()`方法，可设置忽略的连接
    * Tab 和 Page 对象增加`disconnect()`、`reconnect()`和`save()`方法
    * Tab 和 Page 对象增加`add_init_js()`和`remove_init_js()`方法
    * `wait.ele_delete()`方法改为`wait.ele_deleted()`
    * `wait.ele_display()`方法改为`wait.ele_displayed()`
    * `wait.load_complete()`方法改为`wait.doc_loaded()`
    * `quit()`方法增加`force`参数，可强制关闭浏览器进程
    * `ChromiumFrame`增加`ract`属性
    * `ChromiumFrame`的`frame_size`属性改为`rect.size`
    * 优化`SessionPage`和`WebPage`s 模式访问速度
    * `WebPage`在 d 模式时，`post()`返回`Response`对象
  * 标签页管理改进 
    * 删除`to_tab()`方法
    * 删除`to_main_tab()`、`set.main_tab()`方法
    * 删除`main_tab`属性
    * `new_tab()`方法删除`switch_to`参数
    * `new_tab()`方法增加`new_window`、`background`、`new_context`参数
    * `rect.borwser_size`改为`rect.window_size`
    * `rect.borwser_location`改为`rect.window_location`
    * `set.window.maximized()`改为`set.window.max()`
    * `set.window.minimized()`改为`set.window.mini()`
    * `set.window.fullscreen()`改为`set.window.full()`
    * Tab 对象增加`set.activate()`、`close()`、`handle_alert()`、`states.has_alert`
    * `get_tab()`的`tab_id`参数改为`id_or_num`，可接收序号
  * cookies 设置改进 
    * `set.cookies()`可接收单个 cookie
    * 增加`set.cookies.clear()`方法用于清除 cookies
    * 增加`set.cookies.remove()`方法用于删除一个 cookie 项
  * 元素相关改进 
    * 查找元素增加`@!`语法
    * 删除`@@-`和`@|-`语法
    * `ele()`和`s_ele()`增加`index`参数，可指定获取第几个
    * 相对定位第一个参数支持接收序号
    * 位置和大小 
      * 删除`size`、`location`、`locations`属性，新增`rect`属性
      * 旧版中`loactions.****`的属性改为`rect.****`
      * 大小和位置信息，从`int`类型改为`float`类型
      * 增加`states.has_rect`属性，返回元素是否拥有大小和位置
      * 增加`states.is_whole_in_viewport`属性，返回元素是否整个都在视口内
    * 点击改进 
      * `click()`增加`wait_stop`参数，默认等待元素运动停止再点击
      * `click()`默认等待元素运动停止再执行点击
      * `click.twice()`改为`click.multiple()`
    * 查找元素失败显示细节
    * 可设置查找失败元素返回默认值
    * 增加`wait.stop_moving()`方法，可等待移动结束
    * 增加`wait()`方法，等待若干秒
    * 增加`check()`方法，可选中或取消选中元素
    * 滚动添加`to_center()`方式，可滚动到视口中央
    * 增加`select.by_option()`和`select.cancel_by_option()`方法，可选取列表项元素
    * 增加`states.has_rect`属性
    * 添加`states.is_whole_in_viewport`属性，判断是否整个都在视口中
    * 元素被覆盖时，`states.is_covered`属性返回覆盖元素的 id
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
  * 启动配置改进 
    * 删除 easy_set 方法
    * 启动或接管浏览器时，可自动关闭弹出的隐私声明
    * 在无界面系统启动浏览器时，自动使用无头，可用`set_headless(False)`禁用
    * 当`set_headless(False)`但接管了无头浏览器，将关闭并启动新的有头浏览器
    * `auto_port()`方法支持多线程
    * ini 文件 
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
    * `ChromiumOptions`
      * 增加`set_flag()`和`clear_flags_in_file()`，用于设置实验项
      * 增加`existing_only()`方法和`is_existing_only`属性，可指定只接管浏览器而不自动启动新的
      * 增加`ignore_certificate_errors()`方法，可忽略证书报错
      * 增加`retry_times`、`retry_interval`属性和`set_retry()`方法，可设置重试参数
      * 增加`incognito()`方法，可设置无痕模式
      * 增加`set_tmp_path()`方法
      * 增加`tmp_path`和`is_auto_port`属性
      * `auto_port()`增加`tmp_path`参数
      * `set_paths()` 方法拆分成`set_browser_path()`、`set_local_port()`、`set_address()`、`set_download_path()`、`set_user_data_path()`、`set_cache_path()` 方法
      * `set_page_load_strategy()`改成`set_load_mode()`
      * `set_headless()`改成`headless()`
      * `set_no_imgs()`改成`no_imgs()`
      * `set_no_js()`改成`no_js()`
      * `set_mute()`改成`mute()`
      * `debugger_address`改成`address`
    * `SessionOptions`
      * `SessionOptions`的`set_paths()`方法改为`set_download_path()`
      * 增加`retry_times`、`retry_interval`属性和`set_retry()`方法，可设置重试参数
  * 其它 
    * 删除 2.x 代码
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
    * `DrissionPage.common`路径增加`get_blob()`方法
    * 异常变化 
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
    * Settings 变化 
      * 增加`singleton_tab_obj`，设置 Tab 对象是否允许多例
      * `raise_ele_not_found`改为`raise_when_ele_not_found`
      * `raise_click_failed`改为`raise_when_click_failed`
  * 优化 
    * MAC 和 Linux 系统添加默认浏览器路径
    * 全面重构对象启动和运行逻辑，大幅提高稳定性
    * 接管或启动浏览器不再要求`--remote-allow-orignins`参数
    * 所有涉及循环的代码都加上超时设施，杜绝卡死
    * 对`ChromiumFrame`进行完全重构，提高稳定性
    * 调整项目结构
  * 问题修复 
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


[上一页📒 v4.1](https://www.drissionpage.cn/versions/4.1.x)[下一页📒 v3.x](https://www.drissionpage.cn/versions/3x)
  * [v4.0.5.6](https://www.drissionpage.cn/versions/4.0.x#v4056)
  * [v4.0.5.2](https://www.drissionpage.cn/versions/4.0.x#v4052)
  * [v4.0.4.25](https://www.drissionpage.cn/versions/4.0.x#v40425)
  * [v4.0.4.23](https://www.drissionpage.cn/versions/4.0.x#v40423)
  * [v4.0.4.22](https://www.drissionpage.cn/versions/4.0.x#v40422)
  * [v4.0.4.21](https://www.drissionpage.cn/versions/4.0.x#v40421)
  * [v4.0.4.17](https://www.drissionpage.cn/versions/4.0.x#v40417)
  * [v4.0.4.16](https://www.drissionpage.cn/versions/4.0.x#v40416)
  * [v4.0.4.13](https://www.drissionpage.cn/versions/4.0.x#v40413)
  * [v4.0.4.12](https://www.drissionpage.cn/versions/4.0.x#v40412)
  * [v4.0.4.9](https://www.drissionpage.cn/versions/4.0.x#v4049)
  * [v4.0.4.8](https://www.drissionpage.cn/versions/4.0.x#v4048)
  * [v4.0.4.5](https://www.drissionpage.cn/versions/4.0.x#v4045)
  * [v4.0.4.3](https://www.drissionpage.cn/versions/4.0.x#v4043)
  * [v4.0.4.1](https://www.drissionpage.cn/versions/4.0.x#v4041)
  * [v4.0.3.4](https://www.drissionpage.cn/versions/4.0.x#v4034)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/versions/4.0.x)
  * [QQ群：391178600](https://www.drissionpage.cn/versions/4.0.x)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
