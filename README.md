# Extract Kundli

This project provides a tool to extract Kundli information from images using anthropic API  
Verified with Real Examples from photos taken from camera

## Requirements

Ensure you have the following packages installed:

```requirements
instructor
anthropic
```

You can install these packages using pip:

```sh
pip install -r requirements.txt
```

## Environmental Variable

Before running the `extractor_anthropic.py` script, ensure you set the `ANTHROPIC_API_KEY` environment variable. You can do this by running the following command in your terminal:

```sh
export ANTHROPIC_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

## Usage

To run the script, use the following command:

```sh
python extractor_anthropic.py /path/to/your/image.png
```

## Sample Output

`python extractor_anthropic.py "imgs/img_4.png"`
```
Kundli Center Text:
20-8-1945 Monday
11-31 p.m. (Actual I.S.T)
12-31 A.M. (War-Time)
Place : 12-30 N 75 E
Ayanamsa : 22-59 (KP)
Balance Dasa at Birth
Sun Dasa
4Y-11M-21D

Aries/Mesha:
XII 23-09

Taurus/Vrishaba:
I.Asc. 27-30

Gemini/Mithun:
Uranus 24-00
II 25-32
Mars 25-52

Cancer/Karka:
Rahu 13-33
III 21-28
Ven. 25-37
Sat. 26-59

Leo/Simha:
IV 18-29

Virgo/Kanya:
Merc. (R) 4-05
Sun 4-20
V 19-02

Libra/Thula:
Jup. 6-05
Nep. 1-1-48
For. 22-08
VI 23-09

Scorpio/Vrishchak:
VII 27-30

Sagittarius/Dhanu:
VIII 25-32

Capricorn/Makar:
Moon 28-56-40
IX 21-28
Kethu 13-33

Aquarius/Kumba:
X 18-29

Pisces/Meena:
XI 19-02
```
## Images

The project contains images used for illustration purposes, located in the `imgs/` directory.

## Attribution

Images have been taken from the book:
```
ASTRO SECRETS & KRISHNAMURTI PADHDHATI [PART - III]  
Edited by K. SUBRAMANIAM S/o, Sothida Mannan, Jyotish Marthand  
Late Prof. K.S. KRISHNAMURTI
```

## License

Please add your project's license information here.