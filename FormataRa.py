class FormataRa:
    @staticmethod
    def formataRa(ra):
        ultimos_4_digitos = ra[-4:]
        print(f"RA: {ra}, Últimos 4 dígitos: {ultimos_4_digitos}")
        return ultimos_4_digitos