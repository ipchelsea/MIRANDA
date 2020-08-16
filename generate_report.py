import os
from typing import Dict, AnyStr
import uuid

from fpdf import FPDF

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MIRANDA_LOGO_PATH = os.path.join(BASE_DIR, 'miranda_logo.png')


class ReportPDF(FPDF):
    def header(self):
        # Logo
        self.image(MIRANDA_LOGO_PATH, h=20)

    # Page footer
    # def footer(self):
    #     self.set_font('Times', '', 10)
    #
    #     self.set_xy(-60, -20)
    #     self.cell(w=50, h=10, txt='Sample Footer Text')


class ReportModel(object):
    def __init__(self, driver_name,
                 location, start_time, end_time,
                 transcript, links: Dict[AnyStr, AnyStr] = None,
                 officer_name=None, officer_id=None):
        self.driver_name = driver_name
        self.location = location
        self.start_time = start_time
        self.end_time = end_time
        self.transcript = transcript
        self.links = links
        self.officer_name = officer_name
        self.officer_id = officer_id


def generate_pdf(output_folder, model: ReportModel):
    """
    Creates the pdf and returns the full path to where the PDF was written to
    """
    # /////////
    # Setup PDF
    # /////////

    pdf = ReportPDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    # Writing data to cells on the page using nifty new python fprint

    pdf.line(10, 35, 200, 35)

    # adjust position to style the Title
    pdf.set_font('Times', 'I', 12)  # Times New Roman, Bold, 15
    pdf.set_xy(x=12, y=40)
    pdf.cell(w=0, h=10, txt='PROJECT MIRANDA :: After-Incident Report', border=0, ln=0)

    pdf.line(10, 55, 200, 55)

    pdf.set_xy(x=12, y=58)
    pdf.set_font('Courier', '', 10)
    pdf.ln(8)
    pdf.cell(w=10, h=5, txt=f'Driver name:      {model.driver_name}')
    pdf.ln(8)
    pdf.cell(w=10, h=5, txt=f'Location:         {model.location}')
    pdf.ln(8)
    pdf.cell(w=10, h=5, txt=f'Start time:       {model.start_time}')
    pdf.ln(8)
    pdf.cell(w=10, h=5, txt=f'End time:         {model.end_time}')
    pdf.ln(16)
    pdf.cell(w=10, h=5, txt=f'Transcript:')
    pdf.ln(8)
    pdf.multi_cell(w=190, h=5, txt=model.transcript, border=1)
    pdf.ln(8)

    output_filename = os.path.join(output_folder, f'report-{uuid.uuid4().__str__()[:6]}.pdf')
    pdf.output(output_filename, dest='F')

    print(f'PDF written to {output_filename}')
