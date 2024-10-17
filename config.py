"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", 8785365)
        self.API_HASH: str = os.environ.get("API_HASH", 48c1934c1df9da5b218cfc1382be1bdf)
        self.SESSION: str = os.environ.get("SESSION", BQCGDdUATyw-qX_T22xrw1Q_tJbMrcOheKS_Qc-dYe4RINWGs5ruvkRG9s01tvOJCRle9IaskG1LDptTsDeCOsZWfWp-t8vpOe0K3_8mA9Xo9r421oK0OB77ahw012uELpc_f8psP7dVKdOzm-3M0pSIFGE2GMEIX_P-sqjXyykhvuwRxLiqkk9x3Y9wjQiNVXrJQ1CER4jxD5wjkILB_pk2xuG6avP2svZApjaoETaG8AeGnezmgyAe5ibO5_JqYBuk7OlfBk1bteajO0nCvZFsjZfdEx2N52fx7X8jZkhnVUaen-4dT92HeDLmoq6pkwatldXUzTQMSgu9IESfIeManUb2ugAAAAFDAnVeAA)
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", 7760699975:AAGQMKV0oTlK7A4d9LM4_y99a-kHWLAkaaA)
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "5419201886 7074356361 ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
