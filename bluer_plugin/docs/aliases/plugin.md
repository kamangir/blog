# aliases: plugin

## leaf

```bash
@plugin \
	leaf \
	[dryrun,upload] \
	[.|<object-name>] \
	[--<keyword-1> <value-1>] \
	[--<keyword-2> <value-2>]
 . bluer-plugin leaf <object-name>.
```

## node

```bash
@plugin \
	node \
	[dryrun] \
	[.|<object-name>]
 . bluer-plugin node <object-name>.
@plugin \
	node \
	leaf \
	[~download,dryrun,~upload] \
	[.|<object-name-1>] \
	[-|<object-name-2>] \
	[--<keyword-1> <value-1>] \
	[--<keyword-2> <value-2>]
 . <object-name-1> -bluer-plugin node leaf-> <object-name-2>.
```

## task

```bash
@plugin \
	task \
	[dryrun,<thing-1+thing-2>|all] \
	[.|<object-name>]
 . task -things-> <object-name>.
```
