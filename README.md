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

`python extractor_anthropic.py "imgs/img_1.png"`
```
Kundli Center Text:


1st House:
Sat. 23-17
VIII 6-21

2nd House:
IX 7-21
Ura 22-57

3rd House:
Kethu 2-40
X 8-21
Merc 17-8
Sun 28-37

4th House:
XI 8-38
Mars 11-11

5th House:
Venus 0-35
XII 8-21

6th House:
Asc 7-55
Nept 25-31

7th House:
II 6-21

8th House:
III 7-21

9th House:
IV 8-21
Rahu 2-40

10th House:
V 8-38
Moon 0-58

11th House:
VI 8-21

12th House:
Fort 10-16
Jup 9-14
VII 7-55
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