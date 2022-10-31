from time import sleep

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import edit_or_reply, ayiin_cmd


@ayiin_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Assalamualaikum ukhti**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@ayiin_cmd(pattern="pe(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Assalamualaikum Akhii**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@ayiin_cmd(pattern="P(?: |$)(.*)")
async def _(event):
    me = await event.client.get_me()
    xx = await edit_or_reply(event, f"**Haii Salken Saya {me.first_name}**")
    sleep(2)
    await xx.edit("**Assalamualaikum...**")


@ayiin_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**Wa'alaikumsalam Masya allah**", reply_to=event.reply_to_msg_id
    )
    await event.delete()


@ayiin_cmd(pattern="a(?: |$)(.*)")
async def _(event):
    me = await event.client.get_me()
    xx = await edit_or_reply(event, f"**Haii Salken Saya {me.first_name}**")
    sleep(2)
    await xx.edit("**Assalamualaikum**")


@ayiin_cmd(pattern="j(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**Ada Mpok ketemu topan**")
    sleep(3)
    await xx.edit("**Assalamu'alaikum dulu biar sopan**")


@ayiin_cmd(pattern="k(?: |$)(.*)")
async def _(event):
    me = await event.client.get_me()
    xx = await edit_or_reply(event, f"**Hallo guys saya {me.first_name}**")
    sleep(2)
    await xx.edit("**sarangheyo ❤️**")
    sleep(3)
    await xx.edit("**tapi boong**")


@ayiin_cmd(pattern="bgt(?: |$)(.*)")
async def _(event):
    me = await event.client.get_me()
    xx = await edit_or_reply(event, f"**begitu syulitt lupakan {me.first_name}**")
    sleep(2.5)
    Await = xx.edit_or_reply(event, f"**apa lagi {me.first_name} baik🥰 **")


CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\n  »  **Perintah :** `{cmd}p`\
        \n  »  **Kegunaan : **Assalamualaikum Dulu Biar Sopan..\
        \n\n  »  **Perintah :** `{cmd}pe`\
        \n  »  **Kegunaan : **salam Kenal dan salam\
        \n\n  »  **Perintah :** `{cmd}l`\
        \n  »  **Kegunaan : **Untuk Menjawab salam\
        \n\n  »  **Perintah :** `{cmd}bgt`\
        \n  »  **Kegunaan : **begitu syulit\
        \n\n  »  **Perintah :** `{cmd}semangat`\
        \n  »  **Kegunaan : **Memberikan Semangat.\
        \n\n  »  **Perintah :** `{cmd}ywc`\
        \n  »  **Kegunaan : **Menampilkan Sama sama\
        \n\n  »  **Perintah :** `{cmd}sayang`\
        \n  »  **Kegunaan : **Kata I Love You.\
        \n\n  »  **Perintah :** `{cmd}k`\
        \n  »  **Kegunaan : **Coba Aja Sendiri\
        \n\n  »  **Perintah :** `{cmd}j`\
        \n  »  **Kegunaan : **pantun salam\
    "
    }
)
