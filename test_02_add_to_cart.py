"""
test_02_add_to_cart.py
Test case 2: Kiểm thử chức năng Thêm sản phẩm vào giỏ hàng (Add to cart)

Kịch bản:
  TC2.1 - Thêm 1 sản phẩm vào giỏ -> biểu tượng giỏ hàng hiển thị số lượng 1
  TC2.2 - Thêm 2 sản phẩm vào giỏ -> số lượng giỏ hàng = 2, vào trang Cart
          kiểm tra đúng tên 2 sản phẩm đã thêm
  TC2.3 - Xóa 1 sản phẩm khỏi giỏ -> số lượng giảm về 1
"""

from selenium.webdriver.common.by import By
from conftest import BASE_URL


def login(driver):
    """Hàm hỗ trợ: đăng nhập trước khi thực hiện các thao tác khác."""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


def test_add_single_product_to_cart(driver):
    """TC2.1: Thêm 1 sản phẩm -> badge giỏ hàng hiển thị '1'."""
    login(driver)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"


def test_add_multiple_products_and_verify_cart(driver):
    """TC2.2: Thêm 2 sản phẩm, vào trang giỏ hàng, kiểm tra tên sản phẩm đúng."""
    login(driver)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "2"

    # Mở trang giỏ hàng
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "cart.html" in driver.current_url

    item_names = [el.text for el in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
    assert "Sauce Labs Backpack" in item_names
    assert "Sauce Labs Bike Light" in item_names


def test_remove_product_from_cart(driver):
    """TC2.3: Thêm 2 sản phẩm rồi xóa 1 -> giỏ hàng chỉ còn 1 sản phẩm."""
    login(driver)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    # Xóa sản phẩm Backpack ngay tại trang Products
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"
