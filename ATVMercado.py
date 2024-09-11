class Item:
    def __init__(self, codigo, descricao, valor):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor
        self.acrescimo = 0
        self.desconto = 0

    def aplicar_acrescimo(self, acrescimo):
        self.acrescimo += acrescimo
        self.valor += acrescimo

    def aplicar_desconto(self, desconto):
        self.desconto += desconto
        self.valor -= desconto


class Carrinho:
    def __init__(self):
        self.itens = []

    def inserir_item(self, codigo, descricao, valor):
        self.itens.append(Item(codigo, descricao, valor))

    def aplicar_acrescimo_item(self, codigo, acrescimo):
        item = self._encontrar_item(codigo)
        if item:
            item.aplicar_acrescimo(acrescimo)

    def aplicar_desconto_item(self, codigo, desconto):
        item = self._encontrar_item(codigo)
        if item:
            item.aplicar_desconto(desconto)

    def aplicar_acrescimo_total(self, acrescimo_total):
        if not self.itens:
            return
        acrescimo_por_item = acrescimo_total / len(self.itens)
        for item in self.itens:
            item.aplicar_acrescimo(acrescimo_por_item)

    def aplicar_desconto_total(self, desconto_total):
        if not self.itens:
            return
        desconto_por_item = desconto_total / len(self.itens)
        for item in self.itens:
            item.aplicar_desconto(desconto_por_item)

    def finalizar_venda(self):
        total_acrescimo = sum(item.acrescimo for item in self.itens)
        total_desconto = sum(item.desconto for item in self.itens)
        total_final = sum(item.valor for item in self.itens)

        print("Itens no carrinho:")
        for item in self.itens:
            print(
                f"Código: {item.codigo}, Descrição: {item.descricao}, Valor: {item.valor}, Acréscimo: {item.acrescimo}, Desconto: {item.desconto}")

        print(f"Total de acréscimo: {total_acrescimo}")
        print(f"Total de desconto: {total_desconto}")
        print(f"Valor final: {total_final}")

    def _encontrar_item(self, codigo):
        for item in self.itens:
            if item.codigo == codigo:
                return item
        print(f"Item com código {codigo} não encontrado.")
        return None


def menu():
    carrinho = Carrinho()

    while True:
        print("\nMenu:")
        print("1. Inserir item ao carrinho")
        print("2. Acréscimo de item")
        print("3. Desconto de item")
        print("4. Acréscimo total")
        print("5. Desconto total")
        print("6. Finalizar venda")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            codigo = input("Digite o código do produto: ")
            descricao = input("Digite a descrição do produto: ")
            valor = float(input("Digite o valor do produto: "))
            carrinho.inserir_item(codigo, descricao, valor)
        elif opcao == '2':
            codigo = input("Digite o código do produto: ")
            acrescimo = float(input("Digite o valor do acréscimo: "))
            carrinho.aplicar_acrescimo_item(codigo, acrescimo)
        elif opcao == '3':
            codigo = input("Digite o código do produto: ")
            desconto = float(input("Digite o valor do desconto: "))
            carrinho.aplicar_desconto_item(codigo, desconto)
        elif opcao == '4':
            acrescimo_total = float(input("Digite o valor total do acréscimo: "))
            carrinho.aplicar_acrescimo_total(acrescimo_total)
        elif opcao == '5':
            desconto_total = float(input("Digite o valor total do desconto: "))
            carrinho.aplicar_desconto_total(desconto_total)
        elif opcao == '6':
            carrinho.finalizar_venda()
        elif opcao == '7':
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
