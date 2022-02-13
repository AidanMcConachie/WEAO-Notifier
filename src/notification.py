from win10toast import ToastNotifier

n = ToastNotifier()


def toast(title, msg, duration=5):
    n.show_toast(title, msg, duration=duration, icon_path="assets/iconWEAO.ico", )