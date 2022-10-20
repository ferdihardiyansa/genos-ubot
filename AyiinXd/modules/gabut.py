from time import sleep
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, edit_or_reply


@ayiin_cmd(pattern="con(?: |$)(.*)")
async def _(teemo):
    yins = await edit_or_reply(con, "`I HAVE CRUSH ON YOU`")
    sleep(3)
    await yins.edit("`EH TAPI BOOONG😛`")


@ayiin_cmd(pattern="capek1(?: |$)(.*)")
async def _(giveaway):
    ayiin = await edit_or_reply(capek1, "`BOLEH NGOMONG JUJUR BOLEH GA KAK?`")
    sleep(4)
    await ayiin.edit("`JUJUR`")
    sleep(3)
    await ayiin.edit("`CAPE YAH? JANGAN SEMANGAT`")


@ayiin_cmd(pattern="capek2(?: |$)(.*)")
async def _(uno):
    xd = await edit_or_reply(uno, "`BOLEH NGOMONG BANYAK HAL GA KAK?`")
    sleep(2)
    await xd.edit("`HAL HAL HAL HAL`")
    sleep(1)
    await xd.edit("`CAPE YAH? JANGAN SEMANGAT`")


CMD_HELP.update(
    {
        "gabut2": f"**Plugin : **`gabut2`\
        \n\n  »  **Perintah :** `{cmd}con`\
        \n  »  **Kegunaan : **Coba Sendiri Tod.\
        \n\n  »  **Perintah :** `{cmd}capek1`\
        \n  »  **Kegunaan : **Coba Sendiri Tod.\
        \n\n  »  **Perintah :** `{cmd}capek2`\
        \n  »  **Kegunaan : **Coba Sendiri Tod.\
    "
    }
)
