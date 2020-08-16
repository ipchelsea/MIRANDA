from generate_report import generate_pdf, ReportModel


if __name__ == '__main__':
    with open('transcript.txt') as f:
        transcript = f.read()

    generate_pdf(
        output_folder='.',
        model=ReportModel(
            driver_name='Pramod Kotipalli',
            location='123 Sesame Street, Elmoville',
            start_time='Aug 15, 2020 at 7pm',
            end_time='Aug 15, 2020 at 7:15pm',
            transcript=transcript,
        )
    )
