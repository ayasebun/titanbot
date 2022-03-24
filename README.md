###### Another dumb discord bot

## Justifying titanbot's existence
titanbot was created with the intention of teasing my friends. Please note that this is extremely ameteur code.

## Hopefully helpful information to someone looking for discord bot examples
Some discord bot examples may ask that you toss your token directly into the bot. Through the use of `configparser`, we're able to get away with keeping a `settings.ini` file instead. It will look as so:

```
[discord]
token = ENTIRETOKENHERE
```

You will see that it is loaded at the end of the script with:

```
client.run(config['discord']['token'])
```

While some emote IDs are hardcoded, ( to be fixed later, maybe. I'm not sure yet) he's intended to read from a listing of about 100+ emotes. There's a special list of titans called `teetans` that we won't talk about, though its all the same.

The emote list will look something along the lines of this:

```
<:emotename:00000000000000000000>
<:emotename1:00000000000000000001>
<:emotename2:00000000000000000002>
<a:animatedemote1:00000000000000000003>
<a:animatedemote2:00000000000000000004>
```

With each emote being on its own line, `read().splitlines()` is able to parse and use them as needed.

While this bot is nothing special, I need to prove to future employers that I'm capable of using git to some degree. Thank you for taking out the time to peek at titanbot. He brings me joy.
