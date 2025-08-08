class ProductService:
    def __init__(self, mahsulotlar):
        self.mahsulotlar = mahsulotlar

    def print_products(self):
        if not self.mahsulotlar:
            print("Mahsulotlar ro'yxati bo'sh.")
        else:
            print("Mahsulotlar ro'yxati:")
            for i, mahsulot in enumerate(self.mahsulotlar, start=1):
                nom = mahsulot.get("nom", "Noma'lum")
                narx = mahsulot.get("narx", "Narx ko'rsatilmagan")
                print(f"{i}. Mahsulot nomi: {nom}, Narxi: {narx} so'm")
    def add_product(self, mahsulot):
        self.mahsulotlar.append(mahsulot)
        print(f"{mahsulot['nom']} mahsuloti qo'shildi.")
        self.print_products()
        return self.mahsulotlar
    def remove_product(self, mahsulot_nomi):
        for mahsulot in self.mahsulotlar:
            if mahsulot.get("nom") == mahsulot_nomi:
                self.mahsulotlar.remove(mahsulot)
                print(f"{mahsulot_nomi} mahsuloti o'chirildi.")
                self.print_products()
                return True
        print(f"{mahsulot_nomi} mahsuloti topilmadi.")
        return False            
