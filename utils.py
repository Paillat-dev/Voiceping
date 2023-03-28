import json
import os
from config import data_dir

async def add_channel_roles(channel, member):
    '''Different cases:
    1. The channel has no roles in the json file:
        - Create a new role
        - Add the role to the json file
        - Add to the member the role
        - Return the role
    2. The channel has a role in the json file:
        - Add to the member the role
        - Return the role
    '''
    role = None
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    if not os.path.exists(os.path.join(data_dir, f'{channel.guild.id}.json')):
        with open(os.path.join(data_dir, f'{channel.guild.id}.json'), 'w') as f:
            json.dump({}, f)
    with open(os.path.join(data_dir, f'{channel.guild.id}.json'), 'r') as f:
        data = json.load(f)
    if str(channel.id) not in data:
        "Case 1"
        role = await channel.guild.create_role(name=channel.name)
        data[str(channel.id)] = role.id
        with open(os.path.join(data_dir, f'{channel.guild.id}.json'), 'w') as f:
            json.dump(data, f)
            f.close()
    else:
        "Case 2"
        role = channel.guild.get_role(data[str(channel.id)])
    await member.add_roles(role)

async def remove_channel_roles(channel, member):
    '''Different cases:
    1. The channel has no roles in the json file:
        - Do nothing
    2. The channel has a role in the json file:
        - Remove the role from the member
        - If the role is not used by any other member, delete the role from the server and the json file
    '''
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    if not os.path.exists(os.path.join(data_dir, f'{channel.guild.id}.json')):
        with open(os.path.join(data_dir, f'{channel.guild.id}.json'), 'w') as f:
            json.dump({}, f)
    with open(os.path.join(data_dir, f'{channel.guild.id}.json'), 'r') as f:
        data = json.load(f)
    if str(channel.id) in data:
        "Case 2"
        role = channel.guild.get_role(data[str(channel.id)])
        await member.remove_roles(role)
        if role.members == []:
            await role.delete()
            del data[str(channel.id)]
            with open(os.path.join(data_dir, f'{channel.guild.id}.json'), 'w') as f:
                json.dump(data, f)
                f.close()