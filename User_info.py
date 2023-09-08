@Raiden.tree.command(name='about', description='To see any person info frome server') # Replace "Raiden" with the name of your bot and if haven't gave any namee to your bot just put bot there 
async def about(context: discord.Interaction, person: discord.Member):
  
  time = person.joined_at
  t = time.strftime("**%d:%m:%Y, Time: %H:%M:%S**") 
  authorid = person.id
  author_url = f'https://discord.com/users/{authorid}'
  list = []
  for key in person._user._to_minimal_user_json(): 
    list.append(f'**『 {key} : {person._user._to_minimal_user_json()[key]} 』** ') 
    
  em = discord.Embed(description=f'> {list[0]}\n\n> {list[4]}\n\n> **『 avatar : {person.avatar} 』**\n\n> {list[1]}\n\n> **『 Joined at : {t} 』**\n\n> {list[5]}')
  em.set_thumbnail(url= person._user.avatar)
  em.set_image(url='https://media.discordapp.net/attachments/1010954815192440935/1125824654033035304/Tumblr_l_108190584885447.gif?width=737&height=8')
  em.set_author(name= person._user.name, url= author_url, icon_url= person.avatar)
  await context.channel.send(embed= em)
  await context.response.send_message('> ***Process finished ^_^***', ephemeral=True) 
