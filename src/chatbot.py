class StudyIA:

    def responder(self, pergunta):

        pergunta = pergunta.lower()

        if "python" in pergunta:
            return "Python é uma linguagem de programação de alto nível utilizada para desenvolvimento web, automação, análise de dados e Inteligência Artificial."

        elif "sql" in pergunta:
            return "SQL é uma linguagem utilizada para consultar e manipular bancos de dados relacionais."

        elif "select" in pergunta:
            return "O comando SELECT é utilizado para consultar dados em uma tabela."

        elif "join" in pergunta:
            return "JOIN é utilizado para combinar informações de duas ou mais tabelas."

        elif "chave primária" in pergunta:
            return "Uma chave primária identifica exclusivamente cada registro de uma tabela."

        elif "banco de dados" in pergunta:
            return "Um banco de dados é uma coleção organizada de informações armazenadas eletronicamente."

        elif "inteligência artificial" in pergunta or "ia" in pergunta:
            return "Inteligência Artificial é uma área da computação que desenvolve sistemas capazes de aprender e tomar decisões com base em dados."

        else:
            return "Desculpe, não encontrei essa informação na minha base de conhecimento."
