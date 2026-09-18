"""
Script di accesso a Garmin Connect.

Da eseguire UNA SOLA VOLTA dal terminale (non dall'app!) per autenticarti.
Dopo il primo accesso riuscito, i dati di sessione restano salvati sul PC
e l'app principale (garmin_uscite.py) potrà leggerli senza chiedere di
nuovo email e password.

Se in futuro l'app principale segnala che non riesce più a collegarsi,
rilancia semplicemente questo script per accedere di nuovo.
"""

from getpass import getpass

from garminconnect import Garmin

# Cartella dove vengono salvati i dati di sessione (non la password!),
# così le prossime volte non serve rifare il login da zero.
CARTELLA_TOKEN = "~/.garminconnect"


def main():
    print("=== Accesso a Garmin Connect ===")
    email = input("Email Garmin: ").strip()
    password = getpass("Password Garmin (non verrà mostrata mentre scrivi): ")

    client = Garmin(
        email,
        password,
        prompt_mfa=lambda: input(
            "Codice di verifica (se Garmin te lo chiede via mail/app): "
        ).strip(),
    )
    client.login(CARTELLA_TOKEN)

    print("\nAccesso riuscito!")
    print("Ora puoi avviare l'app principale (garmin_uscite.py) senza reinserire le credenziali.")


if __name__ == "__main__":
    main()
