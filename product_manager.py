# Quản lý các chức năng liên quan đến sản phẩm Laptop

import json

# =========
# 1. Đọc dữ liệu từ file
# =========
def load_data():
    try:
        with open("products.json" , "r" , encoding="utf-8") as file:
            products = json.load(file)
            return products
    except FileNotFoundError:
        # Nếu chưa có file thì sẽ trả về danh sách rỗng
        return []
    
# =========
# 2. Lưu dữ liệu vào file
# =========
def save_data(products):
    with open("products.json" , "w" , encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=4)

# =========
# 3. Thêm sản phẩm mới
# =========
def add_product(products):
    print("=== THÊM SẢN PHẨM ===")

    name = input("Nhập tên sản phẩm: ")
    brand = input("Nhập thương hiệu: ")
    price = int(input("Nhập giá: "))
    quantity = int(input("Nhấp số lượng: "))

    # Tạo ID tự động
    product_id = "LT" + str(len(products) + 1).zfill(2)

    product = {
        "id": product_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity,
    }

    products.append(product)
    print("Đã thêm sản phẩm thành công!")

# =========
# 4. Cập nhật thêm sản phẩm
# =========
def update_product(products):
    print("=== CẬP NHẬT SẢN PHẨM ===")
    pid = input("Nhập tên sản phẩm cần sửa: ")

    for p in products:
            if p["id"] == pid:
                p["name"] = input("Tên mới: ")
                p["brand"] = input("Thương hiệu mới: ")
                p["price"] = int(input("Giá mới: "))
                p["quantity"] = int(input("Số lượng mới: "))
                print("Cập nhật thành công!")
                return
            
            print("Không tìm thấy sản phẩm!")

# =========
# 5. Xoá sản phẩm
# =========
def delete_product(products):
    print("=== XOÁ SẢN PHẨM ===")
    pid = input("Nhập mã sản phẩm cần xoá: ")

    for p in products:
        if p["id"] == pid:
            products.remove(p)
            print("Đã xoá thành công sản phẩm!")
            return
        
        print("Không tìm thấy sản phẩm!")

# =========
# 6. Tìm sản phẩm theo tên
# =========
def search_product_by_name(products):
    keyword = input("Nhập từ khoá cần tìm: ").lower()

    found = False
    for p in products:
        if keyword in p["name"].lower():
            print(p)
            found = True

    if not found:
        print("Không có sản phẩm phù hợp!")

# =========
# 7. Hiển thị tát cả sản phẩm
# =========
def display_all_products(products):
    if len(products) == 0:
        print("Kho hàng trống.")
        return

    print("=== DANH SÁCH SảN PHẨM ===")
    for p in products:
        print(p)        