import sys
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def create_pdf(image_folder, output_file):
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4
    margin_x = 50
    margin_y = 50
    img_w = (width - 2 * margin_x) / 3
    img_h = (height - 2 * margin_y - 50) / 2

    folder_name = os.path.basename(os.path.normpath(image_folder))

    images = [os.path.join(image_folder, f) for f in os.listdir(image_folder)
              if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    images.sort()

    for i, image_path in enumerate(images):
        if i % 6 == 0:
            if i > 0:
                c.showPage()
            c.setFont("Helvetica-Bold", 14)
            c.drawCentredString(width/2, height - 30, folder_name)

        col = (i % 6) % 3
        row = (i % 6) // 3

        x = margin_x + col * img_w
        y = height - margin_y - 50 - (row + 1) * img_h

        img = ImageReader(image_path)
        iw, ih = img.getSize()
        scale = min(img_w / iw, img_h / ih)
        new_w, new_h = iw * scale, ih * scale

        c.drawImage(img, x + (img_w - new_w) / 2, y + (img_h - new_h) / 2,
                    new_w, new_h, preserveAspectRatio=True, anchor='c')

    c.save()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder = sys.argv[1]
        if os.path.isdir(folder):
            create_pdf(folder, "Photo_Report.pdf")
        else:
            print("Invalid folder path")
    else:
        print("Usage: photo_report.exe <image_folder>")
