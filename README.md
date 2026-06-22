## lab9
## 1. Mục tiêu

Thực hành công cụ kiểm thử tự động **Selenium WebDriver** kết hợp framework **pytest**, xây dựng tối thiểu 3 test case kiểm thử tự động cho một website thực tế.

## 2. Website kiểm thử

**[https://www.saucedemo.com/](https://www.saucedemo.com/)** 

Tài khoản test có sẵn:
| Username | Password | Ghi chú |
|---|---|---|
| `standard_user` | `secret_sauce` | Tài khoản hoạt động bình thường |
| `locked_out_user` | `secret_sauce` | Tài khoản bị khóa |

## 3. Công nghệ sử dụng

- Python 3.10+
- Selenium WebDriver 4.21
- Pytest 8.2 (test runner)
- webdriver-manager (tự động tải đúng phiên bản ChromeDriver)
- Trình duyệt: Google Chrome (chạy ở chế độ headless)

## 4. Cấu trúc thư mục

```
selenium-project/
├── conftest.py              # Fixture khởi tạo/đóng trình duyệt (dùng chung cho mọi test)
├── requirements.txt         # Danh sách thư viện cần cài
├── README.md                # Báo cáo (file này)
└── tests/
    ├── test_01_login.py         # Test case 1: Đăng nhập
    ├── test_02_add_to_cart.py   # Test case 2: Thêm sản phẩm vào giỏ hàng
    └── test_03_logout.py        # Test case 3: Đăng xuất
```

## 5. Danh sách test case

### Test case 1 — Đăng nhập (`test_01_login.py`)
| ID | Mô tả | Kết quả mong đợi |
|---|---|---|
| TC1.1 | Đăng nhập với tài khoản hợp lệ `standard_user` | Chuyển sang trang `inventory.html`, tiêu đề "Products" |
| TC1.2 | Đăng nhập với mật khẩu sai | Hiển thị thông báo lỗi "Username and password do not match...", không vào được trang sản phẩm |
| TC1.3 | Đăng nhập với tài khoản bị khóa `locked_out_user` | Hiển thị thông báo lỗi "...locked out" |

### Test case 2 — Thêm sản phẩm vào giỏ hàng (`test_02_add_to_cart.py`)
| ID | Mô tả | Kết quả mong đợi |
|---|---|---|
| TC2.1 | Thêm 1 sản phẩm (Sauce Labs Backpack) vào giỏ | Biểu tượng giỏ hàng hiển thị số "1" |
| TC2.2 | Thêm 2 sản phẩm, vào trang giỏ hàng | Số lượng = 2, đúng tên 2 sản phẩm đã chọn |
| TC2.3 | Thêm 2 sản phẩm rồi xóa 1 sản phẩm | Giỏ hàng còn lại đúng 1 sản phẩm |

### Test case 3 — Đăng xuất (`test_03_logout.py`)
| ID | Mô tả | Kết quả mong đợi |
|---|---|---|
| TC3.1 | Đăng nhập rồi đăng xuất | Quay về trang đăng nhập (`/`), form login hiển thị lại |
| TC3.2 | Sau khi đăng xuất, truy cập thẳng URL `inventory.html` | Bị chặn, hiển thị thông báo lỗi yêu cầu đăng nhập |

**Tổng cộng: 8 test case con, bao phủ 3 chức năng chính (đăng nhập, giỏ hàng, đăng xuất).**

## 6. Hướng dẫn cài đặt & chạy

### Bước 1: Clone repo
```bash
git clone <link-repo-cua-ban>
cd selenium-project
```

### Bước 2: Tạo môi trường ảo & cài thư viện
```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Bước 3: Yêu cầu hệ thống
- Đã cài **Google Chrome** trên máy (webdriver-manager sẽ tự tải driver phù hợp).

### Bước 4: Chạy toàn bộ test
```bash
pytest -v
```

### Chạy riêng từng file test
```bash
pytest tests/test_01_login.py -v
pytest tests/test_02_add_to_cart.py -v
pytest tests/test_03_logout.py -v
```

### Xem trình duyệt chạy trực quan (không headless)
Mở file `conftest.py`, comment dòng:
```python
options.add_argument("--headless=new")
```

## 7. Kỹ thuật Selenium đã áp dụng

- Định vị phần tử bằng `By.ID`, `By.CLASS_NAME`, `By.CSS_SELECTOR`
- `implicitly_wait` để chờ phần tử tải xong
- Fixture `pytest` (`conftest.py`) để khởi tạo/đóng driver tự động cho từng test, tránh lặp code
- Tách hàm `login()`/`logout()` dùng chung giữa các test (tái sử dụng code)
- Chạy headless để có thể tích hợp CI/CD (GitHub Actions) sau này
- `webdriver-manager` giúp không cần tải ChromeDriver thủ công

## 8. Kết quả

Khi chạy trên máy có Chrome, toàn bộ 8 test case đều **PASS**.
>><img width="1053" height="270" alt="Ảnh màn hình 2026-06-22 lúc 08 02 52" src="https://github.com/user-attachments/assets/58e73914-14bd-41b4-8c4f-df982392647a" />


```
tests/test_01_login.py::test_login_success PASSED
tests/test_01_login.py::test_login_wrong_password PASSED
tests/test_01_login.py::test_login_locked_out_user PASSED
tests/test_02_add_to_cart.py::test_add_single_product_to_cart PASSED
tests/test_02_add_to_cart.py::test_add_multiple_products_and_verify_cart PASSED
tests/test_02_add_to_cart.py::test_remove_product_from_cart PASSED
tests/test_03_logout.py::test_logout_returns_to_login_page PASSED
tests/test_03_logout.py::test_cannot_access_inventory_after_logout PASSED

======================== 8 passed in XX.XXs ========================
```
