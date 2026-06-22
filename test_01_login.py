"""
test_01_login.py
Test case 1: Kiểm thử chức năng Đăng nhập (Login)

Kịch bản:
  TC1.1 - Đăng nhập thành công với tài khoản hợp lệ (standard_user)
  TC1.2 - Đăng nhập thất bại với mật khẩu sai -> hiển thị thông báo lỗi
  TC1.3 - Đăng nhập thất bại với tài khoản bị khóa (locked_out_user)
"""

from selenium.webdriver.common.by import By
from conftest import BASE_URL


def test_login_success(driver):
    """TC1.1: Đăng nhập đúng tài khoản/mật khẩu -> chuyển sang trang sản phẩm."""
    driver.get(BASE_URL)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Kiểm tra đã chuyển sang trang danh sách sản phẩm (inventory)
    assert "inventory.html" in driver.current_url
    title = driver.find_element(By.CLASS_NAME, "title")
    assert title.text == "Products"


def test_login_wrong_password(driver):
    """TC1.2: Sai mật khẩu -> hiển thị thông báo lỗi, không vào được trang sản phẩm."""
    driver.get(BASE_URL)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("sai_mat_khau")
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Username and password do not match" in error.text
    assert "inventory.html" not in driver.current_url


def test_login_locked_out_user(driver):
    """TC1.3: Tài khoản bị khóa -> hiển thị thông báo 'locked out'."""
    driver.get(BASE_URL)

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "locked out" in error.text.lower()
