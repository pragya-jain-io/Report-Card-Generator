# Report Card Generator

This Python script generates a report card in PDF format for students. The script utilizes the `fpdf` library to create a structured PDF document with student details and scores for various subjects. It also includes emojis to visually represent the performance.

## Features

- Customizable student details and subject scores.
- Generates a professional-looking report card in PDF format.
- Includes a score bar and emojis for each subject to visually represent the scores.

## Prerequisites

- Python 3.x
- `fpdf` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/report-card-generator.git
    ```

2. Navigate to the project directory:
    ```sh
    cd report-card-generator
    ```

3. Install the required library:
    ```sh
    pip install fpdf
    ```

## Usage

1. Open the `report_card_generator.py` file.
2. Modify the `student_details`, `subjects`, and `subject_scores` dictionaries to suit your needs.
3. Ensure the emoji images are available in the `emojis` directory.
4. Run the script:
    ```sh
    python report_card_generator.py
    ```

The generated report card PDF will be saved in the current directory.

## Example

Here is an example of how to customize the student details and scores:

```python
student_details = {
    'Name': 'John Doe',
    'Class': '10',
    'Roll Number': '23',
    'School': 'ABC High School'
}

subjects = [
    ('Mathematics', 'Excellent understanding of mathematical concepts.'),
    ('Science', 'Demonstrates a solid grasp of scientific principles.'),
    ('History', 'Shows a keen interest and knowledge in historical events.')
]

subject_scores = {
    'Mathematics': 95,
    'Science': 88,
    'History': 90
}
