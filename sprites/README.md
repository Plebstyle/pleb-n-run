# Orange Pill Runner — Sprite-Assets

Hier kommen die PNG-Grafiken rein. Solange eine Datei fehlt, zeichnet das Spiel
automatisch die Vektor-Version als Fallback — es bricht also nie.

## Regeln für ALLE Sprites
- **Format:** PNG mit **transparentem Hintergrund** (kein weißer/farbiger Kasten!)
- **Blickrichtung:** Figur schaut nach **RECHTS**. Das Spiel spiegelt automatisch.
- **Kein Boden-Schatten** im Bild (das Spiel setzt die Figur selbst auf den Boden).
- Figur **füllt den Rahmen** möglichst aus, mittig.
- Wichtig: Bei den Animations-Frames (run1/run2, _1/_2) muss es **dieselbe Figur**
  in derselben Kleidung sein — nur die Pose ändert sich.

## Dateiliste (exakte Namen!) + empfohlene Größe (Seitenverhältnis zählt)

| Datei                | Größe (px)  | Was                                          |
|----------------------|-------------|----------------------------------------------|
| pleb_idle.png        | 256 × 384   | Pleb steht                                   |
| pleb_run1.png        | 256 × 384   | Pleb läuft, Pose A                           |
| pleb_run2.png        | 256 × 384   | Pleb läuft, Pose B                           |
| pleb_jump.png        | 256 × 384   | Pleb springt                                 |
| alt_1.png            | 240 × 320   | Altcoiner läuft, Pose A                      |
| alt_2.png            | 240 × 320   | Altcoiner läuft, Pose B                      |
| alt_pilled.png       | 240 × 320   | Altcoiner „orange-pilled" (bekehrt)          |
| fud_1.png            | 240 × 320   | FUDster läuft, Pose A                         |
| fud_2.png            | 240 × 320   | FUDster läuft, Pose B                         |
| fud_pilled.png       | 240 × 320   | FUDster bekehrt                               |
| boss_1.png           | 360 × 500   | Boss „Peter Shill" normal                     |
| boss_2.png           | 360 × 500   | Boss wütend (rote Laseraugen)                 |
| coin.png             | 128 × 128   | Bitcoin-Münze (Frontansicht)                  |
| pill.png             | 128 × 64    | Orange Pille (waagerecht)                      |
| laserpill.png        | 128 × 64    | Rot glühende Laser-Pille (waagerecht)         |
| powerup.png          | 128 × 128   | „Laser Eyes" Power-up Icon                     |

> Minimum zum Loslegen: **pleb_idle, alt_1, fud_1, boss_1, coin, pill** — der Rest
> fällt automatisch auf vorhandene Frames / Vektor zurück.

---

## KI-Prompts (für ChatGPT/DALL·E, Midjourney, etc.)

**Style-Zeile — bei JEDEM Prompt vorne anstellen** (sorgt für einheitlichen Look):

> `2D platformer game character sprite, bold clean vector illustration, thick dark
> outline, flat vibrant colors with simple cel-shading, full body, facing right,
> centered, plain transparent background, no ground shadow, Bitcoin meme / sticker
> art style, crisp ::`

### Pleb (Held)
- **pleb_idle:** `...young friendly "pleb" hero standing confidently, wearing a bright orange hoodie with a white Bitcoin ₿ logo on the chest, an orange beanie with a small ₿ patch, blue jeans, orange sneakers, holding a glowing orange-and-white pill capsule in one hand, slight grin`
- **pleb_run1 / pleb_run2:** `...the SAME orange-hoodie pleb hero running to the right, mid-stride [Pose A: left leg forward / Pose B: right leg forward], leaning slightly forward, holding the orange pill`
- **pleb_jump:** `...the SAME orange-hoodie pleb hero in a dynamic jump, legs tucked up, one arm raised`

### Altcoiner (Gegner)
- **alt_1 / alt_2:** `...a smug "shitcoiner" villain walking, flashy neon-cyan tracksuit, big gold chain necklace, backwards cap, oversized sunglasses, cocky open-mouth grin, holding a smartphone [two walk poses]`
- **alt_pilled:** `...the same character now "orange-pilled" and converted: glowing warm orange, happy peaceful smile, glowing Bitcoin ₿ symbols in the eyes, tiny orange party hat, holding a gold Bitcoin coin`

### FUDster (Gegner, Banker-Typ)
- **fud_1 / fud_2:** `...a greedy banker "FUD" villain walking, dark green money-suit, red tie, slicked-back hair, angry scowling greedy expression [two walk poses]`
- **fud_pilled:** `...the same banker now orange-pilled: glowing orange, relieved happy smile, Bitcoin ₿ eyes`

### Boss — „Peter Shill"
- **boss_1:** `...an arrogant tall banker BOSS villain, navy-blue power suit, red tie, bald head with grey hair on the sides, holding a golden briefcase with a $ sign, sneering condescending face, intimidating`
- **boss_2:** `...the SAME banker boss enraged, glowing red laser eyes shooting out, furious face, red aura`

### Items
- **coin:** `shiny gold Bitcoin coin, front view, embossed white ₿ symbol, glossy, thick outline, transparent background`
- **pill:** `a horizontal medicine capsule pill, one half bright orange one half white, glossy highlight, glowing, thick outline, transparent background`
- **laserpill:** `a horizontal medicine capsule pill glowing red-hot like energy, fiery, thick outline, transparent background`
- **powerup:** `a glowing red eye shooting a red laser beam ("laser eyes" power-up icon), comic style, thick outline, transparent background`

---

## Workflow-Tipp
1. Generiere zuerst **pleb_idle**. Wenn dir die Figur gefällt, sag der KI
   „same character, [neue Pose]" für die anderen Pleb-Frames — so bleibt sie konsistent.
2. PNG mit transparentem Hintergrund exportieren (bei DALL·E: „transparent background"
   in den Prompt; bei Midjourney v6: `--style raw` + Hintergrund später entfernen mit
   z.B. remove.bg).
3. Datei mit dem **exakten Namen** aus der Tabelle hier in diesen Ordner legen.
4. Im Browser Hard-Reload (Strg+F5) — die Figur erscheint sofort.
