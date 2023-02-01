# mc-google-lang
Google translated minecraft  

## About  

I already did the exact same thing many years ago but I thought it would be fun to refactor everything and do it again.  
This script reads in a normal minecraft language file and translates all entries using the amazing power of google translate.  
This Repo contains a minecraft resource pack with a language file. It is German.  
A path of different languages can be supplied using arguments.  

## Usage  

```
usage: ./main.py [OPTIONS]  
required options:  
--input     <file> : Input language file to translate  
--output    <file> : Output language file  

optional options:  
--lang-list <list> : List of languages to use (default: "fr, ch-zn, la, ru")  
--lang-out  <lang> : Final output language  
--timeout  <delay> : Seconds between translations  
```

## Future  

TODO:  
- [ ] Some garbage is still not cleaned up after translation
- [ ] Google messes with my way of preventing "%s" from being translated...
- [ ] Parse entire file afterwards and fix obvious issues  

## Demo  

The language file supplied in the resourrce pack folder was generated using this path: "fr ch-zn la ru fr".  
Choosing french as the first language turned out to be funny as the english word "chat" means "cat" in french so that caused some weirdness...  
Some of my personal favorites for the german translation:  
| Original | Translated | Translated to english |
| --- | :-: | --: |
| Elder Guardian Spawn Egg | Seniorenei | Senioregg |
| Donkey Spawn Egg | Der Eierel | ? |
| Wolf Spawn Egg | Die Lumpus - Frau erzeugt Eier | The Lumpus - Woman produces eggs |
| Frostwalker | Der Gefrierschrank | The refrigerator |
| Swift Sneak | Kirschenarrangement | Cherryarrangement |
| Leaping | Wahnsinn | Insanity |
| Awkward Potion | Dummes Hartnäckiges Getränk | Stupid stubborn drink |
| Water | FeU | FeU (Some Uranium-Iron compound?) |
| Poison | Dichtergift | Poetrypoison |
| Infested Cobblestone | Sex infiziert | sex infested |
| Dropper | Vergewaltigen | To rape |
| Stripped Oak Log | Nackte Zeitung | Naked Newspaper |
| Stripped Oak Wood | Nackte Eiche | Naked Oak |
| Redstone Torch | Den Gummi, den wir machen | The rubber we make |
