# -*- coding: utf-8 -*-

# from PyQt5 import QtCore, QtGui, QtWidgets
# from Scripts.Utils import dict_result, get_config_path, resource_path, get_user_info
# import websocket
# import requests
# import json
# import threading
# import time


# class Login_Ui(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(520, 360)
#         Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
#         Dialog.setWindowIcon(QtGui.QIcon(resource_path("UI\\Image\\favicon.ico")))

#         # 根布局：垂直，包含标题、主体、底部提示
#         self.rootLayout = QtWidgets.QVBoxLayout(Dialog)
#         self.rootLayout.setContentsMargins(20, 16, 20, 12)
#         self.rootLayout.setSpacing(10)

#         # 标题
#         self.title_label = QtWidgets.QLabel(Dialog)
#         self.title_label.setText("登录雨课堂")
#         self.title_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.title_label.setStyleSheet("font: 16pt '微软雅黑'; color: #111;")
#         self.rootLayout.addWidget(self.title_label)

#         # 主体：左右分栏
#         self.bodyWidget = QtWidgets.QWidget(Dialog)
#         self.bodyLayout = QtWidgets.QHBoxLayout(self.bodyWidget)
#         self.bodyLayout.setContentsMargins(0, 0, 0, 0)
#         self.bodyLayout.setSpacing(24)

#         # 左侧：二维码 / 头像
#         self.leftWidget = QtWidgets.QWidget(self.bodyWidget)
#         self.leftLayout = QtWidgets.QVBoxLayout(self.leftWidget)
#         self.leftLayout.setContentsMargins(0, 0, 0, 0)
#         self.leftLayout.setSpacing(6)
#         self.leftLayout.setAlignment(QtCore.Qt.AlignCenter)

#         self.QRcode = QtWidgets.QLabel(self.leftWidget)
#         self.QRcode.setFixedSize(220, 220)
#         self.QRcode.setScaledContents(True)
#         self.QRcode.setAlignment(QtCore.Qt.AlignCenter)
#         self.QRcode.setStyleSheet(
#             "border: 1px solid #e0e0e0; border-radius: 8px; background: #fafafa;"
#         )
#         self.leftLayout.addWidget(self.QRcode, 0, QtCore.Qt.AlignCenter)

#         self.qr_hint = QtWidgets.QLabel("微信扫码登录", self.leftWidget)
#         self.qr_hint.setAlignment(QtCore.Qt.AlignCenter)
#         self.qr_hint.setStyleSheet("font: 9pt '微软雅黑'; color: #888;")
#         self.leftLayout.addWidget(self.qr_hint)

#         self.bodyLayout.addWidget(self.leftWidget)

#         # 右侧：用户信息面板
#         self.rightWidget = QtWidgets.QWidget(self.bodyWidget)
#         self.rightWidget.setMinimumWidth(200)
#         self.rightLayout = QtWidgets.QVBoxLayout(self.rightWidget)
#         self.rightLayout.setContentsMargins(0, 0, 0, 0)
#         self.rightLayout.setSpacing(10)
#         self.rightLayout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)

#         # 登录状态标签（未登录 / 已登录）
#         self.status_badge = QtWidgets.QLabel(self.rightWidget)
#         self.status_badge.setFixedHeight(26)
#         self.status_badge.setAlignment(QtCore.Qt.AlignCenter)
#         self._set_badge_waiting()
#         self.rightLayout.addWidget(self.status_badge, 0, QtCore.Qt.AlignHCenter)

#         # 姓名
#         self.name_label = QtWidgets.QLabel("—", self.rightWidget)
#         self.name_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.name_label.setStyleSheet("font: bold 14pt '微软雅黑'; color: #222;")
#         self.name_label.setWordWrap(True)
#         self.rightLayout.addWidget(self.name_label)

#         # 分割线
#         line = QtWidgets.QFrame(self.rightWidget)
#         line.setFrameShape(QtWidgets.QFrame.HLine)
#         line.setStyleSheet("color: #e8e8e8;")
#         self.rightLayout.addWidget(line)

#         # 信息网格（学校、学号）
#         self.infoGrid = QtWidgets.QWidget(self.rightWidget)
#         self.infoGridLayout = QtWidgets.QGridLayout(self.infoGrid)
#         self.infoGridLayout.setContentsMargins(4, 0, 4, 0)
#         self.infoGridLayout.setHorizontalSpacing(8)
#         self.infoGridLayout.setVerticalSpacing(6)

#         def make_key(text):
#             lbl = QtWidgets.QLabel(text)
#             lbl.setStyleSheet("font: 9pt '微软雅黑'; color: #999;")
#             return lbl

#         def make_val(text="—"):
#             lbl = QtWidgets.QLabel(text)
#             lbl.setStyleSheet("font: 9pt '微软雅黑'; color: #333;")
#             lbl.setWordWrap(True)
#             return lbl

#         self.school_key = make_key("学校")
#         self.school_val = make_val()
#         self.sno_key = make_key("学号")
#         self.sno_val = make_val()

#         self.infoGridLayout.addWidget(self.school_key, 0, 0)
#         self.infoGridLayout.addWidget(self.school_val, 0, 1)
#         self.infoGridLayout.addWidget(self.sno_key,    1, 0)
#         self.infoGridLayout.addWidget(self.sno_val,    1, 1)
#         self.infoGridLayout.setColumnStretch(1, 1)

#         self.rightLayout.addWidget(self.infoGrid)
#         self.rightLayout.addStretch()

#         # 关闭按钮（登录成功后显示）
#         self.close_btn = QtWidgets.QPushButton("完成", self.rightWidget)
#         self.close_btn.setFixedHeight(32)
#         self.close_btn.setVisible(False)
#         self.close_btn.setStyleSheet(
#             "QPushButton {"
#             "  background-color: #07c160; color: white;"
#             "  border: none; border-radius: 6px;"
#             "  font: 10pt '微软雅黑';"
#             "}"
#             "QPushButton:hover { background-color: #06ad56; }"
#         )
#         self.close_btn.clicked.connect(Dialog.accept)
#         self.rightLayout.addWidget(self.close_btn)

#         self.bodyLayout.addWidget(self.rightWidget)
#         self.bodyLayout.setStretch(0, 0)
#         self.bodyLayout.setStretch(1, 1)

#         self.rootLayout.addWidget(self.bodyWidget)

#         # 底部提示
#         self.hint_label = QtWidgets.QLabel(
#             "注：扫码登录仅用于获取您的登录状态以便软件监听雨课堂信息。", Dialog
#         )
#         self.hint_label.setWordWrap(True)
#         self.hint_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.hint_label.setStyleSheet("font: 8pt '微软雅黑'; color: #aaa;")
#         self.rootLayout.addWidget(self.hint_label)

#         # 错误提示（登录失败时用）
#         self.login_return = QtWidgets.QLabel("", Dialog)
#         self.login_return.setAlignment(QtCore.Qt.AlignCenter)
#         self.login_return.setStyleSheet("font: 8pt '微软雅黑'; color: rgb(255,0,0);")
#         self.rootLayout.addWidget(self.login_return)

#         self.rootLayout.setStretch(1, 1)

#         # 启动 WebSocket 登录流程
#         self.start_wssapp(Dialog)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)

#     # 状态徽标辅助方法

#     def _set_badge_waiting(self):
#         self.status_badge.setText("⏳ 等待扫码")
#         self.status_badge.setStyleSheet(
#             "font: 9pt '微软雅黑'; color: #888;"
#             "background: #f5f5f5; border-radius: 12px; padding: 0 12px;"
#         )

#     def _set_badge_scanning(self):
#         self.status_badge.setText("📱 已扫码，请确认")
#         self.status_badge.setStyleSheet(
#             "font: 9pt '微软雅黑'; color: #fa8c16;"
#             "background: #fff7e6; border-radius: 12px; padding: 0 12px;"
#         )

#     def _set_badge_success(self):
#         self.status_badge.setText("✅ 已登录")
#         self.status_badge.setStyleSheet(
#             "font: 9pt '微软雅黑'; color: #07c160;"
#             "background: #f0fff4; border-radius: 12px; padding: 0 12px;"
#         )

#     # 登录成功后更新右侧面板

#     def _update_user_panel(self, sessionid):
#         """登录成功后拉取用户信息并更新右侧面板，在子线程调用。"""
#         try:
#             code, data = get_user_info(sessionid)
#             if code != 0:
#                 return
#             name      = data.get("name", "—")
#             school    = data.get("school", "—")
#             sno       = data.get("schoolNumber", "—")
#             avatar_url = data.get("avatar", "")

#             # 拉取头像图片
#             avatar_pixmap = None
#             if avatar_url:
#                 try:
#                     img_bytes = requests.get(
#                         avatar_url, proxies={"http": None, "https": None}, timeout=5
#                     ).content
#                     avatar_pixmap = QtGui.QPixmap()
#                     avatar_pixmap.loadFromData(img_bytes)
#                 except Exception:
#                     pass

#             # 回到主线程更新 UI（通过信号）
#             self._user_info_ready.emit(name, school, sno, avatar_pixmap or QtGui.QPixmap())
#         except Exception:
#             pass

#     # WebSocket 登录流程

#     def _flush_login_QRcode(self):
#         count = 0
#         while self.flush_on:
#             if count == 60:
#                 count = 0
#                 data = {"op": "requestlogin", "role": "web", "version": 1.4,
#                         "type": "qrcode", "from": "web"}
#                 self.wsapp.send(json.dumps(data))
#             else:
#                 time.sleep(1)
#                 count += 1

#     def close_all(self):
#         self.flush_on = False
#         self.wsapp.close()
#         self.flush_t.join()

#     def load_config(self, config):
#         self.config = config

#     def save(self, sessionid):
#         config = self.config
#         config["sessionid"] = sessionid
#         config_path = get_config_path()
#         with open(config_path, "w+") as f:
#             json.dump(config, f)

#     def start_wssapp(self, Dialog):
#         # 自定义信号用于跨线程更新用户信息面板
#         # 需要借助一个临时 QObject 来发信号
#         class _Bridge(QtCore.QObject):
#             user_info_ready = QtCore.pyqtSignal(str, str, str, QtGui.QPixmap)

#         self._bridge = _Bridge()
#         self._user_info_ready = self._bridge.user_info_ready
#         self._user_info_ready.connect(self._on_user_info_ready, QtCore.Qt.QueuedConnection)

#         def on_open(wsapp):
#             data = {"op": "requestlogin", "role": "web", "version": 1.4,
#                     "type": "qrcode", "from": "web"}
#             wsapp.send(json.dumps(data))

#         def on_close(wsapp):
#             print("closed")

#         def on_message(wsapp, message):
#             data = dict_result(message)

#             if data["op"] == "requestlogin":
#                 # 更新二维码
#                 img = requests.get(
#                     url=data["ticket"], proxies={"http": None, "https": None}
#                 ).content
#                 img_pixmap = QtGui.QPixmap()
#                 img_pixmap.loadFromData(img)
#                 self.QRcode.setPixmap(img_pixmap)
#                 self.qr_hint.setText("微信扫码登录")
#                 self._set_badge_waiting()

#             elif data["op"] == "scanned":
#                 # 已扫码尚未确认
#                 self._set_badge_scanning()
#                 self.qr_hint.setText("请在手机上确认登录")

#             elif data["op"] == "loginsuccess":
#                 web_login_url = "https://www.yuketang.cn/pc/web_login"
#                 login_data = json.dumps({
#                     "UserID": data["UserID"],
#                     "Auth":   data["Auth"]
#                 })
#                 headers = {
#                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; "
#                                   "rv:104.0) Gecko/20100101 Firefox/104.0"
#                 }
#                 r = requests.post(
#                     url=web_login_url, data=login_data, headers=headers,
#                     proxies={"http": None, "https": None}
#                 )
#                 sessionid = dict(r.cookies)["sessionid"]
#                 self.config["sessionid"] = sessionid
#                 self.save(sessionid)

#                 # 拉取用户信息（子线程，避免阻塞 ws 线程）
#                 threading.Thread(
#                     target=self._update_user_panel, args=(sessionid,), daemon=True
#                 ).start()

#         login_wss_url = "wss://www.yuketang.cn/wsapp/"
#         self.wsapp = websocket.WebSocketApp(
#             url=login_wss_url,
#             on_open=on_open,
#             on_message=on_message,
#             on_close=on_close
#         )
#         self.wsapp_t = threading.Thread(target=self.wsapp.run_forever, daemon=True)
#         self.wsapp_t.start()
#         self.flush_on = True
#         self.flush_t = threading.Thread(target=self._flush_login_QRcode, daemon=True)
#         self.flush_t.start()

#         self._dialog = Dialog

#     def _on_user_info_ready(self, name, school, sno, avatar_pixmap):
#         """主线程槽：用户信息拉取完毕，更新右侧面板。"""
#         # 左侧切换为圆形头像
#         if not avatar_pixmap.isNull():
#             # 裁成圆形
#             size = 220
#             avatar_pixmap = avatar_pixmap.scaled(
#                 size, size,
#                 QtCore.Qt.KeepAspectRatioByExpanding,
#                 QtCore.Qt.SmoothTransformation
#             )
#             rounded = QtGui.QPixmap(size, size)
#             rounded.fill(QtCore.Qt.transparent)
#             painter = QtGui.QPainter(rounded)
#             painter.setRenderHint(QtGui.QPainter.Antialiasing)
#             path = QtGui.QPainterPath()
#             path.addEllipse(0, 0, size, size)
#             painter.setClipPath(path)
#             painter.drawPixmap(0, 0, avatar_pixmap)
#             painter.end()
#             self.QRcode.setPixmap(rounded)
#             self.QRcode.setStyleSheet(
#                 "border: 2px solid #07c160; border-radius: 110px; background: #fff;"
#             )

#         self.qr_hint.setText("登录成功")
#         self.qr_hint.setStyleSheet("font: 9pt '微软雅黑'; color: #07c160;")

#         # 右侧信息更新
#         self._set_badge_success()
#         self.name_label.setText(name)
#         self.school_val.setText(school)
#         self.sno_val.setText(sno)

#         # 显示完成按钮
#         self.close_btn.setVisible(True)

#         # 3 秒后自动关闭对话框
#         QtCore.QTimer.singleShot(3000, self._dialog.accept)