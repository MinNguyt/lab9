import time
from selenium.webdriver.common.by import By
from conftest import BASE_URL


def login(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


def logout(driver):
    # 1. Bấm mở Burger Menu góc trái màn hình
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    
    # 2. Chờ 1 giây để Menu trượt ra hoàn toàn
    time.sleep(1)
    
    # 3. Tìm phần tử Đăng xuất
    logout_link = driver.find_element(By.ID, "logout_sidebar_link")
    
    # 4. Sử dụng JavaScript để click trực tiếp nhằm tránh lỗi thẻ href="#" chạy sai cách
    driver.execute_script("arguments[0].click();", logout_link)
    
    # 5. Chờ 1 giây để trang kịp chuyển về trang chủ đăng nhập
    time.sleep(1)


def test_logout_returns_to_login_page(driver):
    """TC3.1: Đăng xuất thành công -> quay về trang đăng nhập (login form hiển thị)."""
    login(driver)
    assert "inventory.html" in driver.current_url

    logout(driver)

    assert driver.current_url == BASE_URL
    assert driver.find_element(By.ID, "login-button").is_displayed()


def test_cannot_access_inventory_after_logout(driver):
    """TC3.2: Sau khi đăng xuất, truy cập thẳng URL inventory.html -> bị chặn."""
    login(driver)
    logout(driver)

    driver.get(BASE_URL + "inventory.html")

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "you can only access" in error.text.lower() or "log in" in error.text.lower()