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
