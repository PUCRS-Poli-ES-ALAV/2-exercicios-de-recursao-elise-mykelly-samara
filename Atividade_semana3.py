class Recursao:
    
    # Método recursivo para calcular o fatorial de um número n
    def fatorial(self, n):
        if n == 0:
            return 1
        return n * self.fatorial(n - 1)

    # Método recursivo para calcular o somatório de 0 até n
    def somatorio(self, n):
        if n == 0:
            return 0
        return n + self.somatorio(n - 1)

    # Método recursivo para calcular o n-ésimo número de Fibonacci
    def fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    # Método recursivo para calcular o somatório entre k e j
    def somatorio_entre(self, k, j):
        if k > j:
            return 0
        return k + self.somatorio_entre(k + 1, j)

    # Método recursivo para verificar se uma string é um palíndromo
    def is_pal(self, s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return self.is_pal(s[1:-1])

    # Método recursivo para converter um número inteiro para binário
    def conv_base2(self, n):
        if n == 0:
            return "0"
        if n == 1:
            return "1"
        return self.conv_base2(n // 2) + str(n % 2)

    # Método recursivo para calcular o somatório de uma lista de inteiros
    def somatorio_lista(self, ar):
        if not ar:
            return 0
        return ar[0] + self.somatorio_lista(ar[1:])

    # Método recursivo para encontrar o maior elemento de uma lista
    def find_biggest(self, ar):
        if len(ar) == 1:
            return ar[0]
        biggest = self.find_biggest(ar[1:])
        return max(ar[0], biggest)

    # Método recursivo para verificar se uma string ocorre dentro de outra
    def find_substr(self, str, match):
        if match == "":
            return True
        if len(str) < len(match):
            return False
        if str.startswith(match):
            return True
        return self.find_substr(str[1:], match)

    # Método recursivo para contar o número de dígitos de um número
    def nro_digit(self, n):
        if n < 10:
            return 1
        return 1 + self.nro_digit(n // 10)

    # Método recursivo para gerar todas as permutações de uma string
    def permutations(self, s):
        result = []
        if len(s) == 0:
            result.append("")
            return result
        for i in range(len(s)):
            current_char = s[i]
            remaining_string = s[:i] + s[i + 1:]
            remaining_permutations = self.permutations(remaining_string)
            for perm in remaining_permutations:
                result.append(current_char + perm)
        return result


def main():
    recursao = Recursao()

    while True:
        # Menu de opções
        print("\nEscolha um exercício para testar:")
        print("1 - Fatorial")
        print("2 - Somatório de 0 até n")
        print("3 - Fibonacci")
        print("4 - Somatório entre k e j")
        print("5 - Palíndromo")
        print("6 - Conversão para binário")
        print("7 - Somatório de uma lista")
        print("8 - Maior elemento de uma lista")
        print("9 - Substring em uma string")
        print("10 - Contar número de dígitos")
        print("11 - Permutações de uma string")
        print("0 - Sair")
        
        escolha = int(input("Digite o número da opção que deseja testar: "))
        
        if escolha == 0:
            print("Saindo...")
            break
        
        if escolha == 1:  # Fatorial
            n = int(input("Digite um número para calcular o fatorial: "))
            print(f"Fatorial de {n} é {recursao.fatorial(n)}")
        
        elif escolha == 2:  # Somatório
            n = int(input("Digite um número para calcular o somatório de 0 até n: "))
            print(f"Somatório de 0 até {n} é {recursao.somatorio(n)}")
        
        elif escolha == 3:  # Fibonacci
            n = int(input("Digite o número para calcular o n-ésimo número de Fibonacci: "))
            print(f"O {n}-ésimo número de Fibonacci é {recursao.fibonacci(n)}")
        
        elif escolha == 4:  # Somatório entre k e j
            k = int(input("Digite o valor de k: "))
            j = int(input("Digite o valor de j: "))
            print(f"Somatório entre {k} e {j} é {recursao.somatorio_entre(k, j)}")
        
        elif escolha == 5:  # Palíndromo
            s = input("Digite uma string para verificar se é um palíndromo: ")
            print(f"A string '{s}' é um palíndromo? {recursao.is_pal(s)}")
        
        elif escolha == 6:  # Conversão para binário
            n = int(input("Digite um número para converter para binário: "))
            print(f"O número {n} em binário é {recursao.conv_base2(n)}")
        
        elif escolha == 7:  # Somatório de uma lista
            ar = list(map(int, input("Digite os elementos da lista separados por espaço: ").split()))
            print(f"O somatório da lista {ar} é {recursao.somatorio_lista(ar)}")
        
        elif escolha == 8:  # Maior elemento da lista
            ar = list(map(int, input("Digite os elementos da lista separados por espaço: ").split()))
            print(f"O maior elemento da lista {ar} é {recursao.find_biggest(ar)}")
        
        elif escolha == 9:  # Substring em uma string
            str = input("Digite a string principal: ")
            match = input("Digite a substring para verificar se ocorre na string principal: ")
            print(f"A substring '{match}' ocorre em '{str}'? {recursao.find_substr(str, match)}")
        
        elif escolha == 10:  # Contar número de dígitos
            n = int(input("Digite um número para contar o número de dígitos: "))
            print(f"O número {n} tem {recursao.nro_digit(n)} dígitos")
        
        elif escolha == 11:  # Permutações de uma string
            s = input("Digite uma string para gerar suas permutações: ")
            print(f"As permutações da string '{s}' são {recursao.permutations(s)}")
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
