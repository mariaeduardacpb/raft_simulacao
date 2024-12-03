# **Simulação do Algoritmo Raft com Threading**

## **Descrição do Projeto**
Este projeto é uma simulação do algoritmo de consenso **Raft** utilizando `threading` em Python. Ele demonstra como múltiplos nós em um sistema distribuído conseguem alcançar consenso por meio de eleições de líderes, envio de heartbeats e reconhecimento de lideranças. Cada nó é executado como uma thread separada, simulando comportamento assíncrono.

---

## **Funcionamento do Algoritmo**
### **Estados do Nó**
1. **Seguidor**:
   - Aguarda mensagens (heartbeats) de um líder.
   - Caso o timeout ocorra sem mensagens, inicia uma eleição e muda para o estado de candidato.

2. **Candidato**:
   - Incrementa o termo atual.
   - Solicita votos dos outros nós.
   - Se obtiver a maioria, torna-se líder. Caso contrário, volta a ser seguidor.

3. **Líder**:
   - Envia heartbeats periodicamente para os seguidores, confirmando sua liderança.

---

## **Estrutura do Código**
- **`Nodo`**: Classe que representa um nó em um cluster.
  - Implementa os três estados (`seguidor`, `candidato`, `líder`).
  - Gerencia eleições, heartbeats e votação.
- **`main`**: Configura um cluster de nós e inicia as threads correspondentes.

---

## **Requisitos**
- **Python**: Versão 3.8 ou superior.
- **Bibliotecas**: Apenas bibliotecas padrão do Python (`threading`, `time`, `random`).

---

## **Como Executar**
1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/raft-threading-simulation.git
   cd raft-threading-simulation

## **Exemplo de Logs**
Durante a execução, o programa exibe logs que mostram o comportamento dos nós. Aqui estão exemplos de diferentes situações:

1. **Timeout e Eleição**:
   - Quando um seguidor não recebe heartbeats do líder, ele inicia uma eleição.
   ```plaintext
   Nodo 0: tempo expirado, iniciando eleição.
   Nodo 0: iniciou eleição no termo 1
   Nodo 1: votou para 0.
   Nodo 2: votou para 0.
   Nodo 0: eleito líder no termo 1
   
2. **Heartbeats**:
   - O líder envia heartbeats para os seguidores, garantindo que eles reconheçam sua liderança.
   ```plaintext
   Nodo 0: enviando heartbeats como líder.
   Nodo 1: reconheceu o líder 0.
   Nodo 2: reconheceu o líder 0.
   Nodo 3: reconheceu o líder 0.
   Nodo 4: reconheceu o líder 0.
   
3. **Reconhecimento de Líder**:
   - Os seguidores reconhecem o líder ao receber mensagens de heartbeat.
   ```plaintext
   Nodo 1: reconheceu o líder 0.
   Nodo 2: reconheceu o líder 0.
   Nodo 3: reconheceu o líder 0.
   Nodo 4: reconheceu o líder 0.

