import base64
import instructor
from anthropic import Anthropic
from pydantic import BaseModel
import argparse


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


class Kundli(BaseModel):
    cell_1_1: str
    cell_1_2: str
    cell_1_3: str
    cell_1_4: str
    cell_2_1: str
    cell_2_4: str
    cell_3_1: str
    cell_3_4: str
    cell_4_1: str
    cell_4_2: str
    cell_4_3: str
    cell_4_4: str
    center_cell: str


def process_kundli(image_path):
    client = instructor.from_anthropic(Anthropic())
    base64_encoded_image = encode_image(image_path)
    # note that client.chat.completions.create will also work
    resp = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Extract information from the following astrological chart table image. The table has a specific 4x4 format with the following characteristics:\n\nStructure:\n- Total 13 distinct cells\n- 12 outer cells arranged in a 4x4 grid\n- 1 larger center cell (formed by merging the 4 center cells)\n- The center cell spans positions [(2,2),(2,3),(3,2),(3,3)]\n\nCell Positions Reference:\nRow 1: (1,1), (1,2), (1,3), (1,4)\nRow 2: (2,1), [center cell], (2,4)\nRow 3: (3,1), [center cell], (3,4)\nRow 4: (4,1), (4,2), (4,3), (4,4)\n\nRequirements:\n1. Extract text from each cell maintaining exact formatting and numbers\n2. Include all planetary positions, degrees, and astronomical notations\n3. For the center cell, preserve any:\n   - Questions or statements\n   - Dates\n   - Times\n   - Locations\n   - Coordinates\n4. Note any empty cells explicitly\n5. Maintain the original sequence of information within each cell\n6. Preserve all numerical values, including degrees, minutes, and seconds\n7. Keep all planetary symbols and their corresponding positions\n\nPlease format the output as:\n1st Cell (1,1): [content]\n2nd Cell (1,2): [content]\n[...]n12th Cell (4,4): [content]\nCenter Cell: [content]\n"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": f"{base64_encoded_image}"
                        }
                    }
                ]
            }
        ],
        response_model=Kundli,
    )

    assert isinstance(resp, Kundli)
    print(f"Kundli Center Text:\n{resp.center_cell}\n")
    print(f"1st House:\n{resp.cell_1_1}\n")
    print(f"2nd House:\n{resp.cell_1_2}\n")
    print(f"3rd House:\n{resp.cell_1_3}\n")
    print(f"4th House:\n{resp.cell_1_4}\n")
    print(f"5th House:\n{resp.cell_2_4}\n")
    print(f"6th House:\n{resp.cell_3_4}\n")
    print(f"7th House:\n{resp.cell_4_4}\n")
    print(f"8th House:\n{resp.cell_4_3}\n")
    print(f"9th House:\n{resp.cell_4_2}\n")
    print(f"10th House:\n{resp.cell_4_1}\n")
    print(f"11th House:\n{resp.cell_3_1}\n")
    print(f"12th House:\n{resp.cell_2_1}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process an astrological chart image.')
    parser.add_argument('image_path', type=str, help='The path to the astrological chart image')
    args = parser.parse_args()

    process_kundli(args.image_path)
