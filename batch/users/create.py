
# FIX BEGIN
# Python 3 imports fix
import sys
sys.path.append("../../")
# FIX END

from users import User
from databases import MongoDatabase

print("[+] CREATING USER, WALLETS, AND ACCOUNTS... ", end="")

omar = User("otrenav@gmail.com", MongoDatabase(), new=True).update_name("Omar")
ruben = User("rjtr30@gmail.com", MongoDatabase(), new=True).update_name("Rubén")
yuli = User("yuli.godinez@gmail.com", MongoDatabase(), new=True).update_name("Yuli")
gomez = User("ricargom2000@hotmail.com", MongoDatabase(), new=True).update_name("Gómez")
nestor = User("nestor.sag@gmail.com", MongoDatabase(), new=True).update_name("Cristy")
cristy = User("rod.cristina28@gmail.com", MongoDatabase(), new=True).update_name("Néstor")
jama = User("ja.morales.alfaro@gmail.com", MongoDatabase(), new=True).update_name("Jama")

omar.new_account("Bittrex", "d151aeb3caab4fc79ae35ee68083543a", "8630ea05bd0844bf988798e58726311f")
omar.new_wallet("BTC", "15yLPAMjkHNs87D9BZ1a5kUswBUepTT8F1")
omar.new_wallet("ETH", "0x029925B8B12C189cc703407c353c4d85B771E8b2", "Trading")
omar.new_wallet("ETH", "0x1294a3c6741329558d098b40C8E1eFDA6A06bE4C", "Storage")
omar.new_wallet("LTC", "LebkCtqWKbmdvYDJjw8ugFwQKXtNzT3FtS")
omar.new_wallet("NEO", "AXhkA1jwstxVMbXtGaSxbkLw7hUbWdoENE")
omar.new_wallet("ARK", "AXECvVgDVLTsVmkoV5HJPVHQj6zhQ9Jnw1")
omar.new_wallet("IOTA", "WLXMAVSMAPRSLLKWSCDJLWIWAXRMBAKZRIDRSEORIMQXIEEXBMDMDKQFVBFKGNGOEF9ONMVHQPNYS9QSXKVIXSQQE9")

ruben.new_account("Bittrex", "6a3f0e6c3309440a815929589d61dca3", "54072b41823c4a5bac1b636bd7fe0ca7")
ruben.new_wallet("BTC", "1PF11BHEKi4NmUeJPNVTiED99XpUJrMGFf")
ruben.new_wallet("ETH", "0xC271435D93523E3C50211501E67dBE2F8E15738F", "Trading")
ruben.new_wallet("ETH", "0x48000270DF47870754907A8856e510473E70e67d", "Storage")
ruben.new_wallet("LTC", "LWfRVKrtoUHici9BMHGXc3Xj5M4K5g9jcB")
ruben.new_wallet("NEO", "AaGmgFp73HNGk6cVR8z79yADUjVLz7Ri8M")
ruben.new_wallet("ARK", "AH62mhYYUb9ZoHTa4CEFTHi4xqRdtrc7q7")
ruben.new_wallet("IOTA", "MVQKSOVKXZMQGJTNRILSDMVGDGV9GATZRBQNYMT9OHUXTZFDXT9RRTKFWNGQRDSWYVLVCC9SABZJFX9VD9XBZOVBQC")

yuli.new_account("Bittrex", "e03704d124b54bd3bd4faeb61dc2f4ff", "37d35f4b3f084cff8844c74e03c4f165")
yuli.new_wallet("BTC", "1824Gsy5KrbjsJPgJNaEc8f38o3G6PXdjV")
yuli.new_wallet("ETH", "0xDA1a44Bac256c10CD44Fa2cA56246AC11C9C9B7f", "Trading")
yuli.new_wallet("ETH", "0x19B5Bb3b9Aa168ba9D126f3E8DADE47E2dAA0500", "Storage")
yuli.new_wallet("LTC", "LdgVs9cMVYL4FPdYUgxW6Zfish6HGfYPom")
yuli.new_wallet("NEO", "Ae3kH1eCoDr2w5fM28cpHdsvDRvBTpmXmJ")
yuli.new_wallet("ARK", "AKvpQ7185MZavwZ7mb1PvgrqtcNckxPFrF")
yuli.new_wallet("IOTA", "NWRAY9LJQWRUXPZJSPCBMJCHJFHOWYCSLCPQTDAFSXZENLOOTMXCQVOFYSPBPFONYYUTZKUSX9HSYJSTYUV9KNTFGB")

gomez.new_account("Bittrex", "6b7a3fd4eb6a4ca3a50a1e01a2947069", "938c78516747443db8babc7f2789bf45")
gomez.new_wallet("BTC", "1Q96KC19qeGnycnmNrSiM7YdwdhJBeemfQ")
gomez.new_wallet("ETH", "0xBC10C2B1796254F95A731Ab199e87f01842b4c3F", "Trading")
gomez.new_wallet("ETH", "0x209AC83370Cc321fa76210B07D60Ec1A217fc17F", "Storage")
gomez.new_wallet("LTC", "LhULyWpJAqC76TqPgqtaMBSGgASAHzc1ru")
gomez.new_wallet("NEO", "AV7t59enYBkFgimNrevUNMPvH7JyixsJvW")
gomez.new_wallet("ARK", "AUdMd8WyRVaiR7GkUJobcSJsZZnqir94Fi")
gomez.new_wallet("IOTA", "IDRJSLNUTNM9JITG9MINMHPGCXEJDSTOBUQHNOHPOJCRSNWKXOKYZNBUKS9ZUSHPSCINJOQERNUKIOUTX9GMXUHKDD")

nestor.new_account("Bittrex", "5f2903316cd14cfe90769d230b645525", "")
nestor.new_wallet("BTC", "12mpEeDQrM2EvrYTvm1V3eUwh4vK6RggQ4")
nestor.new_wallet("ETH", "0x362Ba688DFCd8fc154070b7395688a80f7B075F7", "Trading")
nestor.new_wallet("ETH", "0x18378BC5b32d2F20AEd7e3cb51b27f580DCBeC2A", "Storage")
nestor.new_wallet("LTC", "LLNPXJLiz5FkxpAthv6Xu5GdDvdpHQp34R")
nestor.new_wallet("NEO", "AbDXe6m22DHhLbtNnww7512fG97hKp8tAt")
nestor.new_wallet("ARK", "AZvHeJeXpAp2ZfuUmvqHrAyqdaBth11vAY")
nestor.new_wallet("IOTA", "U9TWNUAHEUEUQYPMGRWMDU9ASNDKKUIRRMQKKFXFRGJZGQMCFDS9UTNF9RTUOLQ9NGIQPXKDQIYQQDXQYUGQTAAAFD")

cristy.new_account("Bittrex", "81b40627fa1a43dd8d3345c6b52e35af", "b8bb0df2accf419fbcaac834cd3b6e1c")
cristy.new_wallet("BTC", "1J9VY7dXva6tEo43sc332QhSyFQb18KNXE")
cristy.new_wallet("ETH", "0xed84DD113F0DCf41F279512Ad0205c8274C297AF", "Trading")
cristy.new_wallet("ETH", "0xB1039e770673A94556B5D1A012ef5d9deE3d4780", "Storage")
cristy.new_wallet("LTC", "Lgpdt3hvPRkJxwPfk3Sg5psxmaLSo2WWG8")
cristy.new_wallet("NEO", "AbFaYbRf32uSkFHpVboFwBQHSQDJwQa1MK")
cristy.new_wallet("ARK", "AUWJcxGSrzq4x73oRgSYcE6YTqSRXH8bSd")
cristy.new_wallet("IOTA", "GQJQFOKHTAEIXICIPXCVLRTJSJSXBEN9XFMNDQOMDCCWYLGBH9VOYTUBSLUPBHLMXPMHWFFEFZ9HADVCDFOLEAETYD")

jama.new_account("Bittrex", "cdac2fb8744d46b285a284357874a1e6", "465927e2e4a244da8be1e223747d74bb")
jama.new_wallet("BTC", "13chLcExDqwnPCki1eXzBuuoR21Cx4dp61")
jama.new_wallet("ETH", "0xdfe375d51B8D5d116fe12FaD80D3C581d0Cf0320", "Trading")
jama.new_wallet("ETH", "0xB7B0684a480DB369d613f2A42c62c3e5d04ED629", "Storage")
jama.new_wallet("LTC", "LM5KoLZ1mSL6XYPKSnH33to1djsppSK73E")
jama.new_wallet("NEO", "AKwBU9s1UWZmrnL4daWyd4oKxcS3afPuQc")
jama.new_wallet("ARK", "AagcjZGK9sCvbAg8TskP5apfpBKDfCytt8")
jama.new_wallet("IOTA", "LLVLRBNFOFDMDLVUBNHPBKFHMQNH9CELXSGIGXKFDHZFXEUFVGCOLU9JQIACSCDZTPUDOEPBONBORKXJBLTQZFUGRX")
jama.new_wallet("IOTA", "SC9QYHZCHEBIBDVNBBYTZUSIHIPMQGDLQUFZU99BQQUOPE9VYRBARXMOGFXCBIJUSYC9NCRAAQKYKUVTXKDOSYWZZD")

print("DONE.")
