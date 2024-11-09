# Extract Kundli

This project provides a tool to extract Kundli information from images using anthropic API

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