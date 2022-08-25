import time
import threading
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
app = Application(backend='uia').start("C:\Program Files (x86)\Elcomsoft Password Recovery\Advanced Archive Password Recovery\ARCHPR.exe /dontstart F:\JGB\重庆\主城区（重庆）_XXJ_2022_05月公路.zip")
# 描述Notepad.exe进程内的窗口

dlg_spec = app.UntitledNotepad
# 等到窗户真的开着
#actionable_dlg = dlg_spec.wait('visible') 
#方式二:
dlg = app.Dialog

#打印窗口所有控件
# dlg.print_control_identifiers()

# dlg.app['攻击类型'].print_control_identifiers()
type= dlg.child_window(title="攻击类型", auto_id="920", control_type="ComboBox")

type.打开.click()


# type.print_control_identifiers()
xz=type.child_window(title="攻击类型", control_type="List")
# xz.print_control_identifiers()
xz.child_window(title="担保 WinZip 恢复", control_type="ListItem").click_input()
dlg.child_window(title="开始!", auto_id="902", control_type="Pane").click_input()

# timer=threading.Timer(5,dlg.print_control_identifiers())  # 每秒运行
# timer.start()  # 执行方法
text=dlg.child_window(auto_id="1034", control_type="Pane")
count=0
while (count <= 0):
  if text.window_text()=='WinZip 恢复正在进行， 尝试找回口令(最长 9 个符号)':
    print(1)
    count=1
    dlg.child_window(title="停止", auto_id="903", control_type="Pane").click_input()
  else:
    print(0)
    
send_keys('{VK_TAB}')
send_keys('{ENTER}')
time.sleep(1)
send_keys('{ENTER}')
# dlg.print_control_identifiers()

# a1=dlg.child_window(title="加密密钥已成功恢复!", control_type="Window")
# a2=a1.child_window(title="确定", auto_id="1101", control_type="Pane")
# a3=a2.click_input()
# send_keys('{ENTER}')
# time.sleep(3)
# send_keys('{y}')
# time.sleep(3)
time.sleep(1)
send_keys('{ENTER}')

time.sleep(1)
send_keys('{ENTER}')

time.sleep(1)
dlg.close()
time.sleep(1)
send_keys('{VK_TAB}')
send_keys('{ENTER}')
# timer0=threading.Timer(2,send_keys('{ENTER}'))  # 每秒运行
# timer0.start()  # 执行方法



# timer=threading.Timer(5,dlg.close())  # 每秒运行
# timer.start()  # 执行方法
# dlg.child_window(title="ARCHPR 4.54 - 1%", control_type="Window").child_window(title="加密密钥已成功恢复!", control_type="Window"). child_window(title="确定", auto_id="1101", control_type="Pane").click_input()
# dlg.child_window(title="停止", auto_id="903", control_type="Pane").click_input()


# type.select('攻击类型2','R189')
#关闭窗口
# dlg.close()