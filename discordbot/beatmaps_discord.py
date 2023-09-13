import backend.osuapi.beatmaps as beatmaps
import discord


def getuserscore(access_token, arg1, arg2, arg3=None, arg4=None):
    
    data = beatmaps.getUserBeatmapScore(access_token, arg1, arg2, arg3, arg4)
    
    beatmap_data = beatmaps.getBeatmap(access_token, arg1)
    
    embed = discord.Embed(
    title="User Score Information",
    description=f"Position: {data['position']}",
    color=discord.Color.blue()
)
    score_data = data['score']
    embed.add_field(name="Accuracy", value=score_data['accuracy'], inline=True)
    embed.add_field(name="Best ID", value=score_data['best_id'], inline=True)
    embed.add_field(name="Mods", value=score_data['mods'], inline=False)
    # ... Add more fields as needed ...

    # Set the user's avatar as the thumbnail
    embed.set_thumbnail(url=beatmap_data['beatmapset']['covers']['list@2x'])

    # Set the author as the user's username and avatar
    embed.set_author(name=score_data['user']['username'], icon_url=score_data['user']['avatar_url'])
    
    print(data)
    
    return embed
    
   
    