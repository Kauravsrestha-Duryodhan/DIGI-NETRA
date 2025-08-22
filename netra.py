from finalkit.Numbercheck import search_google, validate_phone_number, look, WhatsappInfo
from finalkit.username import main as check_username
from finalkit.ipcheck import check_ip_address
from finalkit.idcheck import instafind as id_instafind
from pyfiglet import Figlet
from rich import print
from validator.emails import email_check
from validator.firefox import firefox
from validator.hudson import hudson
from validator.paste import paste
from validator.instagram import instafind as validator_instafind

f = Figlet(font='slant')
ascii_art = f.renderText('DIGI-NETRA')

welcome_banner = """
[bold cyan]    ✦━─━────༺༻────━─━✦
     Welcome to DIGI-NETRA
     Created By : [bold magenta]@Kauravsresth-Duryodhan[/bold magenta]
     Version    : 0.1
    ✦━─━────༺༻────━─━✦[/bold cyan]
"""
print(f"[bold magenta]{ascii_art}[/bold magenta]")
print(welcome_banner)

print("[bold green]DIGI-NETRA - Your Terminal-Based OSINT Toolkit[/bold green]")
print("[bold yellow]Gather intelligence from numbers, usernames, IPs & more — all in one place![/bold yellow]")

try:
    while True:
        print("Please select an option:")
        print("1. Information By Number")
        print("2. Information By Username")
        print("3. Information By Email")
        print("4. Information By IP")
        print("5. Exit")
        options = input("Enter Your Choice: ").strip()
        if options == "1": 
            print("[magenta]Enter username to search[/magenta]: ")
            query = int(input())
            search_google(query)
            print("\n" + "="*50 + "\n")
            validate_phone_number(query)
            look(query)
            WhatsappInfo(query)
            id_instafind(query)
        elif options == "2":
            check_username()
        elif options == "3":
            print("[magenta]Enter username to search[/magenta]: ",end="")
            email = input()
            print(f"\n[bold blue]Checking Email: {email}[/bold blue]")
            print("[bold cyan]Only Registered Data Will Be Provided...[/bold cyan]\n")
            email_check(email) 
            
            print("\n[bold yellow]Checking On Firefox....[/bold yellow]")
            firefox(email)
            print("\n[bold yellow]Checking On Breach Data....[/bold yellow]")
            hudson(email)
            print("\n[bold yellow]Checking On PASTEBIN....[/bold yellow]")
            paste(email)
            print("\n[bold yellow]Checking On Instagram....[/bold yellow]")
            validator_instafind(email)
        elif options == "4":
            check_ip_address()
        elif options == "5":
            print("Thank you for using DIGI-NETRA. Goodbye!")    
            break
        else:
            print("Invalid Input Please Enter Valid Input")
except (KeyboardInterrupt, EOFError):
    print("\n[bold yellow]Exiting gracefully. Thank you for using DIGI-NETRA.[/bold yellow]")
