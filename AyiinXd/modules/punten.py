from time import sleep

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd


@ayiin_cmd(pattern="sadboy(?: |$)(.*)")
async def _(event):
    await event.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await event.edit("`Kedua kamu manis`")
    sleep(1)
    await event.edit("`Dan yang terakhir adalah kamu bukan jodohku`")


# Create by myself @localheart


@ayiin_cmd(pattern="at2(?: |$)(.*)")
async def _(event):
    await event.edit("**Nissa sabyan i love you so much**")
    sleep(3.2)
    await event.edit("**Nissa sabya...n tetap semangat**")
    sleep(3.2)
    await event.edit("**Nissa sabyan kok cantik banget**")
    sleep(3.2)
    await event.edit("**Nissa sabya...n tetap semangat**")


@ayiin_cmd(pattern="pantau(?: |$)(.*)")
async def _(event):
    await event.edit(
        "`\n┻┳|―-∩`"
        "`\n┳┻|     ヽ`"
        "`\n┻┳|    ● |`"
        "`\n┳┻|▼) _ノ`"
        "`\n┻┳|￣  )`"
        "`\n┳ﾐ(￣ ／`"
        "`\n┻┳T￣|`"
        "\n**Masih Gua Pantau**"
    )


# Create by myself @localheart


CMD_HELP.update(
    {
        "punten": f"**Plugin : **`Animasi Punten`\
        \n\n  »  **Perintah :** `{cmd}at2` ; `{cmd}pantau`\
        \n  »  **Kegunaan : **Arts Beruang kek lagi mantau.\
        \n\n  »  **Perintah :** `{cmd}sadboy`\
        \n  »  **Kegunaan : **ya sadboy coba aja.\
    "
    }
)
