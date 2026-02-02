import os


def rename_pdf_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder path not found.")
        return

    files = os.listdir(folder_path)
    pdf_files = [f for f in files if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("⚠️ No PDF files found.")
        return

    for index, file in enumerate(pdf_files, start=1):
        old_path = os.path.join(folder_path, file)
        new_name = f"Document_{index}.pdf"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

    print("✅ All PDF files renamed successfully!")
