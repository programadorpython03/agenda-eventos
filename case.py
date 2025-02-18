class MinhaClasse:
    def __enter__(self):
        print("Entrando na classe")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saindo da classe")

    def __call__(self):
        print("Chamando a classe")

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"
    
with MinhaClasse() as mc:
    print("Estou aqui dentro")