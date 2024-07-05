# Migração Automatizada MongoDB

Este projeto visa realizar a migração de dados entre dois bancos de dados MongoDB de forma automatizada.

## Pré-requisitos

- Python 3.x
- Biblioteca `pymongo`

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/leandrosroc/mongodb-migration.git
    cd mongodb-migration
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  #No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install pymongo
    ```

## Configuração

Atualize as variáveis `source_uri` e `destination_uri` no script `main.py` com as URLs dos seus bancos de dados MongoDB de origem e destino.

```python
# URL do MongoDB de origem
source_uri = "mongodb://root:root@86.*.*.*:27017/?authSource=admin&readPreference=primary&ssl=false&directConnection=true"

# URL do MongoDB de destino
destination_uri = "mongodb://admin:admin@62.*.*.*:27017/?authSource=admin&readPreference=primary&ssl=false&directConnection=true"
```

## Uso

Execute o script de migração:

```
python main.py
```

## Contribuição

Sinta-se à vontade para contribuir ou relatar problemas neste repositório. Contribuições são bem-vindas!

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE) - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
