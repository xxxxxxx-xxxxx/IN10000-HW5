# app.py
import json, os, hashlib
from getpass import getpass
from filmklubb import Filmklubb

USERS_FILE = "users.json"

# ---------- password hashing + user storage ----------
def hash_pw(pw: str) -> str:
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()

def load_users() -> dict:
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_users(users: dict) -> None:
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

def login_flow(users: dict) -> str | None:
    print("Welcome to MovieClub!")
    while True:
        choice = input("[L]ogin / [R]egister / [Q]uit: ").strip().lower()
        if choice == "q":
            return None
        if choice not in ("l", "r"):
            print("Please choose L, R or Q.")
            continue

        username = input("Username: ").strip()
        if not username:
            print("Username cannot be empty.")
            continue

        if choice == "r":
            if username in users:
                print("User already exists.")
                continue
            pw1 = getpass("Create password: ")
            pw2 = getpass("Repeat password: ")
            if pw1 != pw2 or not pw1:
                print("Passwords do not match or empty.")
                continue
            users[username] = {"password_hash": hash_pw(pw1)}
            save_users(users)  # creates/updates users.json
            print("User registered. You can log in now.")
            continue

        # choice == "l"
        if username not in users:
            print("User not found. Register first.")
            continue
        pw = getpass("Password: ")
        if users[username]["password_hash"] != hash_pw(pw):
            print("Wrong password.")
            continue
        print(f"Hello, {username}!")
        return username

# ---------- main menu using Filmklubb ----------
def main_menu(fk: Filmklubb):
    while True:
        print("\n=== MovieClub Menu ===")
        print("1) List all movies")
        print("2) Add a new movie")
        print("3) Find movie by title prefix")
        print("4) Add actors to a movie")
        print("5) Find movies in a year range")
        print("q) Quit")
        choice = input("Choose: ").strip().lower()

        if choice == "q":
            print("Bye!")
            break

        elif choice == "1":
            fk.skriv_ut_alle_filmer()

        elif choice == "2":
            fk.registrer_film()  # will prompt for title/year

        elif choice == "3":
            prefix = input("Title starts with: ")
            film = fk.finn_film_tittel(prefix)
            if film:
                print("Found:")
                film.skriv_ut_film()
            else:
                print("No match.")

        elif choice == "4":
            prefix = input("Which film (title starts with): ")
            film = fk.finn_film_tittel(prefix)
            if film:
                fk.legg_til_skuespillere(film)  # prompts for name/role
            else:
                print("No such film.")

        elif choice == "5":
            try:
                a = int(input("After year: "))
                b = int(input("Before year: "))
            except ValueError:
                print("Please enter valid years.")
                continue
            res = fk.finn_filmer_periode(a, b)
            if not res:
                print("No films in that range.")
            else:
                for f in res:
                    print("-", f.hent_tittel())

        else:
            print("Unknown choice.")

# ---------- entry point ----------
if __name__ == "__main__":
    users = load_users()                # {} if file doesn’t exist yet
    user = login_flow(users)            # choose Register the first time
    if user is None:
        raise SystemExit

    fk = Filmklubb()
    fk.les_filmer_fra_fil("filmer.txt") # load films once
    main_menu(fk)
