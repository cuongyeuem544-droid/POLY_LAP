# Commit 1
# Commit 2
# Commit 3
# Commit 4
# Commit 5
# Commit 6
# Chương trình quản lý cửa hàng POLY_LAP

from product_manager import*

# Tải dữ liệu khi bắt đầu chương trình
products = load_data()

while True:
    print("\n==== MENU ====")
    print("1. Thêm sản phẩm")
    print("2. Sửa sản phẩm")
    print("3. Xoá sản phẩm")
    print("4. Tìm sản phẩm theo tên")
    print("5. Hiển thị tát cả sản phẩm")
    print("6. Thoát")
    
    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        add_product(products)
    elif choice == "2":
        update_product(products)
    elif choice == "3":
        delete_product(products)
    elif choice == "4":
        search_product_by_name(products)
    elif choice == "5":
        display_all_products(products)
    elif choice == "6":
        save_data(products)
        print(" Đã lưu dữ liệu. Thoát chương trình.")
        break
    else:
        print("Lựa chọn của bạn không hợp lệ!")    