# Projeto-Grafos-AV3

## Grupo:
    - Guadalupe Prado
    - Ian Lucas
    - Letícia Maria Cunha

### Detalhes da Implementação do Trabalho:
- Sistema de infraestrutura de postes de energia utilizando Grafos. O tipo de grafo utilizado é uma Árvore Espelhada Mínima.
- O Grafo é Não-Direcionado.
- A distância entre os postes serão estipulados por meio de uma matriz de adjâncência.
- Quando o poste estiver inativo, suas arestas serão cortadas e o caminho será recalculado utilizando algoritmos Prim ou Kruskal.

## Passo-a-passo para execução do ambiente:
1. Utilizar Python 3.13.3 para o projeto
2. Criar um ambiente virtual com o comando no terminal dentro da pasta do projeto:
```bash
python -m venv venv
```
3. Ativar o ambiente virtual:
- No Windows:
```bash
venv\Scripts\activate
```
- No Linux:
```bash
source venv/bin/activate
```
5. Execute o comando para instalar as dependências:
```bash
pip install -r requirements.txt
```
