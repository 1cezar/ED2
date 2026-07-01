# Estruturas de Dados II — Códigos de Referência

Repositório de apoio para as aulas práticas da disciplina **Estruturas de Dados II**.

## Organização

```text
ED2/
├── README.md
├── codigos-referencia/
│   ├── arvore_bst_referencia.py
│   ├── rubro_negra_referencia.py
│   ├── hash_referencia.py
│   └── grafos_referencia.py
└── codigos-base/
    ├── rubro_negra_base_alunos.py
    ├── hash_base_alunos.py
    └── grafos_base_alunos.py
```

## Como usar

Clone o repositório:

```bash
git clone https://github.com/1cezar/ED2.git
cd ED2
```

Execute qualquer arquivo Python:

```bash
python codigos-referencia/arvore_bst_referencia.py
python codigos-referencia/hash_referencia.py
python codigos-referencia/grafos_referencia.py
python codigos-referencia/rubro_negra_referencia.py
```

## Conteúdos

### Árvores binárias e BST

Arquivo:

```text
codigos-referencia/arvore_bst_referencia.py
```

Contém:

- árvore binária comum;
- árvore binária de busca;
- inserção;
- busca;
- caminho de busca;
- percursos;
- altura;
- contagem de nós;
- contagem de folhas;
- remoção em BST.

### Árvore Rubro-Negra

Arquivos:

```text
codigos-base/rubro_negra_base_alunos.py
codigos-referencia/rubro_negra_referencia.py
```

O arquivo base deve ser completado durante a aula. O arquivo de referência serve para conferência.

### Tabelas Hash

Arquivos:

```text
codigos-base/hash_base_alunos.py
codigos-referencia/hash_referencia.py
```

Conteúdos:

- função hash;
- colisões;
- encadeamento separado;
- busca;
- remoção;
- fator de carga.

### Grafos

Arquivos:

```text
codigos-base/grafos_base_alunos.py
codigos-referencia/grafos_referencia.py
```

Conteúdos:

- lista de adjacência;
- matriz de adjacência;
- BFS;
- DFS;
- grafos direcionados e não direcionados.

## Orientação para os alunos

Nas atividades práticas, vocês podem consultar os códigos de referência para entender a estrutura geral, mas devem construir suas próprias soluções, principalmente nas funções solicitadas pelo professor.

O objetivo não é apenas copiar o código, mas compreender:

- qual estrutura de dados está sendo usada;
- como os dados são inseridos;
- como ocorre a busca;
- como representar a estrutura em memória;
- como interpretar as saídas.
