import time
import functions
from colorama import init, Fore


init(autoreset=True)

RED     = Fore.RED
GREEN   = Fore.GREEN
WHITE   = Fore.WHITE
ORANGE  = Fore.YELLOW
TOKENS  = functions.get_file("tokens")
PROXIES = functions.get_file("proxies")
EMOJIS  = open("data/emojis.txt", 'r')



def main():
	functions.clear_screen()
	Content = {
		"0t":f"{ORANGE}[Warning!]{WHITE} Tokens file is empty.",
		"0p":f"{ORANGE}[Warning!]{WHITE} Proxies file is empty.",
		"vt":f"{GREEN}[Success!]{WHITE} Tokens file loaded successfully",
		"ve":f"{GREEN}[Success!]{WHITE} Emojis file loaded successfully",
		"vp":f"{GREEN}[Success!]{WHITE} Proxies file loaded successfully",
	}


	print(Content["0t"] if len(TOKENS) == 0 else Content["vt"])
	time.sleep(0.2)
	print(Content["0p"] if len(PROXIES) == 0 else Content["vp"])
	time.sleep(0.2)
	print(Content["ve"])
	time.sleep(0.2)

	print(f"[{RED}discord.gg/person{WHITE}] Welcome to the free version of Person Multitool.")

	input(f"\r\n\r\n{RED}[Person]{WHITE} Click enter to continue...")

	functions.home_page(RED, WHITE)
	functions.handle_commands(RED, WHITE, TOKENS)


if __name__ == "__main__":
	main()
