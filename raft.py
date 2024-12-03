import threading
import time
import random

class Nodo:
    def __init__(self, id_nodo, cluster):
        self.id_nodo = id_nodo
        self.cluster = cluster
        self.estado = "seguidor"  # seguidor, candidato, líder
        self.termo_atual = 0
        self.voto_para = None
        self.votos_recebidos = 0
        self.lider_atual = None
        self.timeout = random.uniform(3, 5)  # Tempo de espera para iniciar eleição

    def executar(self):
        while True:
            if self.estado == "seguidor":
                self.loop_seguidor()
            elif self.estado == "candidato":
                self.loop_candidato()
            elif self.estado == "líder":
                self.loop_lider()

    def loop_seguidor(self):
        inicio = time.time()
        while time.time() - inicio < self.timeout:
            if self.lider_atual:
                time.sleep(0.5)
                return
        print(f"Nodo {self.id_nodo}: tempo expirado, iniciando eleição.")
        self.estado = "candidato"

    def loop_candidato(self):
        self.termo_atual += 1
        self.voto_para = self.id_nodo
        self.votos_recebidos = 1
        print(f"Nodo {self.id_nodo}: iniciou eleição no termo {self.termo_atual}")

        for nodo in self.cluster:
            if nodo.id_nodo != self.id_nodo:
                if nodo.solicitar_voto(self.id_nodo, self.termo_atual):
                    self.votos_recebidos += 1

        if self.votos_recebidos > len(self.cluster) // 2:
            print(f"Nodo {self.id_nodo}: eleito líder no termo {self.termo_atual}")
            self.estado = "líder"
            self.lider_atual = self.id_nodo
        else:
            print(f"Nodo {self.id_nodo}: falhou em ser eleito, voltando a seguidor.")
            self.estado = "seguidor"

    def loop_lider(self):
        print(f"Nodo {self.id_nodo}: enviando heartbeats como líder.")
        for nodo in self.cluster:
            if nodo.id_nodo != self.id_nodo:
                nodo.receber_heartbeat(self.id_nodo, self.termo_atual)
        time.sleep(2)

    def solicitar_voto(self, id_candidato, termo):
        if termo > self.termo_atual and self.voto_para is None:
            print(f"Nodo {self.id_nodo}: votou para {id_candidato}.")
            self.voto_para = id_candidato
            self.termo_atual = termo
            return True
        return False

    def receber_heartbeat(self, id_lider, termo):
        if termo >= self.termo_atual:
            self.lider_atual = id_lider
            self.termo_atual = termo
            print(f"Nodo {self.id_nodo}: reconheceu o líder {id_lider}.")
            return True
        return False


def main():
    cluster = [Nodo(i, None) for i in range(5)]
    for nodo in cluster:
        nodo.cluster = cluster

    threads = []
    for nodo in cluster:
        thread = threading.Thread(target=nodo.executar)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
