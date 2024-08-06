from fpdf import FPDF

# Data for sections
subjects = [
    ('Mathematics', 'Excellent understanding of mathematical concepts.'),
    ('Science', 'Demonstrates a solid grasp of scientific principles.'),
    ('History', 'Shows a keen interest and knowledge in historical events.')
]

student_details = {
    'Name': 'John Doe',
    'Class': '10',
    'Roll Number': '23',
    'School': 'ABC High School'
}

subject_scores = {
    'Mathematics': 95,
    'Science': 88,
    'History': 90
}

emojis = [
    'emojis/Very Negative.png',
    'emojis/Negative.png',
    'emojis/Neutral.png',
    'emojis/Positive.png',
    'emojis/Very Positive.png'
]

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 18)
        self.cell(0, 10, 'Report Card', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    def add_titles(self, string, y):
        self.set_font('Arial', 'B', 16)
        self.set_x(10)
        self.set_y(y)
        self.cell(0, 10, string, 0, 1, 'L')
    
    def add_student_details(self, details, y):
        self.set_font('Arial', '', 12)
        for key, value in details.items():
            self.set_xy(10, y)
            self.cell(0, 10, f'{key}: {value}', 0, 1, 'L')
            y += 10
        return y + 10
    
    def add_subjects(self, subjects, y, scores):
        
        for subject, description in subjects:
            self.set_font('Arial', 'B', 12)
            self.set_xy(10, y)
            self.cell(0, 10, subject, 0, 1, 'L')
            self.set_font('Arial', '', 10)
            self.set_xy(10, y + 10)
            self.multi_cell(130, 5, description, 0)
            y += 20
            self.draw_score_line(150, y - 10, scores[subject])
            y += 10
            self.add_emojis(150, y)
            y += 15
        return y + 10
    
    def draw_score_line(self, x, y, score, max_score=100):
        bar_width = 50
        bar_height = 2
        filled_width = (score / max_score) * bar_width
        
        self.set_fill_color(220, 220, 220)
        self.rect(x, y, bar_width, bar_height, 'F')
        
        self.set_fill_color(0, 200, 0)
        self.rect(x, y, filled_width, bar_height, 'F')
        
        self.set_xy(x, y+5)
        self.set_font('Arial', '', 12)
        self.cell(bar_width, 10, f'{score}/{max_score}', 0, 0, 'C')
    
    def add_emojis(self, x, y):
        emoji_size = (8, 8)  # Width and height of emojis
        spacing = 5  # Space between emojis

        # Calculate total width of all emojis and spacing
        total_emoji_width = len(emojis) * emoji_size[0] + (len(emojis) - 1) * spacing

        # Center emojis horizontally on the bar
        current_x = x + (50 - total_emoji_width) / 2
        for emoji_path in emojis:
            self.image(emoji_path, current_x, y-23, *emoji_size)
            current_x += emoji_size[0] + spacing

def generate_report_card(student_details, subjects, scores, filename):
    pdf = PDF()
    pdf.add_page()
    pdf.set_title('Report Card')
    
    current_y = pdf.add_student_details(student_details, 30)
    current_y = pdf.add_subjects(subjects, current_y, scores)

    pdf.output(f'./{filename}.pdf')
    print("Report card PDF created successfully!")

generate_report_card(student_details, subjects, subject_scores, 'Report_Card')
