"""Generate the sample files for testing the agent and print the answers it should find.

- statement.pdf: a fictional bank statement. Besides the transaction table, it contains data
  that isn't part of the page text: document metadata, form fields, a comment on one
  transaction and an embedded CSV attachment.
- ledger.xlsx: the company's ledger for the same month, with a few planted differences.

All names and amounts are fictional. Every run produces the same transactions and differences.

Usage: python generate.py [--output-dir DIR]
"""
import argparse
import io
import random
from datetime import date, timedelta
from pathlib import Path

from openpyxl import Workbook
from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

VENDORS = [
    "Blue Harbor Logistics", "Northgate Office Supply", "Summit Cloud Hosting", "Riverbend Catering",
    "Copperline Electric", "Maple Street Rentals", "Brightpath Training", "Ironwood Freight",
]
TRANSACTION_COUNT = 60
ROWS_PER_PAGE = 30


def make_transactions(rng: random.Random) -> list[dict]:
    day = date(2026, 3, 1)
    transactions = []
    for index in range(TRANSACTION_COUNT):
        day += timedelta(days=rng.choice([0, 0, 1]))
        transactions.append({
            "date": day.isoformat(),
            "reference": f"TX-{10400 + index}",
            "description": rng.choice(VENDORS),
            "amount": round(rng.uniform(-4800, -25), 2) if rng.random() < 0.85 else round(rng.uniform(500, 9000), 2),
        })
    return transactions


def plant_differences(rng: random.Random, statement: list[dict]) -> tuple[list[dict], dict]:
    """Copy the statement into a ledger, then change it in ways the agent should find."""
    picks = rng.sample(range(len(statement)), 5)
    missing = [statement[i]["reference"] for i in picks[:3]]
    disputed = missing[0]  # The PDF comment explains why this one isn't in the ledger.
    adjusted, mismatched = statement[picks[3]]["reference"], statement[picks[4]]["reference"]

    ledger = [dict(row) for row in statement if row["reference"] not in missing]
    for row in ledger:
        if row["reference"] == adjusted:
            # The bank corrected this amount after the statement was printed; the CSV attachment
            # in the PDF has the corrected amount, which matches the ledger.
            row["original"], row["amount"] = row["amount"], round(row["amount"] - 120.00, 2)
        if row["reference"] == mismatched:
            row["original"], row["amount"] = row["amount"], round(row["amount"] + 45.50, 2)
    extra = {"date": "2026-03-31", "reference": "TX-19999", "description": "Bank fee (manual entry)", "amount": -35.00}
    ledger.append(extra)

    adjusted_row = next(row for row in ledger if row["reference"] == adjusted)
    return ledger, {
        "disputed": disputed, "missing": missing, "adjusted": adjusted_row, "mismatched": mismatched,
        "extra": extra["reference"],
    }


def write_statement(path: Path, statement: list[dict], answers: dict) -> None:
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setTitle("Account statement, March 2026")
    pdf.setAuthor("Example Community Bank")
    pdf.setSubject("Business checking account ending 4821")

    for page_start in range(0, len(statement), ROWS_PER_PAGE):
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(50, 750, "Example Community Bank: Account statement, March 2026")
        pdf.setFont("Helvetica-Bold", 9)
        for x, header in zip((50, 130, 210, 480), ("Date", "Reference", "Description", "Amount (USD)")):
            pdf.drawString(x, 720, header)
        pdf.setFont("Helvetica", 9)
        y = 705
        for row in statement[page_start:page_start + ROWS_PER_PAGE]:
            pdf.drawString(50, y, row["date"])
            pdf.drawString(130, y, row["reference"])
            pdf.drawString(210, y, row["description"])
            pdf.drawRightString(550, y, f"{row['amount']:,.2f}")
            if row["reference"] == answers["disputed"]:
                pdf.textAnnotation(
                    "Customer disputes this charge. Do not book it until the dispute is resolved.",
                    Rect=(555, y - 2, 575, y + 10),
                )
            y -= 20
        if page_start + ROWS_PER_PAGE >= len(statement):
            pdf.drawString(50, y - 20, "Review")
            form = pdf.acroForm
            form.textfield(name="prepared_by", value="J. Rivera", x=50, y=y - 50, width=200, height=18)
            form.textfield(name="reviewed_by", value="A. Chen", x=260, y=y - 50, width=200, height=18)
            form.checkbox(name="approved", checked=False, x=470, y=y - 50, size=18)
            form.textfield(
                name="reviewer_notes", value="Hold approval until the TX-19999 bank fee is confirmed.",
                x=50, y=y - 80, width=410, height=18,
            )
        pdf.showPage()
    pdf.save()

    # reportlab can't embed files, so pypdf adds the attachment and custom metadata.
    writer = PdfWriter(clone_from=PdfReader(buffer))
    adjusted = answers["adjusted"]
    writer.add_attachment(
        "adjustments.csv",
        f"reference,original_amount,corrected_amount,reason\n"
        f"{adjusted['reference']},{adjusted['original']:.2f},{adjusted['amount']:.2f},Corrected by the bank after the statement date\n".encode(),
    )
    writer.add_metadata({"/StatementId": "ECB-2026-03-4821"})
    writer.write(path)


def write_ledger(path: Path, ledger: list[dict]) -> None:
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Ledger March 2026"
    sheet.append(["Date", "Reference", "Description", "Amount"])
    for row in ledger:
        sheet.append([date.fromisoformat(row["date"]), row["reference"], row["description"], row["amount"]])
    workbook.save(path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent / "output")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    rng = random.Random(2026)
    statement = make_transactions(rng)
    ledger, answers = plant_differences(rng, statement)
    write_statement(args.output_dir / "statement.pdf", statement, answers)
    write_ledger(args.output_dir / "ledger.xlsx", ledger)

    mismatched = next(row for row in ledger if row["reference"] == answers["mismatched"])
    adjusted = answers["adjusted"]
    print(f"Wrote statement.pdf and ledger.xlsx to {args.output_dir}\n")
    print("Expected findings:")
    print(f"- On the statement but not in the ledger: {', '.join(answers['missing'])}")
    print(f"  ({answers['disputed']} has a PDF comment saying the charge is disputed)")
    print(f"- In the ledger but not on the statement: {answers['extra']}")
    print(f"- Amount differs, explained by the adjustments.csv attachment: {adjusted['reference']} "
          f"(statement {adjusted['original']:.2f}, ledger {adjusted['amount']:.2f})")
    print(f"- Amount differs, unexplained: {mismatched['reference']} "
          f"(statement {mismatched['original']:.2f}, ledger {mismatched['amount']:.2f})")
    print("- Form fields: prepared_by=J. Rivera, reviewed_by=A. Chen, approved=unchecked,")
    print("  reviewer_notes=Hold approval until the TX-19999 bank fee is confirmed.")
    print("- Metadata: author Example Community Bank, custom /StatementId ECB-2026-03-4821")


if __name__ == "__main__":
    main()
