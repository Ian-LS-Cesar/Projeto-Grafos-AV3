# Projeto-Grafos-AV3

## Grupo:
    - Guadalupe Prado
    - Ian Lucas
    - Letícia Maria Cunha

### Detalhes da Implementação do Trabalho:
- Sistema de infraestrutura de postes de energia utilizando Grafos. O tipo de grafo implementado é uma Árvore Espalhada Mínima.
- O Grafo é Ponderado, Não-Direcionado e Acíclico na implementação do Prim para geração do melhor caminho.
- Quando o poste estiver inativo, suas arestas serão cortadas e o caminho será recalculado utilizando algoritmos Prim.

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
