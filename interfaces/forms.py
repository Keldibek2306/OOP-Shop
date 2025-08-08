from rich.prompt import Prompt

class FormHandler:
    @staticmethod
    def get_product_info():
        name = Prompt.ask("Mahsulot nomi")
        price = Prompt.ask("Narxi", default="0")
        quantity = Prompt.ask("Miqdori", default="1")
        return {
            "name": name,
            "price": float(price),
            "quantity": int(quantity)
        }