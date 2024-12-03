# **Raft Consensus Algorithm Simulation**

## **Descrição do Projeto**
Este projeto é uma simulação do algoritmo de consenso **Raft**, amplamente utilizado em sistemas distribuídos para garantir consistência e confiabilidade. A implementação simula um ambiente distribuído onde múltiplos nós participam do processo de consenso, incluindo eleições, replicação de logs e envio de heartbeats.

O objetivo principal é demonstrar as etapas do algoritmo Raft de forma simplificada, abordando como os nós alcançam consenso em um ambiente simulado.

---

## **Algoritmo Implementado**
### **Raft**
O algoritmo Raft é uma alternativa ao Paxos e foi projetado para ser mais simples e fácil de entender. Ele divide o consenso em três componentes principais:

1. **Eleição de Líder**:
   - Quando um nó não recebe mensagens do líder, ele se torna candidato e inicia uma eleição.
   - O nó que obtiver a maioria dos votos se torna o líder.

2. **Replicação de Logs**:
   - O líder recebe comandos dos clientes e os adiciona ao log.
   - O líder replica o log para os seguidores.

3. **Envio de Heartbeats**:
   - O líder envia heartbeats periodicamente para os seguidores para mantê-los sincronizados e evitar novas eleições.

---

## **Estrutura do Repositório**
