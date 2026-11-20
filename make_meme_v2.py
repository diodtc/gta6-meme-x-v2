"""Build the v2 meme for make.fun gta6-meme-x-01.

The user supplied the base picture (a GTA 6 purchase-receipt meme, 1254x1254).
The bounty requires the picture to show make.fun's ghost / logo / name
recognisably at 480px, and this picture has none, so the real make.fun ghost
mark from the press kit is composited onto it as a sticker in the open pink
space at the bottom-left, clear of every line of text: it covers only the
decorative palm tree and a sliver of the COMING 2026 stamp's left border.

Output: meme.png (1254x1254) and meme-480.png (480px preview, to check the
ghost still reads at the size the house judges it).
"""

from PIL import Image, ImageDraw

BASE = "base.png"
GHOST = "ghost-mark.png"
OUT = "meme.png"
PREVIEW = "meme-480.png"

# Ghost sticker: 160px disc, top-left corner at (8, 1005) on the 1254 canvas.
# At 480px display that is ~61px across: the white ghost on magenta reads.
GHOST_SIZE = 160
GHOST_XY = (8, 1005)

base = Image.open(BASE).convert("RGB")
ghost = Image.open(GHOST).convert("RGBA")

if ghost.size != (GHOST_SIZE, GHOST_SIZE):
    ghost = ghost.resize((GHOST_SIZE, GHOST_SIZE), Image.LANCZOS)

# If the mark has no real transparency (a solid square), cut it to a disc.
alpha = ghost.getchannel("A")
corners = [alpha.getpixel(p) for p in [(0, 0), (GHOST_SIZE - 1, 0),
                                       (0, GHOST_SIZE - 1),
                                       (GHOST_SIZE - 1, GHOST_SIZE - 1)]]
if min(corners) > 250:
    mask = Image.new("L", (GHOST_SIZE, GHOST_SIZE), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, GHOST_SIZE - 1, GHOST_SIZE - 1], fill=255)
    ghost.putalpha(mask)

out = base.copy()
out.paste(ghost, GHOST_XY, ghost)
out.save(OUT, "PNG")
out.resize((480, 480), Image.LANCZOS).save(PREVIEW, "PNG")

print(f"{OUT}: {out.size}, {len(open(OUT, 'rb').read())} bytes")
print(f"{PREVIEW}: 480x480")
print(f"ghost sticker: {GHOST_SIZE}px at {GHOST_XY}")
