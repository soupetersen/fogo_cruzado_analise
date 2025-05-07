# Instruções para Rodar o Projeto Fogo Cruzado

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/fogo-cruzado.git
   cd fogo-cruzado
   ```

2. (Opcional) Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Como rodar as análises

1. Certifique-se de que os dados necessários estão na pasta `data/`.
2. Execute os notebooks Jupyter:
   ```sh
   jupyter notebook
   ```
   Abra o arquivo `notebooks/analise.ipynb` e execute as células.

3. Para rodar scripts Python diretamente:
   ```sh
   python main.py
   ```

## Como usar o main.py

Ao rodar o arquivo `main.py`, será exibido um menu interativo com as seguintes opções:

1. **Login**: Realize o login na API do Fogo Cruzado informando seu e-mail e senha. O token de acesso será salvo para uso nas próximas requisições.
2. **Refresh token**: Atualize o token de acesso caso ele expire.
3. **Get city data**: Busque dados de uma cidade informando o nome. O resultado será salvo em um arquivo JSON na pasta `data/`.
4. **Get occurrences by city**: Busque ocorrências por cidade, informando o ID da cidade, ID do estado (opcional), datas inicial e final, ordem e página. O resultado será salvo em um arquivo JSON na pasta `data/`.
5. **Get occurrences by state**: Busque ocorrências por estado, informando o ID do estado e o período desejado. O resultado será salvo em um arquivo JSON na pasta `data/`.
6. **Get all states**: Baixe a lista de todos os estados disponíveis na API. O resultado será salvo em `data/states.json`.

### Recomendações de uso

- Antes de buscar ocorrências, utilize a opção 6 para obter os estados e a opção 3 para obter os dados da cidade e identificar os IDs necessários.
- Use as opções 4 e 5 para baixar os dados de ocorrências conforme sua necessidade.
- Os arquivos gerados podem ser utilizados para análise no notebook `notebooks/analise.ipynb`.

> **Dica:** Sempre confira se o token está válido antes de buscar dados. Caso expire, utilize a opção 2 para atualizar.

## Visualização do Mapa

- O mapa interativo é gerado em `data/maps/map_ocorrences.html`.
- Para visualizar no relatório, abra o arquivo HTML no navegador ou veja o print em `data/maps/map_ocorrences.png` no arquivo `analise.md`.

## Observações

- Para atualizar os dados, consulte a documentação da API do Fogo Cruzado.
- Se precisar de mais dependências, adicione ao `requirements.txt`.

---