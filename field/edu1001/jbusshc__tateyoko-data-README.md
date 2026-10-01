# Tateyoko · datos

Diccionario de la app [Tateyoko](https://github.com/jbusshc) (crucigramas de kana). Este repositorio solo contiene datos, publicados como releases; el código de la app no es público.

## Qué hay en cada release

| Archivo | Qué es |
|---|---|
| `tateyoko-dict.sqlite.gz` | Diccionario precompilado (SQLite comprimido con gzip) |
| `dict-manifest.json` | Versión, fecha de JMdict, tamaños y SHA-256 del paquete |
| `NOTICE.md`, `LICENSE-DATA.md` | Atribución y licencia |

Se regenera cada mes desde la última versión de JMdict. La app descarga siempre de `releases/latest/download/`.

## Licencia

This app uses the JMdict/EDICT and KANJIDIC dictionary files. These files are the property of the Electronic Dictionary Research and Development Group, and are used in conformance with the Group's licence.

El diccionario es una obra derivada de [JMdict](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project) y se distribuye bajo [Creative Commons Attribution-ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/), como exige la [licencia de EDRDG](https://www.edrdg.org/edrdg/licence.html). Contiene solo los componentes japonés e inglés de JMdict.
