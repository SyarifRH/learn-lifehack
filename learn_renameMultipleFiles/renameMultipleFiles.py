import os

folder_path = "learn_renameMultipleFiles\\files"
for index, filename in enumerate(os.listdir(folder_path)):
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, f"reportAutomation{index+1}.csv")
    os.rename(old_path, new_path)

print("✅ Semua file berhasil di-rename!")
