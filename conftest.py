import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# BỔ SUNG DÒNG NÀY ĐỂ CÁC FILE TEST KHÔNG BỊ LỖI IMPORT
BASE_URL = "https://www.saucedemo.com/"

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless=new") # Tháo comment nếu muốn chạy ẩn danh
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    drv = webdriver.Chrome(options=options)
    
    yield drv
    drv.quit()