# mc-google-lang
Google translated minecraft  

## About  

I already did the exact same thing many years ago but I thought it would be fun to refactor everything and do it again.  
This script reads in a normal minecraft language file and translates all entries using the amazing power of google translate.  
A path of different languages can be supplied using arguments.  

## Usage  

```
usage: ./main.py [OPTIONS]  
required options:  
--input     <file> : Input language file to translate  
--output    <file> : Output language file  

optional options:  
--lang-list <list> : List of languages to use (default: "ar, la, ja, zh-cn, de")  
--lang-out  <lang> : Final output language  
--timeout  <delay> : Seconds between translations  
```

## Future  

TODO:  
- [ ] Some garbage is still not cleaned up after translation
- [ ] Google messes with my way of preventing "%s" from being translated...
- [ ] Parse entire file afterwards and fix obvious issues  



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
