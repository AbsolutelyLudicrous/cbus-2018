# Here's your guide to Not Fucking It Up(tm)

# (A crash course on the FAMP stack)

---

## Stuff you'll learn:

+ Basic POSIX, Unix, and BSD

+ The filesystem hierarchy (the important bits)

+ Getting the FAMP stack running smoothly

+ Website workflow (no, you're not pushing directly to prod)

+ How the hell this thing gets hosted

---

## POSIX, Unix, BSD for dummies

You have been dropped into bare POSIX shell.
POSIX shell, `sh`, is not `bash` or `zsh` or 

---

## The (important bits of the) filesystem hierarchy

### `man hier`

Unix has no `C:`, `D:`, `E:`, etc.
The equivalent is `/`, and there is *only* `/`.

(`/` is pronounced as "root")

`/` is the top level directory in the filesystem.
All other directories exist under it.

## TODO

---

## Hosting, DNS, domain names

It turns out that it's really hard to get a human-readable address.

### Who does our hosting?

Linode.
I have two linodes through them.
A 1024 running `cutie-computie` and a 2048 running my personal server.

Linode is a cloud hosting service.
They just provide a server and an IP address.

(We can do our DNS through them, but it's finicky and I hate it.)

### DNS - Who does it, if not Linode?


