import streamlit as st
import base64
import os

# 1. Cấu hình trang web
st.set_page_config(
    page_title="Hồ sơ Minecraft của Tôi",
    page_icon="🧱",
    layout="centered"
)
st.markdown("""
    <style>
    /* Ẩn toàn bộ menu, header, footer mặc định */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    div[data-testid="stToolbar"] {visibility: hidden !important;}
    div[data-testid="stDecoration"] {display: none !important;}
    
    /* Quét sạch tất cả các phần tử lạ nằm ngoài khung chứa nội dung chính */
    #root ~ div, 
    body > div:not(#root), 
    [class*="viewerBadge"], 
    [data-testid="stManageAppButton"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
# Tên file ảnh nền của bạn
bg_image_path = "minecraft-deluxe-3840x2160-26243.jpg"


# Hàm chuyển đổi ảnh cục bộ (local) thành dữ liệu Base64 để vượt qua bảo mật trình duyệt
def get_base64_of_encoded_file(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Kiểm tra nếu file ảnh tồn tại thì tiến hành mã hóa thành nền web
if os.path.exists(bg_image_path):
    try:
        bin_str = get_base64_of_encoded_file(bg_image_path)

        # --- CẤU HÌNH GIAO DIỆN (CSS) VỚI ẢNH NỀN HỢP LỆ ---
        st.markdown(f"""
            <style>
            /* Áp dụng ảnh nền dạng base64 */
            .stApp {{
                background-image: url("data:image/jpg;base64,{bin_str}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}

            /* Font chữ mặc định của hệ thống */
            .stApp {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
            }}

            /* Làm đẹp các khối chữ và thêm bóng đổ */
            h2, p, span, div {{
                font-family: inherit !important;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
                color: white !important;
            }}

            /* Khung nền đen mờ ở giữa để làm nổi bật các nút bấm */
            .stMainBlockContainer {{
                background-color: rgba(0, 0, 0, 0.6);
                padding: 30px !important;
                border-radius: 15px;
                border: 2px solid rgba(255, 255, 255, 0.2);
                max-width: 450px !important;
                margin: 0 auto !important;
                margin-top: 120px !important; /* Thêm dòng này để đẩy khung dịch xuống dưới chữ MINECRAFT */
            }}

            /* Phong cách nút bấm */
            .stButton > button {{
                width: 100%;
                border-radius: 25px;
                background-color: #4a4a4a;
                color: white;
                height: 3.5em;
                font-size: 16px;
                font-weight: bold;
                border: 2px solid white;
                box-shadow: 0px 4px 6px rgba(0,0,0,0.3);
                transition: 0.2s;
            }}

            /* Hiệu ứng di chuột qua nút */
            .stButton > button:hover {{
                background-color: #5c5c5c;
                border-color: #fff;
                color: #ffffa0 !important;
                transform: translateY(-2px);
                box-shadow: 0px 6px 8px rgba(0,0,0,0.4);
            }}

            /* Hiệu ứng khi bấm nút */
            .stButton > button:active {{
                transform: translateY(1px);
            }}
        /* Phong cách nút bấm Bio mới với Logo thật */
            .bio-btn {{
                background-color: white;
                border-radius: 25px;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 12px 20px;
                margin-bottom: 15px;
                box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
                transition: all 0.3s ease;
                border: 1px solid rgba(0, 0, 0, 0.1);
                cursor: pointer;
            }}
            .bio-btn:hover {{
                transform: translateY(-3px);
                box-shadow: 0px 6px 12px rgba(0,0,0,0.3);
                background-color: #f8f9fa;
            }}
            .bio-btn-icon {{
                width: 24px;
                height: 24px;
                margin-right: 15px;
                object-fit: contain;
            }}
            .bio-btn-text {{
                font-size: 16px;
                font-weight: bold;
                color: #333333 !important;
                text-shadow: none !important;
            }}    
            </style>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Lỗi khi xử lý ảnh nền: {e}")
else:
    st.error(
        f"⚠️ Vẫn không tìm thấy ảnh! Bạn hãy chắc chắn đã kéo file ảnh tên '{bg_image_path}' vào đúng thư mục chứa file 'link bio.py' trong PyCharm nhé.")
    st.stop()

# 2. Xử lý và hiển thị Ảnh đại diện cùng Thông tin cá nhân
avatar_url = "avt.jpg"
if os.path.exists(avatar_url):
    try:
        # Tự động đọc định dạng ảnh (jpg, png)
        img_ext = os.path.splitext(avatar_url)[1].replace(".", "")
        if img_ext.lower() == "jpg": img_ext = "jpeg"

        # Mã hóa ảnh sang Base64 để trình duyệt không chặn
        avatar_bin = get_base64_of_encoded_file(avatar_url)
        st.markdown(f"""
            <div style="text-align: center; width: 100%;">
                <img src="data:image/{img_ext};base64,{avatar_bin}" style="width: 120px; height: 120px; border-radius: 50%; border: 3px solid white; object-fit: cover; margin: 0 auto; display: block;">
            </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Lỗi ảnh đại diện: {e}")
else:
    st.warning(f"Không tìm thấy file '{avatar_url}' trong thư mục!")
st.markdown("<h2 style='text-align: center;'>Thuê id giá rẻ ib zalo: 0817.961.437</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Bạn muốn chơi Minecraft nhưng chưa có ID? Đừng lo! Chúng tôi cung cấp dịch vụ cho thuê ID tải Minecraft, giúp bạn trải nghiệm game mà không cần mua tài khoản chính thức.🎮</p>", unsafe_allow_html=True)
st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

# 3. Các nút liên kết mạng xã hội (Đã căn giữa và sử dụng Logo chính thức cực đẹp)
# Bạn hãy thay "yourusername" thành tên tài khoản thật của bạn nhé
links = [

    {
        "title": "TikTok",
        "url": "https://www.tiktok.com/@chechaolinhtinh?_r=1&_t=ZS-986TTKQZB4L",
        "logo": "https://cdn-icons-png.flaticon.com/512/3046/3046121.png"
    },
    {
        "title": "Facebook",
        "url": "https://www.facebook.com/dongyeuem",
        "logo": "https://cdn-icons-png.flaticon.com/512/5968/5968764.png"
    },
    {
        "title": "Zalo",
        "url": "http://zalo.me/0817961437",
        "logo": "https://dichvumarketing.net/wp-content/uploads/2025/12/Tai-Logo-Zalo.webp"
    }
]

# Tạo danh sách các nút bằng HTML để căn giữa hoàn hảo và thêm hiệu ứng di chuột (hover)
buttons_html = ""
for link in links:
    buttons_html += f"""
    <a href="{link['url']}" target="_blank" style="text-decoration: none;">
        <div class="bio-btn">
            <img src="{link['logo']}" class="bio-btn-icon">
            <span class="bio-btn-text">{link['title']}</span>
        </div>
    </a>
    """

st.markdown(buttons_html, unsafe_allow_html=True)

# 4. Phần chân trang
st.markdown(
    "<br><p style='text-align: center; font-size: 12px; color: #999 !important;'>Tạo linkbio liên hệ: 0817.961.437 -- Van Dong </p>",
    unsafe_allow_html=True)