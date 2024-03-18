from discord import Intents, Client
import responses

def run_bot(token: str):
    # Basic setup
    intents = Intents.default()
    intents.message_content = True
    client = Client(intents=intents)
    knowledge: dict = responses.load_knowledge("knowledge.json")

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content:
            print(f'({message.channel}){message.author}: "{message.content}"')
            response: str = responses.get_response(message.content, knowledge=knowledge)
            await message.channel.send(response)
        else:
            print("!!!TURN ON YOUR INTENTS!!!")

    client.run(token=token)

if __name__ ==  "__main__":
    run_bot(token="MTIxNzI5MDI4NDc4Njc3ODEyMg.GBZObV.yxPTeV-HiQq4p4EXxsCNpo-3ynqKigYYTIHXXY")