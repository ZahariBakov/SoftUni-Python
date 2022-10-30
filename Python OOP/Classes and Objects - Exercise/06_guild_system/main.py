from project.player import Player
from project.guild import Guild

player = Player("George", 50, 100)
second_player = Player("Peter", 30, 120)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(second_player.add_skill("Shield Break", 20))
print(guild.guild_info())
second_guild = Guild("HVT")
print(player.add_skill("New Attack", 50))
print(second_guild.assign_player(player))
print(second_player.player_info())
print(second_guild.assign_player(second_player))
print(second_guild.assign_player(second_player))
print(second_guild.guild_info())
print(guild.guild_info())
