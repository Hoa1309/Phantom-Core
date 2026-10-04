# ==============================================================================
# PROGRAM: ULTIMATE OMNI-EXPLOIT GOD_MODE OVERLOAD v80.0 (SPECIAL FOR HOA)
# AUTHOR: LINH (DEV ASSISTANT)
# TARGET: MULTI-PLATFORM (ANDROID / TERMUX / PYDROID3 / SINGLE TARGET INPUT)
# TOTAL MODULES: 20 ULTRA DETAILED SIMULATION & TROLL MODULES
# ==============================================================================

import time
import sys
import random
import os
import webbrowser

# ------------------------------------------------------------------------------
# 1. BẢNG MÃ MÀU TERMINAL ANSI 256 BẬC VIP & STYLES
# ------------------------------------------------------------------------------
XANH = "\033[92m"
VANG = "\033[93m"
DO = "\033[91m"
TIM = "\033[95m"
XANH_DUONG = "\033[96m"
XANH_LA = "\033[32m"
TRANG = "\033[97m"
XAM = "\033[90m"
CHOP_NHAY = "\033[5m"
DAM = "\033[1m"
NGHIENG = "\033[3m"
GACH_CHAN = "\033[4m"
RESET = "\033[0m"

# ------------------------------------------------------------------------------
# 2. HÀM BỔ TRỢ HỆ THỐNG CAO CẤP
# ------------------------------------------------------------------------------
def xoa_man_hinh():
    """Xóa sạch màn hình Terminal"""
    os.system('clear' if os.name != 'nt' else 'cls')

def in_chuyendung(text, delay=0.002, mau=XANH):
    """In từng ký tự mượt mà tạo hiệu ứng máy đánh chữ hacker"""
    sys.stdout.write(mau)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)

def thanh_tien_trinh(mo_ta, thoi_gian=0.8, mau=XANH):
    """Hiển thị thanh Load phần trăm từ 0% đến 100%"""
    buoc = 50
    for i in range(buoc + 1):
        phan_tram = int((i / buoc) * 100)
        thanh = "█" * i + "░" * (buoc - i)
        sys.stdout.write(f"\r{mau}[*] {mo_ta}: [{thanh}] {phan_tram}%{RESET}")
        sys.stdout.flush()
        time.sleep(thoi_gian / buoc)
    print()

def rung_may():
    """Kích hoạt vẩy rung thiết bị Android qua Termux API nếu có"""
    os.system('termux-vibrate -d 150 > /dev/null 2>&1')

def phat_tieng_bip():
    """Phát tiếng bíp cảnh báo của hệ thống"""
    sys.stdout.write("\a")
    sys.stdout.flush()

def generate_random_hex(length):
    """Tạo chuỗi Hex ngẫu nhiên phục vụ giả lập Dump RAM"""
    return ''.join(random.choice('0123456789ABCDEF') for _ in range(length))

def generate_mac_address():
    """Tạo địa chỉ MAC ngẫu nhiên chuẩn Ethernet/Wi-Fi"""
    return ":".join([f"{random.randint(0, 255):02X}" for _ in range(6)])

def nhap_mat_khau_an(prompt="► Mật khẩu VIP (3 chữ số): "):
    """Hàm nhập mật khẩu ẩn từng ký tự thành dấu *"""
    sys.stdout.write(prompt)
    sys.stdout.flush()
    password = ""
    
    try:
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            while True:
                char = sys.stdin.read(1)
                if char in ('\n', '\r'):
                    print()
                    break
                elif char in ('\x7f', '\x08'):
                    if len(password) > 0:
                        password = password[:-1]
                        sys.stdout.write('\b \b')
                        sys.stdout.flush()
                elif ord(char) == 3:
                    raise KeyboardInterrupt
                else:
                    password += char
                    sys.stdout.write('*')
                    sys.stdout.flush()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    except Exception:
        import getpass
        password = getpass.getpass("")
        
    return password

def mo_link_youtube():
    """Mở link Youtube theo yêu cầu của Hòa"""
    url = "https://youtu.be/dQw4w9WgXcQ?si=zsiaR0vo1Ij1yXOu"
    try:
        os.system(f'termux-open-url "{url}" > /dev/null 2>&1')
    except Exception:
        pass
    try:
        webbrowser.open(url)
    except Exception:
        pass

# ------------------------------------------------------------------------------
# 3. KÍCH HOẠT BANNER VÀ ĐĂNG NHẬP VIP (MODULE 0)
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(XANH_DUONG + DAM + """
██████╗ ██████╗ ███████╗████████╗██╗██████╗ ██╗   ██╗███████╗
██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██║██╔══██╗██║   ██║██╔════╝
██████╔╝██████╔╝█████╗     ██║   ██║██████╔╝██║   ██║███████╗
██╔═══╝ ██╔══██╗██╔══╝     ██║   ██║██╔══██╗██║   ██║╚════██║
██║     ██║  ██║███████╗   ██║   ██║██║  ██║╚██████╔╝███████║
╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
  [+] OMNI-EXPLOIT GOD_MODE OVERLOAD EDITION v80.0 [ARM64 VIP]
  [+] ULTRA EXPANDED PAYLOAD SYSTEM (20 FULL MODULES)
  [+] AUTOMATIC SINGLE INPUT EXPLOIT SYSTEM FOR HOA
================================================================
""" + RESET)

in_chuyendung("[*] Khởi động hệ thống kiểm tra Sandbox & Anti-Debugging...", 0.002, VANG)
in_chuyendung("[*] Bypassing Google Play Protect & Samsung Knox Security Core...", 0.002, VANG)
in_chuyendung("[*] Kích hoạt Kernel Injector v16.0 (ARM64_V8A)...", 0.002, VANG)
time.sleep(0.2)
in_chuyendung("[✓] Không phát hiện Virtual Machine. Quyền hạn Kernel: GRANTED", 0.002, XANH)
time.sleep(0.3)

print("\n" + VANG + "[!] YÊU CẦU XÁC THỰC QUYỀN HẠN ROOT/ADMINISTRATOR:" + RESET)
user_login = input(TIM + "  ► Tài khoản Admin DarkNet: " + RESET) or "Hoa_GodMode"

# Nhập mật khẩu ẩn dấu *
pass_login = nhap_mat_khau_an(TIM + "  ► Mật khẩu VIP (3 chữ số): " + RESET)

# Kiểm tra điều kiện mật khẩu 3 chữ số
if len(pass_login) != 3 or not pass_login.isdigit():
    print(DO + "\n[ERROR] SAI MẬT KHẨU! MẬT KHẨU PHẢI LÀ 3 CHỮ SỐ (VD: 123)." + RESET)
    sys.exit()

print("\n" + XANH + "[*] Đang kết nối mạng vệ tinh Starlink & mã hóa AES-256..." + RESET)
thanh_tien_trinh("Bypass Firewall & ISP Proxy", thoi_gian=0.8, mau=XANH)

print("\n" + XANH + f"[SUCCESS] XÁC THỰC THÀNH CÔNG! WELCOME {user_login.upper()} TO DARKNET CONSOLE" + RESET)
time.sleep(0.5)

# ------------------------------------------------------------------------------
# 4. THIẾT LẬP NẠN NHÂN (CHỈ NHẬP TÊN TỰ ĐỘNG KHAI THÁC)
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(TIM + DAM + """
================================================================
              THIẾT LẬP THÔNG TIN MỤC TIÊU CẦN TẤN CÔNG
================================================================
""" + RESET)

# CHỈ CẦN NHẬP TÊN NẠN NHÂN
target_name = input(VANG + "  ► Nhập Tên Nạn Nhân: " + RESET) or "Nguyen Van A"

# Tự động tạo dữ liệu ngẫu nhiên dựa trên tên
target_roblox = target_name.replace(" ", "_") + "_Roblox"
id_ff = str(random.randint(1000000000, 9999999999))
target_phone = "09" + "".join([str(random.randint(0, 9)) for _ in range(8)])
ip_pub = f"113.161.{random.randint(10, 99)}.{random.randint(100, 255)}"
ip_loc = f"192.168.1.{random.randint(2, 254)}"
mac_addr = generate_mac_address()
imei_device = f"86492005{random.randint(1000000, 9999999)}"

print("\n" + XANH + f"[*] Đã nhận diện Target: {target_name.upper()}" + RESET)
print(TIM + f"  ├── Tự tạo User Roblox: {target_roblox}" + RESET)
print(TIM + f"  ├── Tự tạo ID Free Fire: {id_ff}" + RESET)
print(TIM + f"  ├── Tự dò Số Điện Thoại: {target_phone}" + RESET)
print(TIM + f"  ├── Tự tạo IMEI Thiết Bị: {imei_device}" + RESET)
print(TIM + f"  └── Tự khóa IP Public: {ip_pub}" + RESET)

print("\n" + XANH + "[*] Nạp Payload v80.0 siêu cấp (20 Modules). Khởi chạy chuỗi Exploit toàn diện..." + RESET)
time.sleep(0.8)

# ------------------------------------------------------------------------------
# 5. MODULE 1: TRÍCH XUẤT PHẦN CỨNG & TỌA ĐỘ ĐỊA LÝ CHI TIẾT
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(DO + DAM + f"=== [MODULE 1] TRÍCH XUẤT TỌA ĐỘ VÀ PHẦN CỨNG NẠN NHÂN: {target_name.upper()} ===" + RESET)
in_chuyendung("[*] Đang phát gói tin Ping vệ tinh quét phần cứng nạn nhân...", 0.002)
time.sleep(0.2)

geo_hw_info = [
    ("Nạn nhân Target", f"{target_name.upper()} [ACTIVE]"),
    ("Quốc gia / Tỉnh thành", "Việt Nam 🇻🇳 | Lâm Đồng - Nam Đà / TP.HCM"),
    ("Mã Zip / Múi giờ", "670000 | Asia/Ho_Chi_Minh (UTC+7)"),
    ("Nhà mạng (ISP)", "Viettel Telecom / VNPT Broadband (AS7552)"),
    ("Tọa độ GPS chính xác", "11.8341° N, 107.8219° E (Sai số < 0.8 mét)"),
    ("IP Public / Local", f"{ip_pub} | Local: {ip_loc}"),
    ("Địa chỉ MAC / BSSID", f"{mac_addr} | BSSID: Wi-Fi_6E_VIP_5G"),
    ("Mã IMEI Thiết bị", f"{imei_device} [SLOT 1 & SLOT 2]"),
    ("Vi xử lý (CPU)", "Snapdragon 8 Gen 3 (8 Cores @ 3.3GHz) - Temp: 58.4°C"),
    ("Đồ họa (GPU)", "Adreno 750 @ 1000 MHz [Drivers Hacked]"),
    ("Bộ nhớ RAM", "12GB LPDDR5X (Đã chiếm dụng 94.2% bộ nhớ)"),
    ("Bộ nhớ trong (ROM)", "256GB UFS 4.0 (Còn trống: 12.4 GB)"),
    ("Tình trạng Pin", "3,850 mAh / 5,000 mAh (Pin Nóng: 42.5°C - 4.2V)"),
    ("Màn hình Display", "1080x2400 AMOLED 120Hz [Đã can thiệp Driver]"),
    ("Cảm biến kết nối", "Bluetooth 5.4, NFC, Gyroscope, Accelerometer [ACTIVE]"),
    ("Các Port bị bẻ khóa", "Port 22 (SSH), 80 (HTTP), 443 (HTTPS), 5555 (ADB) [OPEN]")
]

for item, detail in geo_hw_info:
    sys.stdout.write(f"  {VANG}► {item}: {RESET}{detail}")
    sys.stdout.flush()
    time.sleep(0.03)
    print(" [ĐÃ KHÓA]")

print("\n" + DO + f"[!] ĐÃ KHÓA CỨNG IP {ip_pub} & CHÍP XỬ LÝ MÁY {target_name.upper()}!" + RESET)
time.sleep(0.6)

# ------------------------------------------------------------------------------
# 6. MODULE 2: ROBLOX & BLOX FRUITS / PET SIM 99 EXPLOIT
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(XANH_DUONG + DAM + f"=== [MODULE 2] ROBLOX & BLOX FRUITS / PET SIM 99 (TARGET: {target_roblox}) ===" + RESET)
in_chuyendung(f"[*] Hack Cookie API Roblox cho Target: {target_roblox} qua IP {ip_pub}...", 0.002)
in_chuyendung("[*] Bypassing 2FA, Email OTP & Pin Security...", 0.002)
time.sleep(0.2)

roblox_info = [
    ("Tài khoản / Mật khẩu", f"{target_roblox} | Pass: {target_roblox}2026@vip_xXx"),
    ("Mã PIN Cấp 2", f"{random.randint(1000, 9999)} [Đã bẻ khóa]"),
    ("Số dư Robux", f"{random.randint(100000, 500000):,} Robux"),
    ("Blox Fruits Inventory", "Kitsune, Dragon Rework, Trái Ác Quỷ vĩnh viễn, Dark Blade, V4 Full Tier"),
    ("Pet Simulator 99", "Trộm 50x Huge Pets, 10x Titanic Pets, 5.0 Billion Gems"),
    ("King Legacy & Blade Ball", "Mở khóa toàn bộ Kiếm Cổ Đại, Cánh Rồng & Effect VIP"),
    ("Kho Đồ Trang Phục", "Chuyển hết Item Limitted & Accessories đắt tiền về Kho Admin")
]

for item, spec in roblox_info:
    sys.stdout.write(f"  {TIM}► {item}: {RESET}{spec}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [XONG]")

print("\n" + XANH + "[+] DÒ VÀ TRÍCH XUẤT MÃ COOKIE CHÌA KHÓA TÀI KHOẢN:" + RESET)
chars = "0123456789ABCDEF_|WARNING:-DO-NOT-SHARE-THIS.-_ROBLOSECURITY"
for _ in range(25):
    cookie_part = "".join(random.choice(chars) for _ in range(45))
    print(f"{XANH}._ROBLOSECURITY={cookie_part}...{RESET}")
    time.sleep(0.003)

rung_may()
phat_tieng_bip()
print(DO + f"\n[ALERT] ĐÃ ĐỔI PASS, ĐỔI EMAIL & RÚT HẾT ROBUX CỦA {target_name.upper()} THÀNH CÔNG!" + RESET)
time.sleep(0.6)

# ------------------------------------------------------------------------------
# 7. MODULE 3: FREE FIRE & GARENA DATABASE SERVER
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(DO + DAM + f"=== [MODULE 3] FREE FIRE & GARENA DATABASE (ID: {id_ff}) ===" + RESET)
in_chuyendung(f"[*] Xâm nhập ID Free Fire: {id_ff} thuộc sở hữu {target_name}...", 0.002)
in_chuyendung("[*] Bypassing Garena Anti-Hack Kernel v16.0...", 0.002)
time.sleep(0.2)

ff_features = [
    ("Bơm Kim Cương", "+999,999 Kim Cương vào hòm thư"),
    ("Bơm Huy Hiệu", "+10,000 Huy Hiệu Thẻ Vô Cực"),
    ("Trang Phục VIP", "Mở khóa Nhật Ấn Rồng, AK Rồng Xanh LV7, MP40 Mãng Xà LV7"),
    ("Chức Năng Hack", "Auto Headshot 100%, Đạn đuổi, Ghìm tâm ngực, Tàng hình, Đi xuyên tường"),
    ("Cấu hình ESP", "Hiện khoảng cách, Hiện Tên, Hiện Máu & Lượng đạn địch"),
    ("Lệnh Khóa Acc", f"Gửi 50,000 Báo cáo giả -> Ban vĩnh viễn ID {id_ff}")
]

for item, detail in ff_features:
    sys.stdout.write(f"  {TIM}► {item}: {RESET}{detail}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [KÍCH HOẠT]")

thanh_tien_trinh("Gửi Packet dữ liệu ảo qua IP Việt Nam " + ip_pub, thoi_gian=0.6, mau=DO)

rung_may()
phat_tieng_bip()
print(DO + f"[ALERT] ĐÃ NẠP FULL KC & KHÓA ID {id_ff} TRÊN SERVER GARENA!" + RESET)
time.sleep(0.6)

# ------------------------------------------------------------------------------
# 8. MODULE 4: DỮ LIỆU MẠNG XÃ HỘI & MEDIA STEALER
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(TIM + DAM + f"=== [MODULE 4] MẠNG XÃ HỘI & MEDIA STEALER CỦA {target_name.upper()} ===" + RESET)
in_chuyendung(f"[*] Đang quét SĐT: {target_phone} kết nối từ IP {ip_pub}...", 0.002)
time.sleep(0.2)

socials = [
    ("Zalo / Tin Nhắn", f"Lấy 1,420 tin nhắn ẩn, ảnh nhật ký của {target_name}"),
    ("TikTok / Reels", "Trộm Session Cookie, danh sách video nháp & tin nhắn riêng"),
    ("Facebook / Messenger", "Lấy Access Token, danh sách bạn bè & mật khẩu mã hóa"),
    ("Instagram / Threads", "Đã tải xuống toàn bộ Direct Messages & ảnh lưu trữ private"),
    ("Telegram / WhatsApp", "Trộm file Session, trích xuất tất cả nhóm Chat bí mật"),
    ("Camera IP & Webcam", "Đã bẻ khóa luồng Stream RTSP -> Quay lén 24/7"),
    ("Lịch sử Duyệt Web", "Đã lấy 5,800 link Chrome, Safari, Cốc Cốc private"),
    ("Thư viện Ảnh (/DCIM)", "Đã tải xuống 3,450 Ảnh & 210 Video HD sang Server Mẹ")
]

for app, status in socials:
    sys.stdout.write(f"  {VANG}► {app}: {RESET}{status}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [100%]")

print("\n" + XANH + "[+] DANH SÁCH FILE ẢNH & DỮ LIỆU VỪA RÒ RỈ:" + RESET)
file_list = [
    f"IMG_{target_name.replace(' ','_')}_001.jpg", "VID_20260912_REC.mp4", "Zalo_Backup_Private.zip", 
    "Pass_Bank_Note.txt", "Facebook_Cookies.json", "DCIM_Camera_Secret.tar.gz"
]
for file_name in file_list:
    print(f"  {TIM}---> Đang tải: {file_name} (100%) -> IP DarkNet Server{RESET}")
    time.sleep(0.03)

time.sleep(0.6)

# ------------------------------------------------------------------------------
# 9. MODULE 5: HACK TÀI KHOẢN NGÂN HÀNG & KÉT SẮT
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(VANG + DAM + f"=== [MODULE 5] BANKING & E-WALLET EXPLOIT (TARGET: {target_name.upper()}) ===" + RESET)
in_chuyendung(f"[*] Đang can thiệp SMS OTP & Smart OTP Ngân hàng MBBank/VCB...", 0.002)
time.sleep(0.2)

bank_info = [
    ("Tên chủ tài khoản", f"{target_name.upper()}"),
    ("Số tài khoản / Mã PIN", f"999018273645 | PIN: {random.randint(100000, 999999)}"),
    ("Số dư khả dụng", f"{random.randint(50000000, 900000000):,} VND"),
    ("Mã Smart OTP Key", f"OTP-{random.randint(100000, 999999)} [BYPASSED]"),
    ("Ví Momo / ZaloPay", f"Số dư ví: {random.randint(1000000, 20000000):,} VND [TỰ ĐỘNG CHUYỂN]"),
    ("Mã Két Sắt Điện Tử", f"Key-Door: #{random.randint(1000, 9999)} [UNLOCKED]")
]

for item, status in bank_info:
    sys.stdout.write(f"  {XANH_DUONG}► {item}: {RESET}{status}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [SUCCESS]")

thanh_tien_trinh(f"Rút sạch tiền của {target_name} về Tài Khoản Admin", thoi_gian=0.6, mau=VANG)
print(XANH + "[!] TRANSACTION COMPLETE: ĐÃ RÚT TOÀN BỘ SỐ DƯ TÀI KHOẢN!" + RESET)
time.sleep(0.6)

# ------------------------------------------------------------------------------
# 10. MODULE 6: BẺ KHÓA WI-FI NHÀ BÊN CẠNH & ROUTER AP
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(XANH_LA + DAM + f"=== [MODULE 6] WI-FI BSSID BRUTE-FORCE & ROUTER OVERLOAD ===" + RESET)
in_chuyendung(f"[*] Dò sóng Wi-Fi xung quanh tọa độ GPS của {target_name}...", 0.002)
time.sleep(0.2)

wifi_list = [
    ("Wi-Fi Nhà Nạn Nhân", f"Viettel_5G_VIP_{random.randint(100,999)}", "WPA3-Personal", "Pass: 88888888 [DECRYPTED]"),
    ("Wi-Fi Hàng Xóm 1", f"VNPT_Family_Guest", "WPA2-PSK", "Pass: khongcoi123 [DECRYPTED]"),
    ("Wi-Fi Hàng Xóm 2", f"FPT_Telecom_HighSpeed", "WPA2-PSK", "Pass: 123456789 [DECRYPTED]"),
    ("Wi-Fi Quán Cà Phê", f"Coffee_Free_WiFi", "Open / No Pass", "Access: Granted [HIJACKED]")
]

for tag, ssid, sec, res in wifi_list:
    sys.stdout.write(f"  {VANG}► [{tag}] {ssid} ({sec}): {RESET}{res}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [CONNECTED]")

thanh_tien_trinh("Bẻ khóa Router Gateway 192.168.1.1", thoi_gian=0.6, mau=XANH_LA)
print(XANH + "[!] ROUTER HIJACKED: ĐÃ CHIẾM QUYỀN ĐIỀU KHIỂN TOÀN BỘ MẠNG INTRA-NET!" + RESET)
time.sleep(0.6)

# ------------------------------------------------------------------------------
# 11. MODULE 7: TẤN CÔNG SMART TV, TỦ LẠNH & THIẾT BỊ IOT
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(XANH_DUONG + DAM + f"=== [MODULE 7] SMART HOME & IOT DEVICE HIJACK (TARGET: {target_name}) ===" + RESET)
in_chuyendung("[*] Quét các thiết bị IoT kết nối chung mạng Wi-Fi...", 0.002)
time.sleep(0.2)

iot_list = [
    ("Smart TV Samsung 65 inch", "Ép bật kênh Youtube Rickroll & tăng max 100% Âm lượng"),
    ("Điều hòa Panasonic Inverter", "Ép hạ nhiệt độ xuống 16°C & bật chế độ Băng Giá"),
    ("Tủ Lạnh Thông Minh LG", "Cảnh báo mở cửa tủ & Tắt quạt làm lạnh từ xa"),
    ("Robot Hút Bụi Xiaomi", "Khởi động chạy vòng quanh nhà & phát âm thanh báo động"),
    ("Bóng Đèn Thông Minh Tuya", "Bật tắt liên tục tạo hiệu ứng Đèn Chớp Nhảy (Strobe Light)")
]

for device, action in iot_list:
    sys.stdout.write(f"  {TIM}► {device}: {RESET}{action}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [OVERRIDDEN]")

thanh_tien_trinh("Gửi lệnh Firmware Overload đến các thiết bị IoT", thoi_gian=0.6, mau=XANH_DUONG)
print(DO + "[!] SMART HOME CONTROL: ĐÃ CHIẾM TOÀN BỘ NGÔI NHÀ NẠN NHÂN!" + RESET)
time.sleep(0.6)

# ------------------------------------------------------------------------------
# 12. MODULE 8: KHAI THÁC BLUETOOTH & LOA KÉO HÀNG XÓM
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(TIM + DAM + f"=== [MODULE 8] BLUETOOTH PAIRING & AUDIO SPOOFING ===" + RESET)
in_chuyendung("[*] Quét dải tần Bluetooth 2.4GHz gần thiết bị...", 0.002)
time.sleep(0.2)

bt_devices = [
    ("Loa Kéo Bluetooth 500W", "Mã PIN 0000 -> Đã kết nối -> Bật nhạc max volume"),
    ("Tai Nghe Airpods Pro", "Hijack luồng âm thanh -> Phát tiếng gầm rú ma quái"),
    ("Đồng Hồ Thông Minh Watch 6", "Ép gửi 999 thông báo rác -> Đầy bộ nhớ Watch"),
    ("Bàn Phím / Chuột Wireless", "Ghi đè phím ảo -> Tự động gõ dòng chữ 'BẠN ĐÃ BỊ HACK'")
]

for bt, effect in bt_devices:
    sys.stdout.write(f"  {VANG}► {bt}: {RESET}{effect}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [PAIRED]")

time.sleep(0.6)

# ------------------------------------------------------------------------------
# 13. MODULE 9: THEO DÕI HÀNH TRÌNH GPS & GOOGLE MAPS
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(VANG + DAM + f"=== [MODULE 9] REAL-TIME GPS TRACKING & MOVEMENT HISTORY ===" + RESET)
in_chuyendung(f"[*] Định vị vệ tinh GPS gian hàng & vị trí hiện tại của {target_name}...", 0.002)
time.sleep(0.2)

gps_points = [
    ("07:30 AM", "Có mặt tại Nhà Riêng (Tọa độ: 11.8341° N, 107.8219° E)"),
    ("08:15 AM", "Di chuyển qua Đường Nguyễn Huệ bằng Xe Máy"),
    ("09:00 AM", "Dừng chân tại Quán Cà Phê Cây Điệp (Wifi: Coffee_Free_WiFi)"),
    ("11:45 AM", "Ghé Trường Học / Cơ quan làm việc"),
    ("14:30 PM", f"Vị trí Hiện tại: Đang cầm điện thoại lướt web [IP {ip_pub}]")
]

for t, loc in gps_points:
    sys.stdout.write(f"  {XANH}► [{t}]: {RESET}{loc}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [TRACKED]")

print("\n" + DO + "[!] MAPS SPOOFING: ĐÃ VẼ XONG BẢN ĐỒ HÀNH TRÌNH BÍ MẬT!" + RESET)
time.sleep(0.6)

# ------------------------------------------------------------------------------
# 14. MODULE 10: TRÍCH XUẤT MESSENGER & CHAT BÍ MẬT
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(DO + DAM + f"=== [MODULE 10] MESSENGER / ZALO SECRET CHAT DECRYPTOR ===" + RESET)
in_chuyendung(f"[*] Giải mã cơ sở dữ liệu SQLite Chat của {target_name}...", 0.002)
time.sleep(0.2)

chats = [
    ("Tin Nhắn Ẩn Zalo", "Mã PIN 1234 -> Đoạn chat bí mật với 'Người Yêu Cũ'"),
    ("Messenger Inbox", "Lấy 50 đoạn hội thoại gần nhất + 120 tệp đính kèm audio"),
    ("Lịch Sử Cuộc Gọi", "15 cuộc gọi nhỡ, 42 cuộc gọi đi (Tổng thời lượng: 120 phút)"),
    ("Danh Bạ Điện Thoại", f"Trộm toàn bộ {random.randint(200, 800)} số điện thoại trong máy")
]

for c_type, c_detail in chats:
    sys.stdout.write(f"  {TIM}► {c_type}: {RESET}{c_detail}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [DUMPED]")

time.sleep(0.6)

# ------------------------------------------------------------------------------
# 15. MODULE 11: CAN THIỆP TẦN SỐ ĐÀI FM & SÓNG DI ĐỘNG 4G/5G
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(XANH_LA + DAM + f"=== [MODULE 11] CELLULAR TOWER & FREQUENCY SPOOFING ===" + RESET)
in_chuyendung("[*] Khóa sóng trạm BTS Viettel / Vinaphone khu vực...", 0.002)
time.sleep(0.2)

towers = [
    ("Trạm BTS #1029", "Ép hạ sóng di động từ 5G xuống 2G Edge"),
    ("Mã USSD Request", "Chuyển tiếp cuộc gọi (*21*) sang số Admin DarkNet"),
    ("Tin nhắn SMS rác", "Gửi 500 tin nhắn OTP ảo làm nghẽn tổng đài điện thoại"),
    ("Sóng FM Radio", "Ghi đè tần số 99.9MHz bằng đoạn băng ghi âm trêu đùa")
]

for tw, act in towers:
    sys.stdout.write(f"  {VANG}► {tw}: {RESET}{act}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [SPOOFED]")

time.sleep(0.6)

# ------------------------------------------------------------------------------
# 16. MODULE 12: HACK CLOUD DRIVE, GOOGLE PHOTOS & ICLOUD
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(TIM + DAM + f"=== [MODULE 12] CLOUD STORAGE & BACKUP EXPLOITER ===" + RESET)
in_chuyendung(f"[*] Xâm nhập Google Drive & Google Photos của {target_name}...", 0.002)
time.sleep(0.2)

clouds = [
    ("Google Drive", "Tải xuống 12 file PDF, Docs, Excel quan trọng"),
    ("Google Photos", "Sao chép toàn bộ 5,000 ảnh tự động sao lưu Cloud"),
    ("iCloud / OneDrive", "Trộm file Token đăng nhập không cần mật khẩu"),
    ("GMail / Yahoo Mail", "Đọc trộm 300 Email công việc & Hóa đơn thanh toán")
]

for cl, st in clouds:
    sys.stdout.write(f"  {XANH_DUONG}► {cl}: {RESET}{st}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [SYNCED]")

time.sleep(0.6)

# ------------------------------------------------------------------------------
# 17. MODULE 13: XÂM NHẬP SÀN THƯƠNG MẠI ĐIỆN TỬ (SHOPEE/LAZADA)
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(VANG + DAM + f"=== [MODULE 13] E-COMMERCE ACCOUNT EXPLOIT (SHOPEE/TIKTOK SHOP) ===" + RESET)
in_chuyendung(f"[*] Quét tài khoản Shopee / Lazada gắn liền SĐT {target_phone}...", 0.002)
time.sleep(0.2)

ecom = [
    ("Voucher Khuyến Mãi", "Trộm toàn bộ Voucher Giảm 500k, Mã FreeShip VIP"),
    ("Ví ShopeePay", f"Số dư ví: {random.randint(100000, 2000000):,} VND [Đã chuyển]"),
    ("Đơn Hàng Đang Giao", "Đổi địa chỉ nhận hàng về Trụ sở Admin DarkNet"),
    ("Lịch Sử Mua Sắm", "Đã lưu 150 đơn hàng cũ vào tệp hồ sơ cá nhân")
]

for ec, ed in ecom:
    sys.stdout.write(f"  {DO}► {ec}: {RESET}{ed}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [DRAINED]")

time.sleep(0.6)

# ------------------------------------------------------------------------------
# 18. MODULE 14: GIẢ LẬP DEEPFAKE AI VOICE & VIDEO SPOOFER (MỚI BỔ SUNG)
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(TIM + DAM + f"=== [MODULE 14] DEEPFAKE AI VOICE & FACE REPLICATION (TARGET: {target_name.upper()}) ===" + RESET)
in_chuyendung(f"[*] Đang thu thập mẫu giọng nói từ các đoạn Video/Audio của {target_name}...", 0.002)
time.sleep(0.2)

deepfake_items = [
    ("Mẫu Giọng Nói AI", f"Đã clone thành công 100% tần số giọng {target_name}"),
    ("Khuôn Mặt 3D Deepfake", "Đã dựng xong mô hình 3D từ 150 bức ảnh thu thập"),
    ("Cuộc Gọi Giả Mạo", f"Ép gửi 10 cuộc gọi video giả {target_name} cho bạn bè"),
    ("Xác Thực Sinh Trắc Học", "Bypass FaceID & Cảm biến vân tay bằng mô hình AI")
]

for df_item, df_status in deepfake_items:
    sys.stdout.write(f"  {XANH_DUONG}► {df_item}: {RESET}{df_status}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [CLONED]")

time.sleep(0.6)

# ------------------------------------------------------------------------------
# 19. MODULE 15: CRYPTO & NFT WALLET DRAINER (MỚI BỔ SUNG)
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(VANG + DAM + f"=== [MODULE 15] CRYPTO WALLET & METAMASK DRAINER ===" + RESET)
in_chuyendung(f"[*] Quét 12 từ khóa Seed Phrase trong bộ nhớ Clipboard của {target_name}...", 0.002)
time.sleep(0.2)

crypto_items = [
    ("Ví MetaMask / Trust Wallet", "Đã tìm thấy Seed Phrase: [12 WORDS RECOVERED]"),
    ("Số dư Bitcoin (BTC)", f"{random.uniform(0.5, 3.8):.4f} BTC [Tự động rút về ví Admin]"),
    ("Số dư Ethereum (ETH)", f"{random.uniform(5.0, 25.0):.2f} ETH [Rút sạch gas fee]"),
    ("Bộ Bộ Tắm NFT VIP", "Trộm 3x Bored Ape Yacht Club NFT sang ví Sol")
]

for cr_item, cr_status in crypto_items:
    sys.stdout.write(f"  {XANH}► {cr_item}: {RESET}{cr_status}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [DRAINED]")

time.sleep(0.6)

# ------------------------------------------------------------------------------
# 20. MODULE 16: GPS SATELLITE OVERRIDE & DRONE TRACKING (MỚI BỔ SUNG)
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(XANH_DUONG + DAM + f"=== [MODULE 16] GPS SATELLITE OVERRIDE & DRONE SPY ===" + RESET)
in_chuyendung(f"[*] Điều hướng vệ tinh GPS Starlink quét góc rộng tại Lâm Đồng...", 0.002)
time.sleep(0.2)

drone_items = [
    ("Kết Nối Vệ Tinh NORAD", "SPOOFED -> Đã ghi đè tín hiệu vị trí sai lệch 10km"),
    ("Drone Quét Trên Không", "Đã phát hiện 1 Drone thương mại gần vị trí nạn nhân"),
    ("Khóa Camera Vệ Tinh", "Xem trực tiếp ảnh chụp hồng ngoại góc nhìn từ không trung"),
    ("Lệnh Báo Báo Ảo", "Gửi tọa độ giả tới hệ thống radar vùng")
]

for dr_item, dr_status in drone_items:
    sys.stdout.write(f"  {TIM}► {dr_item}: {RESET}{dr_status}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [OVERRIDDEN]")

time.sleep(0.6)

# ------------------------------------------------------------------------------
# 21. MODULE 17: SMART WATCH & WEARABLE HIJACK (MỚI BỔ SUNG)
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(DO + DAM + f"=== [MODULE 17] WEARABLE BIOMETRICS & SMART WATCH HIJACK ===" + RESET)
in_chuyendung(f"[*] Đồng bộ dữ liệu nhịp tim & sức khỏe của {target_name}...", 0.002)
time.sleep(0.2)

wear_items = [
    ("Đồng Hồ Apple/Galaxy Watch", "Đã kết nối Bluetooth LE -> Ghi đè dữ liệu sức khỏe"),
    ("Nhịp Tim Hiện Tại", f"{random.randint(70, 140)} BPM (Cảnh báo nhịp tim đập nhanh)"),
    ("Dữ Liệu Giấc Ngủ", "Đã xuất 30 ngày theo dõi giấc ngủ riêng tư"),
    ("Kích Hoạt Rung Liên Tục", "Gửi lệnh Rung điên cuồng làm rung tay nạn nhân")
]

for wr_item, wr_status in wear_items:
    sys.stdout.write(f"  {VANG}► {wr_item}: {RESET}{wr_status}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [HIJACKED]")

time.sleep(0.6)

# ------------------------------------------------------------------------------
# 22. MODULE 18: CAR INFOTAINMENT & SMART VEHICLE CONTROL (MỚI BỔ SUNG)
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(XANH_LA + DAM + f"=== [MODULE 18] SMART CAR & VEHICLE CAN-BUS CONTROL ===" + RESET)
in_chuyendung(f"[*] Dò sóng chìa khóa Smartkey & hệ thống Bluetooth Xe Máy/Ô tô...", 0.002)
time.sleep(0.2)

car_items = [
    ("Hệ Thống Mạng CAN-Bus", "Bypass khóa điện tử xe máy / ô tô gần vị trí"),
    ("Còi Cảnh Báo", "Tự động phát tiếng còi xe liên tục 5 lần"),
    ("Đèn Pha / Đèn Xi-nhan", "Bật chớp nháy đè sáng hệ thống đèn xe"),
    ("Mở Cốp Tự Động", "Gửi tín hiệu giả lập chìa khóa Smartkey -> Unlocked")
]

for cr_item, cr_status in car_items:
    sys.stdout.write(f"  {DO}► {cr_item}: {RESET}{cr_status}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [CONTROLLED]")

time.sleep(0.6)

# ------------------------------------------------------------------------------
# 23. MODULE 19: DUMP TOÀN BỘ LOG SYSTEM (MODULE PHỤ MỚI)
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(TIM + DAM + f"=== [MODULE 19] FULL SYSTEM LOG & MEMORY DUMPING ===" + RESET)
in_chuyendung(f"[*] Xuất dữ liệu hệ thống Android/iOS của {target_name}...", 0.002)
time.sleep(0.2)

log_items = [
    ("Dung Lượng Dump", "15.4 GB System Data -> Mã hóa AES-256"),
    ("Tệp File Hồ Sơ", f"Target_{target_name.replace(' ','_')}_FULL_EXPLOIT.bin"),
    ("Tốc Độ Truyền", "1 Gbps qua đường truyền vệ tinh Starlink"),
    ("Trạng Thái Lưu", "Lưu trữ vĩnh viễn trên Server DarkNet Admin")
]

for lg_item, lg_status in log_items:
    sys.stdout.write(f"  {XANH_DUONG}► {lg_item}: {RESET}{lg_status}")
    sys.stdout.flush()
    time.sleep(0.04)
    print(" [SAVED]")

time.sleep(0.6)

# ------------------------------------------------------------------------------
# 24. MODULE 20: GIẢ LẬP DDOS & TRÍCH XUẤT MATRIX DUMP SỐ LƯỢNG LỚN (FINAL)
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(DO + DAM + "=== [MODULE 20] DDOS ATTACK & CRITICAL SYSTEM OVERWRITE ===" + RESET)
in_chuyendung(f"[*] Gửi 5,000,000 UDP Packets tới CPU Snapdragon qua IP {ip_pub}...", 0.002, DO)
in_chuyendung("[*] Bypassing Google Play Protect & Samsung Knox Protection...", 0.002, DO)
time.sleep(0.2)

print("\n" + VANG + "[+] ÉP TẮT QUẠT TẢN NHIỆT & TĂNG NHIỆT ĐỘ CHIP CPU:" + RESET)
for temp in range(50, 115, 5):
    vol = 3.5 + (temp / 35)
    print(f"  {DO}► CPU Temp Warning: {temp}°C | Core Voltage: {vol:.2f}V [OVERHEAT DANGER]{RESET}")
    time.sleep(0.03)

print("\n" + XANH + "[+] CHẠY CHUỖI MÃ MATRIX TRÍCH XUẤT BỘ NHỚ RAM TRỰC TIẾP:" + RESET)
chars = "0123456789ABCDEFCRITICALSYSTEMOVERFLOWERROR_EXPLOIT_PAYLOAD_V80_ULTIMATE"
for _ in range(120):
    line = "".join(random.choice(chars) for _ in range(56))
    hex_addr = f"0x{random.randint(4096, 65535):04X}"
    print(f"{XANH}{hex_addr} | {line}{RESET}")
    time.sleep(0.002)

print("\n" + DO + DAM + "!" * 66 + RESET)
in_chuyendung("[CẢNH BÁO NGHIÊM TRỌNG] HỆ THỐNG MẤT KIỂM SOÁT - KERNEL PANIC!", 0.003, DO)
in_chuyendung(f"[KÍCH HOẠT] ĐANG MÃ HÓA VÀ HỦY CHIP NHỚ TẠI VIỆT NAM (IP {ip_pub})...", 0.003, DO)
print(DO + DAM + "!" * 66 + RESET + "\n")

thanh_tien_trinh("Mã hóa ổ đĩa & Thiêu hủy Chipset", thoi_gian=1.0, mau=DO)

# ------------------------------------------------------------------------------
# 25. ĐẾM NGƯỢC CHUẨN 3.. 2.. 1.. VÀ MỞ LINK YOUTUBE
# ------------------------------------------------------------------------------
in_chuyendung("\n[DANGER] HỆ THỐNG SẼ MỞ TRÌNH DUYỆT TRONG:", 0.005, DO)
for sec in [3, 2, 1]:
    rung_may()
    phat_tieng_bip()
    print(f"{DO}{DAM}{CHOP_NHAY}    >>> {sec} <<< {RESET}")
    time.sleep(1)

# Tự động bật link Youtube Rickroll
mo_link_youtube()

# ------------------------------------------------------------------------------
# 26. KẾT THÚC CÚ LỪA TROLL SIÊU KHỦNG (20 MODULES)
# ------------------------------------------------------------------------------
xoa_man_hinh()
print(XANH_DUONG + DAM + f"""
  __________________________________________________________________________
 |                                                                          |
 |   AHIHI ĐÃ HACK THÀNH CÔNG NẠN NHÂN: {target_name.upper()}!                
 |   Đã đếm đúng 3.. 2.. 1.. và mở link YouTube cho Hòa rồi nha!            |
 |   Link YouTube: https://youtu.be/dQw4w9WgXcQ                             |
 |   Máy Hòa vẫn an toàn 100%, đây chỉ là code giả lập troll vui thôi nhé! |
 |__________________________________________________________________________|
""" + RESET)

print(VANG + "Bấm Enter để thoát chương trình..." + RESET)
input()

# ==============================================================================
# END OF CODE - ULTIMATE OMNI-EXPLOIT GOD_MODE OVERLOAD v80.0 (20 FULL MODULES)
# ==============================================================================
