import telnetlib
import time

# ==========================================
# CONFIGURAÇÕES DE ACESSO
# ==========================================
HOST = "Coletores.jsl.tech"
PORT = 23000  # Se não funcionar, tente 23020
USUARIO = "SEU_USUARIO"
SENHA = "SUA_SENHA"
DEPOSITO = "J8"

def executar_acesso():
    try:
        print(f"[*] Conectando ao WMS JSL em {HOST}:{PORT}...")
        # Timeout de 10 segundos para a conexão inicial
        tn = telnetlib.Telnet(HOST, PORT, timeout=10)
        
        # 1. TELA DE BOAS VINDAS
        # O sistema costuma pedir um 'Enter' para iniciar
        print("[*] Aguardando tela de boas-vindas...")
        time.sleep(2) 
        tn.write(b"\r\n") 
        print("[>] Enter enviado.")

        # 2. LOGIN (Ajuste o texto 'USUARIO' se na tela aparecer diferente)
        # O script vai esperar até ler a palavra USUARIO na tela
        tn.read_until(b"USUARIO", timeout=5)
        tn.write(USUARIO.encode('ascii') + b"\r\n")
        print(f"[>] Usuário {USUARIO} enviado.")

        # 3. SENHA
        tn.read_until(b"SENHA", timeout=5)
        tn.write(SENHA.encode('ascii') + b"\r\n")
        print("[>] Senha enviada.")

        # 4. DEPÓSITO (J8)
        tn.read_until(b"DEPOSITO", timeout=5)
        tn.write(DEPOSITO.encode('ascii') + b"\r\n")
        print(f"[>] Depósito {DEPOSITO} enviado.")

        # 5. RESULTADO FINAL
        print("\n" + "="*30)
        print("LOGIN REALIZADO COM SUCESSO!")
        print("="*30 + "\n")

        # Pequena pausa para o sistema carregar o menu principal
        time.sleep(2)
        
        # Lê tudo o que está aparecendo na tela agora
        tela_menu = tn.read_very_eager().decode('ascii', errors='ignore')
        print("CONTEÚDO DA TELA ATUAL:")
        print(tela_menu)

        # MODO INTERATIVO (Opcional)
        # Descomente a linha abaixo se quiser assumir o controle pelo teclado após o login automático
        # tn.interact()

    except Exception as e:
        print(f"\n[!] ERRO: Não foi possível completar a automação.\nDetalhes: {e}")

if __name__ == "__main__":
    executar_acesso()