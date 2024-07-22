from dotenv import load_dotenv
import genshin
import asyncio
import os

async def main():
    load_dotenv();

    cookies = {
        "account_id": os.environ['account_id'],
        "account_id_v2": os.environ['account_id_v2'], 
        "account_mid_v2": os.environ['account_mid_v2'],
        "cookie_token": os.environ['cookie_token'],
        "cookie_token_v2": os.environ['cookie_token_v2'],
        "ltmid_v2": os.environ['ltmid_v2'],
        "ltoken_v2": os.environ['ltoken_v2'],
        "ltuid_v2": os.environ['ltuid_v2']
    }
    client = genshin.Client(cookies)

    for game in [
        genshin.Game.GENSHIN,
        genshin.Game.STARRAIL,
        genshin.Game.ZZZ
    ]:
        try:
            await client.claim_daily_reward(game=game)
            print(f"Successfully claimed daily reward for {game}")
        except genshin.AlreadyClaimed:
            print(f"Already claimed daily reward for {game}")
        except:
            pass

asyncio.run(main())