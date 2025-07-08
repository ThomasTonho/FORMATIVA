# Gerenciador de Lista de Frutas

Este projeto em Python permite ao usuário criar e gerenciar uma lista de frutas de forma interativa via terminal.

## 🚀 Funcionalidades

- Permite ao usuário cadastrar 3 frutas, sem repetições.
- Exibe a lista inicial cadastrada.
- Pergunta continuamente se o usuário deseja excluir frutas da lista.
- Remove frutas da lista caso existam.
- Encerra o processo se o usuário não quiser mais excluir ou se a lista ficar vazia.

## 📋 Fluxo do Programa

### Início

- Criar uma lista vazia chamada `frutas`.

### Entrada Inicial

- Solicita 3 frutas ao usuário.
- Se a fruta já existir na lista, solicita outra até que seja digitada uma diferente.
- As frutas válidas são adicionadas à lista.

### Saída Inicial

- Exibe: **"Lista inicial"** com os itens cadastrados.

### Processo de Exclusão

- Enquanto o usuário desejar:
  - Pergunta: **"Deseja excluir alguma fruta da lista? (sim/não)"**
  - Se `sim`:
    - Exibe as frutas cadastradas.
    - Solicita o nome da fruta a excluir.
    - Se a fruta estiver na lista:
      - Remove a fruta e exibe mensagem de exclusão.
    - Se não estiver:
      - Exibe: **"Fruta não encontrada"**
    - Se a lista ficar vazia:
      - Exibe: **"Lista vazia. Encerrando..."** e finaliza o programa.
  - Se `não` ou `nao`:
    - Finaliza o laço de exclusão.
  - Se resposta inválida:
    - Exibe: **"Opção inválida. Tente novamente."**

### Saída Final

- Exibe: **"Lista final de frutas"** com o conteúdo atualizado.

## 💡 Exemplo de Uso

```bash
Digite a 1ª fruta: maçã  
Digite a 2ª fruta: banana  
Digite a 3ª fruta: maçã  
Fruta já cadastrada. Digite outra: uva  
Lista inicial: ['maçã', 'banana', 'uva']

Deseja excluir alguma fruta da lista? (sim/não): sim  
Frutas cadastradas: ['maçã', 'banana', 'uva']  
Digite o nome da fruta a ser excluída: banana  
Fruta 'banana' removida com sucesso!

Deseja excluir alguma fruta da lista? (sim/não): não  
Lista final de frutas: ['maçã', 'uva']
